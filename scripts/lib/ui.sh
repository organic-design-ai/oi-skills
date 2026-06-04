# shellcheck shell=bash
# Terminal UI helpers for oi-skills scripts (source only).

UI_RESET=""
UI_BOLD=""
UI_DIM=""
UI_RED=""
UI_GREEN=""
UI_YELLOW=""
UI_BLUE=""
UI_MAGENTA=""
UI_CYAN=""
UI_WHITE=""
UI_ROSE=""

# Step / progress state (set by install scripts)
UI_STEP_CURRENT=0
UI_STEP_TOTAL=0

# Skill checklist: parallel arrays (bash 3.2 compatible)
UI_CHECK_IDS=()
UI_CHECK_LABELS=()
UI_CHECK_STATUSES=() # pending | active | done | fail | skip
UI_CHECK_TOTAL=0
UI_CHECK_DONE_COUNT=0
# Explicit install counters (install script sets total; avoids array/subshell issues)
UI_INSTALL_ITEM_TOTAL=0
# Default pause between UI snapshots (ms); override: UI_PAUSE_MS=600 ./scripts/...
UI_PAUSE_MS="${UI_PAUSE_MS:-400}"

# Install timeline (┌ │ └ + ◇ ◆ □) — reference: skills CLI wizard
UI_TIMELINE_OPEN=false
UI_TL_ACTIVE_LINE_PRINTED=false
UI_STEP_FOLD_TOTAL=0
UI_STEP_FOLD_CURRENT=0
UI_STEP_FOLD_TITLE=""

ui_init() {
  if [[ -n "${NO_COLOR:-}" ]] || [[ ! -t 1 ]]; then
    return 0
  fi
  UI_RESET="\033[0m"
  UI_BOLD="\033[1m"
  UI_DIM="\033[2m"
  UI_RED="\033[38;5;203m"
  UI_GREEN="\033[38;5;82m"
  UI_YELLOW="\033[38;5;221m"
  UI_BLUE="\033[38;5;39m"
  UI_MAGENTA="\033[38;5;208m"
  UI_CYAN="\033[38;5;45m"
  UI_WHITE="\033[38;5;252m"
  UI_ROSE="\033[38;5;210m"
}

# ── Install timeline rail (┌ │ └ · ◇ done · ◆ active · □ pending) ─────────────

_ui_tl_rail() {
  printf '%b│%b' "${UI_DIM}" "${UI_RESET}"
}

ui_timeline_open() {
  local badge="${1:-oi-skills}"
  UI_TIMELINE_OPEN=true
  UI_TL_ACTIVE_LINE_PRINTED=false
  ui_init
  printf '\n'
  if ui_is_tty; then
    printf '  %b┌%b ' "$UI_DIM" "$UI_RESET"
    printf '%b %s %b' "${UI_BLUE}${UI_BOLD}" "$badge" "$UI_RESET"
    printf '\n'
  else
    printf '== %s ==\n' "$badge"
  fi
}

ui_timeline_meta() {
  local text="$1"
  [[ -n "$text" ]] || return 0
  ui_init
  if ui_is_tty; then
    printf '  '; _ui_tl_rail; printf '  %b%s%b\n' "$UI_DIM" "$text" "$UI_RESET"
  else
    printf '  %s\n' "$text"
  fi
}

ui_timeline_active_clear() {
  [[ "$UI_TL_ACTIVE_LINE_PRINTED" == true ]] || return 0
  if ui_is_tty; then
    printf '\033[1A\033[2K'
  fi
  UI_TL_ACTIVE_LINE_PRINTED=false
}

ui_timeline_active() {
  local title="$1" indent="${2:-0}"
  ui_timeline_active_clear
  ui_init
  if ui_is_tty; then
    local sp=""
    [[ "$indent" -gt 0 ]] && sp="$(printf '%*s' "$((indent * 2))" '')"
    printf '  '; _ui_tl_rail; printf ' %s%b◆%b %b%s%b\n' \
      "$sp" "$UI_BLUE${UI_BOLD}" "$UI_RESET" "$UI_CYAN${UI_BOLD}" "$title" "$UI_RESET"
    UI_TL_ACTIVE_LINE_PRINTED=true
  else
    printf '  > %s\n' "$title"
  fi
}

