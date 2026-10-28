#!/usr/bin/env python3
"""Generate 100 EGX Tool Pine files (مجموعة الزخم→البروفايل)."""
from __future__ import annotations

from pathlib import Path

OUT = Path("/Users/kareem/Desktop/pine/pine/tools")

HEAD = '''//@version=6
indicator("{title}", shorttitle="{short}", overlay={ov}, {extra}max_tables_count=2, calc_bars_count=5000)

// مجموعة {group} · #{n:02d}/100 · docs/EGX_TOOLS.md
// vote: +1 صاعد · 0 محايد · -1 هابط · OHLCV فقط — تعليمي مش نصيحة

'''

TAIL = '''
plot(vote, "{plot}_Vote", display=display.all)
plot(vote == 1 ? 1 : 0, "{plot}_Bull", display=display.all)
plot(vote == -1 ? 1 : 0, "{plot}_Bear", display=display.all)

var table t = table.new(position.top_left, 2, 2, border_width=1)
if barstate.islast
    table.clear(t, 0, 0, 1, 1)
    table.cell(t, 0, 0, "{code}", bgcolor=color.black, text_color=color.white, text_size=size.small)
    table.cell(t, 1, 0, vote > 0 ? "▲ شراء" : vote < 0 ? "▼ بيع" : "— محايد", text_color=vote > 0 ? color.lime : vote < 0 ? color.red : color.gray, text_size=size.small)

alertcondition(vote == 1 and vote[1] != 1, "EGX T-{code} صاعد", "EGX Tool {code}: vote صاعد")
alertcondition(vote == -1 and vote[1] != -1, "EGX T-{code} هابط", "EGX Tool {code}: vote هابط")
'''


def wrap(n: int, code: str, ar: str, en: str, group: str, overlay: bool, body: str) -> str:
    extra = "max_labels_count=80, max_lines_count=80, max_boxes_count=40, " if overlay else ""
    title = f"EGX Tool {n:02d} {ar} — {en}"
    short = f"EGX T-{code}"
    return (
        HEAD.format(title=title, short=short, ov="true" if overlay else "false", extra=extra, group=group, n=n)
        + body.strip()
        + "\n"
        + TAIL.format(plot=f"EGXT_{code}", code=code)
    )


# n, code, ar, en, group, overlay, body
TOOLS: list[tuple] = []

# ══════════════ A زخم 1–20 ══════════════
TOOLS += [
(1, "RSI", "RSI", "RSI", "أ الزخم", False, '''
int len = input.int(14, "RSI")
float v = ta.rsi(close, len)
int vote = v >= 55 and v <= 70 ? 1 : v <= 45 and v >= 30 ? -1 : v < 30 ? 1 : v > 70 ? -1 : 0
plot(v, "EGXT_RSI_Val", color=color.teal, linewidth=2)
hline(70, "70", color=color.red)
hline(30, "30", color=color.lime)
hline(50, "50", color=color.gray)
'''),
(2, "CRSI", "كونورز RSI", "Connors RSI-2", "أ الزخم", False, '''
int rsiLen = input.int(3, "RSI")
int stkLen = input.int(2, "Streak RSI")
int prLen = input.int(100, "PercentRank")
float streak = 0.0
streak := close > close[1] ? (nz(streak[1]) > 0 ? nz(streak[1]) + 1.0 : 1.0) : close < close[1] ? (nz(streak[1]) < 0 ? nz(streak[1]) - 1.0 : -1.0) : 0.0
float v = (ta.rsi(close, rsiLen) + ta.rsi(streak, stkLen) + ta.percentrank(ta.roc(close, 1), prLen)) / 3.0
int vote = v < 15 ? 1 : v > 85 ? -1 : 0
plot(v, "EGXT_CRSI_Val", color=color.orange, linewidth=2)
hline(15, "15", color=color.lime)
hline(85, "85", color=color.red)
'''),
(3, "STOCH", "ستوكاستك", "Stochastic", "أ الزخم", False, '''
int kLen = input.int(14, "%K")
int dLen = input.int(3, "%D")
k = ta.sma(ta.stoch(close, high, low, kLen), 3)
d = ta.sma(k, dLen)
int vote = k > d and k < 80 ? 1 : k < d and k > 20 ? -1 : 0
plot(k, "EGXT_STOCH_K", color=color.teal, linewidth=2)
plot(d, "EGXT_STOCH_D", color=color.orange, linewidth=1)
hline(80, "80", color=color.red)
hline(20, "20", color=color.lime)
'''),
(4, "STOCHRSI", "StochRSI", "StochRSI", "أ الزخم", False, '''
int len = input.int(14, "RSI/Stoch")
float rsi = ta.rsi(close, len)
k = ta.sma(ta.stoch(rsi, rsi, rsi, len), 3)
d = ta.sma(k, 3)
int vote = ta.crossover(k, d) and k < 30 ? 1 : k > d and k < 80 ? 1 : k < d and k > 20 ? -1 : 0
plot(k, "EGXT_SRSI_K", color=color.aqua, linewidth=2)
plot(d, "EGXT_SRSI_D", color=color.orange)
hline(80, "80", color=color.red)
hline(20, "20", color=color.lime)
'''),
(5, "MACD", "MACD", "MACD", "أ الزخم", False, '''
[macdL, macdS, macdH] = ta.macd(close, 12, 26, 9)
int vote = macdH > 0 and macdL > macdS ? 1 : macdH < 0 and macdL < macdS ? -1 : 0
plot(macdH, "EGXT_MACD_H", color=macdH >= 0 ? color.lime : color.red, style=plot.style_columns)
plot(macdL, "EGXT_MACD_L", color=color.teal)
plot(macdS, "EGXT_MACD_S", color=color.orange)
hline(0, "0", color=color.gray)
'''),
(6, "CCI", "CCI", "CCI", "أ الزخم", False, '''
int len = input.int(20, "CCI")
float v = ta.cci(close, len)
int vote = v > 0 and v < 200 ? 1 : v < 0 and v > -200 ? -1 : v <= -200 ? 1 : v >= 200 ? -1 : 0
plot(v, "EGXT_CCI_Val", color=color.fuchsia, linewidth=2)
hline(100, "+100", color=color.red)
hline(-100, "-100", color=color.lime)
hline(0, "0", color=color.gray)
'''),
(7, "WILLIAMSR", "ويليامز %R", "Williams %R", "أ الزخم", False, '''
int len = input.int(14, "%R")
float v = ta.wpr(len)
int vote = v > -20 ? -1 : v < -80 ? 1 : v > -50 ? 1 : -1
plot(v, "EGXT_WPR_Val", color=color.yellow, linewidth=2)
hline(-20, "-20", color=color.red)
hline(-80, "-80", color=color.lime)
'''),
(8, "ROC", "ROC", "Rate of Change", "أ الزخم", False, '''
int len = input.int(12, "ROC")
float v = ta.roc(close, len)
int vote = v > 1 ? 1 : v < -1 ? -1 : 0
plot(v, "EGXT_ROC_Val", color=v >= 0 ? color.lime : color.red, linewidth=2)
hline(0, "0", color=color.gray)
'''),
(9, "MFI", "MFI", "Money Flow Index", "أ الزخم", False, '''
int len = input.int(14, "MFI")
float v = ta.mfi(hlc3, len)
int vote = v >= 55 and v <= 80 ? 1 : v <= 45 and v >= 20 ? -1 : v < 20 ? 1 : v > 80 ? -1 : 0
plot(v, "EGXT_MFI_Val", color=color.teal, linewidth=2)
hline(80, "80", color=color.red)
hline(20, "20", color=color.lime)
hline(50, "50", color=color.gray)
'''),
(10, "UO", "المذبذب النهائي", "Ultimate Oscillator", "أ الزخم", False, '''
float bp = close - math.min(low, close[1])
float trR = math.max(high, close[1]) - math.min(low, close[1])
float a7 = math.sum(bp, 7) / math.max(math.sum(trR, 7), syminfo.mintick)
float a14 = math.sum(bp, 14) / math.max(math.sum(trR, 14), syminfo.mintick)
float a28 = math.sum(bp, 28) / math.max(math.sum(trR, 28), syminfo.mintick)
float v = 100.0 * (4.0 * a7 + 2.0 * a14 + a28) / 7.0
int vote = v > 55 ? 1 : v < 45 ? -1 : 0
plot(v, "EGXT_UO_Val", color=color.aqua, linewidth=2)
hline(70, "70", color=color.red)
hline(30, "30", color=color.lime)
hline(50, "50", color=color.gray)
'''),
(11, "TSI", "TSI", "True Strength Index", "أ الزخم", False, '''
float v = ta.tsi(close, 13, 25)
float sig = ta.ema(v, 13)
int vote = v > sig and v > 0 ? 1 : v < sig and v < 0 ? -1 : 0
plot(v, "EGXT_TSI_Val", color=color.teal, linewidth=2)
plot(sig, "EGXT_TSI_Sig", color=color.orange)
hline(0, "0", color=color.gray)
'''),
(12, "FISHER", "فيشر", "Fisher Transform", "أ الزخم", False, '''
int len = input.int(10, "Fisher")
float fhh = ta.highest(hl2, len)
float fll = ta.lowest(hl2, len)
float fv = 0.0
fv := 0.66 * ((hl2 - fll) / math.max(fhh - fll, syminfo.mintick) - 0.5) + 0.67 * nz(fv[1])
fv := math.max(math.min(fv, 0.999), -0.999)
float fish = 0.0
fish := 0.5 * math.log((1.0 + fv) / (1.0 - fv)) + 0.5 * nz(fish[1])
int vote = fish > fish[1] and fish > 0 ? 1 : fish < fish[1] and fish < 0 ? -1 : 0
plot(fish, "EGXT_FISH_Val", color=color.fuchsia, linewidth=2)
plot(fish[1], "EGXT_FISH_Trig", color=color.gray)
hline(0, "0", color=color.gray)
'''),
(13, "CMO", "CMO", "Chande Momentum", "أ الزخم", False, '''
int len = input.int(14, "CMO")
float chg = ta.change(close)
float su = math.sum(math.max(chg, 0.0), len)
float sd = math.sum(math.max(-chg, 0.0), len)
float v = 100.0 * (su - sd) / math.max(su + sd, syminfo.mintick)
int vote = v > 20 ? 1 : v < -20 ? -1 : 0
plot(v, "EGXT_CMO_Val", color=color.orange, linewidth=2)
hline(50, "50", color=color.red)
hline(-50, "-50", color=color.lime)
hline(0, "0", color=color.gray)
'''),
(14, "PPO", "PPO", "Percentage Price Osc", "أ الزخم", False, '''
float fast = ta.ema(close, 12)
float slow = ta.ema(close, 26)
float v = slow > 0 ? 100.0 * (fast - slow) / slow : 0.0
float sig = ta.ema(v, 9)
int vote = v > sig and v > 0 ? 1 : v < sig and v < 0 ? -1 : 0
plot(v, "EGXT_PPO_Val", color=color.teal, linewidth=2)
plot(sig, "EGXT_PPO_Sig", color=color.orange)
hline(0, "0", color=color.gray)
'''),
(15, "AO", "AO", "Awesome Oscillator", "أ الزخم", False, '''
float v = ta.sma(hl2, 5) - ta.sma(hl2, 34)
int vote = v > 0 and v > v[1] ? 1 : v < 0 and v < v[1] ? -1 : 0
plot(v, "EGXT_AO_Val", color=v >= v[1] ? color.lime : color.red, style=plot.style_columns)
hline(0, "0", color=color.gray)
'''),
(16, "TRIX", "TRIX", "TRIX", "أ الزخم", False, '''
int len = input.int(15, "TRIX")
float v = 10000.0 * ta.change(ta.ema(ta.ema(ta.ema(math.log(math.max(close, syminfo.mintick)), len), len), len))
float sig = ta.sma(v, 9)
int vote = v > sig and v > 0 ? 1 : v < sig and v < 0 ? -1 : 0
plot(v, "EGXT_TRIX_Val", color=color.aqua, linewidth=2)
plot(sig, "EGXT_TRIX_Sig", color=color.orange)
hline(0, "0", color=color.gray)
'''),
(17, "KST", "KST", "Know Sure Thing", "أ الزخم", False, '''
float rcma1 = ta.sma(ta.roc(close, 10), 10)
float rcma2 = ta.sma(ta.roc(close, 15), 10)
float rcma3 = ta.sma(ta.roc(close, 20), 10)
float rcma4 = ta.sma(ta.roc(close, 30), 15)
float v = rcma1 + 2.0 * rcma2 + 3.0 * rcma3 + 4.0 * rcma4
float sig = ta.sma(v, 9)
int vote = v > sig and v > 0 ? 1 : v < sig and v < 0 ? -1 : 0
plot(v, "EGXT_KST_Val", color=color.teal, linewidth=2)
plot(sig, "EGXT_KST_Sig", color=color.orange)
hline(0, "0", color=color.gray)
'''),
(18, "COPPOCK", "كوبوك", "Coppock Curve", "أ الزخم", False, '''
float v = ta.wma(ta.roc(close, 14) + ta.roc(close, 11), 10)
int vote = v > 0 and v > v[1] ? 1 : v < 0 and v < v[1] ? -1 : 0
plot(v, "EGXT_COP_Val", color=v >= 0 ? color.lime : color.red, linewidth=2)
hline(0, "0", color=color.gray)
'''),
(19, "DPO", "DPO", "Detrended Price Osc", "أ الزخم", False, '''
int len = input.int(21, "DPO")
int k = int(len / 2) + 1
float v = close[k] - ta.sma(close, len)
int vote = v > 0 ? 1 : v < 0 ? -1 : 0
plot(v, "EGXT_DPO_Val", color=color.purple, linewidth=2)
hline(0, "0", color=color.gray)
'''),
(20, "WAVETREND", "WaveTrend", "Market Cipher WT", "أ الزخم", False, '''
int chLen = input.int(10, "Channel")
int avgLen = input.int(21, "Average")
float esa = ta.ema(hlc3, chLen)
float de = ta.ema(math.abs(hlc3 - esa), chLen)
float ci = (hlc3 - esa) / (0.015 * math.max(de, syminfo.mintick))
float wt1 = ta.ema(ci, avgLen)
float wt2 = ta.sma(wt1, 4)
int vote = wt1 > wt2 and wt1 < 60 ? 1 : wt1 < wt2 and wt1 > -60 ? -1 : 0
plot(wt1, "EGXT_WT1", color=color.teal, linewidth=2)
plot(wt2, "EGXT_WT2", color=color.orange)
hline(60, "+60", color=color.red)
hline(-60, "-60", color=color.lime)
hline(0, "0", color=color.gray)
'''),
]

