# EGX — الخلاصة (قرار نهائي)

> **مرجع واحد** لكل مشروع Pine في هذا المجلد: ماذا تستخدم، متى تشتري، متى تنتظر، متى تخرج، وكيف تمسح السوق.  
> البيانات: **OHLCV + مؤشرات EGX30/70/100 فقط** — تقديرات احتمالية، **ليست توصية استثمارية**.

---

## 1. القرار النهائي: أي ملف؟

| الهدف | الملف | القرار |
|--------|--------|--------|
| **100 أداة موحّدة + قرار A/B** | `pine/EGX_TOOLS_MASTER.pine` | **نعم — منهج الرؤية الشاملة** · `docs/EGX_TOOLS.md` |
| **TOOLS سريع / ماسح / محفظة** | `EGX_TOOLS_QUICK` · `SCREENER` · `WATCHLIST` · `BOARD` | lite 16–24 صوت · `EGXTScr_*` / `EGXTQ_*` |
| **TOOLS × فوليوم / Meta** | `EGX_TOOLS_QxV` · `EGX_TOOLS_META_SCREENER` | `EGXTxV_Agree` · `EGXTMeta_Triple` |
| **TOOLS مسح السوق** | `EGX_TOOLS_OPP` · `BOARD200` · `BOARD` (5 صفحات) | `EGXTTOpp_Pro` · `EGXTTB200_*` · `EGXTxOpp_Mega` |
| **باك‌تست Tools lite** | `EGX_TOOLS_LITE_STRATEGY.pine` | مرآة OPP · ليس MASTER 100 |
| **TOOLS + Uni فني/فوليوم** | `EGX_TOOLS_UNIFIED.pine` | `EGXTUni_Pro=1` |
| **8 مجموعات lite** | `pine/EGX_TOOLS_GROUPS.pine` | `EGXTGrp_A`…`H` · مقارنة بأوزان الماستر |
| **باك‌تست الـ 100** | `pine/EGX_TOOLS_MASTER_STRATEGY.pine` | مرآة Buy A/B · عمولة 0.125% |
| **تداول / تحليل يومي على EGX** | `pine/EGX_الاخير.pine` | **نعم — هذا هو المعيار** (v1.2، halt/LULD · حجم 1–2%) |
| **اختبار Strategy Tester** | `pine/EGX_الاخير_STRATEGY.pine` | **نعم — مرتبط بالأخير** |
| **قرار نهائي فقط على الشارت** | `pine/EGX_الخلاصة.pine` | **بانر + فعل + ماسح** (v1.1: مبتدئ · جلسة · قطاع) |
| **باك‌تست الخلاصة** | `pine/EGX_الخلاصة_STRATEGY.pine` | buyConfluence |
| **أفضل فرص — 200 سهم** | `EGX_افضل_فرص_BOARD200` · `WATCHLIST` · `STRATEGY` | 8★ مثبتة + دوّar · Screener `EGXOpp_Score`↓ · Hub `EGXAlHub_OppPro` |
| **ماسح بدون overlay** | `pine/EGX_SCREENER.pine` | `EGXScr_Pro = 1` |
| **محفظة 6 أسهم** | `pine/EGX_WATCHLIST.pine` | Rank سريع vs EGX30 |
| **مكتبة مشتركة** | `pine/EGX_Core.pine` | انشر على TV ثم import |
| **شارت بسيط بدون تعقيد** | `pine/EGX_BEST.pine` + `EGX_BEST_STRATEGY.pine` | **بديل خفيف** (نفس الفلسفة، أقل محركات) |
| **فوليوم + B1/S1 + PRO** | `pine/EGX_VOLUME_MASTER.pine` | **all-in-one** · `docs/EGX_VOLUME.md` |
| **مناطق شراء/بيع بالحجم** | `pine/EGX_VOLUME_ZONES.pine` | B1/S1 · grades · خطة R/R |
| **ماسح فوليوم** | `pine/EGX_VOLUME_SCREENER.pine` | `EGVScr_Pro = 1` |
| **رتبة فوليوم محفظة** | `pine/EGX_VOLUME_WATCHLIST.pine` | `EGVWL_Rank` · `EGVWL_Pass` |
| **فوليوم سريع (مبتدئ)** | `pine/EGX_VOLUME_QUICK.pine` | `EGVQ_Buy` · بانر B1/S1 |
| **POC / VA / HVN** | `pine/EGX_VOLUME_PROFILE.pine` | `EGVP_InVA` |
| **دلتا buy−sell** | `pine/EGX_VOLUME_DELTA.pine` | `EGVD_CumDelta` |
| **Climax SC/BC** | `pine/EGX_VOLUME_CLIMAX.pine` | `EGVClx_BuyClx` |
| **جلسة EGX** | `pine/EGX_VOLUME_SESSION.pine` | 15د/60د |
| **تدفق CMF/OBV** | `pine/EGX_VOLUME_FLOWS.pine` | `EGVF_Acc` |
| **RS vol vs 30** | `pine/EGX_VOLUME_RELATIVE.pine` | `EGVRel_RSVol30` |
| **Wyckoff SC/BC** | `pine/EGX_VOLUME_WYCKOFF.pine` | `EGVWk_SC` |
| **VWAP جلسة** | `pine/EGX_VOLUME_VWAP.pine` | `EGVVW_Above` |
| **سيولة Tier** | `pine/EGX_VOLUME_LIQUIDITY.pine` | `EGVLiq_Tier` |
| **شذوذ حجم+فجوة** | `pine/EGX_VOLUME_ANOMALY.pine` | `EGVAn_GapVol` |
| **أكبر N شموع** | `pine/EGX_VOLUME_BARS.pine` | `EGVBars_Rank` |
| **رتبة مركبة /100** | `pine/EGX_VOLUME_RANK.pine` | `EGVRank_Score` |
| **تراكم 3/5/10** | `pine/EGX_VOLUME_MULTIDAY.pine` | `EGVMulti_Pass` |
| **امتصاص حجم** | `pine/EGX_VOLUME_ABSORB.pine` | `EGVAbs_Bull` |
| **جفاف→توسع** | `pine/EGX_VOLUME_DRYUP.pine` | `EGVDry_ExpandUp` |
| **كسر + RVOL** | `pine/EGX_VOLUME_BREAKOUT.pine` | `EGVBrk_Up` |
| **جهد vs نتيجة** | `pine/EGX_VOLUME_EFFORT.pine` | `EGVEff_EasyUp` |
| **حجم pivots** | `pine/EGX_VOLUME_SWING.pine` | `EGVSw_AccLow` |
| **Heat شموع** | `pine/EGX_VOLUME_HEAT.pine` | `EGVHeat_HotBuy` |
| **تباعد flow** | `pine/EGX_VOLUME_DIVERGE.pine` | `EGVDiv_Bull` |
| **PVT / Force** | `pine/EGX_VOLUME_OSC.pine` | `EGVOsc_BullX` |
| **Churn تدوير** | `pine/EGX_VOLUME_CHURN.pine` | `EGVChn_Any` |
| **Z-Score** | `pine/EGX_VOLUME_ZSCORE.pine` | `EGVZ_Extreme` |
| **Buy vs Sell** | `pine/EGX_VOLUME_BUYSELL.pine` | `EGVBS_BuyDay` |
| **Gap + V** | `pine/EGX_VOLUME_GAP.pine` | `EGVGap_UpVol` |
| **COG خط** | `pine/EGX_VOLUME_COG.pine` | `EGVCog_CrossUp` |
| **Dist/Acc** | `pine/EGX_VOLUME_DIST.pine` | `EGVDst_AccBias` |
| **S/R + RVOL** | `pine/EGX_VOLUME_TOUCH.pine` | `EGVTch_SupBounce` |
| **Alerts hub** | `pine/EGX_VOLUME_ALERTS.pine` | `EGVAl_Any` |
| **Vol ROC** | `pine/EGX_VOLUME_ROC.pine` | `EGVROC_Hot` |
| **Up/Down vol** | `pine/EGX_VOLUME_ADVDEC.pine` | `EGVUD_Bull` |
| **NVI · PVI** | `pine/EGX_VOLUME_NVI.pine` | `EGVNP_Smart` |
| **EOM** | `pine/EGX_VOLUME_EOM.pine` | `EGVEOM_EasyUp` |
| **Vol Bollinger** | `pine/EGX_VOLUME_VBANDS.pine` | `EGVBB_BreakUp` |
| **Compression** | `pine/EGX_VOLUME_COMPRESS.pine` | `EGVCmp_BreakUp` |
| **Spike flags** | `pine/EGX_VOLUME_SPIKE.pine` | `EGVSpk_Bull` |
| **Dashboard** | `pine/EGX_VOLUME_DASH.pine` | `EGVDash_Pass` |
| **Klinger KVO** | `pine/EGX_VOLUME_KVO.pine` | `EGVKVO_Bull` |
| **VPT** | `pine/EGX_VOLUME_VPT.pine` | `EGVVPT_Acc` |
| **Vol MA cross** | `pine/EGX_VOLUME_VOLMA.pine` | `EGVVX_BullX` |
| **Imbalance** | `pine/EGX_VOLUME_IMBAL.pine` | `EGVImb_Bull` |
| **Print bar** | `pine/EGX_VOLUME_PRINT.pine` | `EGVPr_Any` |
| **Regime L/M/H** | `pine/EGX_VOLUME_REGIME.pine` | `EGVRgm_High` |
| **Vol streak** | `pine/EGX_VOLUME_STREAK.pine` | `EGVStr_Pass` |
| **HVN lite** | `pine/EGX_VOLUME_HVN_LITE.pine` | `EGVHVN_NearB1` |
| **VWMA** | `pine/EGX_VOLUME_VWMA.pine` | `EGVVWMA_XUp` |
| **V / ATR** | `pine/EGX_VOLUME_ATRV.pine` | `EGVATR_Hot` |
| **MFI** | `pine/EGX_VOLUME_MFI.pine` | `EGVMFI_Acc` |
| **UV / DV** | `pine/EGX_VOLUME_UVDV.pine` | `EGVUV_Bull` |
| **POC move** | `pine/EGX_VOLUME_POCMOVE.pine` | `EGVPOC_Up` |
| **Up + V run** | `pine/EGX_VOLUME_CONSEC.pine` | `EGVCsq_Pass` |
| **SNR** | `pine/EGX_VOLUME_SNR.pine` | `EGVSNR_Loud` |
| **Avg size** | `pine/EGX_VOLUME_AVGSIZE.pine` | `EGVAvg_Block` |
| **A/D line** | `pine/EGX_VOLUME_ADL.pine` | `EGVAD_XUp` |
| **Chaikin** | `pine/EGX_VOLUME_CHAIKIN.pine` | `EGVChk_Bull` |
| **Elder Force** | `pine/EGX_VOLUME_EFI.pine` | `EGVEFI_XUp` |
| **Exhaustion** | `pine/EGX_VOLUME_EXHAUST.pine` | `EGVExh_Bear` |
| **Volume trap** | `pine/EGX_VOLUME_TRAP.pine` | `EGVTrp_BearTrap` |
| **Vol MA slope** | `pine/EGX_VOLUME_SLOPE.pine` | `EGVSlp_Rising` |
| **Week pace** | `pine/EGX_VOLUME_WEEKLY.pine` | `EGVWk_Hot` |
| **3-check confirm** | `pine/EGX_VOLUME_CONFIRM.pine` | `EGVCfm_Buy` |
| **Williams WAD** | `pine/EGX_VOLUME_WAD.pine` | `EGVWAD_Acc` |
| **CLV × V** | `pine/EGX_VOLUME_CLV.pine` | `EGVCLV_Bull` |
| **Vol ratio** | `pine/EGX_VOLUME_VR.pine` | `EGVVR_HotDay` |
| **Low-V pullback** | `pine/EGX_VOLUME_PULLBACK.pine` | `EGVPb_Bull` |
| **Breakaway gap** | `pine/EGX_VOLUME_BREAKAWAY.pine` | `EGVBrkA_Up` |
| **Corr ΔP/V** | `pine/EGX_VOLUME_CORREL.pine` | `EGVCor_Sync` |
| **VZO** | `pine/EGX_VOLUME_VZO.pine` | `EGVVZO_High` |
| **Twin peaks** | `pine/EGX_VOLUME_TWIN.pine` | `EGVTwn_Any` |
| **Vol MACD** | `pine/EGX_VOLUME_VMACD.pine` | `EGVMACD_Bull` |
| **Vol RSI** | `pine/EGX_VOLUME_VRSI.pine` | `EGVVRSI_Acc` |
| **3-bar surge** | `pine/EGX_VOLUME_SURGE.pine` | `EGVSur_Bull` |
| **Halt / wake** | `pine/EGX_VOLUME_HALT.pine` | `EGVHlt_WakeUp` |
| **Net buy 5d** | `pine/EGX_VOLUME_NET5.pine` | `EGVN5_Pass` |
| **Vs 52w vol** | `pine/EGX_VOLUME_HV52.pine` | `EGVH52_Record` |
| **VFI** | `pine/EGX_VOLUME_VFI.pine` | `EGVVFI_Bull` |
| **Range base** | `pine/EGX_VOLUME_RANGE.pine` | `EGVRng_BrkUp` |
| **فهرس كامل** | `docs/EGX_VOLUME.md` | 87 ملف فوليوم |
| **قرار / PRO / Mega** | `EGX_قرار.pine` · `PRO` · `VOL` · `MEGA` · **`BOARD_UNIFIED`** · `ALERTS` | **EGXQ_* · EGXQP_* · EGXMega_* · D** |
| Analyzer · Quant · Cycle · Wave · Behavior · Master · MI | باقي `pine/EGX_*.pine` | **مرجع فقط** — لا تضع أكثر من مؤشرين ثقيلين على نفس الشارت |

