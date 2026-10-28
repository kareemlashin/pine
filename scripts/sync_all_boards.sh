#!/usr/bin/env bash
# Regenerate TOOLS market boards from أفضل فرص sources.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
python3 scripts/gen_egx_tools_board200.py
python3 scripts/gen_egx_tools_board.py
python3 scripts/check_pine.sh
echo "OK: EGX_TOOLS_BOARD200.pine + EGX_TOOLS_BOARD.pine"
