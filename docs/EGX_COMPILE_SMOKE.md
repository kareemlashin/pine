# EGX — Compile smoke (TradingView)

التحقق يدوياً في Pine Editor — لا CI في الم repo.

## ترتيب مقترح

1. `pine/EGX_Core.pine` — **Library** → Publish → `import …/EGX_Core/4` (اختياري؛ معظم الملفات inline).
2. `pine/EGX_الاخير.pine`
3. `pine/EGX_ALERT_HUB.pine`
4. `pine/EGX_افضل_فرص_BOARD200.pine` (max `request.security` — انتظر تحميل الدفعات)
5. `pine/EGX_MEGA_SCREENER.pine` · `EGX_UNIFIED_SCREENER.pine`
6. Strategies: `EGX_الاخير_STRATEGY` · `EGX_افضل_فرص_STRATEGY`

## أخطاء شائعة

| الخطأ | سبب |
|--------|-----|
| `Undeclared identifier execProfile` | أضف inputs في ST أو أعد سحب آخر `EGX_افضل_فرص_STRATEGY` |
| input في منتصف الملف | انقل `input.*` لأعلى المؤشر (مثل Uni Screener) |
| `nearLimitLim` | legacy patch — تأكد inputs `egxBoardLim` |
| BOARD200 بطيء | طبيعي · `ReadyPct` < 100 حتى تكتمل الدفعات |

## بعد التعديل

- Save → Add to chart · افتح **Data window** للـ plots.
- Screener: أضف عمود plot مرة واحدة من أي شارت مرجعي.
