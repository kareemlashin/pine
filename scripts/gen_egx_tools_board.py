#!/usr/bin/env python3
"""Generate pine/EGX_TOOLS_BOARD.pine (200 stocks, 5 pages) from EGX_افضل_فرص_BOARD.pine."""

from pathlib import Path

from tools_lite_f_tools import F_TOOLS_BOARD as F_TOOLS

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "pine" / "EGX_افضل_فرص_BOARD.pine"
OUT = ROOT / "pine" / "EGX_TOOLS_BOARD.pine"

text = SRC.read_text(encoding="utf-8")
start = text.index("f_p0(int i)")
end = text.index("f_opp()")
sym_block = text[start:end]

HEADER = '''//@version=6
indicator("EGX TOOLS — 200 سهم (5 صفحات)", shorttitle="T200", overlay=false, max_tables_count=1, calc_bars_count=5000)

// 40×5 صفحات · lite tools · plots: EGXTTB_*
// Screener: EGX_TOOLS_OPP · لوحة كاملة: EGX_TOOLS_BOARD200

int N = 40
string G = "═══ 200 سهم ═══"
string page = input.string("1 كبار 1–40", "صفحة", options=["1 كبار 1–40","2 SCEM–BONY","3 SUGR–ADCI","4 GDWA–AALR","5 GTWL–UNIP"], group=G)
string bench = input.symbol("EGX:EGX30", "EGX30", group=G)
bool chartIs30 = input.bool(true, "الشارت EGX30", group=G)
float minVol = input.float(800.0, "حد حجم", group=G)
float sigMin = input.float(20.0, "حد Score %", minval=10, maxval=50, group=G)
int showTop = input.int(40, "Top N", minval=5, maxval=40, group=G)
float minScoreShow = input.float(25.0, "حد Score", minval=0, maxval=80, group=G)
bool hideWeak = input.bool(false, "إخفاء ضعيف", group=G)
bool onlyBuy = input.bool(false, "A/B فقط", group=G)
string egxBoard = input.string("نشط (EGX100)", "لوحة", options=["نشط (EGX100)", "EGX30 (بيع مكشوف)", "SME تميّز", "SME نايل", "غير نشط"], group=G)

'''

