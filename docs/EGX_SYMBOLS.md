# EGX — قوائم رموز (Presets)

> عدّل الرموز على TradingView حسب توفرها. البادئة المعتادة: `EGX:SYMBOL`.

## EGX30 — سيولة (أمثلة)

| الرمز | ملاحظة |
|--------|--------|
| `EGX:COMI` | بنك |
| `EGX:SWDY` | |
| `EGX:TMGH` | |
| `EGX:HRHO` | |
| `EGX:FWRY` | |
| `EGX:UNIP` | |

## عدّاء / استثمار (أمثلة — راجع `EGX_قرar_PRESETS.pine`)

| الرمز | ملاحظة |
|--------|--------|
| `EGX:OCDI` | |
| `EGX:SKPC` | |
| `EGX:PHDC` | |
| `EGX:ACGC` | |
| `EGX:CNIN` | |

## مؤشرات

| الرمز | |
|--------|--|
| `EGX:EGX30` | المؤشر الرئيسي |
| `EGX:EGX70EWI` | EGX70 |
| `EGX:EGX100EWI` | EGX100 |

## أفضل فرص — 200 سهم

قائمة استيراد: [`EGX_WATCHLIST_200.txt`](EGX_WATCHLIST_200.txt) (200 رمز سائل).  
الاستخدام: [`EGX_افضل_فرص.md`](EGX_افضل_فرص.md) · لوحة `pine/EGX_افضل_فرص_BOARD.pine` (5 صفحات × 40).

```text
EGXOpp = 1
EGXOpp_Score ≥ 68
EGXOpp_Pro = 1
```

## ملفات تستخدم قوائم ثابتة

- `pine/EGX_افضل_فرص_BOARD200.pine` — 200/294 · Top N · `EGXOppB200_ReadyPct` · `Top1Score`
- `pine/EGX_افضل_فرص_WATCHLIST.pine` — 6 رموز · `EGXOppWL_LeaderScore`
- `pine/EGX_افضل_فرص_STRATEGY.pine` — باك‌تست · `EGXOppST_Pro`
- `pine/EGX_OPP_META.pine` — Opp×Meta · `EGXOppMeta_Pro`
- `pine/EGX_OPP_UNIFIED.pine` — Opp×Vol · `EGXOppUni_Pro` · `EGXAlHub_OppSpikePro`
- `pine/EGX_ALERT_HUB.pine` — `EGXAlHub_OppPro` · `EGXAlHub_OppBuy`
- `pine/EGX_افضل_فرص_BOARD.pine` — 200 رمز · 5 صفحات × 40 · فوري
- `pine/EGX_قرar_BOARD.pine` — 12 رمز
- `pine/EGX_قرar_BOARD20.pine` — 20 رمز
- `pine/EGX_قرar_PRESETS.pine` — عدّاء / EGX30 / فلسي
- `pine/EGX_SECTOR_BOARD.pine` — قطاعات · ثبات 3 أيام `EGXSec_Lead3d`
- `pine/EGX_RS_BOARD.pine` — مئوي 20 سهم `EGXRS_Top70`
- `pine/EGX_WATCHLIST.pine` — 6 رموز

## كون RS20 الافتراضي

`COMI · SWDY · TMGH · HRHO · FWRY · UNIP · ETEL · EAST · PHDC · OCDI · SKPC · ACGC · CNIN · EFIH · HELI · EMFD · ORWE · ABUK · MFPC · CIRA`

## ماسح موحّد

```text
EGXUni = 1
EGXUni_Pro = 1
```

## توافق قرar × فوليوم

```text
EGXQV_Agree = 1
```
