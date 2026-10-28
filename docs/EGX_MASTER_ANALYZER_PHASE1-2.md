# EGX MASTER ANALYZER — المرحلة 1 و 2

## المرحلة الأولى: ما يمكن وما لا يمكن في Pine Script v6

### ممكن (ضمن بيانات الشارت)
| القدرة | المصدر / الآلية |
|--------|----------------|
| تحليل متعدد الأطر | `request.security()` مع `barmerge.lookahead_off` وإغلاق الشمعة على TF الأعلى |
| HH/HL, BOS, CHoCH | قمم/قيعان `ta.pivothigh` / `ta.pivotlow` بعد تأكيد النافذة |
| EMA, RSI, MACD, ATR, ADX | دوال `ta.*` القياسية |
| VWAP | `ta.vwap()` — مناسب للجلسات داخل اليوم؛ على اليومي/الأسبوعي يُعرض مع تحذير |
| دعم/مقاومة ديناميكية | مستويات من المحاور + نطاقات ATR حولها |
| Relative Volume, OBV, CMF, A/D | حجم الشمعة + `ta.obv`, `ta.cmf`, `ta.accdist` |
| Fibonacci | حساب يدوي من آخر موجة محورية مؤكدة |
| لوحة معلومات، صناديق، خطوط محدودة | `table`, `box`, `line`, `label` ضمن الحدود |
| تنبيهات | `alertcondition()` بشروط غير متكررة (`barstate.isconfirmed`) |
| استراتيجية منفصلة | ملف `strategy()` مع عمولة وانزلاق |

### مستحيل أو غير موثوق (لا يُدّعى في المؤشر)
| الطلب | السبب |
|-------|--------|
| Footprint, Delta, Bid/Ask, صفقات منفردة | غير متاحة في Pine لمعظم رموز EGX |
| تحديد «مؤسسات / ميكر» بالهوية | لا توجد بيانات طرف مقابل |
| قيمة تداول EGP دقيقة لكل سهم | تعتمد على وحدات الحجم من المزود؛ قد تكون حجمًا أو تick volume |
| بيانات مالية أساسية (P/E, أرباح) | خارج OHLCV إلا ما يوفره `syminfo.*` المحدود |
| Elliott Wave «مؤكد» | عدّ استكشافي؛ يُعرض «غير محسوم» عند ضعف البنية |
| Gann / توقيت القمة مسبقًا | نوافذ احتمالية فقط بعد تثبيت المحاور |
| MTF بدون أي تأخير | تأكيد pivot يتأخر بعد `pivotLen` شموع — ليس repainting لكن تأخير طبيعي |
| اختبار 252 جلسة على كل TF | على intraday قد لا تتوفر 252 شمعة يومية في التاريخ |
| إشارات لا تختفي | إشارات «مبكرة» على الشمعة الحالية قد تتغير حتى الإغلاق — مُوسَمة صراحة |

### قيود الأداء والمنصة
- حدود: عدد `request.security`, الخطوط, الصناديق, حجم السكربت.
- الأسهم منخفضة السيولة: RVOL قد يقفز؛ يُستخدم حد أدنى للحجم المتوسط.
- تجزئة الأسهم / زيادة رأس المال: مقارنات حجم تاريخية طويلة قد تتشوه — تحذير في اللوحة.
- حدود EGX اليومية: لا تُنمذج رسميًا في Pine؛ يُذكر كتحذير نوعي.

---

## المرحلة الثانية: تصميم معماري مختصر

```
┌─────────────────────────────────────────────────────────────┐
│                    EGX MASTER ANALYZER                       │
├──────────────┬──────────────┬──────────────┬────────────────┤
│  MTF Layer   │  Structure   │  Momentum    │  Levels/Zones  │
│  D/W/M/60/15 │  Pivot BOS   │  RSI MACD    │  S/R boxes     │
│  EMA stack   │  CHoCH HH/HL │  ADX ATR     │  Fib targets   │
├──────────────┴──────────────┴──────────────┴────────────────┤
│  Volume Intelligence (أولوية)                                │
│  RVOL | CMF/OBV/A-D | acc/dist score | vol climax patterns   │
├──────────────────────────────────────────────────────────────┤
│  Time Module          │  Wave Module (heuristic)              │
│  bars since pivot     │  3-swing scenario + invalidation      │
│  Gann windows (opt)   │  alt scenario / «غير محسوم»           │
├──────────────────────────────────────────────────────────────┤
│  Mode A Swing | Mode B Invest → sub-scores                   │
│  Composite 0–100 (weights in inputs) → verdict Arabic        │
├──────────────────────────────────────────────────────────────┤
│  Dashboard table | Alerts | Optional early vs confirmed      │
└─────────────────────────────────────────────────────────────┘
                              │
                    EGX_MASTER_ANALYZER_STRATEGY.pine
                    (entries: confirmed + score + mode filters)
```

### مصادر الإشارة (لا مؤشر واحد يكفي)
- **اتجاه**: MTF EMA20/50 + بنية HH/HL.
- **زخم**: RSI + MACD histogram + ADX.
- **حجم**: RVOL + CMF + OBV slope + شروط تجميع/تصريف.
- **بنية**: BOS/CHoCH + اختبار مستوى.
- **دخول**: تقارب منطقة + R/R ≥ حد + Composite ≥ حد (وضع A أو B).

### منطق anti-repaint
- محاور، BOS، CHoCH، التصنيف النهائي، التنبيهات الافتراضية: **`barstate.isconfirmed`**.
- «مبكرة»: على الشمعة الجارية فقط، مع نص «غير مؤكدة».

---

الملفات:
- `pine/EGX_MASTER_ANALYZER.pine` — المؤشر
- `pine/EGX_MASTER_ANALYZER_STRATEGY.pine` — الاستراتيجية
- `docs/EGX_MASTER_ANALYZER_USAGE.md` — المرحلة 5 و 6
