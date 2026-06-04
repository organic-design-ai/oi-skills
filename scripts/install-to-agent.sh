#!/usr/bin/env bash
# Install oi-skills package under <agent-dir>/skills/oi-skills/<category>/<skill>/
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=lib/ui.sh
source "$SCRIPT_DIR/lib/ui.sh"

AGENT=""
AGENT_LABEL=""
SCOPE="global"
SKILL_NAME=""
SKIP_CONFIRM=false
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PACKAGE_NAME="oi-skills"
INSTALL_EXCLUDE=(skill.yaml)
PACKAGE_SKILL_SRC="$REPO_ROOT/docs/package/SKILL.md"
INSTALL_STEPS=5

usage() {
  ui_banner
  cat <<'EOF'
Usage: install-to-agent.sh [TARGET] [options] [--args FLAG ...]

TARGET (optional; on a TTY you can skip the menu by passing TARGET):
  agents | .cursor | qoder | claude

Without TARGET on a TTY: menu → confirm path → install (5 steps).

Flags:
  --agents --cursor --qoder --claude   TARGET (skip menu, still confirm on TTY)
  -g, --global | --project             Install scope (default: --global)
  --all                                Preset: .agents + global + all skills + -y
  --skill NAME                         Install one child skill only
  -y, --yes                            Skip confirmation (CI / scripts)
  --args                               Pass following flags (npx / CI forwarding)

Installs all skills in this repo (default) to:

  ~/.agents/skills/oi-skills/     (default)
  ~/.cursor/skills/oi-skills/
  ~/.qoder/skills/oi-skills/
  ~/.claude/skills/oi-skills/

Examples:
  ./scripts/install-to-agent.sh
  ./scripts/install-to-agent.sh --global -y
  ./scripts/install-to-agent.sh --all -y -g
  ./scripts/install-to-agent.sh --args --all -y -g
  ./scripts/install-to-agent.sh cursor --global
  ./scripts/install-to-agent.sh --agents --global --skill oi-video-to-gif

npx skills add (then flatten layout):
  npx skills add organic-design-ai/oi-skills --all -y -g -a agents --copy
  ~/.agents/skills/oi-skills/scripts/install-to-agent.sh --all -y -g

Non-interactive: OI_SKILLS_AGENT=agents OI_SKILLS_YES=1 ./scripts/install-to-agent.sh --global
EOF
}

# Parse one argv batch (used for main args and for --args forwarding).
parse_install_flags() {
  while [[ $# -gt 0 ]]; do
    case "$1" in
      agents|agent|.agents|cursor|.cursor|qoder|.qoder|claude|claude-code|.claude)
        normalize_agent "$1"
        ;;
      --agents|--agent) AGENT="agents" ;;
      --cursor)         AGENT="cursor" ;;
      --qoder)          AGENT="qoder" ;;
      --claude)         AGENT="claude" ;;
      -g|--global)      SCOPE="global" ;;
      --project)        SCOPE="project" ;;
      --skill)
        shift
        SKILL_NAME="${1:?--skill requires a name}"
        ;;
      --all)
        AGENT="${AGENT:-agents}"
        SCOPE="global"
        SKIP_CONFIRM=true
        ;;
      -y|--yes)         SKIP_CONFIRM=true ;;
      -h|--help)
        usage
        exit 0
        ;;
      --args)
        shift
        parse_install_flags "$@"
        return 0
        ;;
      --)
        shift
        parse_install_flags "$@"
        return 0
        ;;
      *)
        ui_err "Unknown argument: $1"
        usage
        exit 1
        ;;
    esac
    shift
  done
}

normalize_agent() {
  case "$1" in
    agents|agent|.agents) AGENT="agents" ;;
    cursor|.cursor)       AGENT="cursor" ;;
    qoder|.qoder)         AGENT="qoder" ;;
    claude|claude-code|.claude) AGENT="claude" ;;
    *)
      ui_err "Unknown target: $1 (use agents | cursor | qoder | claude)"
      return 1
      ;;
  esac
}

