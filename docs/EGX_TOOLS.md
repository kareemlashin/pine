# EGX — 100 أداة (Tools)

> منهج الرؤية الشاملة: **8 مجموعات × 100 صوت** (+1 صاعد / 0 محايد / −1 هابط).  
> البيانات: **OHLCV فقط** — تقديرات، **ليست توصية استثمارية**.

## ابدأ من هنا

| الهدف | الملف |
|--------|--------|
| **شارت موحّد (الكل)** | `pine/EGX_TOOLS_MASTER.pine` |
| **باك‌تست** | `pine/EGX_TOOLS_MASTER_STRATEGY.pine` |
| **قرار سريع (24 صوت)** | `pine/EGX_TOOLS_QUICK.pine` → `EGXTQ_*` |
| **ماسح lite** | `pine/EGX_TOOLS_SCREENER.pine` → `EGXTScr_*` |
| **Rank 6 أسهم** | `pine/EGX_TOOLS_WATCHLIST.pine` → `EGXTTWL_*` |
| **محفظة 6/12** | `pine/EGX_TOOLS_BOARD.pine` → `EGXTTBD_*` |
| **تنبيهات lite** | `pine/EGX_TOOLS_ALERTS.pine` → `EGXTAl_*` |
| **8 مجموعات (lite)** | `pine/EGX_TOOLS_GROUPS.pine` → `EGXTGrp_A` … `EGXTGrp_H` |
| **Tools × Vol** | `pine/EGX_TOOLS_QxV.pine` → `EGXTxV_Agree=1` |
| **ماسح ثلاثي T+Vol+Q** | `pine/EGX_TOOLS_META_SCREENER.pine` → `EGXTMeta_Triple=1` |
| **فرص السوق (رمز واحد)** | `pine/EGX_TOOLS_OPP.pine` → `EGXTTOpp_Pro=1` · `EGXTTOpp_Rank` |
| **باك‌تست Opp lite** | `pine/EGX_TOOLS_OPP_STRATEGY.pine` → `EGXTTOppST_Pro` |
| **محفظة Opp 6** | `pine/EGX_TOOLS_OPP_WATCHLIST.pine` → `EGXTTOppWL_*` |
| **Super Pass 2-of-3** | `pine/EGX_SUPER_PASS.pine` → `EGXSP_Pass` · `EGXSP_Veto` |
| **تعارض Buy/Exit** | `pine/EGX_CONFLICT.pine` → `EGXCF_Conflict` |
| **مكتبة lite13** | `pine/EGX_T_Core.pine` (انشر ثم `import user/EGX_T_Core/1`) |
| **لوحة 200/294** | `pine/EGX_TOOLS_BOARD200.pine` → `EGXTTB200_*` (regen: `./scripts/sync_all_boards.sh`) |
| **200 سهم · 5 صفحات** | `pine/EGX_TOOLS_BOARD.pine` → `EGXTTB_*` (regen: `python3 scripts/gen_egx_tools_board.py`) |
| **فرص × Tools** | `pine/EGX_TOOLS_x_OPP.pine` → `EGXTxOpp_Mega=1` |
| **Opp × Tools لوحة 40** | `pine/EGX_OPP_x_TOOLS_BOARD.pine` → `EGXOxT40_MegaCount` |
| **15 دقيقة intraday** | `pine/EGX_TOOLS_15M.pine` → `EGXT15_BuyA` |
| **باك‌تست lite** | `pine/EGX_TOOLS_LITE_STRATEGY.pine` |
| **شريط على الشارت** | `pine/EGX_TOOLS_CHART_STRIP.pine` → `EGXTStrip_*` |
| **Mega (فرص+Tools+Vol)** | `pine/EGX_MEGA_SCREENER.pine` → `EGXMega_Triple=1` |
| **موحّد Tools+Vol+فني** | `pine/EGX_TOOLS_UNIFIED.pine` → `EGXTUni_Pro=1` |
| **أداة واحدة** | `pine/tools/EGX_T_01_RSI.pine` … `EGX_T_100_REGIME.pine` |
| الزمني (29 مؤشر + نوافذ) | `pine/EGX_ZAMANI.pine` |
| شراء/بيع فوليوم | `pine/EGX_BSV.pine` |
| صفقات كبيرة | `pine/EGX_BIGTRADES.pine` |

