#!/usr/bin/env python3
"""Generate EGX_OPP_x_TOOLS_BOARD200.pine — full 294 scan: فرص + Tools lite13 + Mega."""

from pathlib import Path

from tools_lite_f_tools import F_TOOLS_BOARD_FULL

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "pine" / "EGX_افضل_فرص_BOARD200.pine"
OUT = ROOT / "pine" / "EGX_OPP_x_TOOLS_BOARD200.pine"

HEADER = """//@version=6
indicator("EGX Opp × Tools — لوحة 200/294", shorttitle="O×T294", overlay=false, max_tables_count=4, calc_bars_count=5000)

// فرص (f_opp) + Tools (f_tools) · Mega = Opp Pro ∧ Tools Pro · regen: scripts/gen_egx_opp_x_tools_board200.py
// plots: EGXOxTB200_* · Filter: EGXOxTB200_MegaCount · EGXOxTB200_LeaderMega=1

"""

PATCH_ARRAYS = """
var float[] toolRankC = array.new_float(MAX, na)
var bool[] toolProC = array.new_bool(MAX, false)
var bool[] megaC = array.new_bool(MAX, false)
"""

PATCH_FETCH = """
f_fetchTools(string s) =>
    request.security(s, "D", f_tools(), barmerge.gaps_off, barmerge.lookahead_off)

f_cacheTools(int gi, float tRank, float tPr) =>
    if gi >= 0 and gi < TOTAL
        bool tPro = tPr > 0 and regimeOk
        array.set(toolRankC, gi, tRank)
        array.set(toolProC, gi, tPro)
        array.set(megaC, gi, array.get(proC, gi) and tPro)
"""

PATCH_LOOP_PIN = """        if p < pinUse
            int gip = f_gi(f_pin(p))
            f_cache(gip, opp, rank, tech, buR, paR, prR, st, rv, roc20, ac, ds, rrv, dp, act, cyc, ch, lim)
            [_, trk, _, _, _, tpr, _, _, _, _, _, _, _, _, _, _, _] = f_fetchTools(ps)
            f_cacheTools(gip, trk, tpr)"""

PATCH_LOOP_ROT = """        if gi < TOTAL
            f_cache(gi, opp, rank, tech, buR, paR, prR, st, rv, roc20, ac, ds, rrv, dp, act, cyc, ch, lim)
            [_, trk2, _, _, _, tpr2, _, _, _, _, _, _, _, _, _, _, _] = f_fetchTools(sym)
            f_cacheTools(gi, trk2, tpr2)"""

INPUT_MEGA = 'bool onlyMega = input.bool(false, "Mega فقط (Opp Pro + Tools Pro)", group=G)\n'

SORT_PATCH_OLD = 'sortMode == "Rank" ? array.get(rkC, ix) : sortMode == "RS20"'
SORT_PATCH_NEW = (
    'sortMode == "Mega" ? (array.get(megaC, ix) ? array.get(oppC, ix) : -1.0) : '
    'sortMode == "Rank" ? array.get(rkC, ix) : sortMode == "RS20"'
)

VIS_FILTER = """    if onlyMega and not array.get(megaC, ix)
        continue
"""

MEGA_CNT_BLOCK = """
int megaCnt = 0
for i = 0 to TOTAL - 1
    if array.get(okC, i) and array.get(megaC, i)
        megaCnt += 1
bool leaderMega = nVis > 0 and array.get(megaC, leader)
"""

PLOTS = """
plot(megaCnt, "EGXOxTB200_MegaCount", display=display.data_window)
plot(leaderMega ? 1 : 0, "EGXOxTB200_LeaderMega", display=display.data_window)
plot(nVis > 0 ? array.get(toolRankC, leader) : na, "EGXOxTB200_LeaderToolRank", display=display.data_window)
plot(1, "EGXOxTB200", display=display.data_window)

alertcondition(leaderMega and readyAlert, "O×T — Leader Mega", "{{ticker}} EGXOxTB200 leader mega")
alertcondition(megaCnt >= 2 and readyAlert, "O×T — 2+ Mega", "{{ticker}} EGXOxTB200 multi mega")
"""

