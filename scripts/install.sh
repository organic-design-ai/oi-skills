#!/usr/bin/env bash
# Entry point for npx skills add / CI — forwards to install-to-agent.sh
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec "$SCRIPT_DIR/install-to-agent.sh" "$@"