**تثبيت الماستر:** Pine Editor → الصق `EGX_TOOLS_MASTER.pine` → Save → Add to chart (إطار **D**).  
القرار من اللوحة يمين: شراء A / شراء B / خروج / انتظار.  
جدول الـ 100 صوت: فعّل «جدول 100 صوت».

## Screener

**100 صوت كامل (شارت واحد):** حقول `EGXT_*` من `EGX_TOOLS_MASTER`.  
**ماسح خفيف (Watchlist):** `EGXTScr_*` من `EGX_TOOLS_SCREENER` — 16 صوت تقريبي، أسرع على مئات الرموز.

| الحقل | المعنى |
|--------|--------|
| `EGXT_Buy` | شراء A أو B |
| `EGXT_BuyA` | شراء ممتاز (مكان + أموال + 5/6 شروط) |
| `EGXT_Pro` | BuyA + R/R + ≥45 أخضر + Clarity≥3 + مش ضغط EGX30 |
| `EGXT_Score` | السكور المرجّح % |
| `EGXT_Net` | أخضر − أحمر |
| `EGXT_Green` / `EGXT_Red` | عدد الأصوات |
| `EGXT_RR` | عائد/مخاطرة لـ T1 |
| `EGXT_Hits` | شروط الصفقة /6 |

كل ملف منفرد: `EGXT_<CODE>_Vote` · `EGXT_<CODE>_Bull` · `EGXT_<CODE>_Bear`

## قرار الشراء (الماستر)

شروط **A:** سيولة + مش قرب +10% + مش ضغط EGX30 + مش مطاردة + R/R≥1.5 + مكان (فيبو/داروفاس/خصم) + أموال (A/D+CMF) + ≥5/6 شروط + سكور ≥ الحد.  
**B:** نفس الفلاتر مع مكان و ≥4/6 بدون شرط الأموال الكامل.  
**خروج:** شاندلير ينقلب أو كسر داروفاس أو السكور يقطع الحد السالب أو BOS هابط.

Strategy: عمولة **0.125%** · slippage **3** · جزئي 50% عند منتصف T1 ثم trail.

### Meta / توافق

| الحقل | المعنى |
|--------|--------|
| `EGXTMeta_Triple` | Tools Pro + Vol Pro + Q-lite |
| `EGXTMeta_ToolsPro` | شراء A lite + 🟢 كافية |
| `EGXTxV_Agree` | Tools buy + B1/Net فوليوم |
| `EGXTGrp_Total` | مجموع مرجّح lite (8 مجموعات) |
| `EGXAlHub_Tools` | Tools lite داخل Alert Hub |
| `EGXAlHub_ToolsPro` | Tools lite13 Pro (D) |
| `EGXAlHub_Mega` | Opp Pro + Tools Pro + Vol Pro، بدون veto |
| `EGXAlHub_Veto` | bitmask (chase/limit/bear/halt100) |

**Runbook / matrix:** [`EGX_SCREENER_MATRIX.md`](EGX_SCREENER_MATRIX.md) · [`EGX_DAILY_RUNBOOK.md`](EGX_DAILY_RUNBOOK.md)

## أ — زخم (20)

