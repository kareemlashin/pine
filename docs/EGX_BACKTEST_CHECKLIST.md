# EGX — checklist باك‌تست

> منهجية — ليست نتيجة مسبقة. OHLCV + عمولة تقريبية.

## 1. إعداد Strategy Tester

| البند | قيمة موصى |
|--------|-----------|
| Symbol | `EGX:COMI` أو `EGX:ETEL` (سائل) + سهم رقيق للاختبار |
| Timeframe | **D** |
| Capital | 100,000 EGP |
| Commission | **0.125%** |
| Slippage | سائل **2** · متوسط **3** · رقيق **5** ticks |
| Position size | مخاطرة **1.5%** + سقف **8% ADV** (أو Kelly ≤ 15% في الأخير ST) |

غيّر slippage في السطر الأول من ملف `.pine` Strategy:

```pine
strategy(..., slippage=3, ...)
```

## 2. مواءمة مع المؤشر

| الهدف | الإعداد |
|--------|---------|
| مطابقة `EGX_BuyFlag` | `EGX_الاخير_STRATEGY` → **مرآة EGX_BuyFlag = ON** |
| منطق الخلاصة | `EGX_الخلاصة_STRATEGY.pine` |
| backtest أصرّ (أنماط) | مرآة **OFF** + فلاتر Pro/gates |

## 3. سجل يدوي (10–20 صفقة)

لكل صفقة: تاريخ · دخول · وقف · T1 · هل جزئي 50% · سبب الخروج · هل تطابق `primaryDec` على الشارت.

## 4. مقارنة

- Strategy vs **Buy & Hold** على نفس الفترة.
- راقب: **Max DD** · **# trades** · **Profit factor** · فترات 2022–2024 ضغط EGX.

## 5. قيود

- أسهم illiquid: fills غير واقعية. الملف «EGX رقيق» يمنع الشراء أبكر من halt.
- لا تملأ صفقة قرب halt اليومي أو LULD.
- إضافة دورة 7: `qty_percent=` (نسبة من المحفظة) وليست عدد أسهم.
- intraday على رموز بدون تاريخ 15m/60m كامل → MTF ضعيف.
- النتائج التاريخية ≠ أداء مستقبلي.

راجع [`EGX_MICROSTRUCTURE.md`](EGX_MICROSTRUCTURE.md).
