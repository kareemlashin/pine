# EGX — دليل الفوليوم والمناطق

> OHLCV فقط — **buy/sell volume = تقدير** من موقع الإغلاق/الافتتاح داخل الشمعة.  
> **ليس** footprint ولا هوية ميكر/مؤسسات.  
> **تجميد:** لا تضف ملفات فوليوم جديدة — 87 كافية. PRO-S يحتاج تعليم السهم كـ EGX30.

---

## 1. فهرس الملفات (87)

| # | الملف | Overlay | الاستخدام |
|---|--------|---------|-----------|
| 1 | `EGX_VOLUME_MASTER.pine` | نعم | All-in-one |
| 2 | `EGX_VOLUME_QUICK.pine` | نعم | مبتدئ B1/S1 |
| 3 | `EGX_VOLUME_ZONES.pine` | نعم | B1/S1 PRO |
| 4 | `EGX_VOLUME_MM.pine` | نعم | ميكر/صفقات |
| 5 | `EGX_VOLUME_PROFILE.pine` | نعم | POC/VA/HVN |
| 6 | `EGX_VOLUME_SESSION.pine` | نعم | جلسة EGX |
| 7 | `EGX_VOLUME.pine` | pane | RVOL/climax |
| 8 | `EGX_VOLUME_DELTA.pine` | pane | دلتا |
| 9 | `EGX_VOLUME_CLIMAX.pine` | pane | SC/BC/جفاف |
| 10 | `EGX_VOLUME_FLOWS.pine` | pane | CMF/OBV/MFI |
| 11 | `EGX_VOLUME_RELATIVE.pine` | pane | vs EGX30 |
| 12 | `EGX_VOLUME_SCREENER.pine` | pane | ماسح |
| 13 | `EGX_VOLUME_WATCHLIST.pine` | pane | رتبة |
| 14 | `EGX_VOLUME_MASTER_STRATEGY.pine` | strat | PRO |
| 15 | `EGX_VOLUME_ZONES_STRATEGY.pine` | strat | B1 |
| 16 | `EGX_VOLUME_STRATEGY.pine` | strat | SC+acc |
| 17 | `EGX_VOLUME_WYCKOFF.pine` | نعم | SC/BC/VSA |
| 18 | `EGX_VOLUME_VWAP.pine` | نعم | VWAP ±σ |
| 19 | `EGX_VOLUME_LIQUIDITY.pine` | pane | Tier/Turnover |
| 20 | `EGX_VOLUME_ANOMALY.pine` | نعم | أيام شذوذ |
| 21 | `EGX_VOLUME_BARS.pine` | نعم | أكبر N شموع |
| 22 | `EGX_VOLUME_RANK.pine` | pane | رتبة مركبة /100 |
| 23 | `EGX_VOLUME_MULTIDAY.pine` | pane | تراكم 3/5/10 |
| 24 | `EGX_VOLUME_ABSORB.pine` | نعم | امتصاص VSA |
| 25 | `EGX_VOLUME_DRYUP.pine` | pane | جفاف→توسع |
| 26 | `EGX_VOLUME_BREAKOUT.pine` | نعم | كسر+RVOL |
| 27 | `EGX_VOLUME_EFFORT.pine` | pane | جهد vs نتيجة |
| 28 | `EGX_VOLUME_SWING.pine` | نعم | حجم عند pivot |
| 29 | `EGX_VOLUME_HEAT.pine` | نعم | شدة حجم |
| 30 | `EGX_VOLUME_DIVERGE.pine` | pane | تباعد flow |
| 31 | `EGX_VOLUME_OSC.pine` | pane | PVT / Force |
| 32 | `EGX_VOLUME_CHURN.pine` | نعم | Churn/تدوير |
| 33 | `EGX_VOLUME_ZSCORE.pine` | pane | Z-score |
| 34 | `EGX_VOLUME_BUYSELL.pine` | pane | Buy vs Sell |
| 35 | `EGX_VOLUME_GAP.pine` | نعم | Gap + V |
| 36 | `EGX_VOLUME_COG.pine` | نعم | COG/VWAP roll |
| 37 | `EGX_VOLUME_DIST.pine` | pane | Dist/Acc score |
| 38 | `EGX_VOLUME_TOUCH.pine` | نعم | S/R + RVOL |
| 39 | `EGX_VOLUME_ALERTS.pine` | pane | Hub تنبيهات |
| 40 | `EGX_VOLUME_ROC.pine` | pane | Vol ROC |
| 41 | `EGX_VOLUME_ADVDEC.pine` | pane | Up/Down index |
| 42 | `EGX_VOLUME_NVI.pine` | pane | NVI / PVI |
| 43 | `EGX_VOLUME_EOM.pine` | pane | Ease of Movement |
| 44 | `EGX_VOLUME_VBANDS.pine` | pane | Bollinger vol |
| 45 | `EGX_VOLUME_COMPRESS.pine` | نعم | Coil + V |
| 46 | `EGX_VOLUME_SPIKE.pine` | نعم | Spike flags |
| 47 | `EGX_VOLUME_DASH.pine` | نعم | Dashboard |
| 48 | `EGX_VOLUME_KVO.pine` | pane | Klinger |
| 49 | `EGX_VOLUME_VPT.pine` | pane | VPT |
| 50 | `EGX_VOLUME_VOLMA.pine` | pane | Vol MA cross |
| 51 | `EGX_VOLUME_IMBAL.pine` | نعم | Imbalance % |
| 52 | `EGX_VOLUME_PRINT.pine` | نعم | Print bar |
| 53 | `EGX_VOLUME_REGIME.pine` | pane | L/M/H regime |
| 54 | `EGX_VOLUME_STREAK.pine` | pane | Rising V streak |
| 55 | `EGX_VOLUME_HVN_LITE.pine` | نعم | Nearest HVN |
| 56 | `EGX_VOLUME_VWMA.pine` | نعم | VWMA price |
| 57 | `EGX_VOLUME_ATRV.pine` | pane | V / ATR |
| 58 | `EGX_VOLUME_MFI.pine` | pane | MFI |
| 59 | `EGX_VOLUME_UVDV.pine` | pane | Cum UV/DV |
| 60 | `EGX_VOLUME_POCMOVE.pine` | نعم | POC shift |
| 61 | `EGX_VOLUME_CONSEC.pine` | pane | Up+V run |
| 62 | `EGX_VOLUME_SNR.pine` | pane | Signal/noise |
| 63 | `EGX_VOLUME_AVGSIZE.pine` | pane | Avg size proxy |
| 64 | `EGX_VOLUME_ADL.pine` | pane | A/D line |
| 65 | `EGX_VOLUME_CHAIKIN.pine` | pane | Chaikin osc |
| 66 | `EGX_VOLUME_EFI.pine` | pane | Elder Force |
| 67 | `EGX_VOLUME_EXHAUST.pine` | نعم | Exhaustion |
| 68 | `EGX_VOLUME_TRAP.pine` | نعم | Bull/bear trap |
| 69 | `EGX_VOLUME_SLOPE.pine` | pane | Vol MA slope |
| 70 | `EGX_VOLUME_WEEKLY.pine` | pane | Week pace |
| 71 | `EGX_VOLUME_CONFIRM.pine` | نعم | 3-check confirm |
| 72 | `EGX_VOLUME_WAD.pine` | pane | Williams A/D |
| 73 | `EGX_VOLUME_CLV.pine` | pane | CLV × V |
| 74 | `EGX_VOLUME_VR.pine` | pane | V ratio |
| 75 | `EGX_VOLUME_PULLBACK.pine` | نعم | Low-V pullback |
| 76 | `EGX_VOLUME_BREAKAWAY.pine` | نعم | Breakaway gap |
| 77 | `EGX_VOLUME_CORREL.pine` | pane | Corr |ΔP|,V |
| 78 | `EGX_VOLUME_VZO.pine` | pane | Volume zone osc |
| 79 | `EGX_VOLUME_TWIN.pine` | pane | Twin vol peaks |
| 80 | `EGX_VOLUME_VMACD.pine` | pane | Vol MACD |
| 81 | `EGX_VOLUME_VRSI.pine` | pane | Vol RSI |
| 82 | `EGX_VOLUME_SURGE.pine` | نعم | 3-bar surge |
| 83 | `EGX_VOLUME_HALT.pine` | نعم | Quiet → wake |
| 84 | `EGX_VOLUME_NET5.pine` | pane | Net buy 5d |
| 85 | `EGX_VOLUME_HV52.pine` | pane | Vs 52w vol high |
| 86 | `EGX_VOLUME_VFI.pine` | pane | Volume Flow Idx |
| 87 | `EGX_VOLUME_RANGE.pine` | نعم | Range base break |

