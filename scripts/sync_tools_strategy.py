#!/usr/bin/env python3
"""Sync session gate block from EGX_TOOLS_MASTER → EGX_TOOLS_MASTER_STRATEGY."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "pine" / "EGX_TOOLS_MASTER.pine"
STRAT = ROOT / "pine" / "EGX_TOOLS_MASTER_STRATEGY.pine"

MARKER_START = "// SYNC:GATES:START"
MARKER_END = "// SYNC:GATES:END"


def session_block(master: str) -> str:
    lines = master.splitlines()
    out = []
    capture = False
    for ln in lines:
        if ln.startswith("f_egxSessId()"):
            capture = True
        if capture:
            out.append(ln)
            if ln.startswith("bool sessionOk"):
                break
    if not out:
        raise SystemExit("Could not find session block in MASTER")
    return "\n".join(out)


def main() -> None:
    m = MASTER.read_text(encoding="utf-8")
    s = STRAT.read_text(encoding="utf-8")
    block = MARKER_START + "\n" + session_block(m) + "\n" + MARKER_END
    if MARKER_START in s:
        s = re.sub(
            re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END),
            block,
            s,
            count=1,
            flags=re.DOTALL,
        )
    else:
        anchor = "bool sigOk = not confirmClose"
        idx = s.index(anchor)
        end = s.index("\n", idx) + 1
        s = s[:end] + "\n" + block + "\n" + s[end:]
    STRAT.write_text(s, encoding="utf-8")
    print(f"Updated {STRAT} ({MARKER_START} block)")


if __name__ == "__main__":
    main()