agent_display_label() {
  case "$AGENT" in
    agents) AGENT_LABEL=".agents" ;;
    cursor) AGENT_LABEL=".cursor" ;;
    qoder)  AGENT_LABEL=".qoder" ;;
    claude) AGENT_LABEL=".claude" ;;
    *)      AGENT_LABEL="$AGENT" ;;
  esac
}

resolve_agent_paths() {
  case "$AGENT" in
    agents) AGENT_DIR=".agents/skills" ;;
    cursor) AGENT_DIR=".cursor/skills" ;;
    qoder)  AGENT_DIR=".qoder/skills" ;;
    claude) AGENT_DIR=".claude/skills" ;;
  esac

  if [[ "$SCOPE" == "global" ]]; then
    case "$AGENT" in
      agents) TARGET_BASE="$HOME/.agents/skills" ;;
      cursor) TARGET_BASE="$HOME/.cursor/skills" ;;
      qoder)  TARGET_BASE="$HOME/.qoder/skills" ;;
      claude) TARGET_BASE="$HOME/.claude/skills" ;;
    esac
  else
    TARGET_BASE="$(pwd)/$AGENT_DIR"
  fi
  PKG_ROOT="$TARGET_BASE/$PACKAGE_NAME"
}

global_target_hint() {
  case "$AGENT" in
    agents) printf '%s' "$HOME/.agents/skills/oi-skills/" ;;
    cursor) printf '%s' "$HOME/.cursor/skills/oi-skills/" ;;
    qoder)  printf '%s' "$HOME/.qoder/skills/oi-skills/" ;;
    claude) printf '%s' "$HOME/.claude/skills/oi-skills/" ;;
  esac
}

prompt_agent_target_interactive() {
  ui_init
  if [[ -n "${OI_SKILLS_AGENT:-}" ]]; then
    normalize_agent "$OI_SKILLS_AGENT"
    agent_display_label
    return 0
  fi

  local scope_hint="global (user-level)"
  [[ "$SCOPE" == "project" ]] && scope_hint="current project"

  ui_timeline_group_open "oi-skills"
  ui_timeline_meta "Select install target — ${scope_hint}"
  if [[ "$SCOPE" == "global" ]]; then
    ui_timeline_sub_pending "1) .agents → $HOME/.agents/skills/oi-skills/"
    ui_timeline_sub_pending "2) .cursor → $HOME/.cursor/skills/oi-skills/"
    ui_timeline_sub_pending "3) .qoder  → $HOME/.qoder/skills/oi-skills/"
    ui_timeline_sub_pending "4) .claude → $HOME/.claude/skills/oi-skills/"
  else
    ui_timeline_sub_pending "1) .agents → ./.agents/skills/oi-skills/"
    ui_timeline_sub_pending "2) .cursor → ./.cursor/skills/oi-skills/"
    ui_timeline_sub_pending "3) .qoder  → ./.qoder/skills/oi-skills/"
    ui_timeline_sub_pending "4) .claude → ./.claude/skills/oi-skills/"
  fi
  printf '\n'

  local choice=""
  while true; do
    printf '  %bChoose [1-4], Enter for default .agents:%b ' "${UI_CYAN}${UI_BOLD}" "${UI_RESET}"
    read -r choice
    choice="${choice:-1}"
    case "$choice" in
      1|agents|agent|.agents) AGENT="agents"; break ;;
      2|cursor|.cursor)       AGENT="cursor"; break ;;
      3|qoder|.qoder)         AGENT="qoder"; break ;;
      4|claude|claude-code|.claude) AGENT="claude"; break ;;
      *)
        ui_warn "Invalid choice \"$choice\" — enter 1, 2, 3, or 4"
        ;;
    esac
  done
  agent_display_label
  ui_timeline_done "Install target" "${AGENT_LABEL}"
  ui_timeline_group_close
}