**قرار EGX:** `EGX_الخلاصة.pine` (دمج B1 اختياري).

---

## 2. أي ملف لأي هدف؟

| الهدف | اختر |
|--------|------|
| بداية | **MASTER** أو **QUICK** |
| ملف حجم سعري | **PROFILE** |
| دلتا/تراكم | **DELTA** + **FLOWS** |
| ذروة فقط | **CLIMAX** |
| 15د/60د EGX | **SESSION** |
| أقوى من المؤشر | **RELATIVE** |
| مسح | **SCREENER** / **WATCHLIST** / **RANK** |
| وايكوف VSA | **WYCKOFF** |
| VWAP جلسة | **VWAP** |
| سيولة/رتبة حجم | **LIQUIDITY** |
| يوم حجم+فجوة | **ANOMALY** |
| أين أكبر الصفقات | **BARS** |
| حجم أسبوعي | **MULTIDAY** |
| امتصاص / كسر وهمي | **ABSORB** + **BREAKOUT** |
| قبل حركة | **DRYUP** |
| VSA متقدم | **EFFORT** + **WYCKOFF** |
| pivot + حجم | **SWING** |
| تلوين سريع | **HEAT** |
| تباعد | **DIVERGE** + **OSC** |
| تدوير داخل نطاق | **CHURN** |
| Z / RVOL pane | **ZSCORE** |
| أعمدة buy/sell | **BUYSELL** |
| فجوة افتتاح | **GAP** |
| خط ثقل حجم | **COG** |
| تراكم vs توزيع | **DIST** |
| دعم/مقاومة + V | **TOUCH** |
| تنبيهات قائمة | **ALERTS** |
| زخم حجم | **ROC** |
| أيام صاعد/هابط | **ADVDEC** |
| NVI/PVI | **NVI** |
| EOM | **EOM** |
| BB على الحجم | **VBANDS** |
| ضغط قبل كسر | **COMPRESS** |
| spike سريع | **SPIKE** |
| لوحة أرقام | **DASH** |
| Klinger | **KVO** |
| VPT | **VPT** |
| تقاطع MA حجم | **VOLMA** |
| imb شمعة | **IMBAL** |
| print block | **PRINT** |
| نظام حجم | **REGIME** |
| سلسلة حجم | **STREAK** |
| HVN خفيف | **HVN_LITE** |
| VWMA | **VWMA** |
| V/ATR | **ATRV** |
| MFI | **MFI** |
| UV/DV تراكم | **UVDV** |
| تحرك POC | **POCMOVE** |
| up+V متتالي | **CONSEC** |
| SNR | **SNR** |
| حجم/مدى | **AVGSIZE** |
| A/D · Chaikin | **ADL** · **CHAIKIN** |
| Elder Force | **EFI** |
| إ exhaustion | **EXHAUST** |
| فخ حجم | **TRAP** |
| ميل MA حجم | **SLOPE** |
| وتيرة أسبوع | **WEEKLY** |
| تأكيد 3/3 | **CONFIRM** |
| Williams A/D | **WAD** |
| CLV × حجم | **CLV** |
| V أمس / متوسط | **VR** |
| pullback هادئ | **PULLBACK** |
| breakaway gap | **BREAKAWAY** |
| corr حركة/حجم | **CORREL** |
| VZO | **VZO** |
| twin peaks | **TWIN** |
| MACD حجم | **VMACD** |
| RSI حجم | **VRSI** |
| surge 3 شموع | **SURGE** |
| halt → wake | **HALT** |
| net 5 أيام | **NET5** |
| قرب rec حجم | **HV52** |
| VFI | **VFI** |
| range base | **RANGE** |