**الخلاصة في سطر:**  
**100 أداة = `EGX_TOOLS_MASTER` · تحليل كامل = `EGX_الاخير` · قرار سريع = `EGX_الخلاصة` · باك‌تست الأدوات = `EGX_TOOLS_MASTER_STRATEGY`.**

### تثبيت `EGX_الخلاصة.pine`

1. Pine Editor → الصق الملف → Save → **Add to chart** (إطار **D** موصى).  
2. اقرأ **بانر أسفل يسار** + **فعل** (تنفيذ / انتظر / لا شراء / خروج).  
3. Screener: `EGXKh = 1` و `EGXKh_ScreenerPro = 1` و **`EGX_RegimeOk = 1`** · شراء: `EGXKh_BuyFlag = 1`.  
4. `EGXKh_FinalCode`: 5=شراء · 4=اختراق · 3=جاهز · 2=راقب · 1=ضعيف · 0=كسر دعم.
5. **وضع مبتدئ:** يظهر بانر فقط (قرار + Rank + R/R + فعل).
6. **ملف «جلسة 15/60د»:** minVol 3000 + فلتر جلسة EGX 10:00–14:30.

### Screener — كل البادئات

| بادئة | الملف |
|--------|--------|
| `EGX_*` | الأخير |
| `EGXKh_*` | الخلاصة |
| `EGXB_*` | BEST |
| `EGXOpp_*` | أفضل فرص (ماسح 200) |
| `EGXOppB_*` | أفضل فرص BOARD (5 صفحات) |
| `EGXOppB200_*` | BOARD200 · `ReadyPct` · `Top1Score` · `MktStress` |
| `EGXOppWL_*` | أفضل فرص محفظة 6 |
| `EGXOppST_*` | باك‌تست أفضل فرص |
| `EGXOppMeta_*` | Opp × Meta screener |
| `EGXOppUni_*` | Opp × Vol Rank |
| `EGXAlHub_OppSpikePro` | Hub Opp Pro + spike |
| `EGXAlHub_Opp*` | Alert Hub · مسار Opp يومي |
| `EGXScr_*` | EGX_SCREENER |
| `EGXWL_*` | WATCHLIST |
| `EGXR_*` | RUNNER INVEST · RUNNER SCREENER |
| `EGXRWL_*` | RUNNER WATCHLIST |
| `EGXMeta_*` | META SCREENER |
| `EGXQDR_*` | Q×R DUAL |
| `EGX_VolPro` / `EGX_InB1` | الأخير + B1 (اختياري) |
| `EGXQ_*` | EGX_قرار (سهم واحد) |
| `EGXQWL_*` | EGX_قرار_WATCHLIST |
| `EGXQBD_*` | EGX_قرار_BOARD (12 · Rank↓) |
| `EGVM_*` | VOLUME MASTER |
| `EGVScr_*` | VOLUME SCREENER |
| `EGVZ_*` | VOLUME ZONES |
| `EGVWL_*` | VOLUME WATCHLIST |
| `EGXKh_VolPro` / `EGXKh_InB1` | الخلاصة + B1 |
| `EGVQ_*` | VOLUME QUICK |
| `EGVScr_Rank` | VOLUME SCREENER rank |
| `EGVRank_*` | VOLUME RANK composite |
| `EGVLiq_*` | LIQUIDITY |
| `EGVAn_*` | ANOMALY |
| `EGVMulti_*` | MULTIDAY |
| `EGVAbs_*` / `EGVDry_*` / `EGVBrk_*` | ABSORB · DRYUP · BREAKOUT |
| `EGVEff_*` / `EGVSw_*` / `EGVHeat_*` | EFFORT · SWING · HEAT |
| `EGVDiv_*` / `EGVOsc_*` | DIVERGE · OSC |
| `EGVZ_*` / `EGVBS_*` / `EGVGap_*` | ZSCORE · BUYSELL · GAP |
| `EGVCog_*` / `EGVDst_*` / `EGVTch_*` | COG · DIST · TOUCH |
| `EGVChn_*` / `EGVAl_*` | CHURN · ALERTS |
| `EGVROC_*` / `EGVUD_*` / `EGVNP_*` | ROC · ADVDEC · NVI |
| `EGVEOM_*` / `EGVBB_*` / `EGVCmp_*` | EOM · VBANDS · COMPRESS |
| `EGVSpk_*` / `EGVDash_*` | SPIKE · DASH |
| `EGVKVO_*` / `EGVVPT_*` / `EGVVX_*` | KVO · VPT · VOLMA |
| `EGVImb_*` / `EGVPr_*` / `EGVRgm_*` | IMBAL · PRINT · REGIME |
| `EGVStr_*` / `EGVHVN_*` | STREAK · HVN_LITE |
| `EGVVWMA_*` / `EGVATR_*` / `EGVMFI_*` | VWMA · ATRV · MFI |
| `EGVUV_*` / `EGVPOC_*` / `EGVCsq_*` | UVDV · POCMOVE · CONSEC |
| `EGVSNR_*` / `EGVAvg_*` | SNR · AVGSIZE |
| `EGVAD_*` / `EGVChk_*` / `EGVEFI_*` | ADL · CHAIKIN · EFI |
| `EGVExh_*` / `EGVTrp_*` / `EGVSlp_*` | EXHAUST · TRAP · SLOPE |
| `EGVWk_*` / `EGVCfm_*` | WEEKLY · CONFIRM |
| `EGVWAD_*` / `EGVCLV_*` / `EGVVR_*` | WAD · CLV · VR |
| `EGVPb_*` / `EGVBrkA_*` / `EGVCor_*` | PULLBACK · BREAKAWAY · CORREL |
| `EGVVZO_*` / `EGVTwn_*` | VZO · TWIN |
| `EGVMACD_*` / `EGVVRSI_*` / `EGVSur_*` | VMACD · VRSI · SURGE |
| `EGVHlt_*` / `EGVN5_*` / `EGVH52_*` | HALT · NET5 · HV52 |
| `EGVVFI_*` / `EGVRng_*` | VFI · RANGE |

