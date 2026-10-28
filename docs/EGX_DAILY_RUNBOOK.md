# EGX Daily Runbook

Morning workflow for the EGX Pine stack (تعليمي — not investment advice).

## 1. Market regime (2 min)

- Open **EGX30** daily with `EGX_ALERT_HUB` or `EGX_افضل_فرص_BOARD200` / `EGX_MARKET_ONLY` on a secondary pane.
- Confirm **`EGX_RegimeOk=1`** / no **`EGXAlHub_Veto`** (halt100, bear, limit).
- If EGX100 ≤ −10%: no new buys (`MktHalt100` plots).

## 2. Scan universe (5–10 min)

- **Stock screener:** `EGX_MEGA_SCREENER` / `EGX_UNIFIED_SCREENER` → `EGX_RegimeOk=1` + Pro plot · أو `EGX_TOOLS_OPP` → `EGXTTOpp_Pro=1`.
- **Board:** `EGX_افضل_فرص_BOARD200` → ★ leader, `Breadth`, `Heat`, `BuyCount`.
- **قرar:** `EGX_قرar_SCREENER` + `EGX_OPP_META` for Desk combo.
- **Strict pass:** `EGX_SUPER_PASS` → `EGXSP_Pass=1` and `EGXSP_Veto=0`.

## 3. Shortlist → chart (per symbol)

- Add **`EGX_TOOLS_MASTER`** on the candidate (full 100 votes, A/B, stops).
- Optional: **`EGX_CONFLICT`** — if `EGXCF_Conflict=1`, wait for alignment or skip.
- Intraday: enable **Cairo session** filter on MASTER/Opp if trading 15m/60m.

## 4. Alerts

- Hub: `EGXAlHub_Mega=1` (Opp Pro + Tools Pro + Vol Pro, no veto).
- Board: leader buy / Pro count alerts on `EGX_TOOLS_BOARD200`.

## 5. Intraday (optional)

- **`EGX_TOOLS_15M`** on 15m/60m with `EGXT15_SessionOk=1`.
- Confirm daily bias with **`EGX_TOOLS_MASTER`** on D before acting on 15m A/B.

## 6. Maintenance (when فرص board changes)

```bash
cd /path/to/pine
./scripts/sync_all_boards.sh
./scripts/check_pine.sh
```

## File cheat sheet

| Task | Script |
|------|--------|
| Single symbol decision | `EGX_TOOLS_MASTER.pine` |
| Screener field defs | `docs/EGX_SCREENER_MATRIX.md` |
| Backtest Opp lite | `EGX_TOOLS_OPP_STRATEGY.pine` |
| 6-name watch | `EGX_TOOLS_OPP_WATCHLIST.pine` |