| # | الملف | الأداة |
|---|--------|--------|
| 01 | `EGX_T_01_RSI.pine` | RSI |
| 02 | `EGX_T_02_CRSI.pine` | Connors RSI-2 |
| 03 | `EGX_T_03_STOCH.pine` | Stochastic |
| 04 | `EGX_T_04_STOCHRSI.pine` | StochRSI |
| 05 | `EGX_T_05_MACD.pine` | MACD |
| 06 | `EGX_T_06_CCI.pine` | CCI |
| 07 | `EGX_T_07_WILLIAMSR.pine` | Williams %R |
| 08 | `EGX_T_08_ROC.pine` | ROC |
| 09 | `EGX_T_09_MFI.pine` | MFI |
| 10 | `EGX_T_10_UO.pine` | Ultimate Oscillator |
| 11 | `EGX_T_11_TSI.pine` | TSI |
| 12 | `EGX_T_12_FISHER.pine` | Fisher |
| 13 | `EGX_T_13_CMO.pine` | CMO |
| 14 | `EGX_T_14_PPO.pine` | PPO |
| 15 | `EGX_T_15_AO.pine` | Awesome Oscillator |
| 16 | `EGX_T_16_TRIX.pine` | TRIX |
| 17 | `EGX_T_17_KST.pine` | KST |
| 18 | `EGX_T_18_COPPOCK.pine` | Coppock |
| 19 | `EGX_T_19_DPO.pine` | DPO |
| 20 | `EGX_T_20_WAVETREND.pine` | WaveTrend (Cipher proxy) |

## ب — اتجاه (15)

| # | الملف | الأداة |
|---|--------|--------|
| 21 | `EGX_T_21_ADX.pine` | ADX / DMI |
| 22 | `EGX_T_22_AROON.pine` | Aroon |
| 23 | `EGX_T_23_VORTEX.pine` | Vortex |
| 24 | `EGX_T_24_SAR.pine` | Parabolic SAR |
| 25 | `EGX_T_25_ICHIMOKU.pine` | Ichimoku |
| 26 | `EGX_T_26_HULL.pine` | Hull MA |
| 27 | `EGX_T_27_KAMA.pine` | Kaufman AMA |
| 28 | `EGX_T_28_MCGINLEY.pine` | McGinley |
| 29 | `EGX_T_29_GMMA.pine` | Guppy GMMA |
| 30 | `EGX_T_30_DONCHIAN.pine` | Donchian |
| 31 | `EGX_T_31_EMASTACK.pine` | EMA 20/50/200 |
| 32 | `EGX_T_32_ELDERRAY.pine` | Elder Ray |
| 33 | `EGX_T_33_ELDERIMP.pine` | Elder Impulse |
| 34 | `EGX_T_34_SCHAFF.pine` | Schaff Trend Cycle |
| 35 | `EGX_T_35_SUPERTREND.pine` | SuperTrend |

## ج — حجم (15)

| # | الملف | الأداة |
|---|--------|--------|
| 36 | `EGX_T_36_OBV.pine` | OBV |
| 37 | `EGX_T_37_ADL.pine` | A/D |
| 38 | `EGX_T_38_CMF.pine` | CMF |
| 39 | `EGX_T_39_CHAIKIN.pine` | Chaikin Osc |
| 40 | `EGX_T_40_EFI.pine` | Elder Force |
| 41 | `EGX_T_41_EOM.pine` | Ease of Movement |
| 42 | `EGX_T_42_KVO.pine` | Klinger |
| 43 | `EGX_T_43_VPT.pine` | VPT |
| 44 | `EGX_T_44_NVI.pine` | NVI |
| 45 | `EGX_T_45_VWAP.pine` | VWAP جلسة |
| 46 | `EGX_T_46_AVWAP.pine` | Anchored VWAP (Shannon) |
| 47 | `EGX_T_47_WEIS.pine` | Weis Wave |
| 48 | `EGX_T_48_CVD.pine` | CVD proxy |
| 49 | `EGX_T_49_RVOL.pine` | Relative Volume |
| 50 | `EGX_T_50_BUYSHARE.pine` | نصيب الشراء |

## د — تقلب (10)

| # | الملف | الأداة |
|---|--------|--------|
| 51 | `EGX_T_51_BBPERCENT.pine` | Bollinger %B |
| 52 | `EGX_T_52_BBW.pine` | BB Width |
| 53 | `EGX_T_53_SQUEEZE.pine` | TTM Squeeze |
| 54 | `EGX_T_54_KELTNER.pine` | Keltner |
| 55 | `EGX_T_55_ATR.pine` | ATR% |
| 56 | `EGX_T_56_ULCER.pine` | Ulcer Index |
| 57 | `EGX_T_57_STARC.pine` | STARC |
| 58 | `EGX_T_58_HV.pine` | Historical Volatility |
| 59 | `EGX_T_59_CHANDELIER.pine` | Chandelier Exit |
| 60 | `EGX_T_60_CHOP.pine` | Choppiness |

