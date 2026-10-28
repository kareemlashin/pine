# EGX — هيكل السوق 2025 (للسكربتات)

> مرجع تشغيلي لما دخل في `EGX_Core` v3 والأخير / الخلاصة / قرار / BEST. ليس توصية.

## جلسة (Africa/Cairo · أحد–خميس)

| مرحلة | وقت | `EGX_SessId` | دخول جديد |
|--------|------|--------------|-----------|
| مزاد افتتاح | ≈ 08:30/09:30–10:00 | 1 | لا (اختياري) |
| مستمر | 10:00–14:15 | 2 | نعم |
| مزاد إغلاق | 14:15–14:25 | 3 | لا — الإغلاق الرسمي غالباً هنا |
| TAL | 14:25–14:30 | 4 | لا |
| خارج الجلسة | — | 0 | لا على الإطار داخل اليوم |

تخطّي الأحد: `skipSundayBuy` (افتراضي OFF). Daily لا يفلتر الساعة إلا إذا فعّلت «لا دخول خارج المستمر».

## حدود السعر

| لوحة | halt نشط | LULD | بيع مكشوف | داخل اليوم |
|------|----------|------|-----------|------------|
| نشط (EGX100) | ±10% | ±20% | لا | نعم |
| EGX30 | ±10% | ±20% | نعم (+ ETF EGX30) | نعم |
| SME تميّز / نايل | ±5% | ±10% | لا | نعم |
| غير نشط | ±5% | ±5% | لا | لا |

- **لا تشترِ** قرب halt اليومي (افتراضي: halt−1%، أو المدخل `حد يومي %`).
- **قفل LULD:** يوم ≥ luld−0.25% = لا مطاردة.
- **halt سوق:** EGX100 ≤ −10% → `EGX_MktHalt100=1` يمنع شراء جديد.

## تأكيد اختراق

افتراضي **إغلاقان** فوق مستوى الكسر + حجم. `إغلاقات لتأكيد الاختراق = 1` يعيد السلوك القديم (شمعة الكسر).

## حجم الصفقة

- مخاطرة **1–2%** من المحفظة (افتراضي 1.5%).
- سقف مشاركة **8% من ADV 20 يوم**.
- كيلي سقف **15%** (كان 25%).
- في Strategy: `qty_percent=` وليس `qty=` (الأخير كان يدخل 8 أسهم عند الإضافة).

ملء واعٍ: slippage في `strategy()` ثابت (2 سائل · 3 متوسط · 5 رقيق). الملف الرقيق يمنع الشراء أبكر من السائل. لا تملأ عند halt/LULD.

## Overlay أساسي (مدخلات يدوية)

| مدخل | دور |
|------|-----|
| عقبة أذون بعد الضريبة ≈ 20% | منع شراء إن عائد T1 < الأذون × أيام الاحتفاظ/365 |
| إيراد بالدولار | يخفف العقبة |
| أرباح خلال N شموع | منع 1–5 شموع قبل الحدث |
| هدف وسيط | منع مطاردة فوق 98% من الهدف |

## بيع على المكشوف

مسموح **فقط** EGX30 و ETF المرتبط. `PRO-S` في Volume MASTER يتطلب تعليم السهم كـ EGX30. باقي الملفات long-only.

## ما لا نضيفه

لا ملفات فوليوم جديدة. الكون RS = **20 سهماً** (`EGX_RS_BOARD`) وليس 217. قيادة قطاع تثبت **3 أيام** (`EGXSec_Lead3d`).

## Plots جديدة (الأخير)

`EGX_HaltWarn` · `EGX_LuldLock` · `EGX_MktHalt100` · `EGX_SessId` · `EGX_SundaySkip` · `EGX_HurdleOk` · `EGX_PosPctRisk` · `EGX_AdvCapShares`

## ماسحات / لوحات (نفس المنطق)

مدخل **لوحة** + `nearLimit` / `EGX*_Limit`: `EGX_SCREENER` · `EGX_META_SCREENER` · `EGX_MEGA_SCREENER` · `EGX_TOOLS_META_SCREENER` · `EGX_TOOLS_UNIFIED` · `EGX_افضل_فرص*` · `EGX_قرar_BOARD*` · `EGX_TOOLS_BOARD200` · `EGX_ALERT_HUB` · `EGX_VOLUME_ALERTS` (شراء فقط).

**سوق:** `EGX_MARKET_ONLY` → `EGXMkt_Halt100` مع `EGXMkt_BlockBuy`.

**Legacy ST:** `EGX_ANALYZER_STRATEGY` · `EGX_MARKET_INTELLIGENCE_PRO_STRATEGY` · `EGX_MASTER_ANALYZER_STRATEGY` · `EGX_MARKET_BEHAVIOR_STRATEGY` · `EGX_QUANT_PRO_STRATEGY` · `EGX_CYCLE_MASTER_STRATEGY` · `EGX_WAVE_HUNTER_PRO_STRATEGY` · `EGX_VOLUME_*_STRATEGY` · `EGX_TOOLS_LITE_STRATEGY`.

**TOOLS lite:** `EGX_TOOLS_QUICK` · `EGX_TOOLS_SCREENER` → `EGXTQ_Limit` · `EGXTScr_Limit`.
