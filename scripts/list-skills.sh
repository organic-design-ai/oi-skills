#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=lib/ui.sh
source "$SCRIPT_DIR/lib/ui.sh"

REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PACKAGE_NAME="oi-skills"

skill_short_label() {
  local rel="$1"
  local yaml="$REPO_ROOT/skills/$rel/skill.yaml"
  local desc=""
  if [[ -f "$yaml" ]]; then
    desc="$(grep -E '^description:' "$yaml" 2>/dev/null | head -1 | sed 's/^description:[[:space:]]*//' | sed 's/^"\(.*\)"$/\1/')"
    if [[ -z "$desc" ]]; then
      desc="$(grep -E '^description_zh:' "$yaml" 2>/dev/null | head -1 | sed 's/^description_zh:[[:space:]]*//' | sed 's/^"\(.*\)"$/\1/')"
    fi
  fi
  if [[ -n "$desc" ]]; then
    printf '%s — %s' "$(basename "$rel")" "$desc"
  else
    basename "$rel"
  fi
}

ui_banner
ui_timeline_group_open "oi-skills"
ui_timeline_meta "Installed layout: <agent>/skills/$PACKAGE_NAME/<category>/<skill>/"

ui_checklist_reset
ui_checklist_add "package" "oi-skills (package entry)" "done"

found=0
while IFS= read -r skill_md; do
  skill_dir="$(dirname "$skill_md")"
  rel="${skill_dir#$REPO_ROOT/skills/}"
  ui_checklist_add "$rel" "$(skill_short_label "$rel")" "pending"
  found=$((found + 1))
done < <(find "$REPO_ROOT/skills" -mindepth 3 -maxdepth 3 -name SKILL.md 2>/dev/null | sort)

if [[ $found -eq 0 ]]; then
  ui_warn "No child skills found under skills/"
else
  ui_ok "$found skill(s) ready to install"
fi

UI_INSTALL_ITEM_TOTAL="${#UI_CHECK_IDS[@]}"
ui_checklist_render_rows
ui_checklist_count_done
ui_timeline_done "Catalog" "${UI_CHECK_DONE_COUNT}/${UI_INSTALL_ITEM_TOTAL} skill(s)"
ui_timeline_group_close

echo ""
ui_timeline_group_open "install"
ui_timeline_meta "Entry: $PACKAGE_NAME/SKILL.md"
ui_timeline_sub_pending "npx skills add organic-design-ai/oi-skills --all -y -g -a agents --copy"
ui_timeline_sub_pending "./scripts/install-to-agent.sh --all -y -g"
ui_timeline_sub_pending "./scripts/install-to-agent.sh  (TTY: pick target → confirm)"
ui_timeline_group_close
