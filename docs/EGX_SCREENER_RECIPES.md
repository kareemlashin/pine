# EGX — وصفات Screener

## محافظ (يومي)

```
EGX_RegimeOk = 1
EGXScr_Pro = 1        // أو EGXKh_ScreenerPro
EGXScr_Limit = 0      // إن وُجد
```

## مضarبة (Pro + فوليوم)

```
EGX_RegimeOk = 1
EGXUni_Pro = 1
EGXUni_MktHalt100 = 0
```

## Triple (Desk)

```
EGXMeta_Triple = 1
// أو
EGXAlHub_Triple = 1
EGXAlHub_Votes >= 3
```

## Opp Desk (triple stack)

```
EGX_RegimeOk = 1
EGXOppDesk_Pro = 1
```

## Opp × Meta (Desk)

```
EGX_RegimeOk = 1
EGXOppMeta_Pro = 1
EGXOppMeta_Triple = 1   // اختياري
```

## Super Pass (2-of-3)

```
EGXSP_Veto = 0
EGXSP_Pass = 1
EGX_RegimeOk = 1
```

## Mega (فرص + Tools + Vol)

```
EGXMega_Pro = 1
EGX_RegimeOk = 1
EGXMega_Limit = 0
```

## BOARD200 (سوق — ليس Screener رمز)

- شارت واحد · plots: `EGXOppB200_LeaderScore` · `BuyCount` · `Breadth` · `Heat`
- تنبيهات: `LeadChg` · `LeaderBuy` · `ReadyPct`

## أفضل فرص ST (باك‌تست)

- `EGXOppST_Pro` على **الرمز** · ترتيب السوق من BOARD200 يدوياً

## فلتر Volume legacy

```
EGVBS_BuyDay = 1
EGX_NearLimit = 0
```
