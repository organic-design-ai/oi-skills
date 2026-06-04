#!/usr/bin/env python3
"""Check runtime dependencies for oi-video-crop and suggest install actions."""
from __future__ import annotations

import json
import platform
import shutil
import subprocess
import sys
from typing import Any


MIN_PYTHON = (3, 9)
MARKER_PREFIX = "[VIDEO_CROP_ENV]"


def _run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, capture_output=True, text=True, check=False)


def _version_output(cmd: list[str]) -> str | None:
    proc = _run(cmd)
    if proc.returncode != 0:
        return None
    line = (proc.stdout or proc.stderr or "").strip().splitlines()
    return line[0] if line else None


def _python_check() -> dict[str, Any]:
    ver = ".".join(map(str, sys.version_info[:3]))
    ok = sys.version_info >= MIN_PYTHON
    options: list[dict[str, str]] = []
    system = platform.system()

    if not ok:
        if system == "Darwin":
            options = [
                {
                    "id": "brew_python",
                    "label": "用 Homebrew 安装 Python 3",
                    "command": "brew install python@3.12",
                },
                {
                    "id": "python_org",
                    "label": "从 python.org 下载安装包",
                    "command": "open https://www.python.org/downloads/",
                },
            ]
        else:
            options = [
                {
                    "id": "python_org",
                    "label": "从 python.org 安装 Python 3.9+",
                    "command": "https://www.python.org/downloads/",
                },
            ]

    return {
        "name": "python",
        "ok": ok,
        "version": ver,
        "required": f">= {MIN_PYTHON[0]}.{MIN_PYTHON[1]}",
        "executable": sys.executable,
        "install_options": options,
    }


def _tool_check(name: str) -> dict[str, Any]:
    path = shutil.which(name)
    ok = path is not None
    version = _version_output([name, "-version"]) if ok else None
    return {"name": name, "ok": ok, "path": path, "version": version}


def _ffmpeg_install_options() -> list[dict[str, str]]:
    system = platform.system()
    if system == "Darwin":
        return [
            {
                "id": "brew_ffmpeg",
                "label": "用 Homebrew 安装 ffmpeg（推荐）",
                "command": "brew install ffmpeg",
            },
            {
                "id": "manual_ffmpeg",
                "label": "查看官方安装说明",
                "command": "open https://ffmpeg.org/download.html",
            },
        ]
    if system == "Linux":
        return [
            {
                "id": "apt_ffmpeg",
                "label": "Debian/Ubuntu: apt 安装",
                "command": "sudo apt update && sudo apt install -y ffmpeg",
            },
            {
                "id": "dnf_ffmpeg",
                "label": "Fedora/RHEL: dnf 安装",
                "command": "sudo dnf install -y ffmpeg",
            },
        ]
    if system == "Windows":
        return [
            {
                "id": "winget_ffmpeg",
                "label": "winget 安装",
                "command": "winget install --id Gyan.FFmpeg -e",
            },
            {
                "id": "choco_ffmpeg",
                "label": "Chocolatey 安装",
                "command": "choco install ffmpeg -y",
            },
        ]
    return [
        {
            "id": "manual_ffmpeg",
            "label": "官方下载页",
            "command": "https://ffmpeg.org/download.html",
        },
    ]


def _brew_check() -> dict[str, Any]:
    path = shutil.which("brew")
    return {
        "name": "brew",
        "ok": path is not None,
        "path": path,
        "relevant": platform.system() == "Darwin",
    }


def _is_shell_install_command(command: str) -> bool:
    """True when the option runs a package manager (not open URL / plain link)."""
    prefixes = ("brew install", "sudo apt", "sudo dnf", "winget install", "choco install")
    return any(command.strip().startswith(p) for p in prefixes)


def auto_install_commands(env: dict[str, Any]) -> list[str]:
    """Preferred install commands for the agent to run without asking."""
    commands: list[str] = []
    checks = {c["name"]: c for c in env["checks"]}
    python = checks.get("python", {})
    ffmpeg = checks.get("ffmpeg", {})
    ffprobe = checks.get("ffprobe", {})

    if not python.get("ok"):
        for opt in python.get("install_options", []):
            cmd = opt.get("command", "")
            if _is_shell_install_command(cmd):
                commands.append(cmd)
                break

    if not ffmpeg.get("ok") or not ffprobe.get("ok"):
        for opt in ffmpeg.get("install_options", []):
            cmd = opt.get("command", "")
            if _is_shell_install_command(cmd):
                commands.append(cmd)
                break

    return commands