ui_timeline_done() {
  local title="$1" detail="${2:-}" indent="${3:-0}"
  ui_timeline_active_clear
  ui_init
  if ui_is_tty; then
    local sp=""
    [[ "$indent" -gt 0 ]] && sp="$(printf '%*s' "$((indent * 2))" '')"
    printf '  '; _ui_tl_rail; printf ' %s%b◇%b %b%s%b' \
      "$sp" "$UI_ROSE" "$UI_RESET" "$UI_ROSE" "$title" "$UI_RESET"
    if [[ -n "$detail" ]]; then
      printf ' %b—%b %s' "$UI_DIM" "$UI_RESET" "$detail"
    fi
    printf '\n'
  else
    if [[ -n "$detail" ]]; then
      printf '  ok %s — %s\n' "$title" "$detail"
    else
      printf '  ok %s\n' "$title"
    fi
  fi
}

ui_timeline_fail() {
  local title="$1" detail="${2:-}"
  ui_timeline_active_clear
  ui_init
  if ui_is_tty; then
    printf '  '; _ui_tl_rail; printf ' %b✗%b %b%s%b' \
      "$UI_RED${UI_BOLD}" "$UI_RESET" "$UI_RED" "$title" "$UI_RESET"
    [[ -n "$detail" ]] && printf ' %b—%b %s' "$UI_DIM" "$UI_RESET" "$detail"
    printf '\n'
  else
    printf '  fail %s %s\n' "$title" "$detail"
  fi
}

ui_timeline_sub_pending() {
  local label="$1"
  ui_init
  if ui_is_tty; then
    printf '  '; _ui_tl_rail; printf '   %b□%b %b%s%b\n' \
      "$UI_DIM" "$UI_RESET" "$UI_DIM" "$label" "$UI_RESET"
  else
    printf '  [ ] %s\n' "$label"
  fi
}

ui_timeline_sub_done() {
  local label="$1"
  ui_init
  if ui_is_tty; then
    printf '  '; _ui_tl_rail; printf '   %b◇%b %b%s%b\n' \
      "$UI_ROSE" "$UI_RESET" "$UI_ROSE" "$label" "$UI_RESET"
  else
    printf '    ok %s\n' "$label"
  fi
}

ui_timeline_close() {
  ui_timeline_active_clear
  if ui_is_tty; then
    printf '  %b└%b\n\n' "$UI_DIM" "$UI_RESET"
  else
    printf '\n'
  fi
  UI_TIMELINE_OPEN=false
}

# Secondary timeline block (e.g. summary) without toggling UI_TIMELINE_OPEN
ui_timeline_group_open() {
  local badge="${1:-summary}"
  ui_init
  printf '\n'
  if ui_is_tty; then
    printf '  %b┌%b %b%s%b\n' "$UI_DIM" "$UI_RESET" "$UI_BLUE${UI_BOLD}" "$badge" "$UI_RESET"
  else
    printf '== %s ==\n' "$badge"
  fi
}

ui_timeline_group_close() {
  ui_init
  if ui_is_tty; then
    printf '  %b└%b\n\n' "$UI_DIM" "$UI_RESET"
  else
    printf '\n'
  fi
}

_ui() {
  printf '%b%b%b\n' "$1" "$2" "$UI_RESET"
}

ui_has_tty() {
  [[ -t 1 ]] || [[ -t 2 ]]
}

ui_is_tty() {
  [[ -t 1 ]] && [[ -z "${NO_COLOR:-}" ]]
}

ui_is_tty_stderr() {
  [[ -t 2 ]] && [[ -z "${NO_COLOR:-}" ]]
}

ui_pause() {
  local ms="${1:-$UI_PAUSE_MS}"
  if ! ui_is_tty || [[ "$ms" -le 0 ]]; then
    return 0
  fi
  # $ms inside awk "..." is parsed as awk's $ms field — use -v
  sleep "$(awk -v m="$ms" 'BEGIN { printf "%.3f", m / 1000 }')" 2>/dev/null \
    || sleep $(( (ms + 999) / 1000 ))
}

ui_flush() {
  if ui_is_tty; then
    sleep 0.05
  fi
}