SORT_OPTIONS = 'options=["فرصة", "Rank", "RS20", "RVOL", "R/R", "Mega"]'
SORT_OPTIONS_NEW = 'options=["فرص", "Rank", "RS20", "RVOL", "R/R", "Mega"]'


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    opp_start = text.index("f_opp()")
    bench = text.index("float benchRoc = chartIs30")
    prefix = text[:opp_start]
    opp_fn = text[opp_start:bench]
    suffix = text[bench:]

    # strip original indicator header (keep from int MAX)
    prefix = prefix[prefix.index("int MAX") :]
    if "float sigMin" not in prefix:
        prefix = prefix.replace(
            'float minVol = input.float(800.0, "حد حجم", group=G)\n',
            'float minVol = input.float(800.0, "حد حجم", group=G)\n'
            'float sigMin = input.float(20.0, "Tools Score %", minval=10, maxval=50, group=G)\n',
            1,
        )
    if "onlyMega" not in prefix:
        prefix = prefix.replace("bool onlyHotPro", INPUT_MEGA + "bool onlyHotPro", 1)

    f_tools = F_TOOLS_BOARD_FULL.replace("effMinOppScr", "effMinOppScr")

    suffix = suffix.replace("var bool[] hotProC = array.new_bool(MAX, false)", "var bool[] hotProC = array.new_bool(MAX, false)" + PATCH_ARRAYS, 1)
    suffix = suffix.replace(
        "f_fetch(string s) =>\n    request.security(s, \"D\", f_opp(), barmerge.gaps_off, barmerge.lookahead_off)",
        "f_fetch(string s) =>\n    request.security(s, \"D\", f_opp(), barmerge.gaps_off, barmerge.lookahead_off)" + PATCH_FETCH,
        1,
    )

    suffix = suffix.replace(
        "        if p < pinUse\n            f_cache(f_gi(f_pin(p)), opp, rank, tech, buR, paR, prR, st, rv, roc20, ac, ds, rrv, dp, act, cyc, ch, lim)",
        PATCH_LOOP_PIN,
        1,
    )
    suffix = suffix.replace(
        "        if gi < TOTAL\n            f_cache(gi, opp, rank, tech, buR, paR, prR, st, rv, roc20, ac, ds, rrv, dp, act, cyc, ch, lim)",
        PATCH_LOOP_ROT,
        1,
    )

    if SORT_PATCH_OLD in suffix:
        suffix = suffix.replace(SORT_PATCH_OLD, SORT_PATCH_NEW, 1)
    elif 'sortMode == "RS20"' in suffix and "Mega" not in suffix.split("f_sortVal")[1][:200]:
        suffix = suffix.replace(
            'sortMode == "RS20" ? array.get(rsC, ix)',
            'sortMode == "Mega" ? (array.get(megaC, ix) ? array.get(oppC, ix) : -1.0) : sortMode == "RS20" ? array.get(rsC, ix)',
            1,
        )

    suffix = suffix.replace(SORT_OPTIONS, SORT_OPTIONS_NEW, 1)
    suffix = suffix.replace('options=["فرصة", "Rank"', 'options=["فرص", "Rank", "Mega"', 1)

    anchor = "int hotProCnt = 0"
    if anchor in suffix and "int megaCnt" not in suffix:
        suffix = suffix.replace(anchor, MEGA_CNT_BLOCK.strip() + "\n\n" + anchor, 1)

    vis_anchor = "    if onlyPro and not array.get(proC, ix)"
    if vis_anchor in suffix:
        suffix = suffix.replace(vis_anchor, vis_anchor + "\n" + VIS_FILTER.strip(), 1)

    suffix = suffix.replace("EGXOppB200", "EGXOxTB200")
    suffix = suffix.replace("{{ticker}} فرص", "{{ticker}} O×T")
    suffix = suffix.replace("فرص —", "O×T —")

    if "EGXOxTB200_MegaCount" not in suffix:
        suffix = suffix.rstrip() + "\n" + PLOTS

    OUT.write_text(HEADER + prefix + opp_fn + f_tools + suffix, encoding="utf-8")
    n = OUT.read_text(encoding="utf-8").count("\n") + 1
    print(f"Wrote {OUT} (~{n} lines)")


if __name__ == "__main__":
    main()