---

## 13. مرآة باك‌تست الأخير

في `EGX_الاخير_STRATEGY`: فعّل **مرآة EGX_BuyFlag** لمطابقة `EGX_BuyFlag` على المؤشر؛ OFF = backtest صارم بأنماط (zone / retest / FVG …).

---

## 2. القرار النهائي على الشارت (`primaryDec`)

المؤشر يعرض **قرارًا واحدًا** في البانر / HUD / جدول «قرار». الأولوية من الأعلى للأسفل:

| الأولوية | القرار | معناه النهائي |
|----------|--------|----------------|
| 1 | 🔴 **كسر دعم** | **لا شراء — خروج / تجنب** حتى يتكون دعم جديد |
| 2 | 🟠 **مطاردة** | **لا شراء الآن** (قرب قمة 52 أسبوع + RSI مرتفع + R/R ضعيف) |
| 3 | 🟢 **قاع+شراء** | **أقوى سيناريو شراء** (قاع + تأكيد + إشارة شراء كاملة) |
| 4 | 🟢 **قاع — تأكيد** | قاع محتمل — **انتظر إغلاق** أو `EGX_BuyFlag=1` |
| 5 | 🟢 **شراء** | **تنفيذ مسموح** (كل الشروط + تأكيد مكان الدخول) |
| 6 | 🟢 **اختراق** | زخم — **لا مطاردة**؛ فضّل retest أو منطقة طلب |
| 7 | 🟠 **حذر/مقاومة** | **لا شراء جديد** — جني أو مراقبة |
| 8 | 🟡 **مضاربة / تراكم** | جودة جزئية — **راقب** + راجع «شروط ناقصة» |
| 9 | ⚪ **راقب / ضعيف** | **لا فعل** |

