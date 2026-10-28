# EGX — Pine Scripts (بورصة مصر)

## مسارات جاهزة

| مستوى | ماذا تفتح |
|--------|-----------|
| **Starter** | `EGX_الاخير` أو `EGX_الخلاصة` · Daily · [`EGX_DAILY_WORKFLOW.md`](docs/EGX_DAILY_WORKFLOW.md) |
| **Pro** | `EGX_SCREENER` / `EGX_UNIFIED_SCREENER` + `EGX_ALERT_HUB` |
| **Desk** | `BOARD200` + `EGX_META_SCREENER` + `EGX_قرar` + [`EGX_CONFLUENCE.md`](docs/EGX_CONFLUENCE.md) |

## ابدأ من هنا

| الهدف | الملف |
|--------|--------|
| **100 أداة في شارت واحد** | `pine/EGX_TOOLS_MASTER.pine` · باك‌تست `EGX_TOOLS_MASTER_STRATEGY.pine` · فهرس [`docs/EGX_TOOLS.md`](docs/EGX_TOOLS.md) |
| **TOOLS سريع / ماسح / محفظة** | `OPP` · `15M` · `Opp×Tools BOARD40` · `BOARD200` (~1050L parity) · `SUPER_PASS` · `CONFLICT` · `T_Core` · + `QUICK`/… |
| **ملف لكل مؤشر (01–100)** | `pine/tools/EGX_T_01_RSI.pine` … `EGX_T_100_REGIME.pine` |
| الزمني / BSV / صفقات كبيرة | `pine/EGX_ZAMANI.pine` · `EGX_BSV.pine` · `EGX_BIGTRADES.pine` |
| **أفضل فرص (200 سهم)** | **`BOARD200`** · **`WATCHLIST` (6–12)** · **`STRATEGY`** · **`EGX_OPP_META`** · **`EGX_OPP_UNIFIED`** · ماسح `EGX_افضل_فرص.pine` · [`docs/EGX_افضل_فرص.md`](docs/EGX_افضل_فرص.md) · `scripts/validate_egx_watchlist.py` |
| تحليل كامل | `pine/EGX_الاخير.pine` (v1.2 — halt/LULD · حجم 1–2%) |
| قرار سريع على الشارت | `pine/EGX_الخلاصة.pine` |
| قرار DNA / Ultra / Board | `pine/EGX_قرar.pine` · `QUICK` · `BOARD` · `BOARD20` |
| توافق قرar × عدّاء | `pine/EGX_قرar_DUAL.pine` |
| باك‌تست (مرآة المؤشر) | `pine/EGX_الاخير_STRATEGY.pine` → **مرآة EGX_BuyFlag** |
| باك‌تست المحلل (legacy) | `pine/EGX_ANALYZER_STRATEGY.pine` — halt/LULD · 2-bar break · risk qty |
| باك‌تست الخلاصة / قرar / عدّاء | `EGX_الخلاصة_STRATEGY` · `EGX_قرar_STRATEGY` · `EGX_RUNNER_INVEST_STRATEGY` |
| ماسح بدون overlay | `pine/EGX_SCREENER.pine` · `EGX_قرar_SCREENER` · `EGX_VOLUME_SCREENER` |
| **ماسح مركّب** (أخير+Vol+قرar) | `pine/EGX_META_SCREENER.pine` |
| **Mega Screener** (فرص+Tools+Vol) | `pine/EGX_MEGA_SCREENER.pine` → `EGXMega_Pro=1` |
| **Opp × Meta** | `pine/EGX_OPP_META.pine` → `EGXOppMeta_Pro` · `EGX_RegimeOk` |
| **Opp Desk** (Opp∩Mega∩Meta) | `pine/EGX_OPP_DESK.pine` → `EGXOppDesk_Pro` |
| **Super Pass** (2-of-3) | `pine/EGX_SUPER_PASS.pine` → `EGXSP_Pro` · `EGXSP_Veto=0` |
| **Conflict** (Buy vs Exit) | `pine/EGX_CONFLICT.pine` → `EGXCF_Conflict=0` قبل الدخول |
| **ماسح موحّد** (فني Pro + Vol Rank) | `pine/EGX_UNIFIED_SCREENER.pine` → `EGXUni_Pro=1` |
| **قرar × فوليوم** | `pine/EGX_قرar_QxV.pine` → `EGXQV_Agree=1` |
| **نظام سوق فقط** | `pine/EGX_MARKET_ONLY.pine` |
| **Alert Hub** | `pine/EGX_ALERT_HUB.pine` → `EGXAlHub_Mega` · `ToolsPro` · `Veto` |
| **Screener matrix / runbook** | [`docs/EGX_SCREENER_MATRIX.md`](docs/EGX_SCREENER_MATRIX.md) · [`docs/EGX_DAILY_RUNBOOK.md`](docs/EGX_DAILY_RUNBOOK.md) |
| **قطاعات RS** | `pine/EGX_SECTOR_BOARD.pine` → `EGXSec_Lead3d` |
| **RS مئوي 20 سهم** | `pine/EGX_RS_BOARD.pine` → `EGXRS_Top70` |
| Rank لـ 6 أسهم | `pine/EGX_WATCHLIST.pine` · `EGX_قرar_WATCHLIST` · `EGX_RUNNER_WATCHLIST` |
| استثمار عدّاء | `pine/EGX_RUNNER_INVEST.pine` · ماسح `EGX_RUNNER_SCREENER` |
| فوليوم all-in-one | `pine/EGX_VOLUME_MASTER.pine` — `docs/EGX_VOLUME.md` |
| بديل بسيط | `pine/EGX_BEST.pine` |