**بداية سريعة:** `EGX_VOLUME_MASTER` على **D** + رمز `EGX:XXXX`.

---

## 3. قراءة B1 / S1

| الرمز | المعنى |
|--------|--------|
| **B1** | أكبر **منطقة شراء** (HVN buy) في نافذة المسح |
| **S1** | أكبر **منطقة بيع** (HVN sell) |
| **B1↑** | ارتداد داخل B1 + شمعة صاعدة + RVOL |
| **S1↓** | رفض عند S1 + شمعة هابطة + RVOL |
| **PRO** | B1↑ + Grade ≥ 2 + Net buy % + R/R + بدون تصريف قوي |
| **Heat 🔥** | قوة طلب/عرض **عند السعر الحالي** |

---

## 4. ماسح — البادئات

| Plot | المعنى |
|------|--------|
| `EGVM_Pro` | إشارة PRO (MASTER) |
| `EGVM_B1` / `EGVM_GradeB1` | داخل B1 / درجة المنطقة |
| `EGVM_NetBuy` | نسبة شراء في النافذة |
| `EGVScr_Pro` / `EGVScr_Pass` | ماسح Volume Screener |
| `EGVZ_BuyPass` / `EGVZ_InB1` | من Zones PRO |
| `EGVP_*` | PROFILE |
| `EGVD_*` | DELTA |
| `EGVClx_*` | CLIMAX |
| `EGVF_*` | FLOWS |
| `EGVRel_*` | RELATIVE |
| `EGVS_*` | SESSION |
| `EGVWk_*` | WYCKOFF |
| `EGVVW_*` | VWAP |
| `EGVLiq_*` | LIQUIDITY |
| `EGVAn_*` | ANOMALY |
| `EGVBars_*` | BARS |
| `EGVRank_*` | RANK |
| `EGVMulti_*` | MULTIDAY |
| `EGVAbs_*` | ABSORB |
| `EGVDry_*` | DRYUP |
| `EGVBrk_*` | BREAKOUT |
| `EGVEff_*` | EFFORT |
| `EGVSw_*` | SWING |
| `EGVHeat_*` | HEAT |
| `EGVDiv_*` | DIVERGE |
| `EGVOsc_*` | OSC |
| `EGVChn_*` | CHURN |
| `EGVZ_*` | ZSCORE |
| `EGVBS_*` | BUYSELL |
| `EGVGap_*` | GAP |
| `EGVCog_*` | COG |
| `EGVDst_*` | DIST |
| `EGVTch_*` | TOUCH |
| `EGVAl_*` | ALERTS |
| `EGVROC_*` | ROC |
| `EGVUD_*` | ADVDEC |
| `EGVNP_*` | NVI/PVI |
| `EGVEOM_*` | EOM |
| `EGVBB_*` | VBANDS |
| `EGVCmp_*` | COMPRESS |
| `EGVSpk_*` | SPIKE |
| `EGVDash_*` | DASH |
| `EGVKVO_*` | KVO |
| `EGVVPT_*` | VPT |
| `EGVVX_*` | VOLMA |
| `EGVImb_*` | IMBAL |
| `EGVPr_*` | PRINT |
| `EGVRgm_*` | REGIME |
| `EGVStr_*` | STREAK |
| `EGVHVN_*` | HVN_LITE |
| `EGVVWMA_*` | VWMA |
| `EGVATR_*` | ATRV |
| `EGVMFI_*` | MFI |
| `EGVUV_*` | UVDV |
| `EGVPOC_*` | POCMOVE |
| `EGVCsq_*` | CONSEC |
| `EGVSNR_*` | SNR |
| `EGVAvg_*` | AVGSIZE |
| `EGVAD_*` | ADL |
| `EGVChk_*` | CHAIKIN |
| `EGVEFI_*` | EFI |
| `EGVExh_*` | EXHAUST |
| `EGVTrp_*` | TRAP |
| `EGVSlp_*` | SLOPE |
| `EGVWk_*` | WEEKLY |
| `EGVCfm_*` | CONFIRM |
| `EGVWAD_*` | WAD |
| `EGVCLV_*` | CLV |
| `EGVVR_*` | VR |
| `EGVPb_*` | PULLBACK |
| `EGVBrkA_*` | BREAKAWAY |
| `EGVCor_*` | CORREL |
| `EGVVZO_*` | VZO |
| `EGVTwn_*` | TWIN |
| `EGVMACD_*` | VMACD |
| `EGVVRSI_*` | VRSI |
| `EGVSur_*` | SURGE |
| `EGVHlt_*` | HALT |
| `EGVN5_*` | NET5 |
| `EGVH52_*` | HV52 |
| `EGVVFI_*` | VFI |
| `EGVRng_*` | RANGE |