# Repo root (scripts/lib -> scripts -> repo)
ui_repo_root() {
  cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd
}

# Package version for banner / CLI (edit repo-root VERSION only)
ui_repo_version() {
  local root vfile
  root="$(ui_repo_root)"
  vfile="$root/VERSION"
  if [[ -f "$vfile" ]]; then
    tr -d '[:space:]\r' <"$vfile"
    return 0
  fi
  echo "unknown"
}

# Width of figlet lines in ui_banner (version row is padded to match)
_UI_BANNER_ART_WIDTH=61

_ui_banner_version_line() {
  local ver="v$(ui_repo_version)" pad
  pad=$((_UI_BANNER_ART_WIDTH - ${#ver}))
  ((pad < 0)) && pad=0
  printf '%*s%s' "$pad" '' "$ver"
}

# Banner: DESIGN SKILLS figlet (standard)
ui_banner() {
  ui_init
  local c="$UI_CYAN${UI_BOLD}" d="$UI_DIM" r="$UI_RESET"
  local version_line
  version_line="$(_ui_banner_version_line)"
  local -a art=(
    ' _____           ____    __           ___    ___             '
    '/\  __`\  __    /\  _`\ /\ \      __ /\_ \  /\_ \            '
    '\ \ \/\ \/\_\   \ \,\L\_\ \ \/'\'' /\_\\//\ \ \//\ \     ____  '
    ' \ \ \ \ \/\ \   \/_\__ \\ \ , < \/\ \ \ \ \  \ \ \   /'\'',__\ '
    '  \ \ \_\ \ \ \    /\ \L\ \ \ \\`\\ \ \ \_\ \_ \_\ \_/\__, `\'
    '   \ \_____\ \_\   \ `\____\ \_\ \_\ \_\/\____\/\____\/\____/'
    '    \/_____/\/_/    \/_____/\/_/\/_/\/_/\/____/\/____/\/___/ '
    "$version_line"
  )

  printf '\n'
  local line
  for line in "${art[@]}"; do
    printf '  %b%s%b\n' "$c" "$line" "$r"
  done
  local -a taglines=(
    ''
    'Skills · Page · Widget · Media'
    'Alibaba Cloud Design Innovation Center'
  )
  for line in "${taglines[@]}"; do
    printf '  %b%s%b\n' "$d" "$line" "$r"
  done
  printf '\n'
}

ui_section() {
  _ui "${UI_CYAN}${UI_BOLD}" "── $1 "
}

ui_step() {
  _ui "${UI_BLUE}" "  ▸ $1"
}

ui_ok() {
  _ui "${UI_GREEN}" "  ✓ $1"
}

ui_info() {
  _ui "${UI_DIM}" "    $1"
}

ui_warn() {
  _ui "${UI_YELLOW}" "  ⚠ $1"
}

ui_err() {
  _ui "${UI_RED}${UI_BOLD}" "  ✗ $1" >&2
}

ui_path() {
  _ui "${UI_MAGENTA}" "    → $1"
}

ui_label() {
  printf '  %b%-12s%b %s\n' "${UI_DIM}" "$1" "${UI_RESET}" "$2"
}

ui_skill_line() {
  ui_init
  if ui_is_tty; then
    printf '  '; _ui_tl_rail; printf '   %b◇%b %b%s%b\n' "$UI_ROSE" "$UI_RESET" "$UI_CYAN" "$1" "$UI_RESET"
  else
    printf '  - %s\n' "$1"
  fi
}

ui_divider() {
  _ui "${UI_DIM}" "  ────────────────────────────────────────"
}

ui_success_box() {
  local msg="${1:-Done}"
  ui_init
  if ui_is_tty; then
    printf '\n  %b◇%b %b%s%b\n\n' "$UI_ROSE" "$UI_RESET" "$UI_GREEN${UI_BOLD}" "$msg" "$UI_RESET"
  else
    printf '\nOK: %s\n\n' "$msg"
  fi
}

# ── Step header (Step 2/5 — Title) ───────────────────────────────────────────

ui_step_begin() {
  local n="$1" total="$2" title="$3"
  UI_STEP_CURRENT="$n"
  UI_STEP_TOTAL="$total"
  ui_init
  printf '\n%bStep %s/%s%b  %b%s%b\n' \
    "${UI_CYAN}${UI_BOLD}" "$n" "$total" "${UI_RESET}" \
    "${UI_WHITE}${UI_BOLD}" "$title" "${UI_RESET}"
}

# ── Progress bar ─────────────────────────────────────────────────────────────

ui_progress() {
  local current="$1" total="$2" label="${3:-Progress}"
  ui_init
  [[ "$total" -le 0 ]] && total=1
  [[ "$current" -lt 0 ]] && current=0
  [[ "$current" -gt "$total" ]] && current="$total"
  local pct=$(( current * 100 / total ))
  local width=28
  local filled=$(( current * width / total ))
  local empty=$(( width - filled ))
  local bar_filled bar_empty bar
  bar_filled="$(printf '%*s' "$filled" '' | tr ' ' '█')"
  bar_empty="$(printf '%*s' "$empty" '' | tr ' ' '░')"
  bar="[${bar_filled}${bar_empty}]"
  # macOS bash mishandles "%b%3d%% %b(%d/%d)%b" — split printfs (literal %% via separate call)
  if ui_is_tty; then
    printf '  %b%-14s%b %b%s%b ' \
      "${UI_DIM}" "$label" "${UI_RESET}" \
      "${UI_GREEN}" "$bar" "${UI_RESET}"
    printf '%b%3d' "${UI_CYAN}${UI_BOLD}" "$pct"
    printf '%%'
    printf ' %b(%d/%d)%b\n' "${UI_DIM}" "$current" "$total" "${UI_RESET}"
  else
    printf '  %-14s %s %3d' "$label" "$bar" "$pct"
    printf '%%'
    printf ' (%d/%d)\n' "$current" "$total"
  fi
}

# ── Skill checklist (internal / list-skills only — install uses ui_install_set_done) ─

# Install scripts: drive progress bar without rendering this checklist on screen.
ui_install_set_done() {
  UI_CHECK_DONE_COUNT="$1"
}

ui_checklist_reset() {
  UI_CHECK_IDS=()
  UI_CHECK_LABELS=()
  UI_CHECK_STATUSES=()
  UI_CHECK_TOTAL=0
  UI_CHECK_DONE_COUNT=0
}

ui_checklist_add() {
  local id="$1" label="$2" status="${3:-pending}"
  UI_CHECK_IDS+=("$id")
  UI_CHECK_LABELS+=("$label")
  UI_CHECK_STATUSES+=("$status")
  UI_CHECK_TOTAL="${#UI_CHECK_IDS[@]}"
}

ui_checklist_set() {
  local id="$1" status="$2"
  local i
  for i in "${!UI_CHECK_IDS[@]}"; do
    if [[ "${UI_CHECK_IDS[$i]}" == "$id" ]]; then
      UI_CHECK_STATUSES[$i]="$status"
      return 0
    fi
  done
  return 1
}

ui_checklist_icon() {
  local status="$1"
  case "$status" in
    pending) printf '%b○%b' "${UI_DIM}" "${UI_RESET}" ;;
    active)  printf '%b◉%b' "${UI_YELLOW}${UI_BOLD}" "${UI_RESET}" ;;
    done)    printf '%b●%b' "${UI_GREEN}${UI_BOLD}" "${UI_RESET}" ;;
    fail)    printf '%b✗%b' "${UI_RED}${UI_BOLD}" "${UI_RESET}" ;;
    skip)    printf '%b−%b' "${UI_DIM}" "${UI_RESET}" ;;
    *)       printf '%b?%b' "${UI_DIM}" "${UI_RESET}" ;;
  esac
}

