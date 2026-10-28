#!/usr/bin/env python3
"""Morning desk checklist from watchlists; optional Telegram push.

Usage:
  python3 scripts/egx_opp_digest.py
  TELEGRAM_BOT_TOKEN=... TELEGRAM_CHAT_ID=... python3 scripts/egx_opp_digest.py --send

TradingView still owns live scores — this message is a workflow reminder + symbol list.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_symbols(limit: int) -> list[str]:
    p = ROOT / "docs" / "EGX_WATCHLIST_200.txt"
    out: list[str] = []
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("EGX:"):
            out.append(line.replace("EGX:", ""))
    return out[:limit]


def build_message(symbols: list[str]) -> str:
    lines = [
        "EGX Opp Desk — morning checklist",
        "",
        "1) Screener: EGXOppDesk_Pro=1 (or EGXOpp_Pro=1)",
        "2) EGX30 + BOARD200 until ReadyPct >= 88%",
        "3) Hub EGXAlHub_OppPro on leaders",
        "",
        f"Watchlist head ({len(symbols)} shown):",
    ]
    lines.extend(f"  • {s}" for s in symbols)
    lines.extend(
        [
            "",
            "Filters: RS>0 · Limit=0 · optional EGXOppMeta_Pro",
        ]
    )
    return "\n".join(lines)


def send_telegram(text: str) -> None:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat:
        raise SystemExit("Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({"chat_id": chat, "text": text[:4000]}).encode()
    req = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = json.loads(resp.read().decode())
        if not body.get("ok"):
            raise SystemExit(f"Telegram error: {body}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=15)
    ap.add_argument("--send", action="store_true")
    args = ap.parse_args()
    msg = build_message(load_symbols(args.limit))
    print(msg)
    if args.send:
        send_telegram(msg)
        print("\nSent to Telegram.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