---

## 5. إعداد EGX

- **يومي:** نافذة 400 · RVOL climax ~2.0 · min avg vol ~1000+  
- **مضاربة:** نافذة 200 · RVOL ~1.7 · min vol أعلى للأسهم الركيكة  
- **±10%:** لا تعتمد PRO قرب حد اليوم بدون فلتر (استخدم `EGX_الخلاصة` للبوابات)

---

## 6. تركيب مقترح

1. **تحليل:** `EGX_VOLUME_MASTER` أو `EGX_الاخير` (واحد ثقيل فقط).  
2. **مسح:** `EGX_VOLUME_SCREENER` على قائمة D.  
3. **تأكيد:** `EGX_VOLUME` pane + `EGX_VOLUME_ZONES` إن احتجت تفصيل zones.

---

## 7. دمج مع الخلاصة

في `EGX_الخلاصة.pine` → **فوليوم B1**:

| الوضع | التأثير |
|--------|---------|
| **إيقاف** | بدون B1 |
| **تعزيز فقط** | +6 نقاط + setup hit عند B1/Net buy |
| **بوابة Pro** | `EGXKh_ScreenerPro` يتطلب `volProOk` |

ماسح: `EGXKh_VolScreenerPro = 1` · `EGXKh_B1Bounce = 1`

