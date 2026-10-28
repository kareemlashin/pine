#!/usr/bin/env python3
"""Validate docs/EGX_WATCHLIST_200.txt and docs/EGX_WATCHLIST_270.txt."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SYMBOL_RE = re.compile(r"^EGX:[A-Z0-9]+$")


def load_symbols(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        out.append(line)
    return out


def check(name: str, path: Path, expect: int | None = None) -> int:
    if not path.exists():
        print(f"FAIL {name}: missing {path}")
        return 1
    syms = load_symbols(path)
    err = 0
    if expect is not None and len(syms) != expect:
        print(f"WARN {name}: count {len(syms)} (expected {expect})")
    seen: set[str] = set()
    for s in syms:
        if not SYMBOL_RE.match(s):
            print(f"FAIL {name}: bad symbol {s!r}")
            err += 1
        if s in seen:
            print(f"FAIL {name}: duplicate {s}")
            err += 1
        seen.add(s)
    if err == 0:
        print(f"OK {name}: {len(syms)} symbols, unique, format EGX:XXXX")
    return err


def main() -> int:
    e = 0
    e += check("WATCHLIST_200", ROOT / "docs" / "EGX_WATCHLIST_200.txt", 200)
    p270 = ROOT / "docs" / "EGX_WATCHLIST_270.txt"
    if p270.exists():
        e += check("WATCHLIST_270", p270, None)
    else:
        print("SKIP WATCHLIST_270: file not found")
    return 1 if e else 0


if __name__ == "__main__":
    sys.exit(main())
