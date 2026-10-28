#!/usr/bin/env python3
"""Generate EGX_TOOLS_BOARD200.pine — mirrors EGX_افضل_فرص_BOARD200 engine with f_tools()."""

from pathlib import Path

from tools_lite_f_tools import F_TOOLS_BOARD_FULL

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "pine" / "EGX_افضل_فرص_BOARD200.pine"
OUT = ROOT / "pine" / "EGX_TOOLS_BOARD200.pine"

HEADER = """//@version=6
indicator("EGX TOOLS — لوحة 200/294", shorttitle="T294", overlay=false, max_tables_count=4, calc_bars_count=5000)

// 8★ + 32 دوّar · مرآة EGX_افضل_فرص_BOARD200 · Screener: EGX_TOOLS_OPP
// plots: EGXTTB200_* · regen: ./scripts/sync_all_boards.sh

"""


def toolsify(text: str) -> str:
    reps = [
        ("EGXOppB200", "EGXTTB200"),
        ("leaderOpp", "leaderScore"),
        ("minProOpp", "minProRank"),
        ("minOppShow", "minRankShow"),
        ("effMinOppScr", "effMinToolScr"),
        ('sortMode == "فرصة"', 'sortMode == "Rank"'),
        ('options=["فرصة", "RS20", "RVOL", "R/R"]', 'options=["Rank", "RS20", "RVOL", "R/R"]'),
        ('input.string("فرصة", "ترتيب الرئيسي"', 'input.string("Rank", "ترتيب الرئيسي"'),
        ('"فرص " + str.tostring(TOTAL)', '"TOOLS " + str.tostring(TOTAL)'),
        ("فرص —", "TOOLS —"),
        ("{{ticker}} فرص", "{{ticker}} TOOLS"),
        ('table.cell(tb, 2, 0, "فرصة"', 'table.cell(tb, 2, 0, "Rank"'),
        ('table.cell(tb, 4, 0, "إعداد"', 'table.cell(tb, 4, 0, "Hits"'),
        ('str.tostring(array.get(stC, ix)) + "/11"', 'str.tostring(array.get(stC, ix)) + "/7"'),
        ('table.cell(tbP, 2, 0, "فرصة"', 'table.cell(tbP, 2, 0, "Rank"'),
        ('table.cell(tbB, 2, 0, "فرصة"', 'table.cell(tbB, 2, 0, "Rank"'),
        ("Screener=فوري", "lite13 · MASTER=100"),
        ('"حد فرصة"', '"حد Rank"'),
        ("إخفاء تحت حد الفرصة", "إخفاء تحت حد Rank"),
        ("Pro فقط (Pass+Pro)", "Pro فقط (Pass+Pro Tools)"),
        ("playbook في docs/EGX_افضل_فرص.md", "docs/EGX_TOOLS.md"),
    ]
    for a, b in reps:
        text = text.replace(a, b)
    for i in range(2, 11):
        text = text.replace(f"top{i}Opp", f"top{i}Rank")
    return text


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    input_start = text.index("int MAX")
    input_end = text.index("string Gpin")
    inputs = toolsify(text[input_start:input_end])
    if "float sigMin" not in inputs:
        inputs = inputs.replace(
            'float minVol = input.float(800.0, "حد حجم", group=G)\n',
            'float minVol = input.float(800.0, "حد حجم", group=G)\n'
            'float sigMin = input.float(20.0, "Tools Score %", minval=10, maxval=50, group=G)\n',
            1,
        )
    inputs = inputs.replace(
        "float effMinOppScr = profile == \"استثمار يومي\" ? 62.0 : minProOpp",
        "float effMinToolScr = profile == \"استثمار يومي\" ? 62.0 : minProRank",
    )

    pin_start = text.index("string Gpin")
    pin_end = text.index("f_b0(int i)")
    pin_block = text[pin_start:pin_end]

    sym_start = pin_end
    sym_end = text.index("f_opp()")
    sym_block = text[sym_start:sym_end]

    eng_start = text.index("float benchRoc = chartIs30")
    engine = toolsify(text[eng_start:])
    engine = engine.replace("f_opp()", "f_tools()")

    f_tools_block = toolsify(F_TOOLS_BOARD_FULL).replace("effMinOppScr", "effMinToolScr")

    OUT.write_text(
        HEADER + inputs + pin_block + sym_block + f_tools_block + engine,
        encoding="utf-8",
    )
    nlines = OUT.read_text(encoding="utf-8").count("\n") + 1
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes, ~{nlines} lines)")


if __name__ == "__main__":
    main()