ui_checklist_render_rows() {
  local i label status
  for i in "${!UI_CHECK_IDS[@]}"; do
    label="${UI_CHECK_LABELS[$i]}"
    status="${UI_CHECK_STATUSES[$i]}"
    case "$status" in
      done)  ui_timeline_sub_done "$label" ;;
      fail)  ui_timeline_fail "$label" ;;
      active)
        ui_timeline_active "$label" 1
        ui_timeline_active_clear
        ;;
      *)     ui_timeline_sub_pending "$label" ;;
    esac
  done
}

ui_checklist_render() {
  local title="${1:-Skills}"
  ui_init
  ui_timeline_group_open "$title"
  ui_checklist_render_rows
  ui_timeline_group_close
}

# Sets UI_CHECK_DONE_COUNT in the current shell (never use $(...) — subshell loses arrays)
ui_checklist_count_done() {
  local n=0 s
  for s in "${UI_CHECK_STATUSES[@]}"; do
    [[ "$s" == "done" ]] && n=$((n + 1))
  done
  UI_CHECK_DONE_COUNT="$n"
}

# ── Install flow (timeline + optional progress for non-install callers) ────────

ui_install_progress_refresh() {
  [[ "$UI_TIMELINE_OPEN" == true ]] && return 0
  if [[ "${#UI_CHECK_IDS[@]}" -gt 0 ]]; then
    ui_checklist_count_done
  fi
  local done="${UI_CHECK_DONE_COUNT:-0}"
  local total="${UI_INSTALL_ITEM_TOTAL}"
  [[ "$total" -le 0 ]] && total="${UI_CHECK_TOTAL}"
  [[ "$total" -le 0 ]] && total="${#UI_CHECK_IDS[@]}"
  [[ "$total" -le 0 ]] && total=1
  [[ "$done" -gt "$total" ]] && done="$total"
  ui_progress "$done" "$total" "Install"
}