**قاعدة ذهبية:** لا تعتمد على اللون الأخضر إلا مع **`EGX_BuyFlag = 1`** (أو قرار «شراء» / «قاع+شراء» **بعد إغلاق الشمعة**).

---

## 3. متى يكون «شراء» حقيقيًا؟ (`EGX_BuyFlag`)

الشراء = **`buyConfluence`** — يجب **كل** ما يلي:

### 3.1 منطقة شراء (`buyZoneActive`)

- لا **كسر دعم**
- **سيولة OK** (`متوسط حجم ≥` حسب الملف: قياسي 1500 · مضاربة 3000 · استثمار 800)
- **MTF** غير سلبي (`mtfBias ≥ 1`)
- **تقييم** ≥ 55 + **R/R** ≥ 1.5 (افتراضي)
- **توافق عالمي** `globBull ≥ 0`
- **مضاربة أو استثمار** يحقق حدّه (`scoreSpec` / `scoreInv`) **أو** تقييم كلي ≥ 70

### 3.2 جودة إعداد (`setupOk`)

- **≥ 7 من 11** (درجة **B** أو أعلى) ما لم تُعطّل «بوابة الإعداد»

**الـ 11 شرط:** EMA stack · HTF صاعد · MACD+ · تجميع · RS20 · بنية صاعدة · منطقة طلب · retest دعم · R/R · عالمي · MTF · حجم (spike/RVOL)