# ══════════════ B اتجاه 21–35 ══════════════
TOOLS += [
(21, "ADX", "ADX/DMI", "ADX DMI", "ب الاتجاه", False, '''
int len = input.int(14, "ADX")
[diP, diM, adx] = ta.dmi(len, len)
int vote = adx > 20 and diP > diM ? 1 : adx > 20 and diM > diP ? -1 : 0
plot(adx, "EGXT_ADX", color=color.yellow, linewidth=2)
plot(diP, "EGXT_DI+", color=color.lime)
plot(diM, "EGXT_DI-", color=color.red)
hline(25, "25", color=color.gray)
'''),
(22, "AROON", "أرون", "Aroon", "ب الاتجاه", False, '''
int len = input.int(14, "Aroon")
[arDn, arUp] = ta.aroon(len)
int vote = arUp > arDn and arUp > 70 ? 1 : arDn > arUp and arDn > 70 ? -1 : 0
plot(arUp, "EGXT_AR_UP", color=color.lime, linewidth=2)
plot(arDn, "EGXT_AR_DN", color=color.red, linewidth=2)
'''),
(23, "VORTEX", "فورتكس", "Vortex", "ب الاتجاه", False, '''
int len = input.int(14, "Vortex")
float vmP = math.sum(math.abs(high - low[1]), len)
float vmM = math.sum(math.abs(low - high[1]), len)
float trSum = math.max(math.sum(ta.tr, len), syminfo.mintick)
float viP = vmP / trSum
float viM = vmM / trSum
int vote = viP > viM ? 1 : -1
plot(viP, "EGXT_VI+", color=color.lime, linewidth=2)
plot(viM, "EGXT_VI-", color=color.red, linewidth=2)
'''),
(24, "SAR", "بارابوليك SAR", "Parabolic SAR", "ب الاتجاه", True, '''
float start = input.float(0.02, "Start", step=0.01)
float inc = input.float(0.02, "Increment", step=0.01)
float mx = input.float(0.2, "Max", step=0.05)
float v = ta.sar(start, inc, mx)
int vote = close > v ? 1 : -1
plot(v, "EGXT_SAR", color=vote > 0 ? color.lime : color.red, style=plot.style_cross, linewidth=2)
'''),
(25, "ICHIMOKU", "إيشيموكو", "Ichimoku", "ب الاتجاه", True, '''
float tenkan = (ta.highest(high, 9) + ta.lowest(low, 9)) / 2.0
float kijun = (ta.highest(high, 26) + ta.lowest(low, 26)) / 2.0
float spanA = (tenkan + kijun) / 2.0
float spanB = (ta.highest(high, 52) + ta.lowest(low, 52)) / 2.0
float cloudTop = math.max(spanA[26], spanB[26])
float cloudBot = math.min(spanA[26], spanB[26])
int vote = close > cloudTop and tenkan > kijun ? 1 : close < cloudBot and tenkan < kijun ? -1 : 0
p1 = plot(spanA, "SpanA", color=color.new(color.lime, 70), offset=26)
p2 = plot(spanB, "SpanB", color=color.new(color.red, 70), offset=26)
fill(p1, p2, color=spanA > spanB ? color.new(color.lime, 85) : color.new(color.red, 85))
plot(tenkan, "Tenkan", color=color.red)
plot(kijun, "Kijun", color=color.blue)
plot(close[26], "Chikou", color=color.gray, offset=-26)
'''),
(26, "HULL", "هال", "Hull MA", "ب الاتجاه", True, '''
int len = input.int(21, "HMA")
float v = ta.hma(close, len)
int vote = close > v and v > v[1] ? 1 : close < v and v < v[1] ? -1 : 0
plot(v, "EGXT_HMA", color=v >= v[1] ? color.lime : color.red, linewidth=2)
'''),
(27, "KAMA", "KAMA", "Kaufman AMA", "ب الاتجاه", True, '''
int erLen = input.int(10, "ER")
int fast = input.int(2, "Fast")
int slow = input.int(30, "Slow")
float change = math.abs(close - close[erLen])
float volat = math.sum(math.abs(close - close[1]), erLen)
float er = volat > 0 ? change / volat : 0.0
float sc = math.pow(er * (2.0 / (fast + 1.0) - 2.0 / (slow + 1.0)) + 2.0 / (slow + 1.0), 2.0)
var float kama = na
kama := na(kama[1]) ? close : nz(kama[1]) + sc * (close - nz(kama[1]))
int vote = close > kama and kama > kama[1] ? 1 : close < kama and kama < kama[1] ? -1 : 0
plot(kama, "EGXT_KAMA", color=color.orange, linewidth=2)
'''),
(28, "MCGINLEY", "ماكجينلي", "McGinley Dynamic", "ب الاتجاه", True, '''
int len = input.int(14, "N")
var float mg = na
float prev = nz(mg[1], close)
mg := prev + (close - prev) / (len * math.pow(close / math.max(prev, syminfo.mintick), 4.0))
int vote = close > mg and mg > mg[1] ? 1 : close < mg and mg < mg[1] ? -1 : 0
plot(mg, "EGXT_MG", color=color.aqua, linewidth=2)
'''),
(29, "GMMA", "غابي GMMA", "Guppy MMA", "ب الاتجاه", True, '''
float gS = (ta.ema(close, 3) + ta.ema(close, 5) + ta.ema(close, 8) + ta.ema(close, 10) + ta.ema(close, 12) + ta.ema(close, 15)) / 6.0
float gL = (ta.ema(close, 30) + ta.ema(close, 35) + ta.ema(close, 40) + ta.ema(close, 45) + ta.ema(close, 50) + ta.ema(close, 60)) / 6.0
int vote = gS > gL and close > gS ? 1 : gS < gL and close < gS ? -1 : 0
plot(gS, "EGXT_GMMA_S", color=color.lime, linewidth=2)
plot(gL, "EGXT_GMMA_L", color=color.red, linewidth=2)
'''),
(30, "DONCHIAN", "دونشيان", "Donchian", "ب الاتجاه", True, '''
int len = input.int(20, "Donchian")
float hi = ta.highest(high, len)
float lo = ta.lowest(low, len)
float mid = (hi + lo) / 2.0
int vote = close > hi[1] ? 1 : close < lo[1] ? -1 : close > mid ? 1 : close < mid ? -1 : 0
plot(hi, "EGXT_DC_HI", color=color.lime)
plot(lo, "EGXT_DC_LO", color=color.red)
plot(mid, "EGXT_DC_MID", color=color.gray)
'''),
(31, "EMASTACK", "تكديس EMA", "EMA 20/50/200", "ب الاتجاه", True, '''
float e20 = ta.ema(close, 20)
float e50 = ta.ema(close, 50)
float e200 = ta.ema(close, 200)
int vote = close > e20 and e20 > e50 and e50 > e200 ? 1 : close < e20 and e20 < e50 and e50 < e200 ? -1 : 0
plot(e20, "EMA20", color=color.teal)
plot(e50, "EMA50", color=color.orange)
plot(e200, "EMA200", color=color.purple, linewidth=2)
'''),
(32, "ELDERRAY", "إلدر راي", "Elder Ray", "ب الاتجاه", False, '''
float e13 = ta.ema(close, 13)
float bullP = high - e13
float bearP = low - e13
int vote = e13 > e13[1] and bearP < 0 and bearP > bearP[1] ? 1 : e13 < e13[1] and bullP > 0 and bullP < bullP[1] ? -1 : e13 > e13[1] ? 1 : -1
plot(bullP, "BullPower", color=color.lime, style=plot.style_columns)
plot(bearP, "BearPower", color=color.red, style=plot.style_columns)
hline(0, "0", color=color.gray)
'''),
(33, "ELDERIMP", "إلدر إمبلس", "Elder Impulse", "ب الاتجاه", True, '''
float e13 = ta.ema(close, 13)
[macdL, macdS, macdH] = ta.macd(close, 12, 26, 9)
bool green = e13 > e13[1] and macdH > macdH[1]
bool red = e13 < e13[1] and macdH < macdH[1]
int vote = green ? 1 : red ? -1 : 0
barcolor(green ? color.new(color.lime, 40) : red ? color.new(color.red, 40) : color.new(color.blue, 70))
'''),
(34, "SCHAFF", "شاف", "Schaff Trend Cycle", "ب الاتجاه", False, '''
float macd = ta.ema(close, 23) - ta.ema(close, 50)
float lo = ta.lowest(macd, 10)
float hi = ta.highest(macd, 10)
float stoch1 = hi - lo > 0 ? 100.0 * (macd - lo) / (hi - lo) : 50.0
float pf = ta.ema(stoch1, 3)
float lo2 = ta.lowest(pf, 10)
float hi2 = ta.highest(pf, 10)
float stoch2 = hi2 - lo2 > 0 ? 100.0 * (pf - lo2) / (hi2 - lo2) : 50.0
float v = ta.ema(stoch2, 3)
int vote = v > 25 and v > v[1] ? 1 : v < 75 and v < v[1] ? -1 : 0
plot(v, "EGXT_STC", color=color.fuchsia, linewidth=2)
hline(75, "75", color=color.red)
hline(25, "25", color=color.lime)
'''),
(35, "SUPERTREND", "سوبرترند", "SuperTrend", "ب الاتجاه", True, '''
float factor = input.float(3.0, "Factor", step=0.1)
int atrLen = input.int(10, "ATR")
[stLine, dir] = ta.supertrend(factor, atrLen)
int vote = dir < 0 ? 1 : -1
plot(stLine, "EGXT_ST", color=vote > 0 ? color.lime : color.red, linewidth=2)
'''),
]

