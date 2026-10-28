# EGX — توافق (Confluence) و Votes

## Regime (سوق)

| Plot | المعنى |
|------|--------|
| `EGX_RegimeOk` | 1 = لا ضغط EGX30 (mom30 & tr30) **و** لا halt EGX100 |
| `EGXAlHub_MktHalt100` | EGX100 يوم −10% أو أسوأ |
| `EGXOppB200_MktBear` | ضغط على BOARD200 |

## مسارات Hub (`EGX_ALERT_HUB.pine`)

| Plot | مصدر |
|------|--------|
| `EGXAlHub_Buy` | تجميع + منطقة + regime |
| `EGXAlHub_QBuy` | قرar lite (acc + zone) |
| `EGXAlHub_Tools` | TOOLS score + BOS/طلب |
| `EGXAlHub_VolPro` | RVOL + net buy bar |
| `EGXAlHub_OppPro` | أفضل فرص D (Pro) |
| `EGXAlHub_Invest` | Buy + OppPro + Tools + acc قوي |
| `EGXAlHub_Triple` | OppPro + Tools + VolPro + QBuy + regime |
| `EGXAlHub_Mega` | OppPro + ToolsPro + VolPro + regime + no veto |
| `EGXAlHub_ToolsPro` | TOOLS lite13 Pro على D |
| `EGXAlHub_Veto` | bitmask (chase/limit/bear/h100) — انظر Matrix |
| `EGXAlHub_Votes` | 0–4 (OppPro, Q, ToolsPro, VolPro) |

## Meta / Mega

- `EGXMeta_Triple` = Akhir Pro + Vol Pro + Q Buy + **regimeOk**
- `EGXMeta_Votes` · `EGXMega_Votes` — عدّ مسارات متفقة

## Opp Desk (screener واحد)

`pine/EGX_OPP_DESK.pine` — **Opp Pro ∩ Mega Pro** (+ Meta Triple اختياري)

| Plot | معنى |
|------|------|
| `EGXOppDesk_Pro` | Desk Pro (فلتر Screener الرئيسي) |
| `EGXOppDesk_Triple` | Pro + Mega + Meta Triple |
| `EGXOppDesk_OppPro` | مسار Opp فقط |
| `EGXOppDesk_MegaPro` | Opp + Tools + Vol (Mega) |

## Micro (رمز)

- **nearLimit / halt / LULD / gap** — [`EGX_MICROSTRUCTURE.md`](EGX_MICROSTRUCTURE.md)
- **2-bar break** — `breakConfirmBars` في ST والأخير
- **RS20** — `EGX_RS_BOARD` · gate اختياري في `EGX_افضل_فرص_STRATEGY`

## Legacy

- Analyzer · Quant · Wave · Volume aux · Tools strip: `EGX_NearLimit` + veto على buy flags
- ST كاملة: `EGX_ST_PARITY.md`