### 3.3 فلاتر EGX

- لا **منع نظام هابط** على المؤشرات (`bearRegimeBlock`)
- لا **قرب حد +10%** يومي (افتراضي ≥ 9% من إغلاق أمس)
- لا **مطاردة** إذا فعّلت «منع BUY عند مطarدة»

### 3.4 تأكيد مكان (واحد على الأقل)

- عند **دعم** · **VWAP−σ** · **S1/PP** · **retest دعم + طلب** · **إعادة اختبار اختراق**

### 3.5 التوقيت

- **إغلاق الشمعة** ON (موصى) → `sigOk`

---

## 4. قرار الماسح (Screener) — نهائي

| المستوى | الشرط | متى تستخدمه |
|---------|--------|-------------|
| **عادي** | `EGX_ScreenerPass = 1` | قائمة يومية: رتبة + إعداد + R/R + فرصة + دورة + (اختياري) شراء |
| **+ بوابات** | `EGX_ScreenerPassGates = 1` | نفس العادي + **≥ 8/10 بوابات** |
| **Pro** | `EGX_ScreenerPro = 1` | Pass + **فرصة قوية** + **دورة 12** ضمن نطاق الملف |

**فلتر TradingView جاهز:**

```text
EGX_Akhir = 1
EGX_ScreenerPro = 1
```