# ══════════════ C حجم 36–50 ══════════════
TOOLS += [
(36, "OBV", "OBV", "On Balance Volume", "ج الحجم", False, '''
float v = ta.obv
float sl = ta.linreg(v, 10, 0) - ta.linreg(v, 10, 1)
int vote = sl > 0 and v > v[10] ? 1 : sl < 0 and v < v[10] ? -1 : 0
plot(v, "EGXT_OBV", color=sl >= 0 ? color.lime : color.red, linewidth=2)
'''),
(37, "ADL", "A/D", "Accumulation/Distribution", "ج الحجم", False, '''
float v = ta.accdist
float ema = ta.ema(v, 20)
int vote = v > ema and v > v[10] ? 1 : v < ema and v < v[10] ? -1 : 0
plot(v, "EGXT_AD", color=v >= ema ? color.lime : color.red, linewidth=2)
plot(ema, "EGXT_AD_EMA", color=color.orange)
'''),
(38, "CMF", "CMF", "Chaikin Money Flow", "ج الحجم", False, '''
int len = input.int(20, "CMF")
float mfm = ((close - low) - (high - close)) / math.max(high - low, syminfo.mintick)
float v = ta.sma(mfm * volume, len) / ta.sma(volume, len)
int vote = v > 0.05 ? 1 : v < -0.05 ? -1 : 0
plot(v, "EGXT_CMF", color=v >= 0 ? color.lime : color.red, style=plot.style_histogram)
hline(0, "0", color=color.gray)
'''),
(39, "CHAIKIN", "شايكين", "Chaikin Oscillator", "ج الحجم", False, '''
float v = ta.ema(ta.accdist, 3) - ta.ema(ta.accdist, 10)
int vote = v > 0 ? 1 : -1
plot(v, "EGXT_CHO", color=v >= 0 ? color.lime : color.red, linewidth=2)
hline(0, "0", color=color.gray)
'''),
(40, "EFI", "Force", "Elder Force Index", "ج الحجم", False, '''
int len = input.int(13, "EMA")
float v = ta.ema(ta.change(close) * volume, len)
int vote = v > 0 ? 1 : -1
plot(v, "EGXT_EFI", color=v >= 0 ? color.lime : color.red, linewidth=2)
hline(0, "0", color=color.gray)
'''),
(41, "EOM", "EOM", "Ease of Movement", "ج الحجم", False, '''
int len = input.int(14, "EOM")
float raw = (high - low) > 0 and volume > 0 ? (hl2 - hl2[1]) / (volume / 1000000.0 / (high - low)) : 0.0
float v = ta.sma(raw, len)
int vote = v > 0 ? 1 : -1
plot(v, "EGXT_EOM", color=v >= 0 ? color.lime : color.red, linewidth=2)
hline(0, "0", color=color.gray)
'''),
(42, "KVO", "Klinger", "Klinger Volume Osc", "ج الحجم", False, '''
float trend = hlc3 > hlc3[1] ? 1.0 : -1.0
float dm = high - low
float cm = 0.0
cm := nz(cm[1]) + dm
float vf = volume * trend * 100.0 * math.abs(2.0 * dm / math.max(cm, syminfo.mintick) - 1.0)
float kvo = ta.ema(vf, 34) - ta.ema(vf, 55)
float sig = ta.ema(kvo, 13)
int vote = kvo > sig ? 1 : -1
plot(kvo, "EGXT_KVO", color=color.teal, linewidth=2)
plot(sig, "EGXT_KVO_S", color=color.orange)
hline(0, "0", color=color.gray)
'''),
(43, "VPT", "VPT", "Volume Price Trend", "ج الحجم", False, '''
float v = ta.pvt
float ema = ta.ema(v, 20)
int vote = v > ema ? 1 : -1
plot(v, "EGXT_VPT", color=v >= ema ? color.lime : color.red, linewidth=2)
plot(ema, "EGXT_VPT_EMA", color=color.orange)
'''),
(44, "NVI", "NVI", "Negative Volume Index", "ج الحجم", False, '''
var float nvi = 1000.0
nvi := volume < volume[1] ? nz(nvi[1]) * (1.0 + ta.change(close) / math.max(close[1], syminfo.mintick)) : nz(nvi[1], 1000.0)
float sig = ta.ema(nvi, 255)
int vote = nvi > sig ? 1 : -1
plot(nvi, "EGXT_NVI", color=color.aqua, linewidth=2)
plot(sig, "EGXT_NVI_EMA", color=color.orange)
'''),
(45, "VWAP", "VWAP جلسة", "Session VWAP", "ج الحجم", True, '''
float v = ta.vwap(hlc3)
int vote = close > v ? 1 : -1
plot(v, "EGXT_VWAP", color=color.yellow, linewidth=2)
'''),
(46, "AVWAP", "AVWAP شانون", "Anchored VWAP", "ج الحجم", True, '''
int look = input.int(120, "مرساة قاع/قمة")
int loB = bar_index + ta.lowestbars(low, look)
int hiB = bar_index + ta.highestbars(high, look)
int anchor = loB
var float num = 0.0
var float den = 0.0
if bar_index == anchor or na(num)
    num := hlc3 * volume
    den := volume
else
    num := num[1] + hlc3 * volume
    den := den[1] + volume
float avwap = den > 0 ? num / den : close
int vote = close > avwap ? 1 : -1
plot(avwap, "EGXT_AVWAP", color=color.fuchsia, linewidth=2)
'''),
(47, "WEIS", "وايز ويف", "Weis Wave", "ج الحجم", False, '''
int len = input.int(5, "اتجاه الموجة")
var float wave = 0.0
var int dir = 1
bool up = close > close[len]
bool dn = close < close[len]
if up and dir <= 0
    dir := 1
    wave := volume
else if dn and dir >= 0
    dir := -1
    wave := volume
else
    wave += volume
int vote = dir > 0 ? 1 : -1
plot(dir > 0 ? wave : -wave, "EGXT_WEIS", color=dir > 0 ? color.lime : color.red, style=plot.style_columns)
'''),
(48, "CVD", "CVD", "Cumulative Volume Delta", "ج الحجم", False, '''
float rng = math.max(high - low, syminfo.mintick)
float buyV = volume * (close - low) / rng
float sellV = volume - buyV
float delta = buyV - sellV
var float cvd = 0.0
cvd += delta
float sl = ta.linreg(cvd, 10, 0) - ta.linreg(cvd, 10, 1)
int vote = sl > 0 ? 1 : -1
plot(cvd, "EGXT_CVD", color=sl >= 0 ? color.lime : color.red, linewidth=2)
'''),
(49, "RVOL", "حجم نسبي", "Relative Volume", "ج الحجم", False, '''
int len = input.int(20, "MA حجم")
float volMa = ta.sma(volume, len)
float v = volume / math.max(volMa, 1.0)
int vote = v >= 1.3 and close > open ? 1 : v >= 1.3 and close < open ? -1 : 0
plot(v, "EGXT_RVOL", color=v >= 1.3 ? color.fuchsia : color.gray, style=plot.style_columns)
hline(1.0, "1x", color=color.gray)
hline(1.5, "1.5x", color=color.orange)
'''),
(50, "BUYSHARE", "نصيب الشراء", "Buy Share proxy", "ج الحجم", False, '''
float rng = math.max(high - low, syminfo.mintick)
float v = (close - low) / rng * 100.0
int vote = v >= 60 ? 1 : v <= 40 ? -1 : 0
plot(v, "EGXT_BUYSH", color=v >= 50 ? color.lime : color.red, linewidth=2)
hline(50, "50", color=color.gray)
'''),
]

