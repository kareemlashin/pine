# EGX Tools — 100 ملف Pine

| النطاق | الملفات |
|--------|---------|
| 01–20 | `EGX_T_01_RSI.pine` … `EGX_T_20_WAVETREND.pine` — زخم |
| 21–35 | اتجاه |
| 36–50 | حجم |
| 51–60 | تقلب |
| 61–70 | SMC |
| 71–82 | موجات |
| 83–94 | أنظمة |
| 95–100 | بروفايل |

**إعادة التوليد:** من جذر المشروع:

```bash
python3 scripts/gen_egx_tools.py
```

**موحّد:** `../EGX_TOOLS_MASTER.pine` · **سوق:** OPP · BOARD200 · BOARD · x_OPP · **regen:** `scripts/gen_egx_tools_board200.py` · `gen_egx_tools_board.py`

كل أداة منفردة تُصدّر: `EGXT_<CODE>_Vote` · `_Bull` · `_Bear` (راجع `docs/EGX_TOOLS.md`).