**فلتر يدوي صارم (ملف EGX قياسي):**

```text
EGX_BuyFlag = 1
EGX_SetupTier ≥ 3        // B أو أعلى
EGX_Rank ≥ 65
EGX_RR ≥ 1.5
EGX_AccScore ≥ 60
EGX_DistRisk < 40
EGX_BreakState = 4       // اختراق مؤكد (اختياري للزخم)
EGX_Opportunity ≥ 68
EGX_Cycle12 بين 4 و 7
```

**الخلاصة:** للمسح اليومي استخدم **Pro**؛ للصفقة الواحدة على الشارت اتبع **BuyFlag + primaryDec**.

---

## 5. بوابات الشراء (10/10) — قرار مساعد

| # | البوابة | نعم = |
|---|--------|--------|
| 1 | سيولة | `liqOk` |
| 2 | MTF | `mtfBullOk` |
| 3 | عالمي | `globBull ≥ 0` |
| 4 | R/R | ≥ 1.5 |
| 5 | إعداد | ≥ 7/11 |
| 6 | نظام سوق | لا `bearRegimeBlock` |
| 7 | مطاردة | لا `chaseWarn` (أو غير ممنوع) |
| 8 | تصريف | `DistRisk < 65` |
| 9 | دورة | مرحلة 12 بين 3–8 وليست 9 |
| 10 | مكان | دعم / VWAP / pivot / break retest / طلب |

- **10/10 + BuyFlag** → أعلى جودة  
- **≥ 8/10 + buyZoneActive** → «◐» جاهز — انتظر لمس منطقة  
- صف **«شروط ناقصة»** يقول ما ينقص (صياد موجات)

---

## 6. فرصة / رتبة — كيف تقرأ الرقم؟

| المقياس | قرار عملي |
|---------|-----------|
| **EGX_Rank** | ≥ **65** (قياسي) · ≥ **60** (استثمار) · ≥ **70** تنبيه «رتبة عالية» |
| **EGX_Opportunity** | ≥ **68** = فرصة قوية (مع B+ و Dist < 55) |
| **EGX_Score** | ≥ 70 قوي · 50–69 راقب · < 50 ضعيف |
| **إعداد A/B/C/D** | **A** 9–11 · **B** 7–8 · **C** 5–6 · **D** &lt; 5 → لا شراء مع البوابة |

**Kelly (`EGX_KellyPct`):** حجم **اقتراحي** فقط — سقف منطقي 5–15% من المحفظة ما لم تختبر أنت.

---

## 7. تنفيذ صفقة — قرار نهائي (خطوات)

1. **الإطار:** يومي **D** للقرار؛ 60د/15د بعد تأكيد يومي للتوقيت.  
2. **الرمز:** `EGX:XXXX` · مثال `EGX:COMI`.  
3. **الملف:** `EGX قياسي (موصى)` · **إغلاق الشمعة ON**.  
4. **قبل الدخول:**  
   - `primaryDec` = شراء أو قاع+شراء  
   - `EGX_BuyFlag = 1`  
   - `EGX_RR ≥ 1.5`  
   - ليس 🔴 كسر / 🟠 مطarدة / ⚠ +10%  
5. **من الجدول:** **دخول · وقف** → Entry / SL · **أهداف** T1 → T2 → T3.  
6. **إدارة:**  
   - جني **50%** عند خط منتصف T1 (إن ظهر)  
   - **وقف متحرك** بعد T1 (افتراضي ×1.2 ATR)  
   - **إلغاء السينario:** كسر `stopLoss` أو **إلغاء موجي** أو فشل اختراق  
7. **Strategy Tester:** عمولة **~0.125%** · slippage **2** · عملة **EGP** — كما في `EGX_الاخير_STRATEGY`.

---

## 8. متى **لا** تشتري (قرار نهائي — veto)

- 🔴 **كسر دعم** أو `EGX_SupportBreak = 1`  
- 🟠 **مطاردة** / `EGX_ChaseWarn = 1`  
- **قرب حد EGX +10%** / `EGX_LimitBlock = 1`  
- **ضغط بيعي على EGX30/70/100** (`EGX_BearRegimeBlock = 1`)  
- **تصريف قوي** `EGX_DistRisk ≥ 65–70`  
- **سيولة ضعيفة** تحت حد الملف  
- **R/R &lt; 1.5** (افتراضي)  
- **إعداد &lt; 7/11** مع بوابة الإعداد مفعّلة  

---

## 9. EGX BEST — قرار مختصر (إن استخدمت البديل)