# path, agent label, skill count
ui_install_begin() {
  local path="${1:-}" agent="${2:-}" skill_count="${3:-0}"
  ui_timeline_open "oi-skills"
  [[ -n "$agent" ]] && ui_timeline_done "Install target" "$agent"
  [[ -n "$path" ]] && ui_timeline_done "Destination" "$path"
  if [[ "$skill_count" -gt 0 ]]; then
    ui_timeline_done "Skills manifest" "Found ${skill_count} skill(s)"
  fi
}

ui_install_finish() {
  ui_timeline_close
}

ui_step_fold_start() {
  local n="$1" total="$2" title="$3"
  UI_STEP_FOLD_CURRENT="$n"
  UI_STEP_FOLD_TOTAL="$total"
  UI_STEP_FOLD_TITLE="$title"
  if [[ "$UI_TIMELINE_OPEN" == true ]]; then
    ui_timeline_active "$title"
  else
    ui_step_begin "$n" "$total" "$title"
  fi
}

ui_step_fold_done() {
  local detail="${1:-}"
  if [[ "$UI_TIMELINE_OPEN" == true ]]; then
    ui_timeline_done "$UI_STEP_FOLD_TITLE" "$detail"
  elif [[ -n "$detail" ]]; then
    ui_ok "$detail"
  fi
}

ui_install_abort() {
  if [[ "$UI_TIMELINE_OPEN" == true ]]; then
    ui_timeline_fail "$UI_STEP_FOLD_TITLE" "aborted"
    ui_timeline_close
  fi
}

ui_install_moment() {
  ui_install_progress_refresh
}

ui_usage_box() {
  local agent_label="${1:-.agents}"
  ui_init
  printf '\n'
  if ui_is_tty; then
    printf '  %b┌%b %bdone%b\n' "$UI_DIM" "$UI_RESET" "$UI_BLUE${UI_BOLD}" "$UI_RESET"
    case "$agent_label" in
      .qoder|qoder)
        printf '  '; _ui_tl_rail; printf '  %bQoder:%b /skills reload if needed\n' "$UI_DIM" "$UI_RESET"
        ;;
      .claude|claude)
        printf '  '; _ui_tl_rail; printf '  %bClaude:%b add AGENTS.md snippet if triggers missing\n' "$UI_DIM" "$UI_RESET"
        ;;
    esac
    printf '  '; _ui_tl_rail; printf '  %bChat →%b / → oi-skills or a child skill\n' "$UI_DIM" "$UI_RESET"
    printf '  %b└%b\n' "$UI_DIM" "$UI_RESET"
  else
    ui_section "Next steps"
    case "$agent_label" in
      .qoder|qoder) ui_info "Qoder: /skills reload if needed" ;;
      .claude|claude) ui_info "Claude: add AGENTS.md snippet if triggers missing (README)" ;;
    esac
    ui_step "New chat → / → oi-skills or a child skill"
  fi
  ui_banner
}