# ══════════════ D تقلب 51–60 ══════════════
TOOLS += [
(51, "BBPERCENT", "%B", "Bollinger %B", "د التقلب", False, '''
int len = input.int(20, "BB")
float mult = input.float(2.0, "Mult")
[mid, up, lo] = ta.bb(close, len, mult)
float v = (up - lo) > 0 ? (close - lo) / (up - lo) : 0.5
int vote = v > 0.8 ? -1 : v < 0.2 ? 1 : v > 0.5 ? 1 : -1
plot(v, "EGXT_PB", color=color.aqua, linewidth=2)
hline(1, "1", color=color.red)
hline(0, "0", color=color.lime)
hline(0.5, "0.5", color=color.gray)
'''),
(52, "BBW", "BBW", "Bollinger Bandwidth", "د التقلب", False, '''
int len = input.int(20, "BB")
[mid, up, lo] = ta.bb(close, len, 2.0)
float v = mid > 0 ? (up - lo) / mid : 0.0
float p20 = ta.percentile_linear_interpolation(v, 100, 20)
int vote = v < p20 and close > mid ? 1 : v < p20 and close < mid ? -1 : 0
plot(v, "EGXT_BBW", color=color.orange, linewidth=2)
'''),
(53, "SQUEEZE", "TTM Squeeze", "TTM Squeeze", "د التقلب", False, '''
[bMid, bUp, bLo] = ta.bb(close, 20, 2.0)
[kMid, kUp, kLo] = ta.kc(close, 20, 1.5)
bool sq = bUp < kUp and bLo > kLo
float mom = ta.linreg(close - (ta.highest(high, 20) + ta.lowest(low, 20)) / 2.0, 20, 0)
int vote = not sq and mom > 0 and mom > mom[1] ? 1 : not sq and mom < 0 and mom < mom[1] ? -1 : 0
plot(mom, "EGXT_SQ_MOM", color=mom >= 0 ? color.lime : color.red, style=plot.style_columns)
plot(sq ? 0 : na, "SqueezeON", color=color.red, style=plot.style_circles, linewidth=3)
'''),
(54, "KELTNER", "كيلتنر", "Keltner Channel", "د التقلب", True, '''
[mid, up, lo] = ta.kc(close, 20, 1.5)
int vote = close > up ? 1 : close < lo ? -1 : close > mid ? 1 : -1
plot(up, "KC_UP", color=color.lime)
plot(mid, "KC_MID", color=color.gray)
plot(lo, "KC_LO", color=color.red)
'''),
(55, "ATR", "ATR%", "ATR Percent", "د التقلب", False, '''
float v = ta.atr(14) / close * 100.0
float med = ta.sma(v, 50)
int vote = v < med * 0.85 ? 0 : v > med * 1.6 ? (close > open ? -1 : 1) : close > ta.ema(close, 20) ? 1 : -1
plot(v, "EGXT_ATRP", color=color.yellow, linewidth=2)
plot(med, "Median", color=color.gray)
'''),
(56, "ULCER", "أولسر", "Ulcer Index", "د التقلب", False, '''
int len = input.int(14, "Ulcer")
float maxC = ta.highest(close, len)
float dd = 100.0 * (close - maxC) / math.max(maxC, syminfo.mintick)
float v = math.sqrt(ta.sma(dd * dd, len))
int vote = v < 5 ? 1 : v > 12 ? -1 : 0
plot(v, "EGXT_ULCER", color=color.red, linewidth=2)
hline(5, "5", color=color.lime)
'''),
(57, "STARC", "STARC", "STARC Bands", "د التقلب", True, '''
float mid = ta.sma(close, 15)
float band = ta.atr(15) * 1.33
plot(mid + band, "STARC+", color=color.red)
plot(mid, "STARC", color=color.gray)
plot(mid - band, "STARC-", color=color.lime)
int vote = close > mid and close < mid + band ? 1 : close < mid and close > mid - band ? -1 : close >= mid + band ? -1 : 1
'''),
(58, "HV", "تقلب تاريخي", "Historical Volatility", "د التقلب", False, '''
int len = input.int(20, "HV")
float lr = math.log(close / math.max(close[1], syminfo.mintick))
float v = ta.stdev(lr, len) * math.sqrt(252.0) * 100.0
float med = ta.sma(v, 50)
int vote = v < med ? 1 : -1
plot(v, "EGXT_HV", color=color.purple, linewidth=2)
plot(med, "Med", color=color.gray)
'''),
(59, "CHANDELIER", "شاندلير", "Chandelier Exit", "د التقلب", True, '''
int len = input.int(22, "Look")
float mult = input.float(3.0, "ATR ×")
float atr = ta.atr(14)
float chL = ta.highest(high, len) - mult * atr
float chS = ta.lowest(low, len) + mult * atr
var int dir = 1
if close > chS[1]
    dir := 1
else if close < chL[1]
    dir := -1
int vote = dir
plot(dir == 1 ? chL : chS, "EGXT_CH", color=dir == 1 ? color.lime : color.red, linewidth=2)
'''),
(60, "CHOP", "تشوبنس", "Choppiness Index", "د التقلب", False, '''
int len = input.int(14, "Chop")
float v = 100.0 * math.log10(math.sum(ta.tr, len) / math.max(ta.highest(high, len) - ta.lowest(low, len), syminfo.mintick)) / math.log10(len)
int vote = v < 38.2 ? (close > ta.ema(close, 50) ? 1 : -1) : 0
plot(v, "EGXT_CHOP", color=color.orange, linewidth=2)
hline(61.8, "Range", color=color.red)
hline(38.2, "Trend", color=color.lime)
'''),
]

