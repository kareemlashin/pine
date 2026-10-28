# EGX — تنبيهات TradingView

## إعداد عام

1. **Create Alert** على الشارت الذي عليه المؤشر.
2. Condition: اسم المؤشر → اختر الشرط.
3. **Once per bar close** إذا «إغلاق الشمعة» مفعّل في المؤشر.
4. Notifications: App / Email / Webhook حسب حاجتك.

## EGX الأخير (أهم 10)

| الشرط | متى |
|--------|-----|
| EGX منطقة شراء | `EGX_BuyFlag` / buyConfluence |
| EGX نجاح الماسح | ScreenerPass |
| EGX ماسح احترافي | ScreenerPro |
| EGX فرصة قوية | Opp + B+ |
| EGX كسر دعم | خروج |
| EGX مطarدة | لا شراء |
| EGX قرب حد +10% | veto |
| EGX اختراق مؤكد | break |
| EGX بوابات 9/10 | جودة عالية |
| EGX JSON | فعّل «تنبيه JSON (webhook)» في المؤشر |
| Vol Rank | `EGX_VolRankPass` (بوابة اختيارية) |

## EGX الخلاصة

- EGX خلاصة — شراء نهائي  
- EGX خلاصة — ماسح Pro  
- EGX خلاصة — كسر دعم  
- EGX خلاصة — مطarدة  

## EGX Alert Hub

`pine/EGX_ALERT_HUB.pine` — على **كل رمز** في قائمتك (ليس BOARD200).

| Plot | استخدام |
|------|---------|
| `EGXAlHub_Buy` / `Exit` / `Warn` | قنوات أساسية |
| `EGX_RegimeOk` | 1 = مسموح long سوقياً |
| `EGXAlHub_MktHalt100` | EGX100 −10% |
| `EGXAlHub_OppPro` / `OppBuy` | مسار أفضل فرص D |
| `EGXAlHub_Tools` · `QBuy` · `VolPro` | مسارات فرعية |
| `EGXAlHub_Invest` | OppPro + Tools + Buy fuerte |
| `EGXAlHub_Triple` | توافق كامل + regime |
| `EGXAlHub_Votes` | ≥3 للفلترة في Screener |
| `EGXAlHub_Mega` / `ToolsPro` / `OppPass` | مسارات Desk — [`EGX_SCREENER_MATRIX.md`](EGX_SCREENER_MATRIX.md) |
| `EGXWL` | `EGX_RegimeOk` على محفظة 6 رموز |
| `EGXAlHub_Any` | أي إشارة |

## BOARD200 (لوحة 200)

`pine/EGX_افضل_فرص_BOARD200.pine` — شارت **واحد** · تنبيهات `LeadChg` · `LeaderBuy` · `ReadyPct` · `MktHalt100` — لا تخلط مع Hub على نفس الشرط إلا إذا فهمت الفرق (سوق vs رمز).

## EGX Uni / Q×V

- `EGXUni_Pro` / `EGXUni_Pass` — `EGX_UNIFIED_SCREENER.pine`
- `EGXQV_Agree` — `EGX_قرar_QxV.pine`

## Webhook JSON (الأخير)

فعّل **تنبيه JSON (webhook)** في `EGX_الاخير.pine`.  
الرسالة تحتوي: `event`, `sym`, `rank`, `score`, `opp`, `cycle`, `entry`, `stop`, `t1`, …

مثال استخدام: Zapier / n8n / سيرفرك — **لا تشارك URL علناً**.

## Strategy alerts

على `EGX_الاخير_STRATEGY` / `EGX_الخلاصة_STRATEGY` / `EGX_قرar_STRATEGY`: استخدم تنبيهات **Order fills** من TradingView أو plots `EGXQ_ST_Buy` / `EGXQ_ST_VolPass`.
