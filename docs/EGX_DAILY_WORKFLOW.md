# EGX — سير عمل يومي (Desk)

## Starter (رمز واحد)

1. **Daily** على السهم · `EGX_الاخير.pine` أو `EGX_الخلاصة.pine`.
2. تحقق: `EGX_RegimeOk` = 1 (أو لا `EGX_MktHalt100` · لا ضغط EGX30).
3. دخول: `EGX_BuyFlag` / `EGX_ScreenerPro` · تجنب `EGX_NearLimit` و `EGXAlHub_Chase`.
4. حجم: مخاطرة 1–2% + سقف ADV (استراتيجية أو يدوي).

## Pro (ماسح + قائمة)

1. شارت **`EGX_افضل_فرص_BOARD200.pine`** على أي رمز EGX (لوحة 200).
2. انتظر `EGXOppB200_ReadyPct` ≥ 88% · راقب `Breadth` / `Heat` / `Dispersion`.
3. فلتر Screener: `EGXScr_Pro` أو `EGXMega_Pro` أو `EGXUni_Pro` + `EGX_RegimeOk=1`.
4. **`EGX_ALERT_HUB`** على المرشحين: `EGXAlHub_OppPro` · `EGXAlHub_Triple` · `EGXAlHub_Votes≥3`.

## Desk (قرar + قطاع + باك‌تست)

1. `EGX_قرar.pine` + `EGX_SECTOR_BOARD` + `EGX_RS_BOARD`.
2. Hub موحّد + `EGX_META_SCREENER` (`EGXMeta_Triple`).
3. باك‌تست: `EGX_الاخير_STRATEGY` · `EGX_افضل_فرص_STRATEGY` (exec pad · جلسة · RS gate اختياري).
4. مرجع micro: [`EGX_MICROSTRUCTURE.md`](EGX_MICROSTRUCTURE.md) · وصفات: [`EGX_SCREENER_RECIPES.md`](EGX_SCREENER_RECIPES.md).

## قبل الإغلاق

- إغلاق الشمعة مفعّل للتنبيهات.
- لوحة السهم (SME ±5/10 · نشط ±10 ثم LULD ±20).
- EGX100 ≤ −10% → لا صفقات long جديدة (مؤشرات `MktHalt100`).