# ══════════════ E SMC 61–70 ══════════════
TOOLS += [
(61, "BOS", "BOS", "Break of Structure", "ه SMC", True, '''
int len = input.int(8, "Swing")
float ph = ta.pivothigh(high, len, len)
float pl = ta.pivotlow(low, len, len)
var float lastH = na
var float lastL = na
if not na(ph)
    lastH := ph
if not na(pl)
    lastL := pl
bool bosUp = not na(lastH) and close > lastH and close[1] <= lastH
bool bosDn = not na(lastL) and close < lastL and close[1] >= lastL
var int vote = 0
if bosUp
    vote := 1
if bosDn
    vote := -1
plot(lastH, "LastHigh", color=color.new(color.red, 40), style=plot.style_linebr)
plot(lastL, "LastLow", color=color.new(color.lime, 40), style=plot.style_linebr)
plotshape(bosUp, "BOS+", shape.triangleup, location.belowbar, color.lime, size=size.tiny)
plotshape(bosDn, "BOS-", shape.triangledown, location.abovebar, color.red, size=size.tiny)
'''),
(62, "FVG", "FVG", "Fair Value Gap", "ه SMC", True, '''
bool bullFvg = low > high[2]
bool bearFvg = high < low[2]
int vote = bullFvg ? 1 : bearFvg ? -1 : 0
bgcolor(bullFvg ? color.new(color.lime, 85) : bearFvg ? color.new(color.red, 85) : na)
'''),
(63, "OB", "Order Block", "Order Block", "ه SMC", True, '''
int len = input.int(8, "Swing")
float ph = ta.pivothigh(high, len, len)
float pl = ta.pivotlow(low, len, len)
var float demHi = na
var float demLo = na
var float supHi = na
var float supLo = na
if not na(pl)
    demLo := low[len]
    demHi := high[len]
if not na(ph)
    supLo := low[len]
    supHi := high[len]
bool inDem = not na(demLo) and low <= demHi and close >= demLo
bool inSup = not na(supHi) and high >= supLo and close <= supHi
int vote = inDem ? 1 : inSup ? -1 : 0
plot(demHi, "DemandHi", color=color.new(color.lime, 50), style=plot.style_linebr)
plot(demLo, "DemandLo", color=color.new(color.lime, 50), style=plot.style_linebr)
plot(supHi, "SupplyHi", color=color.new(color.red, 50), style=plot.style_linebr)
plot(supLo, "SupplyLo", color=color.new(color.red, 50), style=plot.style_linebr)
'''),
(64, "LIQ", "سيولة", "Liquidity Pools", "ه SMC", True, '''
int len = input.int(20, "Equal highs/lows")
float eqH = ta.highest(high, len)
float eqL = ta.lowest(low, len)
bool nearH = high > eqH * 0.997 and high < eqH * 1.003
bool nearL = low < eqL * 1.003 and low > eqL * 0.997
int vote = nearL ? 1 : nearH ? -1 : 0
plot(eqH, "BuySideLiq", color=color.new(color.red, 30))
plot(eqL, "SellSideLiq", color=color.new(color.lime, 30))
'''),
(65, "SWEEP", "سويب", "Liquidity Sweep", "ه SMC", True, '''
int len = input.int(8, "Swing")
float ph = ta.pivothigh(high, len, len)
float pl = ta.pivotlow(low, len, len)
var float lastH = na
var float lastL = na
if not na(ph)
    lastH := ph
if not na(pl)
    lastL := pl
bool sweepHi = not na(lastH) and high > lastH and close < lastH
bool sweepLo = not na(lastL) and low < lastL and close > lastL
int vote = sweepLo ? 1 : sweepHi ? -1 : 0
plotshape(sweepLo, "SSL", shape.diamond, location.belowbar, color.lime, size=size.tiny)
plotshape(sweepHi, "BSL", shape.diamond, location.abovebar, color.red, size=size.tiny)
'''),
(66, "PO3", "Power of 3", "AMD Power of Three", "ه SMC", True, '''
int len = input.int(20, "Range")
float hi = ta.highest(high, len)
float lo = ta.lowest(low, len)
float mid = (hi + lo) / 2.0
float rng = hi - lo
bool accum = rng / close < 0.04
bool manip = (high > hi[1] and close < mid) or (low < lo[1] and close > mid)
bool distUp = close > hi[1] and close > open and volume > ta.sma(volume, 20)
bool distDn = close < lo[1] and close < open
int vote = distUp ? 1 : distDn ? -1 : manip ? 0 : accum ? 0 : close > mid ? 1 : -1
plot(hi, "RangeHi", color=color.gray)
plot(lo, "RangeLo", color=color.gray)
'''),
(67, "OTE", "OTE", "Optimal Trade Entry", "ه SMC", True, '''
int len = input.int(20, "Impulse")
float hi = ta.highest(high, len)
float lo = ta.lowest(low, len)
float oteLo = hi - 0.79 * (hi - lo)
float oteHi = hi - 0.62 * (hi - lo)
bool upImp = close > close[len]
float zLo = upImp ? lo + 0.62 * (hi - lo) : oteLo
float zHi = upImp ? lo + 0.79 * (hi - lo) : oteHi
bool inOte = close >= math.min(zLo, zHi) and close <= math.max(zLo, zHi)
int vote = inOte and upImp ? 1 : inOte and not upImp ? -1 : 0
plot(zHi, "OTE_HI", color=color.new(color.aqua, 30))
plot(zLo, "OTE_LO", color=color.new(color.aqua, 30))
'''),
(68, "BREAKER", "بريكر", "Breaker Block", "ه SMC", True, '''
int len = input.int(8, "Swing")
float ph = ta.pivothigh(high, len, len)
float pl = ta.pivotlow(low, len, len)
var float brkHi = na
var float brkLo = na
var int side = 0
if not na(pl) and close < low[len]
    brkLo := low[len]
    brkHi := high[len]
    side := -1
if not na(ph) and close > high[len]
    brkLo := low[len]
    brkHi := high[len]
    side := 1
bool retestBull = side == 1 and not na(brkHi) and low <= brkHi and close > brkLo
bool retestBear = side == -1 and not na(brkLo) and high >= brkLo and close < brkHi
int vote = retestBull ? 1 : retestBear ? -1 : side
plot(brkHi, "BrkHi", color=color.new(color.orange, 40), style=plot.style_linebr)
plot(brkLo, "BrkLo", color=color.new(color.orange, 40), style=plot.style_linebr)
'''),
(69, "PREMIUM", "Premium/Discount", "PD Array 50%", "ه SMC", True, '''
int look = input.int(80, "Swing range")
float hi = ta.highest(high, look)
float lo = ta.lowest(low, look)
float eq = (hi + lo) / 2.0
int vote = close < eq ? 1 : -1
plot(hi, "RangeHi", color=color.new(color.red, 50))
plot(eq, "EQ 50%", color=color.yellow, linewidth=2)
plot(lo, "RangeLo", color=color.new(color.lime, 50))
'''),
(70, "MSS", "MSS", "Market Structure Shift", "ه SMC", True, '''
int len = input.int(5, "MSS swing")
float ph = ta.pivothigh(high, len, len)
float pl = ta.pivotlow(low, len, len)
var float h1 = na
var float h2 = na
var float l1 = na
var float l2 = na
if not na(ph)
    h2 := h1
    h1 := ph
if not na(pl)
    l2 := l1
    l1 := pl
bool hhhl = not na(h1) and not na(h2) and not na(l1) and not na(l2) and h1 > h2 and l1 > l2
bool lhll = not na(h1) and not na(h2) and not na(l1) and not na(l2) and h1 < h2 and l1 < l2
int vote = hhhl ? 1 : lhll ? -1 : 0
plotshape(hhhl and not hhhl[1], "MSS+", shape.circle, location.belowbar, color.lime, size=size.tiny)
plotshape(lhll and not lhll[1], "MSS-", shape.circle, location.abovebar, color.red, size=size.tiny)
'''),
]

