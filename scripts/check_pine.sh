#!/usr/bin/env bash
# Quick sanity checks on generated TOOLS boards (no TradingView compile).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
B200="$ROOT/pine/EGX_TOOLS_BOARD200.pine"
fail=0
for pat in 'f_opp()' 'top6Opp' 'leaderOpp' 'EGXOppB200'; do
  if grep -q "$pat" "$B200" 2>/dev/null; then
    echo "FAIL: $B200 still contains $pat"
    fail=1
  fi
done
for need in 'EGXTTB200_Top10Score' 'EGXTTB200_LeaderRR' 'EGXTTB200_MktHalt100' 'EGXTTB200_Pass' 'EGXTTB200_Breadth' 'EGXTTB200_HotProCount' 'passC' 'hotProC'; do
  if ! grep -q "$need" "$B200" 2>/dev/null; then
    echo "FAIL: missing plot $need"
    fail=1
  fi
done
if [[ $fail -eq 0 ]]; then
  echo "OK: EGX_TOOLS_BOARD200 parity checks passed"
fi
exit "$fail"
