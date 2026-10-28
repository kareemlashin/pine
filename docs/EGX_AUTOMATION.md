# EGX — Automation (outside TradingView)

TradingView Pine cannot push **live BOARD200 leaders** without alerts on **EGX30** (alert ticker = index). Use this stack for **morning ritual + CI + optional Telegram**.

## CI (GitHub)

Workflow: [`.github/workflows/validate.yml`](../.github/workflows/validate.yml)

- `scripts/validate_egx_watchlist.py` — 200/270 symbol format & uniqueness
- `scripts/gen_egx_sector_pine.py --check` — sector map matches `BOARD200` `f_secTag`

After editing watchlists or sectors:

```bash
python3 scripts/gen_egx_sector_pine.py
python3 scripts/validate_egx_watchlist.py
```

## Sector map

| File | Role |
|------|------|
| `docs/EGX_SECTOR_MAP.csv` | `symbol,sector_tag` (296+) |
| `scripts/gen_egx_sector_pine.py` | Regenerates `// --- BEGIN AUTO f_secTag ---` in BOARD200 |

Edit classification rules in the Python script (`BANKS`, `REAL`, … sets), then regen.

## Morning digest (Telegram optional)

```bash
python3 scripts/egx_opp_digest.py
TELEGRAM_BOT_TOKEN=... TELEGRAM_CHAT_ID=... python3 scripts/egx_opp_digest.py --send
```

This does **not** scrape TradingView; it sends **workflow + symbol list**. Rankings come from **Stock Screener** columns (`EGXOppDesk_Pro`, `EGXOpp_Score`).

## Screener confluence (one column)

Add to watchlist indicators:

| Indicator | Filter |
|-----------|--------|
| `EGX_افضل_فرص.pine` | `EGXOpp_Pro = 1` |
| `EGX_OPP_DESK.pine` | `EGXOppDesk_Pro = 1` |
| `EGX_OPP_META.pine` | `EGXOppMeta_Pro = 1` (optional) |
| `EGX_MEGA_SCREENER.pine` | `EGXMega_Pro = 1` (optional) |

**Desk Pro** = Opp Pro + Mega Pro (+ optional Meta Triple) in **one** script → `EGXOppDesk_Pro`.

## Cursor SDK (advanced)

For true nightly full-market rank, use [Cursor SDK](https://cursor.com/docs) against your own export or data feed — see `skills/sdk` in Cursor docs. Pine remains the **rule definition**; SDK runs **batch jobs**.
