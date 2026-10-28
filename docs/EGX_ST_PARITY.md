# EGX — parity الاستراتيجيات vs المؤشر

## مرجع ذهب

| ST | مؤشر | ملاحظة |
|----|--------|--------|
| `EGX_الاخير_STRATEGY` | `EGX_الاخير` | `mirrorBuyFlag` · exec pad · جلسة · halt100 · risk qty |
| `EGX_افضل_فرص_STRATEGY` | `EGX_افضل_فرص` | + exec pad · session · mirror · RS gate · partial/trail |
| `EGX_BEST_STRATEGY` | `EGX_BEST` | مبسّط |
| `EGX_ANALYZER_STRATEGY` | Analyzer legacy | halt · break · risk qty |

## فرص ST — ما يطابق الأخير ST

- ✅ halt/LULD + `execPad`
- ✅ EGX100 halt · Sunday skip
- ✅ 2-bar break · risk 1.5% · ADV cap
- ✅ partial 50% · trail
- ⚠️ overlay (T-bill / earnings / broker TP) — **غير منسوخ** (موجود في الأخير indicator أكثر من ST)
- ⚠️ RS percentile 20 — gate اختياري `useRsGate` (RS spread > 0) وليس board rank

## Legacy indicators (limit فقط)

Analyzer · Quant · Wave · VBS/CLX/CFM/MM · Tools strip · ZAMANI:  
`EGX_NearLimit` + veto على buy — **ليس** full Akhir gates.

## BOARD vs Symbol alerts

- **BOARD200**: leader / breadth / regime plots — alert على شارت اللوحة.
- **Hub / Opp**: alert **لكل رمز** في watchlist.
