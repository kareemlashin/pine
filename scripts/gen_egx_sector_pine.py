#!/usr/bin/env python3
"""Build docs/EGX_SECTOR_MAP.csv and patch f_secTag in BOARD200."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOARD = ROOT / "pine" / "EGX_افضل_فرص_BOARD200.pine"
CSV_PATH = ROOT / "docs" / "EGX_SECTOR_MAP.csv"
BEGIN = "// --- BEGIN AUTO f_secTag ---"
END = "// --- END AUTO f_secTag ---"

# Pine tag (Arabic) — must match f_secOk filters in BOARD200
TAG_BANK = "بنك"
TAG_REAL = "عقار"
TAG_TEL = "اتصالات"
TAG_IND = "صناع"
TAG_STEEL = "حديد"
TAG_FERT = "أسمدة"
TAG_FOOD = "غذاء"
TAG_TECH = "تكنول"
TAG_INV = "استثمار"
TAG_PHAR = "أدوية"
TAG_ENERGY = "طاقة"
TAG_SVC = "خدمات"
TAG_DEF = "—"

BANKS = {
    "COMI", "QNBE", "HDBK", "ADIB", "CIEB", "ABUK", "SAUD", "GBCO", "UBEE", "SAIB",
    "EXPA", "CCAP", "BINV", "ADIB", "NBKE", "SAUD", "EGBE",
}
REAL = {
    "TMGH", "PHDC", "MNHD", "OCDI", "HELI", "EXPA", "CIRA", "HELI", "ORHD", "PHDC",
    "TMGH", "MNHD", "OCDI", "EXPA", "CERA", "MNHD", "HELI", "PHDC", "TMGH",
    "MENA", "NARE", "ECAP", "DAPH", "MAAL", "GTWL", "ODIN", "URBQ",
}
TEL = {"ETEL", "ORHD", "ORWE", "RTVC", "EGTS", "GTHE"}
INDUSTRIAL = {
    "SWDY", "ORAS", "SCTS", "ALCN", "BTFH", "ARCC", "RAYA", "FERC", "SCEM", "IRON",
    "EGCH", "SKPC", "MOIL", "AMOC", "ELEC", "ENGC", "GSSC", "MCRO", "SPIN", "ALUM",
    "KZPC", "MFSC", "MPCI", "PRDC", "DOMT", "ACAP", "OFH", "UEFM", "GDWA", "CFGH",
    "LCSW", "ELKA", "GPIM", "ETRS", "CRST", "EDFM", "ALRA", "ASCM", "ATLC", "MPCO",
    "SMFR", "CEFM", "ICID", "DEIN", "RACC", "NDRL", "KRDI", "MOSC", "WKOL", "GTEX",
    "PRCL", "DTPP", "CAED", "MEGM", "COSG", "RUBX", "RAKT", "LUTS", "APSW", "EBSC",
    "TWSA", "PRMH", "BIOC", "CLHO", "TAQA", "EGSA", "HALN", "FAIT", "VLMR", "ARAB",
}
STEEL = {"EGAL", "IRON", "ALUM"}
FERT = {"MFPC", "UNIP", "ABUK"}  # ABUK is bank — fix ABUK only bank
FERT = {"MFPC", "UNIP", "SKPC"}
FOOD = {
    "JUFO", "EAST", "CANA", "EFID", "GPPL", "POUL", "SUGR", "GOUR", "AJWA", "DOMT",
    "MILS", "OLFI", "WCDF", "KABO", "KORA", "ISMQ", "ZMID", "AXPH", "MICH", "NINH",
}
TECH = {"FWRY", "VALU", "EFIH", "RMDA", "MTIE", "MCQE", "EGTS"}
INVEST = {"HRHO", "EMFD", "CNIN", "PHAR", "CCAP", "EMFD", "BINV", "ECAP", "AIHC", "AALR"}
PHARMA = {"PHAR", "AXPH", "ISPH", "MIPH", "NIPH", "OCPH", "BIOC", "CLHO", "RMDA", "AMIA", "IFAP"}
ENERGY = {"TAQA", "EGAS", "MPRC", "ESRS", "EGTS", "AMOC", "MOIL"}
SERVICES = {
    "RAYA", "FWRY", "VALU", "PHTV", "MHOT", "ATQA", "CICH", "NAPR", "CSAG", "CPCI",
    "OIH", "AMES", "BONY", "MOIN", "SPHT", "SDTI", "SVCE", "DSCW", "UNIT", "ACGC",
    "AFMC", "AMER", "ADCI", "ICFC", "ACTF", "ACAMD", "INFI", "ELSH", "ZEOT", "SNFC",
    "PHGC", "ISMA", "GGRN", "EALR", "EHDR", "ASPI", "IDRE", "NCCW", "GGCC", "SIPC",
    "POCO", "SCFM", "UEGC", "IEEC", "NHPS", "MEPA", "ICLE", "OBRI", "SEIG", "MBEG",
    "TANM", "AFDI", "AIDC", "ACAP", "CNFN", "MBSC", "TALM", "MASR", "EFIC", "ELEC",
}

# Remove mis-assignments
BANKS.discard("EXPA")
FERT.discard("ABUK")
REAL.discard("EXPA") if "EXPA" in REAL else None
REAL.add("EXPA")  # EXPA often real estate holding — keep عقار via REAL set without duplicate logic

EXPLICIT: dict[str, str] = {}


def classify(t: str) -> str:
    if t in EXPLICIT:
        return EXPLICIT[t]
    if t in BANKS:
        return TAG_BANK
    if t in TEL:
        return TAG_TEL
    if t in REAL:
        return TAG_REAL
    if t in STEEL:
        return TAG_STEEL
    if t in FERT:
        return TAG_FERT
    if t in FOOD:
        return TAG_FOOD
    if t in PHARMA:
        return TAG_PHAR
    if t in ENERGY:
        return TAG_ENERGY
    if t in TECH:
        return TAG_TECH
    if t in INVEST:
        return TAG_INV
    if t in INDUSTRIAL:
        return TAG_IND
    if t in SERVICES:
        return TAG_SVC
    return TAG_DEF


def load_symbols() -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for name in ("EGX_WATCHLIST_200.txt", "EGX_WATCHLIST_270.txt"):
        p = ROOT / "docs" / name
        if not p.exists():
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("###"):
                continue
            if line.startswith("EGX:") and line not in seen:
                seen.add(line)
                out.append(line)
    # Symbols only in BOARD200 batches
    if BOARD.exists():
        for m in re.finditer(r'"EGX:([A-Z0-9]+)"', BOARD.read_text(encoding="utf-8")):
            sym = f"EGX:{m.group(1)}"
            if sym not in seen:
                seen.add(sym)
                out.append(sym)
    return sorted(out, key=lambda s: s.split(":")[1])


def pine_switch(rows: list[tuple[str, str]]) -> str:
    lines = [
        "f_secTag(string symFull) =>",
        '    string t = str.replace(symFull, "EGX:", "")',
        "    switch t",
    ]
    for sym, tag in rows:
        t = sym.replace("EGX:", "")
        lines.append(f'        "{t}" => "{tag}"')
    lines.append('        => "—"')
    return "\n".join(lines)


def write_csv(rows: list[tuple[str, str]]) -> None:
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["symbol", "sector_tag"])
        w.writerows(rows)


def patch_board(body: str) -> None:
    text = BOARD.read_text(encoding="utf-8")
    if BEGIN not in text or END not in text:
        # inject: replace old f_secTag ... f_secOk predecessor
        pat = re.compile(
            r"f_secTag\(string symFull\) =>.*?^\s*=> \"—\"\n",
            re.MULTILINE | re.DOTALL,
        )
        if not pat.search(text):
            print("FAIL: cannot find f_secTag in BOARD200", file=sys.stderr)
            sys.exit(1)
        new_block = BEGIN + "\n" + body + "\n" + END + "\n\n"
        text = pat.sub(new_block, text, count=1)
    else:
        pre, rest = text.split(BEGIN, 1)
        _, post = rest.split(END, 1)
        text = pre + BEGIN + "\n" + body + "\n" + END + post
    BOARD.write_text(text, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="Exit 1 if BOARD200 sector block stale")
    ap.add_argument("--no-patch", action="store_true", help="Only write CSV")
    args = ap.parse_args()

    syms = load_symbols()
    rows = [(s, classify(s.split(":")[1])) for s in syms]
    write_csv([(s.split(":")[1], tag) for s, tag in rows])
    body = pine_switch([(s.split(":")[1], tag) for s, tag in rows])

    if args.check:
        text = BOARD.read_text(encoding="utf-8")
        if BEGIN not in text or body.strip() not in text:
            print("FAIL: BOARD200 f_secTag out of date — run gen_egx_sector_pine.py")
            return 1
        print(f"OK sector map: {len(rows)} symbols")
        return 0

    if not args.no_patch:
        patch_board(body)
        print(f"Patched {BOARD.name} with {len(rows)} sector cases")
    print(f"Wrote {CSV_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
