# EGX Screener Matrix

Quick map of **filter plots** and how stacks relate. Timeframe **D** unless noted.

| Indicator | Primary filters | Role |
|-----------|-----------------|------|
| `EGX_TOOLS_OPP` | `EGXTTOpp_Pro=1`, sort `EGXTTOpp_Rank` ↓ | Per-symbol Tools lite13 screener |
| `EGX_TOOLS_BOARD200` | `EGXTTB200_Pass=1`, `Breadth`, `HotProCount` | Market 200/294 board (regen from فرص) |
| `EGX_OPP_x_TOOLS_BOARD` | `EGXOxT40_MegaCount` | Side-by-side Opp vs Tools (40 names) |
| `EGX_TOOLS_15M` | `EGXT15_BuyA=1`, `SessionOk=1` | Intraday lite13 + Cairo session |
| `EGX_TOOLS_MASTER` | `EGXT_BuyA`, `EGXT_Pro`, `EGXT_Score` | Full 100-tool chart decision |
| `EGX_MEGA_SCREENER` | `EGXMega_Pro`, `EGXMega_Triple` | Opp + Tools + Vol combined |
| `EGX_OPP_UNIFIED` | `EGXOppUni_Pro=1`, sort `EGXOppUni_Score` ↓ | Opp Pro + Vol Rank |
| `EGX_OPP_META` | `EGXOppMeta_Pro=1`, `EGXOppMeta_Triple` | Opp + Meta B1/Q |
| `EGX_SUPER_PASS` | `EGXSP_Pass=1`, `EGXSP_Pro=1`, `EGXSP_Veto=0` | 2-of-3 lanes + veto bitmask |
| `EGX_ALERT_HUB` | `EGXAlHub_Mega=1`, `EGXAlHub_ToolsPro=1`, `EGXAlHub_Veto=0` | Unified alerts on chart symbol |
| `EGX_CONFLICT` | `EGXCF_Conflict=1` | Buy lane vs exit lane clash |

## Veto bitmask (`EGXSP_Veto` / `EGXAlHub_Veto`)

| Bit | Meaning |
|-----|---------|
| 1 | Chase |
| 2 | Near limit / LULD |
| 4 | EGX30 bear pressure |
| 8 | EGX100 daily ≤ −10% |
| 16 | Sunday skip (Super Pass only) |
| 32 | Outside Cairo continuous session (Super Pass only) |

## Recommended flow

1. **Regime:** `EGX_RegimeOk=1` on any driver (Hub · Mega · Uni · Kh · Akhir · Q · Opp · BOARD200 · Mkt).
2. **Universe:** `EGX_TOOLS_BOARD200` or `EGX_TOOLS_OPP` screener.
3. **Confirm one name:** `EGX_TOOLS_MASTER` on the chart.
4. **Conflict check:** `EGX_CONFLICT` before sizing.

## Library

Publish `pine/EGX_T_Core.pine` on TradingView for shared lite13 logic: `import user/EGX_T_Core/1 as TC`.

Regenerate boards after فرص changes:

```bash
./scripts/sync_all_boards.sh
./scripts/check_pine.sh
```