| القرار على الشارت | فعل |
|-------------------|-----|
| 🔴 كسر دعم | خروج |
| 🟠 قرب +10% / مطarدة | لا شراء |
| 🟢 شراء | BUY (`EGXB_Buy = 1`) |
| 🟡 جاهز — انتظر المنطقة | راقب اللمس |
| Screener | `EGXB_Buy=1` · Rank≥65 · R/R≥1.5 · Setup≥7 |

---

## 10. التثبيت (30 ثانية)

1. Pine Editor → الصق `EGX_الاخير.pine` → Save → **Add to chart**.  
2. رمز EGX · إطار **Daily**.  
3. للباك‌تست: سكربت **منفصل** → `EGX_الاخير_STRATEGY.pine`.  
4. تنبيهات: **Once per bar close** · اختياري **JSON webhook** من إعدادات المؤشر.

---

## 11. ما لا يفعله Pine (قرار نهائي — لا تتوقعه)

- Footprint · Delta · breadth كامل السوق · هوية مؤسسات/ميكر · إفصاحات تلقائية.  
- Event study / DNA / تشابه = **متوسطات تاريخية** — ليست ضمانًا.

---

## 12. بطاقة قرار سريعة (اطبعها)

```
┌─────────────────────────────────────────────────────────┐
│  EGX — قرار نهائي                                       │
├─────────────────────────────────────────────────────────┤
│  المؤشر: EGX_الاخير · إطار D · إغلاق شمعة ON            │
│  شراء: primaryDec 🟢 شراء/قاع+شراء + EGX_BuyFlag=1      │
│  جودة: Rank≥65 · Setup B+ (7/11) · RR≥1.5 · Opp≥68     │
│  ماسح: EGX_ScreenerPro=1                                │
│  veto: كسر دعم · مطarدة · +10% · bear regime · dist عالي │
│  خروج: SL · إلغاء موجي · كسر دعم · trail بعد T1         │
└─────────────────────────────────────────────────────────┘
```

---

## 14. EGX قرار v4 — سهم واحد

| نوع | متى |
|-----|-----|
| **PRO موحّد** (افتراضي) | عدّاء + يومي + DNA / Ultra في مؤشر واحد |
| **عدّاء استثمار** | موجات 1000% · دورة 4–7 · فخ بعد سقوط |
| **EGX يومي** | retest دعم + تراكم · رتبة 62 |
| **فلسي EGX** | حجم 400 · تجم 50 · رتبة 55 |

**اقرأ:** بانر · HUD · جدول · **«ناقص»** · صندوق منطقة شراء  
**فعل (`EGXQ_Action`):** 4=تنفيذ · 3=امسك/إضافة · 2=انتظر · 1=لا · 0=خروج  
**ماسح:** `EGXQ_ScreenerPro=1` · `EGXQ_ScreenerUltra=1` · `EGXQ_PreBreak=1` · veto `EGXQ_CrashTrap=1`  
**حجم مقترح:** `EGXQ_PosPct` · **مبتدئ:** بانر فقط  
**ملفات:** `pine/EGX_قرار.pine` · `_STRATEGY` · `_SCREENER` · **`_WATCHLIST`** (`EGXQWL_Pass`, `EGXQWL_TopRank`)  
**تنبيهات:** Telegram · JSON webhook · Ultra / PreBreak / Trim  

---

## 15. فلاتر قرار سريعة (TradingView)

```
شراء:      EGXQ_Qarar=1 · EGXQ_Buy=1 · EGXQ_Action=4
Ultra:     + EGXQ_ScreenerUltra=1 · EGXQ_DNA≥55
PreBreak:  EGXQ_PreBreak=1 · EGXQ_CrashTrap=0
تجنّب:     EGXQ_Exit=1 · EGXQ_CrashTrap=1 · EGXQ_ChaseWarn=1
محفظة 6:   EGXQWL_Pass=1 · EGXQWL_AnyBuy=1
```


## 16. QUICK · BOARD · محفظة

| ملف | متى |
|-----|-----|
| `pine/EGX_قرار_QUICK.pine` | **بانر واحد** في وسط الشارت — أخف من قرار كامل |
| `pine/EGX_قرار_WATCHLIST.pine` | **6** رموز · صف ★ أعلى Rank |
| `pine/EGX_قرار_BOARD.pine` | **12** رمز · **مرتب Rank** · `EGXQBD_LeaderBuy=1` |

**Board فلاتر:** `EGXQBD_Pass=1` · `EGXQBD_BuyCount≥1` · `EGXQBD_LeaderDNA≥55`  
**Quick:** نفس `EGXQ_Buy` / `EGXQ_Action` للتنبيهات على سهم واحد.


## 17. BOARD20 · Ultra ST · Telegram