**مرجع القرار:** [`docs/EGX_الخلاصة.md`](docs/EGX_الخلاصة.md) · **رموز:** [`docs/EGX_SYMBOLS.md`](docs/EGX_SYMBOLS.md)

## تثبيت TradingView

1. Pine Editor → الصق السكربت → Save → Add to chart.
2. رمز EGX (مثال `EGX:COMI`) · الإطار **Daily** للقرار الرئيسي.
3. Strategy: سكربت **منفصل** في Pine Editor (نوع Strategy).

## Screener — `EGX_RegimeOk`

Plot مشترك على معظم الماسحات/القرار: **1** = لا ضغط EGX30 (إن مفعّل) **و** لا EGX100 −10%. ادمجه في كل فلتر Pro.

## Screener — أسماء الحقول (أساسي)

| المؤشر | Buy | Pro | تمييز |
|--------|-----|-----|--------|
| الأخير | `EGX_BuyFlag` | `EGX_ScreenerPro` | `EGX_Akhir` |
| الأخير + B1 | `EGX_VolPro` | `EGX_ScreenerVolPro` | — |
| الخلاصة | `EGXKh_BuyFlag` | `EGXKh_ScreenerPro` | `EGXKh` |
| TOOLS MASTER | `EGXT_Buy` | `EGXT_Pro` | `EGXT_Score` |
| BEST | `EGXB_Buy` | `EGXB_Screener` | — |
| ماسح | `EGXScr_BuyFlag` | `EGXScr_Pro` | `EGXScr` |
| قرar | `EGXQ_Buy` | `EGXQ_ScreenerPro` | `EGXQ_Qarar` |
| عدّاء | `EGXR_Buy` | `EGXR_ScreenerPro` | `EGXR_Runner` |
| مركّب | `EGXMeta_Triple` | `EGXMeta_AkhirPro` | `EGXMeta` |
| فوليوم | `EGVScr_Pro` | — | `EGVScr` |
| موحّد | `EGXUni_BuyFlag` | `EGXUni_Pro` | `EGXUni` |
| Q×V | `EGXQV_Agree` | — | `EGXQV` |
| Hub | `EGXAlHub_Buy` | `EGXAlHub_OppPro` / `Triple` | `EGXAlHub` · `EGX_RegimeOk` |
| **أفضل فرص** | `EGXOpp_Buy` | `EGXOpp_Pro` | `EGXOpp` |
| Opp×Vol | `EGXOppUni_Buy` | `EGXOppUni_Pro` | `EGXOppUni` |
| Opp×Meta | `EGXOppMeta_Buy` | `EGXOppMeta_Pro` | `EGXOppMeta` |

## باك‌تست — عمولة و slippage

- عمولة افتراضية **0.125%** (EGX تقريباً).
- Slippage في `strategy(...)`: **2** سائل · **3** متوسط · **5** رقيق — [`docs/EGX_BACKTEST_CHECKLIST.md`](docs/EGX_BACKTEST_CHECKLIST.md).
- حجم افتراضي: **مخاطرة 1.5%** + سقف **8% ADV** — ليس 10% equity أعمى. إضافة دورة 7 تستخدم `qty_percent=`.

## مكتبة مشتركة

`pine/EGX_Core.pine` **v4** — انشر كـ Library ثم `import username/EGX_Core/4` (`f_regimeOk` · exec pad · nearLimit composite).  
`pine/EGX_OppCore.pine` — قطاع/limits (اختياري) · **BOARD200** يطابق Screener على D (حدود ±10 ثم LULD ±20 · لوحات · جلسة · halt EGX100 · حجم 1–2% · B1 · acc/dist · RS).

هيكل السوق: [`docs/EGX_MICROSTRUCTURE.md`](docs/EGX_MICROSTRUCTURE.md)

## لا تضف ملفات فوليوم جديدة

عائلة الـ 87 كافية. القرار اليومي = الأخير + الخلاصة/قرار + ماسح واحد.

## ملفات legacy (مرجع فقط)

[`docs/legacy/README.md`](docs/legacy/README.md) — Analyzer · Quant · Cycle · Wave · Behavior · Master · MI.

## توثيق إضافي

- [`docs/EGX_الاخير.md`](docs/EGX_الاخير.md)
- [`docs/EGX_ALERTS.md`](docs/EGX_ALERTS.md)
- [`docs/EGX_TOOLS.md`](docs/EGX_TOOLS.md)
- [`docs/EGX_VOLUME.md`](docs/EGX_VOLUME.md)
- [`docs/EGX_MICROSTRUCTURE.md`](docs/EGX_MICROSTRUCTURE.md)
- [`docs/EGX_BACKTEST_CHECKLIST.md`](docs/EGX_BACKTEST_CHECKLIST.md)
- [`docs/EGX_RANK_SENSITIVITY.md`](docs/EGX_RANK_SENSITIVITY.md)
- [`docs/EGX_افضل_فرص.md`](docs/EGX_افضل_فرص.md)
- [`docs/EGX_DAILY_WORKFLOW.md`](docs/EGX_DAILY_WORKFLOW.md) · [`EGX_CONFLUENCE.md`](docs/EGX_CONFLUENCE.md) · [`EGX_SCREENER_RECIPES.md`](docs/EGX_SCREENER_RECIPES.md)
- [`docs/EGX_COMPILE_SMOKE.md`](docs/EGX_COMPILE_SMOKE.md) · [`EGX_ST_PARITY.md`](docs/EGX_ST_PARITY.md)