## هـ — SMC / ICT (10)

| # | الملف | الأداة |
|---|--------|--------|
| 61 | `EGX_T_61_BOS.pine` | Break of Structure |
| 62 | `EGX_T_62_FVG.pine` | Fair Value Gap |
| 63 | `EGX_T_63_OB.pine` | Order Block |
| 64 | `EGX_T_64_LIQ.pine` | Liquidity pools |
| 65 | `EGX_T_65_SWEEP.pine` | Sweep |
| 66 | `EGX_T_66_PO3.pine` | Power of Three |
| 67 | `EGX_T_67_OTE.pine` | Optimal Trade Entry |
| 68 | `EGX_T_68_BREAKER.pine` | Breaker |
| 69 | `EGX_T_69_PREMIUM.pine` | Premium / Discount |
| 70 | `EGX_T_70_MSS.pine` | Market Structure Shift |

## و — موجات / فيبو / جان (12)

| # | الملف | الأداة |
|---|--------|--------|
| 71 | `EGX_T_71_FIB.pine` | Fibonacci |
| 72 | `EGX_T_72_ELLIOTT.pine` | Elliott |
| 73 | `EGX_T_73_GANN.pine` | Gann 50% |
| 74 | `EGX_T_74_MURREY.pine` | Murrey Math |
| 75 | `EGX_T_75_HARMONIC.pine` | Harmonic AB=CD |
| 76 | `EGX_T_76_PIVOT.pine` | Floor pivots |
| 77 | `EGX_T_77_ZIGZAG.pine` | Dow zigzag |
| 78 | `EGX_T_78_GANNTIME.pine` | Gann time |
| 79 | `EGX_T_79_FIBTIME.pine` | Fib time |
| 80 | `EGX_T_80_HOSODA.pine` | Hosoda NT/N |
| 81 | `EGX_T_81_SQUARE9.pine` | Square of 9 |
| 82 | `EGX_T_82_NEOWAVE.pine` | NeoWave proxy |

## ز — أنظمة المحترفين (12)

| # | الملف | الأداة |
|---|--------|--------|
| 83 | `EGX_T_83_WYCKOFF.pine` | Wyckoff SC/BC |
| 84 | `EGX_T_84_VSA.pine` | VSA |
| 85 | `EGX_T_85_VCP.pine` | Minervini VCP |
| 86 | `EGX_T_86_CANSLIM.pine` | O'Neil CANSLIM |
| 87 | `EGX_T_87_WEINSTEIN.pine` | Weinstein Stage |
| 88 | `EGX_T_88_TURTLE.pine` | Turtle + Soup |
| 89 | `EGX_T_89_LIVERMORE.pine` | Livermore pivot |
| 90 | `EGX_T_90_QULLA.pine` | Qullamaggie flag |
| 91 | `EGX_T_91_DARVAS.pine` | Darvas Box |
| 92 | `EGX_T_92_BROOKS.pine` | Al Brooks Always-In |
| 93 | `EGX_T_93_HURST.pine` | Hurst-like |
| 94 | `EGX_T_94_MESA.pine` | MAMA / FAMA |

## ح — بروفايل (6)

| # | الملف | الأداة |
|---|--------|--------|
| 95 | `EGX_T_95_VPPOC.pine` | Volume Profile POC |
| 96 | `EGX_T_96_TPO.pine` | TPO proxy |
| 97 | `EGX_T_97_DEMARK.pine` | TD Sequential |
| 98 | `EGX_T_98_CONFLUENCE.pine` | Clarity 0–5 |
| 99 | `EGX_T_99_RS.pine` | RS vs EGX30 |
| 100 | `EGX_T_100_REGIME.pine` | Trend / Range |

## أوزان الماستر الافتراضية

زخم 20% · اتجاه 20% · حجم 20% · تقلب 10% · SMC 10% · موجات 8% · أنظمة 8% · بروفايل 4%.

إعادة توليد الملفات المنفردة:

```bash
python3 scripts/gen_egx_tools.py
```