confirm_install_target() {
  if [[ "$SKIP_CONFIRM" == true ]] || [[ -n "${OI_SKILLS_YES:-}" ]]; then
    return 0
  fi
  if ! ui_is_tty; then
    return 0
  fi

  ui_timeline_group_open "oi-skills"
  if [[ "$SCOPE" == "global" ]]; then
    ui_timeline_done "Scope" "Global (all projects)"
  else
    ui_timeline_done "Scope" "Current project only"
  fi
  ui_timeline_done "Target" "$AGENT_LABEL"
  ui_timeline_done "Destination" "$PKG_ROOT"
  printf '\n'

  local ans=""
  printf '  %bInstall to the path above? [Y/n]:%b ' "${UI_CYAN}${UI_BOLD}" "${UI_RESET}"
  read -r ans
  case "$ans" in
    n|N|no|NO)
      ui_err "Installation cancelled"
      exit 0
      ;;
  esac
  ui_timeline_done "Confirmed" "Starting installation"
  ui_timeline_group_close
}

resolve_install_target() {
  if [[ -n "${OI_SKILLS_AGENT:-}" ]]; then
    normalize_agent "$OI_SKILLS_AGENT"
    agent_display_label
    return 0
  fi

  if [[ -n "$AGENT" ]]; then
    agent_display_label
    if ui_is_tty; then
      ui_timeline_group_open "oi-skills"
      ui_timeline_done "Install target" "From command line — ${AGENT_LABEL}"
      [[ "$SCOPE" == "global" ]] && ui_timeline_done "Destination" "$(global_target_hint)"
      ui_timeline_group_close
    fi
    return 0
  fi

  if ui_is_tty; then
    prompt_agent_target_interactive
  else
    AGENT="agents"
    agent_display_label
  fi
}

discover_skill_dirs() {
  find "$REPO_ROOT/skills" -mindepth 3 -maxdepth 3 -name SKILL.md 2>/dev/null | sort
}

skill_rel_path() {
  local skill_md="$1"
  dirname "$skill_md" | sed "s|^$REPO_ROOT/skills/||"
}

copy_skill_tree() {
  local rel="$1"
  local source="$REPO_ROOT/skills/$rel"
  local target="$PKG_ROOT/$rel"
  if [[ ! -f "$source/SKILL.md" ]]; then
    ui_err "Missing $source/SKILL.md"
    return 1
  fi
  mkdir -p "$(dirname "$target")"
  if [[ -e "$target" ]]; then
    ui_warn "Replacing existing: $target"
    rm -rf "$target"
  fi
  if command -v rsync >/dev/null 2>&1; then
    local excludes=()
    for f in "${INSTALL_EXCLUDE[@]}"; do
      excludes+=(--exclude "$f")
    done
    rsync -a "${excludes[@]}" "$source/" "$target/" >/dev/null
  else
    mkdir -p "$target"
    cp -R "$source/." "$target/"
    for f in "${INSTALL_EXCLUDE[@]}"; do
      rm -f "$target/$f"
    done
  fi
  chmod +x "$target/scripts/"*.py 2>/dev/null || true
}

install_package_skill() {
  if [[ ! -f "$PACKAGE_SKILL_SRC" ]]; then
    ui_err "Package entry missing: $PACKAGE_SKILL_SRC"
    return 1
  fi
  cp "$PACKAGE_SKILL_SRC" "$PKG_ROOT/SKILL.md"
}

remove_legacy_installs() {
  local md name
  while IFS= read -r md; do
    name="$(basename "$(dirname "$md")")"
    local legacy="$TARGET_BASE/$name"
    if [[ -d "$legacy" && "$legacy" != "$PKG_ROOT" ]]; then
      ui_warn "Removing legacy flat install: $legacy"
      rm -rf "$legacy"
    fi
  done < <(discover_skill_dirs)
  local d
  for d in "$TARGET_BASE"/${PACKAGE_NAME}--*; do
    [[ -e "$d" ]] || continue
    ui_warn "Removing legacy alias dir: $d"
    rm -rf "$d"
  done
}