| ملف | ماذا |
|-----|------|
| `pine/EGX_قرار_BOARD20.pine` | **20** رمز · Rank · `EGXQBD20_UltraLeader` |
| `pine/EGX_قرار_PRESETS.pine` | قوائم **عدّاء / EGX30 / فلسي** (12 رمز) |
| `EGX_قرار_STRATEGY.pine` | **Ultra فقط** + plot `EGXQ_Buy` مرآة للماسح |

**ST Ultra:** فعّل «دخول Ultra فقط» · DNA ≥ 55 · PRO موحّd  
**QUICK Telegram:** إعدادات EGX → Telegram ON → Alert `alert()` على إغلاق  
**Board20 فلاتر:** `EGXQBD20_LeaderBuy=1` · `EGXQBD20_UltraLeader=1`

```
محفظة 20:  EGXQBD20_Pass=1 · EGXQBD20_BuyCount≥1
```


## 18. ST مرآة · Q×R · Telegram

| عنصر | تفاصيل |
|------|--------|
| **ST `مرآة قرار`** | افتراضي — نفس `canBuy` في `EGX_قرار.pine` |
| **Ultra ST** | دخول عند `screenerUltra` فقط |
| **plots مرآة** | `EGXQ_Buy` · `EGXQ_ScreenerUltra` من الاستراتيجية |
| **`EGX_قرار_DUAL.pine`** | قرار vs عدّاء · `EGXQDR_Agree=1` |
| **Telegram** | QUICK أو قرار → Alert **Any alert()** · Once per bar close |

**خطوات TV → Telegram:**  
1) `@userinfobot` → Chat ID  
2) Alert على الشارت → Notifications → Webhook URL: `https://api.telegram.org/bot<TOKEN>/sendMessage?chat_id=<ID>&text={{message}}`  
3) أو نسخ نص `alert()` من Q!/قرار

**فلاتر:** `EGXQDR_Agree=1` · `EGXQ_ST_CanBuy=1` · ST + `EGXQ_ScreenerUltra=1`


## 19. حزمة التوحيد (منفّذة)

| ملف | دور |
|-----|-----|
| `EGX_الاخير.pine` v1.2 | halt/LULD · تأكيد اختراق · حجم 1–2% · overlay أذون/دولار/أرباح |
| `EGX_Core.pine` v3 | Library: ±10 ثم LULD ±20 · جلسة · halt EGX100 · حجم |
| `EGX_META_SCREENER.pine` | `EGXMeta_Triple` = أخير Pro + Vol + Q-lite |
| `EGX_RUNNER_SCREENER.pine` | ماسح عدّاء · `EGXR_ScreenerPro` |
| `EGX_RUNNER_WATCHLIST.pine` | 6 رموز · `EGXRWL_Pass` |
| `EGX_قرar_DUAL.pine` | Q×R · `EGXQDR_RecommendedAction` |
| `EGX_قرar_PRESETS.pine` | preset قطاعات EGX |
| `EGX_قرar.pine` | JSON: exit · Pro/Ultra |

**ST:** RUNNER → `EGXR_Buy` · `EGXR_ScreenerPro` · `EGXR_ST_CanBuy`

```
Triple:    EGXMeta=1 · EGXMeta_Triple=1
Runner:    EGXRWL_Pass=1 · EGXR_ScreenerPro=1
Q×R:       EGXQDR_Agree=1 · EGXQDR_RecommendedAction=4
```

## 20. إضافات موحّدة (Uni · Q×V · Hub)

| ملف | فلتر |
|-----|--------|
| `EGX_UNIFIED_SCREENER.pine` | `EGXUni_Pro=1` |
| `EGX_قرar_QxV.pine` | `EGXQV_Agree=1` |
| `EGX_MARKET_ONLY.pine` | `EGXMkt_BlockBuy` |
| `EGX_ALERT_HUB.pine` | `EGXAlHub_Any=1` |
| `EGX_SECTOR_BOARD.pine` | `EGXSec_LeaderRank` · `EGXSec_Lead3d` |
| `EGX_RS_BOARD.pine` | `EGXRS_Top70` · `EGXRS_Pct` |
| `docs/EGX_SYMBOLS.md` | قوائم رموز |
| `docs/EGX_MICROSTRUCTURE.md` | جلسة · حدود · حجم · overlay |

**لا تضف ملفات فوليوم جديدة.** البيع على المكشوف: EGX30 فقط (`isEgx30Short`).

```
هيكل:     EGX_HaltWarn=0 · EGX_LuldLock=0 · EGX_MktHalt100=0
جلسة:     EGX_SessId=2 · EGX_SundaySkip=0
حجم:      EGX_PosPctRisk · EGX_AdvCapShares
قطاع:     EGXSec_Lead3d=1
RS20:     EGXRS_Top70=1
```

---

*آخر مواءمة: `EGX_الاخير.pine` v1.2 · `EGX_Core` v3 · `docs/EGX_MICROSTRUCTURE.md`*