---

## 8. وصفات ماسح (D)

| الهدف | الفلتر |
|--------|--------|
| أفضل فوليوم | `EGVScr_Rank` ≥ 70 |
| Pro B1 | `EGVScr_Pro = 1` |
| خلاصة + B1 | `EGXKh_VolScreenerPro = 1` (بوابة Pro) |
| محفظة | `EGVWL_Pass = 1` sort `EGVWL_Rank` |
| Master | `EGVM_Pro = 1` و `EGVM_LiqOk = 1` |
| QUICK فقط | `EGVQ_Buy = 1` |
| رتبة واحدة | `EGVRank_Pass = 1` sort `EGVRank_Score` |
| سيولة T1/T2 | `EGVLiq_Tier` ≥ 3 |
| تراكم 5 أيام | `EGVMulti_Pass = 1` |
| كسر حجم | `EGVBrk_Up = 1` أو `EGVBrk_Dn = 1` |
| جفاف ثم توسع | `EGVDry_ExpandUp = 1` |
| pivot تراكم | `EGVSw_AccLow = 1` |
| حرارة شراء | `EGVHeat_HotBuy = 1` |
| أي تنبيه hub | `EGVAl_Any = 1` |
| شراء hub | `EGVAl_Buy = 1` |
| Z ش extreme | `EGVZ_Extreme = 1` |
| دعم + حجم | `EGVTch_SupBounce = 1` |
| فجوة + V | `EGVGap_UpVol = 1` |
| spike | `EGVSpk_Bull = 1` |
| coil break | `EGVCmp_BreakUp = 1` |
| Vol BB | `EGVBB_BreakUp = 1` |
| dash pass | `EGVDash_Pass = 1` |
| print | `EGVPr_Any = 1` |
| regime high | `EGVRgm_High = 1` |
| streak | `EGVStr_Pass = 1` |
| near B1 lite | `EGVHVN_NearB1 = 1` |
| POC up | `EGVPOC_Up = 1` |
| up+V run | `EGVCsq_Pass = 1` |
| block trades | `EGVAvg_Block = 1` |
| تأكيد شراء | `EGVCfm_Buy = 1` |
| فخ صاعد | `EGVTrp_BearTrap = 1` |
| أسبوع hot | `EGVWk_Hot = 1` |
| breakaway | `EGVBrkA_Up = 1` |
| low-V dip | `EGVPb_Bull = 1` |
| V zone high | `EGVVZO_High = 1` |
| net 5d | `EGVN5_Pass = 1` |
| 52w vol | `EGVH52_Record = 1` |
| range break | `EGVRng_BrkUp = 1` |
| surge | `EGVSur_Bull = 1` |

**ملف مبتدئ على الشارت:** `EGX_VOLUME_QUICK.pine` — بانر + B1/S1 + Net %.

---

## 9. باك‌تست

- `EGX_VOLUME_MASTER_STRATEGY` — دخول **PRO**، خروج **S1** أو stop/limit.  
- Slippage: 2 سائل · 3 متوسط · 5 رقيق (في إعدادات Strategy).