def run_auto_install(env: dict[str, Any]) -> dict[str, Any]:
    """Run preferred install commands in foreground; return attempt log."""
    commands = auto_install_commands(env)
    attempts: list[dict[str, Any]] = []
    for command in commands:
        print(f"[oi-video-crop] Installing: {command}", file=sys.stderr, flush=True)
        proc = subprocess.run(command, shell=True, check=False)
        attempts.append(
            {
                "command": command,
                "ok": proc.returncode == 0,
                "returncode": proc.returncode,
            }
        )
    return {"commands": commands, "attempts": attempts, "any_ok": any(a["ok"] for a in attempts)}


def collect_env() -> dict[str, Any]:
    python = _python_check()
    ffmpeg = _tool_check("ffmpeg")
    ffprobe = _tool_check("ffprobe")
    brew = _brew_check()

    if not ffmpeg["ok"]:
        ffmpeg["install_options"] = _ffmpeg_install_options()
    else:
        ffmpeg["install_options"] = []

    if not ffprobe["ok"] and ffmpeg["ok"]:
        ffprobe["note"] = "ffprobe 通常随 ffmpeg 一起安装；请重装 ffmpeg。"

    checks = [python, ffmpeg, ffprobe]
    ready = python["ok"] and ffmpeg["ok"] and ffprobe["ok"]

    agent_menu: list[dict[str, Any]] = []
    if not python["ok"]:
        for opt in python.get("install_options", []):
            agent_menu.append({**opt, "fixes": "python"})
    if not ffmpeg["ok"] or not ffprobe["ok"]:
        for opt in ffmpeg.get("install_options", []):
            agent_menu.append({**opt, "fixes": "ffmpeg"})

    payload: dict[str, Any] = {
        "ready": ready,
        "platform": platform.system(),
        "platform_release": platform.release(),
        "checks": checks,
        "brew": brew,
        "agent_menu": agent_menu,
    }
    if not ready:
        cmds = auto_install_commands(payload)
        payload["auto_install"] = {
            "available": bool(cmds),
            "commands": cmds,
        }
    payload["agent_prompt"] = _build_agent_prompt(
        ready, python, ffmpeg, ffprobe, brew, agent_menu, payload.get("auto_install")
    )
    return payload


def _build_agent_prompt(
    ready: bool,
    python: dict[str, Any],
    ffmpeg: dict[str, Any],
    ffprobe: dict[str, Any],
    brew: dict[str, Any],
    menu: list[dict[str, str]],
    auto_install: dict[str, Any] | None = None,
) -> str:
    if ready:
        return "环境已就绪，可继续 oi-video-crop 流程。"

    lines = ["oi-video-crop 缺少运行环境：", ""]
    if not python["ok"]:
        lines.append(f"- Python：当前 {python['version']}，需要 {python['required']}")
    if not ffmpeg["ok"]:
        lines.append("- ffmpeg：未安装")
    if not ffprobe["ok"]:
        lines.append("- ffprobe：未安装")
    if brew["relevant"] and not brew["ok"] and menu:
        lines.append("- Homebrew：未检测到（macOS 上推荐用 brew 安装依赖）")

    ai = auto_install or {}
    if ai.get("available") and ai.get("commands"):
        lines.append("")
        lines.append("Agent：直接执行自动安装（勿等待用户选菜单）：")
        lines.append("```bash")
        lines.append(
            f"python3 <pkg-dir>/widget/oi-video-crop/scripts/check_env.py --install --json"
        )
        lines.append("```")
        for cmd in ai["commands"]:
            lines.append(f"- `{cmd}`")
        return "\n".join(lines)

    lines.append("")
    lines.append("自动安装不可用。请选择要执行的操作（回复序号）：")
    for i, item in enumerate(menu, 1):
        lines.append(f"  {i}) {item['label']} — `{item['command']}`")
    lines.append(f"  {len(menu) + 1}) 跳过，稍后我自己安装")
    lines.append(f"  {len(menu) + 2}) 已安装完成，重新检测环境")
    return "\n".join(lines)


def main() -> int:
    do_install = "--install" in sys.argv
    json_out = "--json" in sys.argv or "-j" in sys.argv

    data = collect_env()
    install_log: dict[str, Any] | None = None

    if do_install and not data["ready"]:
        install_log = run_auto_install(data)
        data = collect_env()
        data["install"] = install_log

    if json_out:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(f"{MARKER_PREFIX} {json.dumps({'ready': data['ready']}, ensure_ascii=False)}")
        print(data["agent_prompt"])
        if not data["ready"] and data["agent_menu"]:
            print("\nInstall commands:", file=sys.stderr)
            for item in data["agent_menu"]:
                print(f"  [{item['id']}] {item['command']}", file=sys.stderr)

    return 0 if data["ready"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