# ══════════════ F موجات 71–82 ══════════════
TOOLS += [
(71, "FIB", "فيبو ارتداد", "Fib Retracement", "و موجات", True, '''
int look = input.int(60, "موجة")
float hi = ta.highest(high, look)
float lo = ta.lowest(low, look)
float rg = hi - lo
float f382 = hi - 0.382 * rg
float f500 = hi - 0.500 * rg
float f618 = hi - 0.618 * rg
bool upLeg = close > close[look]
float zLo = upLeg ? lo + 0.382 * rg : f618
float zHi = upLeg ? lo + 0.618 * rg : f382
int vote = close >= math.min(zLo, zHi) and close <= math.max(zLo, zHi) ? (upLeg ? 1 : -1) : close > hi - 0.236 * rg ? 1 : close < lo + 0.236 * rg ? -1 : 0
plot(f382, "38.2", color=color.new(color.teal, 30))
plot(f500, "50", color=color.yellow)
plot(f618, "61.8", color=color.new(color.orange, 30))
'''),
(72, "ELLIOTT", "إليوت", "Elliott Impulse", "و موجات", True, '''
int len = input.int(8, "Swing")
float ph = ta.pivothigh(high, len, len)
float pl = ta.pivotlow(low, len, len)
var array<float> pr = array.new_float()
var array<int> ty = array.new_int()
if not na(ph)
    array.push(pr, ph)
    array.push(ty, 1)
    if array.size(ty) > 12
        array.shift(pr)
        array.shift(ty)
if not na(pl)
    array.push(pr, pl)
    array.push(ty, -1)
    if array.size(ty) > 12
        array.shift(pr)
        array.shift(ty)
int n = array.size(ty)
int vote = 0
if n >= 5
    float a = array.get(pr, n - 5)
    float b = array.get(pr, n - 4)
    float c = array.get(pr, n - 3)
    float d = array.get(pr, n - 2)
    float e = array.get(pr, n - 1)
    bool impUp = array.get(ty, n - 5) == -1 and b > a and c > a and d > b and e > b
    bool impDn = array.get(ty, n - 5) == 1 and b < a and c < a and d < b and e < b
    vote := impUp ? 1 : impDn ? -1 : 0
plot(close, "Close", display=display.none)
'''),
(73, "GANN", "جان 50%", "Gann 50% retrace", "و موجات", True, '''
int look = input.int(120, "مدى جان")
float hi = ta.highest(high, look)
float lo = ta.lowest(low, look)
float mid = (hi + lo) / 2.0
int vote = close > mid ? 1 : -1
plot(hi, "GannHi", color=color.red)
plot(mid, "Gann50", color=color.orange, linewidth=2)
plot(lo, "GannLo", color=color.lime)
'''),
(74, "MURREY", "موري", "Murrey Math 8/8", "و موجات", True, '''
int look = input.int(64, "Murrey")
float hi = ta.highest(high, look)
float lo = ta.lowest(low, look)
float rng = (hi - lo) / 8.0
float m4 = lo + 4.0 * rng
int vote = close > m4 ? 1 : -1
plot(lo + 8.0 * rng, "8/8", color=color.red)
plot(lo + 5.0 * rng, "5/8", color=color.orange)
plot(m4, "4/8", color=color.yellow, linewidth=2)
plot(lo + 3.0 * rng, "3/8", color=color.teal)
plot(lo, "0/8", color=color.lime)
'''),
(75, "HARMONIC", "هارمونيك AB=CD", "Harmonic AB=CD", "و موجات", True, '''
int len = input.int(8, "Swing")
float ph = ta.pivothigh(high, len, len)
float pl = ta.pivotlow(low, len, len)
var array<float> px = array.new_float()
if not na(ph)
    array.push(px, ph)
if not na(pl)
    array.push(px, pl)
if array.size(px) > 8
    array.shift(px)
int vote = 0
if array.size(px) >= 4
    float w = array.get(px, array.size(px) - 4)
    float x = array.get(px, array.size(px) - 3)
    float y = array.get(px, array.size(px) - 2)
    float z = array.get(px, array.size(px) - 1)
    float ab = math.abs(x - w)
    float cd = math.abs(z - y)
    bool eq = ab > 0 and math.abs(cd / ab - 1.0) < 0.12
    vote := eq and z > y ? -1 : eq and z < y ? 1 : 0
plot(close, "px", display=display.none)
'''),
(76, "PIVOT", "بيفوت كلاسيك", "Classic Floor Pivots", "و موجات", True, '''
float dHi = request.security(syminfo.tickerid, "D", high[1], barmerge.gaps_off, barmerge.lookahead_off)
float dLo = request.security(syminfo.tickerid, "D", low[1], barmerge.gaps_off, barmerge.lookahead_off)
float dCl = request.security(syminfo.tickerid, "D", close[1], barmerge.gaps_off, barmerge.lookahead_off)
float pp = (dHi + dLo + dCl) / 3.0
float r1 = 2.0 * pp - dLo
float s1 = 2.0 * pp - dHi
int vote = close > pp ? 1 : -1
plot(r1, "R1", color=color.red)
plot(pp, "PP", color=color.yellow, linewidth=2)
plot(s1, "S1", color=color.lime)
'''),
(77, "ZIGZAG", "زيغزاغ داو", "Dow ZigZag", "و موجات", True, '''
int len = input.int(8, "Swing")
float ph = ta.pivothigh(high, len, len)
float pl = ta.pivotlow(low, len, len)
var float h1 = na
var float h2 = na
var float l1 = na
var float l2 = na
if not na(ph)
    h2 := h1
    h1 := ph
if not na(pl)
    l2 := l1
    l1 := pl
int vote = not na(h1) and not na(h2) and not na(l1) and not na(l2) ? (h1 > h2 and l1 > l2 ? 1 : h1 < h2 and l1 < l2 ? -1 : 0) : 0
plot(h1, "HH/LH", color=color.new(color.red, 50), style=plot.style_circles)
plot(l1, "HL/LL", color=color.new(color.lime, 50), style=plot.style_circles)
'''),
(78, "GANNTIME", "جان زمني", "Gann time counts", "و موجات", True, '''
int look = input.int(120, "مرساة")
int loB = bar_index + ta.lowestbars(low, look)
int bars = bar_index - loB
bool hit = bars == 30 or bars == 45 or bars == 60 or bars == 90 or bars == 120 or bars == 144 or bars == 180
int vote = hit ? 0 : close > ta.ema(close, 50) ? 1 : -1
bgcolor(hit ? color.new(color.yellow, 80) : na)
'''),
(79, "FIBTIME", "فيبو زمني", "Fib time 8/13/21", "و موجات", True, '''
int look = input.int(120, "مرساة قاع")
int loB = bar_index + ta.lowestbars(low, look)
int bars = bar_index - loB
bool hit = bars == 8 or bars == 13 or bars == 21 or bars == 34 or bars == 55 or bars == 89
int vote = hit ? 0 : close > ta.ema(close, 50) ? 1 : -1
bgcolor(hit ? color.new(color.aqua, 82) : na)
'''),
(80, "HOSODA", "هوسودا", "Ichimoku NT/N targets", "و موجات", True, '''
int len = input.int(8, "Swing")
float ph = ta.pivothigh(high, len, len)
float pl = ta.pivotlow(low, len, len)
var float a = na
var float b = na
var float c = na
if not na(pl)
    a := b
    b := c
    c := pl
if not na(ph)
    a := b
    b := c
    c := ph
float nt = not na(a) and not na(b) and not na(c) ? c + (c - a) : na
float nT = not na(a) and not na(c) ? 2.0 * c - a : na
int vote = not na(nt) and close < nt and close > nz(b, close) ? 1 : not na(nt) and close > nt ? -1 : 0
plot(nt, "NT", color=color.orange, style=plot.style_linebr)
plot(nT, "N", color=color.yellow, style=plot.style_linebr)
'''),
(81, "SQUARE9", "مربع 9", "Gann Square of 9", "و موجات", True, '''
float root = math.sqrt(math.max(close, 0.0))
float up = math.pow(root + 1.0, 2.0)
float dn = math.pow(math.max(root - 1.0, 0.0), 2.0)
int vote = close > (up + dn) / 2.0 ? 1 : -1
plot(up, "Sq9+", color=color.red)
plot(dn, "Sq9-", color=color.lime)
'''),
(82, "NEOWAVE", "نيوويف", "NeoWave proxy", "و موجات", True, '''
int len = input.int(8, "Swing")
float ph = ta.pivothigh(high, len, len)
float pl = ta.pivotlow(low, len, len)
var array<int> bars = array.new_int()
var array<float> px = array.new_float()
if not na(ph)
    array.push(bars, bar_index - len)
    array.push(px, ph)
if not na(pl)
    array.push(bars, bar_index - len)
    array.push(px, pl)
if array.size(px) > 10
    array.shift(bars)
    array.shift(px)
int vote = 0
if array.size(px) >= 3
    int t1 = array.get(bars, array.size(bars) - 1) - array.get(bars, array.size(bars) - 2)
    int t0 = array.get(bars, array.size(bars) - 2) - array.get(bars, array.size(bars) - 3)
    bool timeOK = t0 > 0 and t1 >= int(t0 * 0.382) and t1 <= int(t0 * 2.618)
    float last = array.get(px, array.size(px) - 1)
    vote := timeOK and close > last ? 1 : timeOK and close < last ? -1 : 0
plot(close, "nw", display=display.none)
'''),
]