TAIL = '''
float benchRoc = chartIs30 ? ta.roc(close, 20) : request.security(bench, "D", ta.roc(close, 20), barmerge.gaps_off, barmerge.lookahead_off)

f_row(int i) =>
    string s = f_sym(i)
    s == "" ? [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] : request.security(s, "D", f_tools(), barmerge.gaps_off, barmerge.lookahead_off)

float[] scA = array.new_float(N, 0.0)
float[] rkA = array.new_float(N, 0.0)
float[] buyAA = array.new_float(N, 0.0)
float[] buyBA = array.new_float(N, 0.0)
int[] hitA = array.new_int(N, 0)
int[] netA = array.new_int(N, 0)
float[] rvA = array.new_float(N, 0.0)
float[] rsA = array.new_float(N, 0.0)
float[] dayA = array.new_float(N, 0.0)
bool[] onA = array.new_bool(N, false)

for i = 0 to N - 1
    [sc, bu, ht, rv, roc20, ac, ds, rrv, dp] = f_row(i)
    bool on = f_sym(i) != ""
    float rs = roc20 - benchRoc
    int st2 = int(ht) + (rs > 0 ? 1 : 0)
    float rnk = math.max(0.0, math.min(100.0, sc * 0.55 + st2 / 7.0 * 100.0 * 0.30 + math.min(100.0, rrv / 3.0 * 100.0) * 0.15 + (rs > 0 ? 5.0 : 0.0)))
    array.set(scA, i, on ? sc : -1.0)
    array.set(rkA, i, rnk)
    array.set(buyAA, i, bu > 0 ? 1.0 : 0.0)
    array.set(buyBA, i, 0.0)
    array.set(hitA, i, int(ht))
    array.set(netA, i, int(nn))
    array.set(rvA, i, rv)
    array.set(rsA, i, rs)
    array.set(dayA, i, dp)
    array.set(onA, i, on)

int[] sorted = array.new_int(N, 0)
for k = 0 to N - 1
    array.set(sorted, k, k)
for i = 0 to N - 2
    for j = 0 to N - 2 - i
        int ia = array.get(sorted, j)
        int ib = array.get(sorted, j + 1)
        if array.get(rkA, ia) < array.get(rkA, ib)
            array.set(sorted, j, ib)
            array.set(sorted, j + 1, ia)

int[] vis = array.new_int()
for k = 0 to N - 1
    int ix = array.get(sorted, k)
    if not array.get(onA, ix)
        continue
    float sc = array.get(scA, ix)
    bool bu = array.get(buyAA, ix) > 0 or array.get(buyBA, ix) > 0
    if hideWeak and sc < minScoreShow
        continue
    if onlyBuy and not bu
        continue
    array.push(vis, ix)

int nVis = array.size(vis)
int rows = math.min(showTop, nVis)
int leader = nVis > 0 ? array.get(vis, 0) : 0
float leaderRank = nVis > 0 ? array.get(rkA, leader) : 0.0
bool leaderA = nVis > 0 and array.get(buyAA, leader) > 0
string leaderSym = nVis > 0 ? f_sym(leader) : "—"

int buyCnt = 0
int hotCnt = 0
int liveCnt = 0
for i = 0 to N - 1
    if array.get(onA, i)
        liveCnt += 1
        buyCnt += (array.get(buyAA, i) > 0 or array.get(buyBA, i) > 0) ? 1 : 0
        hotCnt += array.get(scA, i) >= sigMin ? 1 : 0

var table tb = table.new(position.top_right, 10, 44, bgcolor=color.new(#0d1117, 4), border_width=1)
if barstate.islast
    int lastR = math.max(rows + 2, 2)
    table.clear(tb, 0, 0, 9, lastR)
    color hdr = color.new(#1a2332, 8)
    table.cell(tb, 0, 0, "#", bgcolor=hdr, text_color=color.gray, text_size=size.tiny)
    table.cell(tb, 1, 0, "رمز", bgcolor=hdr, text_color=color.gray, text_size=size.tiny)
    table.cell(tb, 2, 0, "Rank", bgcolor=hdr, text_color=color.white, text_size=size.tiny)
    table.cell(tb, 3, 0, "Score", bgcolor=hdr, text_color=color.gray, text_size=size.tiny)
    table.cell(tb, 4, 0, "Hits", bgcolor=hdr, text_color=color.gray, text_size=size.tiny)
    table.cell(tb, 5, 0, "RVOL", bgcolor=hdr, text_color=color.gray, text_size=size.tiny)
    table.cell(tb, 6, 0, "RS20", bgcolor=hdr, text_color=color.gray, text_size=size.tiny)
    table.cell(tb, 7, 0, "يوم%", bgcolor=hdr, text_color=color.gray, text_size=size.tiny)
    table.cell(tb, 8, 0, "Net", bgcolor=hdr, text_color=color.gray, text_size=size.tiny)
    table.cell(tb, 9, 0, "حالة", bgcolor=hdr, text_color=color.gray, text_size=size.tiny)
    if rows > 0
        for row = 0 to rows - 1
            int ix = array.get(vis, row)
            float rnk = array.get(rkA, ix)
            float sc = array.get(scA, ix)
            bool ba = array.get(buyAA, ix) > 0
            bool bb = array.get(buyBA, ix) > 0
            float dp = array.get(dayA, ix)
            color oc = ba ? color.lime : sc >= sigMin ? color.yellow : color.gray
            table.cell(tb, 0, row + 1, str.tostring(row + 1), text_size=size.tiny, text_color=row == 0 ? color.lime : color.gray)
            table.cell(tb, 1, row + 1, f_sym(ix), text_size=size.tiny, text_color=row == 0 ? color.white : color.silver)
            table.cell(tb, 2, row + 1, str.tostring(rnk, "#"), text_size=size.tiny, text_color=oc)
            table.cell(tb, 3, row + 1, str.tostring(sc, "#"), text_size=size.tiny)
            table.cell(tb, 4, row + 1, str.tostring(array.get(hitA, ix)) + "/6", text_size=size.tiny)
            table.cell(tb, 5, row + 1, str.tostring(array.get(rvA, ix), "#.##"), text_size=size.tiny)
            table.cell(tb, 6, row + 1, str.tostring(array.get(rsA, ix), "#.#") + "%", text_size=size.tiny)
            table.cell(tb, 7, row + 1, str.tostring(dp, "#.#") + "%", text_size=size.tiny)
            table.cell(tb, 8, row + 1, str.tostring(array.get(netA, ix)), text_size=size.tiny)
            table.cell(tb, 9, row + 1, ba ? "A" : bb ? "B" : "—", text_size=size.tiny, text_color=ba or bb ? color.lime : color.gray)
    table.cell(tb, 0, rows + 1, "★", text_color=color.lime, text_size=size.small)
    table.cell(tb, 1, rows + 1, leaderSym, text_color=color.white, text_size=size.small)
    table.cell(tb, 2, rows + 1, str.tostring(leaderRank, "#"), text_color=color.lime, text_size=size.small)
    table.cell(tb, 3, rows + 1, leaderA ? "A" : "—", text_size=size.tiny)
    table.cell(tb, 4, rows + 1, "A/B " + str.tostring(buyCnt), text_size=size.tiny)
    table.cell(tb, 0, rows + 2, "TOOLS 200", text_color=color.aqua, text_size=size.tiny)
    table.cell(tb, 1, rows + 2, page, text_color=color.yellow, text_size=size.tiny)

plot(leaderRank, "EGXTTB_LeaderRank", display=display.data_window)
plot(leaderA ? 1 : 0, "EGXTTB_LeaderBuyA", display=display.data_window)
plot(buyCnt, "EGXTTB_BuyCount", display=display.data_window)
plot(liveCnt, "EGXTTB_Live", display=display.data_window)
plot(1, "EGXTTB", display=display.data_window)

alertcondition(leaderA, "TOOLS 200 — A الأول", "{{ticker}} T200 leader A")
'''

OUT.write_text(HEADER + sym_block + F_TOOLS + TAIL, encoding="utf-8")
print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")