[[ -n "${OI_SKILLS_YES:-}" ]] && SKIP_CONFIRM=true
[[ -n "${OI_SKILLS_AGENT:-}" ]] && normalize_agent "$OI_SKILLS_AGENT"

parse_install_flags "$@"

ui_banner
resolve_install_target
resolve_agent_paths
confirm_install_target

RELS=()
if [[ -n "$SKILL_NAME" ]]; then
  found=""
  while IFS= read -r md; do
    rel="$(skill_rel_path "$md")"
    if [[ "$(basename "$rel")" == "$SKILL_NAME" ]]; then
      found="$rel"
      break
    fi
  done < <(discover_skill_dirs)
  if [[ -z "$found" ]]; then
    ui_err "Skill not found: $SKILL_NAME"
    exit 1
  fi
  RELS=("$found")
else
  while IFS= read -r md; do
    RELS+=("$(skill_rel_path "$md")")
  done < <(discover_skill_dirs)
  if [[ ${#RELS[@]} -eq 0 ]]; then
    ui_err "No installable skills under skills/"
    exit 1
  fi
fi

INSTALL_PROGRESS_TOTAL=$((1 + ${#RELS[@]}))
UI_INSTALL_ITEM_TOTAL="$INSTALL_PROGRESS_TOTAL"
INSTALL_PROGRESS_DONE=0

ui_install_begin "$PKG_ROOT" "$AGENT_LABEL" "${#RELS[@]}"

# ── Step 1: Preflight ────────────────────────────────────────────────────────
ui_step_fold_start 1 "$INSTALL_STEPS" "Preflight"
ui_step_fold_done "${#RELS[@]} skill(s)"

# ── Step 2: Prepare target ───────────────────────────────────────────────────
ui_step_fold_start 2 "$INSTALL_STEPS" "Prepare target"
mkdir -p "$PKG_ROOT"
if [[ -z "$SKILL_NAME" && -d "$PKG_ROOT" ]]; then
  find "$PKG_ROOT" -mindepth 1 -maxdepth 1 ! -name SKILL.md -exec rm -rf {} + 2>/dev/null || true
fi
ui_step_fold_done "Ready"

# ── Step 3: Install package entry ────────────────────────────────────────────
ui_step_fold_start 3 "$INSTALL_STEPS" "Package entry"
if install_package_skill; then
  INSTALL_PROGRESS_DONE=$((INSTALL_PROGRESS_DONE + 1))
  ui_install_set_done "$INSTALL_PROGRESS_DONE"
  ui_step_fold_done "SKILL.md"
else
  printf '\n'
  ui_install_abort
  ui_err "Failed to install package entry"
  exit 1
fi

# ── Step 4: Install child skills ─────────────────────────────────────────────
ui_step_fold_start 4 "$INSTALL_STEPS" "Child skills"
for rel in "${RELS[@]}"; do
  if copy_skill_tree "$rel"; then
    INSTALL_PROGRESS_DONE=$((INSTALL_PROGRESS_DONE + 1))
    ui_install_set_done "$INSTALL_PROGRESS_DONE"
    ui_timeline_sub_done "$rel"
  else
    printf '\n'
    ui_install_abort
    ui_err "Failed to install $rel"
    exit 1
  fi
done
ui_step_fold_done "${#RELS[@]} installed"

# ── Step 5: Cleanup & finish ─────────────────────────────────────────────────
ui_step_fold_start 5 "$INSTALL_STEPS" "Finalize"
remove_legacy_installs
ui_step_fold_done "Done"

ui_install_finish

ui_success_box "Installation complete"

ui_timeline_group_open "summary"
ui_skill_line "$PACKAGE_NAME/SKILL.md"
for rel in "${RELS[@]}"; do
  ui_skill_line "$PACKAGE_NAME/$rel"
done
ui_timeline_group_close

ui_usage_box "$AGENT_LABEL"