# ══════════════ G أنظمة 83–94 ══════════════
TOOLS += [
(83, "WYCKOFF", "وايكوف", "Wyckoff SC/BC proxy", "ز أنظمة", True, '''
float volMa = ta.sma(volume, 20)
float rvol = volume / math.max(volMa, 1.0)
float rng = high - low
float rngMa = ta.sma(rng, 20)
bool sc = rvol >= 1.8 and close > open and rng > rngMa and close > (high + low) / 2.0 and close < close[5]
bool bc = rvol >= 1.8 and close < open and rng > rngMa and close > close[5]
float mfm = ((close - low) - (high - close)) / math.max(rng, syminfo.mintick)
float cmf = ta.sma(mfm * volume, 20) / ta.sma(volume, 20)
int vote = sc or cmf > 0.05 ? 1 : bc or cmf < -0.05 ? -1 : 0
plotshape(sc, "SC", shape.diamond, location.belowbar, color.lime, size=size.tiny)
plotshape(bc, "BC", shape.diamond, location.abovebar, color.red, size=size.tiny)
'''),
(84, "VSA", "VSA", "Volume Spread Analysis", "ز أنظمة", False, '''
float volMa = ta.sma(volume, 20)
float spread = high - low
float spMa = ta.sma(spread, 20)
bool effortUp = volume > volMa * 1.4 and spread < spMa * 0.7 and close > open
bool effortDn = volume > volMa * 1.4 and spread < spMa * 0.7 and close < open
bool easyUp = volume < volMa * 0.8 and spread > spMa and close > open
int vote = easyUp or (close > open and volume > volMa and spread > spMa) ? 1 : effortUp ? -1 : effortDn ? 1 : close < open and volume > volMa ? -1 : 0
plot(volume, "Vol", color=vote > 0 ? color.lime : vote < 0 ? color.red : color.gray, style=plot.style_columns)
'''),
(85, "VCP", "VCP مينرفيني", "Minervini VCP", "ز أنظمة", True, '''
float r1 = ta.highest(high, 15) - ta.lowest(low, 15)
float r2 = ta.highest(high, 10) - ta.lowest(low, 10)
float r3 = ta.highest(high, 5) - ta.lowest(low, 5)
bool contract = r1 > r2 and r2 > r3
float volMa = ta.sma(volume, 20)
bool dry = ta.sma(volume, 5) < volMa * 0.85
float pivot = ta.highest(high, 15)
bool fire = contract and dry and close > pivot[1] and volume > volMa * 1.4
int vote = fire ? 1 : contract and dry ? 0 : close > ta.ema(close, 50) ? 1 : -1
plot(pivot, "Pivot", color=color.yellow, style=plot.style_linebr)
plotshape(fire, "VCP", shape.triangleup, location.belowbar, color.lime, size=size.small)
'''),
(86, "CANSLIM", "CANSLIM", "O'Neil RS+volume", "ز أنظمة", True, '''
float roc = ta.roc(close, 63)
float rs = ta.percentrank(roc, 252)
float volMa = ta.sma(volume, 50)
bool volThrust = volume > volMa * 1.4 and close > open
int dist = 0
for i = 0 to 24
    if close[i] < open[i] and volume[i] > ta.sma(volume, 50)[i]
        dist += 1
int vote = rs >= 70 and volThrust and dist < 5 and close > ta.sma(close, 50) ? 1 : dist >= 5 ? -1 : rs < 40 ? -1 : 0
plot(rs, "RS%", display=display.none)
'''),
(87, "WEINSTEIN", "وينستين", "Weinstein Stage", "ز أنظمة", True, '''
float ma30 = ta.sma(close, 150)
float sl = ta.linreg(ma30, 10, 0) - ta.linreg(ma30, 10, 1)
int vote = close > ma30 and sl > 0 ? 1 : close < ma30 and sl < 0 ? -1 : 0
plot(ma30, "MA30W~", color=sl >= 0 ? color.lime : color.red, linewidth=2)
'''),
(88, "TURTLE", "ترتل", "Turtle 20-day", "ز أنظمة", True, '''
int len = input.int(20, "Breakout")
float hi = ta.highest(high[1], len)
float lo = ta.lowest(low[1], len)
bool brkUp = close > hi
bool soupUp = low < lo and close > lo
int vote = brkUp ? 1 : soupUp ? 1 : close < lo ? -1 : 0
plot(hi, "20H", color=color.lime)
plot(lo, "20L", color=color.red)
plotshape(soupUp, "Soup", shape.diamond, location.belowbar, color.aqua, size=size.tiny)
'''),
(89, "LIVERMORE", "ليفرمور", "Livermore Pivotal", "ز أنظمة", True, '''
int len = input.int(8, "Pivot")
float ph = ta.pivothigh(high, len, len)
var float piv = na
if not na(ph)
    piv := ph
bool breakPiv = not na(piv) and close > piv and close[1] <= piv
int vote = breakPiv ? 1 : not na(piv) and close > piv ? 1 : not na(piv) and close < piv ? -1 : 0
plot(piv, "Pivotal", color=color.yellow, style=plot.style_linebr, linewidth=2)
'''),
(90, "QULLA", "كولاماجي", "Qullamaggie flag", "ز أنظمة", True, '''
float impulse = ta.roc(close, 20)
float compress = ta.stdev(close, 5) < ta.stdev(close, 20) * 0.6
float ema10 = ta.ema(close, 10)
bool flag = impulse > 15 and compress and close > ema10
bool fire = flag and close > ta.highest(high[1], 5) and volume > ta.sma(volume, 20)
int vote = fire ? 1 : flag ? 0 : close > ema10 ? 1 : -1
plot(ema10, "EMA10", color=color.teal)
plotshape(fire, "EP", shape.triangleup, location.belowbar, color.lime, size=size.small)
'''),
(91, "DARVAS", "داروفاس", "Darvas Box", "ز أنظمة", True, '''
int dvLen = input.int(20, "قمة الصندوق")
float dvH = ta.highest(high, dvLen)
float dvLow4 = ta.lowest(low, 4)
bool dvNew = dvH[3] > dvH[4] and dvH == dvH[3]
var float dvTop = na
var float dvBot = na
var int dvState = 0
if dvNew
    dvTop := dvH
    dvBot := dvLow4
    dvState := 0
if not na(dvTop)
    if dvState <= 0 and close > dvTop
        dvState := 1
    else if dvState >= 0 and close < dvBot
        dvState := -1
int vote = dvState
plot(dvTop, "BoxTop", color=color.yellow, style=plot.style_linebr)
plot(dvBot, "BoxBot", color=color.yellow, style=plot.style_linebr)
'''),
(92, "BROOKS", "بروكس", "Al Brooks Always-In", "ز أنظمة", True, '''
float ema20 = ta.ema(close, 20)
bool spikeUp = close > open and (high - low) > ta.atr(14) * 1.2 and close > ema20
bool spikeDn = close < open and (high - low) > ta.atr(14) * 1.2 and close < ema20
var int ai = 0
if spikeUp
    ai := 1
if spikeDn
    ai := -1
int vote = ai != 0 ? ai : close > ema20 ? 1 : -1
plot(ema20, "EMA20", color=color.blue)
'''),
(93, "HURST", "هرست", "Hurst-like cycle", "ز أنظمة", False, '''
int len = input.int(32, "R/S")
float mu = ta.sma(close, len)
float dev = close - mu
float z = ta.cum(dev) - ta.sma(ta.cum(dev), len)
float rng = ta.highest(z, len) - ta.lowest(z, len)
float sd = ta.stdev(close, len)
float rs = sd > 0 ? rng / sd : 0.0
int vote = rs > 1.2 and close > mu ? 1 : rs > 1.2 and close < mu ? -1 : 0
plot(rs, "EGXT_HURST", color=color.purple, linewidth=2)
hline(1, "1", color=color.gray)
'''),
(94, "MESA", "MESA", "MAMA/FAMA", "ز أنظمة", True, '''
[mama, fama] = ta.mama(close, 0.5, 0.05)
int vote = mama > fama ? 1 : -1
plot(mama, "MAMA", color=color.lime, linewidth=2)
plot(fama, "FAMA", color=color.red, linewidth=2)
'''),
]

