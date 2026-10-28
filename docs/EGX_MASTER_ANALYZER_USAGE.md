# EGX MASTER ANALYZER — التثبيت والاختبار (مرحلة 5–6)

## إضافة المؤشر إلى TradingView

1. افتح [TradingView](https://www.tradingview.com/chart/) واختر سهم EGX (مثال: `EGX:COMI` أو الرمز كما يظهر عندك).
2. **Pine Editor** → الصق محتوى `pine/EGX_MASTER_ANALYZER.pine` بالكامل.
3. **Save** → **Add to chart**.
4. للاختبار: الصق `pine/EGX_MASTER_ANALYZER_STRATEGY.pine` في سكربت **منفصل** (Strategy Tester).

## ضبط EGX

| الإعداد | توصية |
|---------|--------|
| `حد أدنى متوسط حجم` | ارفعه للأسهم الرقيقة (10k–100k+) |
| `إشارات عند الإغلاق` | اتركه **مفعّل** لتقليل الإشارات المتغيرة |
| `VWAP` | **يومي/60د/15د** — ليس للأسبوعي/الشهري |
| `Commission` (Strategy) | ~0.125% تقريبًا + `Slippage` 1–3 ticks |
| MTF | على 15د/60د تأكد أن الرمز له تاريخ intraday |

## التنبيهات

من **Create Alert** → Condition: **EGX MASTER** → اختر الشرط (BOS، تجميع، T1، …).  
يفضل **Once per bar close** مع `إشارات عند الإغلاق`.

## Composite /100

- **62+** مع `setupQuality`: فرصة محتملة (لا تعني ضمانًا).
- **52–62**: مراقبة.
- **&lt;45** أو تصريف: حذر.

## سينario اختبار عملي (منهجية — ليس نتيجة مسبقة)

1. **السهم**: اختر سهمًا متوسط السيولة (مثال COMI أو ETEL على **Daily**).
2. **تحقق اللوحة**: RVOL، تصنيف التجميع/التصريف، MTF (D/W/M).
3. **انتظر**: BOS أو retest دعم + RVOL ≥ 1 + Composite ≥ 62 + R/R ≥ 1.5.
4. **سجّل**: الدخول، الوقف (`stopSuggest`)، T1–T3، وتاريخ إلغاء السينario (كسر `investInv` أو `waveInv`).
5. **Strategy Tester**: قارن **EGX STRAT** مع **Buy & Hold** على نفس الفترة — راجع Max DD وعدد الصفقات.

> النتائج التاريخية ≠ أداء مستقبلي. الأسهم منخفضة السيولة قد لا تُنفَّذ فيها أوامر Backtest واقعيًا.

## إصلاحات v1.0 (100% compile)

- `ta.atr` + `ta.dmi` بدل `ta.adx` / `ta.taatr`
- MTF عبر دوال داخل `request.security`
- لوحة **/100** + Strategy منفصلة
