#!/usr/bin/env python3
"""
Regenerate f_b0..f_b7 symbol batches from docs/EGX_WATCHLIST_200.txt (+270 tail for 294).

Prints Pine switch blocks to stdout; paste into EGX_افضل_فرص_BOARD200.pine or redirect to docs/generated_board200_batches.pine
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCH = 38
MAX_BATCHES = 8


def load_symbols(path: Path) -> list[str]:
    out: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            out.append(line)
    return out


def emit_batch(name: str, symbols: list[str]) -> str:
    lines = [f"f_{name}(int i) =>", "    switch i"]
    for i, sym in enumerate(symbols):
        lines.append(f'        {i} => "{sym}"')
    lines.append('        => ""')
    return "\n".join(lines)


def main() -> int:
    w200 = ROOT / "docs" / "EGX_WATCHLIST_200.txt"
    w270 = ROOT / "docs" / "EGX_WATCHLIST_270.txt"
    if not w200.exists():
        print("Missing WATCHLIST_200", file=sys.stderr)
        return 1
    s200 = load_symbols(w200)
    s294 = list(s200)
    if w270.exists():
        s270 = load_symbols(w270)
        extra = [s for s in s270 if s not in set(s200)]
        s294 = s200 + extra[: max(0, 294 - len(s200))]
    s294 = s294[:294]

    all_syms = s294
    batches: list[list[str]] = []
    for b in range(MAX_BATCHES):
        start = b * BATCH
        chunk = all_syms[start : start + BATCH]
        if chunk:
            batches.append(chunk)

    print("// AUTO-GENERATED — regen_board200_symbols.py")
    print(f"// total={len(all_syms)} batches={len(batches)} size={BATCH}")
    for bi, chunk in enumerate(batches):
        print(emit_batch(f"b{bi}", chunk))
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