# ══════════════ H بروفايل 95–100 ══════════════
TOOLS += [
(95, "VPPOC", "POC", "Volume Profile POC", "ح بروفايل", True, '''
int look = input.int(80, "نافذة")
int bins = input.int(24, "Bins")
int n = math.min(look, bar_index)
float hi = ta.highest(high, n)
float lo = ta.lowest(low, n)
float step = math.max((hi - lo) / bins, syminfo.mintick)
float best = 0.0
int bi = 0
for b = 0 to bins - 1
    float acc = 0.0
    for i = 0 to n - 1
        int idx = int(math.floor((close[i] - lo) / step))
        if idx == b
            acc += volume[i]
    if acc > best
        best := acc
        bi := b
float poc = lo + (bi + 0.5) * step
int vote = close > poc ? 1 : -1
plot(poc, "POC", color=color.yellow, linewidth=2)
'''),
(96, "TPO", "TPO", "Market Profile TPO proxy", "ح بروفايل", True, '''
int look = input.int(40, "TPO bars")
int bins = input.int(16, "Bins")
int n = math.min(look, bar_index)
float hi = ta.highest(high, n)
float lo = ta.lowest(low, n)
float step = math.max((hi - lo) / bins, syminfo.mintick)
float best = 0.0
int bi = 0
for b = 0 to bins - 1
    float acc = 0.0
    for i = 0 to n - 1
        int idx = int(math.floor((hlc3[i] - lo) / step))
        if idx == b
            acc += 1.0
    if acc > best
        best := acc
        bi := b
float tpo = lo + (bi + 0.5) * step
int vote = close > tpo ? 1 : -1
plot(tpo, "TPO-POC", color=color.orange, linewidth=2)
'''),
(97, "DEMARK", "ديمارك", "TD Sequential setup", "ح بروفايل", True, '''
var int td = 0
td := close > close[4] ? (nz(td[1]) > 0 ? nz(td[1]) + 1 : 1) : close < close[4] ? (nz(td[1]) < 0 ? nz(td[1]) - 1 : -1) : 0
bool buySetup = td <= -9
bool sellSetup = td >= 9
int vote = buySetup ? 1 : sellSetup ? -1 : td < 0 ? 1 : td > 0 ? -1 : 0
plotshape(buySetup, "TD9+", shape.labelup, location.belowbar, color.lime, text="9", textcolor=color.black, size=size.tiny)
plotshape(sellSetup, "TD9-", shape.labeldown, location.abovebar, color.red, text="9", textcolor=color.white, size=size.tiny)
'''),
(98, "CONFLUENCE", "كونفلوينس", "Clarity 0–5 proxy", "ح بروفايل", False, '''
float e20 = ta.ema(close, 20)
float e50 = ta.ema(close, 50)
float rsi = ta.rsi(close, 14)
[macdL, macdS, macdH] = ta.macd(close, 12, 26, 9)
float cmf = ta.sma(((close - low) - (high - close)) / math.max(high - low, syminfo.mintick) * volume, 20) / ta.sma(volume, 20)
float rvol = volume / math.max(ta.sma(volume, 20), 1.0)
int c = 0
c += close > e20 and e20 > e50 ? 1 : 0
c += rsi > 50 ? 1 : 0
c += macdH > 0 ? 1 : 0
c += cmf > 0 ? 1 : 0
c += rvol >= 1.0 and close > open ? 1 : 0
int vote = c >= 4 ? 1 : c <= 1 ? -1 : 0
plot(c, "EGXT_CONF", color=c >= 4 ? color.lime : c <= 1 ? color.red : color.gray, style=plot.style_columns)
hline(3, "3", color=color.gray)
'''),
(99, "RS", "قوة نسبية", "RS vs EGX30", "ح بروفايل", False, '''
string mkt = input.symbol("EGX:EGX30", "مؤشر")
float br = request.security(mkt, timeframe.period, ta.roc(close, 20), barmerge.gaps_off, barmerge.lookahead_off)
float rs = ta.roc(close, 20) - br
int vote = rs > 0 ? 1 : -1
plot(rs, "EGXT_RS", color=rs >= 0 ? color.lime : color.red, linewidth=2)
hline(0, "0", color=color.gray)
'''),
(100, "REGIME", "نظام السوق", "Trend/Range regime", "ح بروفايل", False, '''
[diP, diM, adx] = ta.dmi(14, 14)
float e20 = ta.ema(close, 20)
float e50 = ta.ema(close, 50)
bool trend = adx > 22
int vote = trend and e20 > e50 ? 1 : trend and e20 < e50 ? -1 : 0
plot(adx, "ADX", color=color.yellow, linewidth=2)
hline(22, "Trend", color=color.gray)
'''),
]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    codes = []
    for item in TOOLS:
        n, code, ar, en, group, overlay, body = item
        codes.append(code)
        path = OUT / f"EGX_T_{n:02d}_{code}.pine"
        path.write_text(wrap(n, code, ar, en, group, overlay, body), encoding="utf-8")
    if len(TOOLS) != 100:
        raise SystemExit(f"expected 100 tools, got {len(TOOLS)}")
    if len(codes) != len(set(codes)):
        raise SystemExit("duplicate codes")
    print(f"wrote {len(TOOLS)} files → {OUT}")


if __name__ == "__main__":
    main()
