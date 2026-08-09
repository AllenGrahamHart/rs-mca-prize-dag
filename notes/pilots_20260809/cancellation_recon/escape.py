#!/usr/bin/env python3
"""cancellation_recon ESCAPE TESTS (round 27) -- run from repo root via
   tools/ramguard tiny -- python3 notes/pilots_20260809/cancellation_recon/escape.py

E1: replay THEOREM Z-FLOOR at two banked cells (scratch copy of zcore).
E2: reproduce one banked band-analogue exact count (F7-A2 crossing-fidelity
    ladder, cell (16,8,1,cyclic_step_1,linear), q=97: challengers=109).
Stdlib only, exact integer/Fraction arithmetic.
"""
import re
import sys
import types
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

print("=" * 70)
print("E1  Z-FLOOR replay (scratch copy of z_ceiling_assault/zcore.py)")
print("=" * 70)

import scratch_zcore as Z  # noqa: E402

# banked rows, verbatim from notes/pilots_20260808/z_ceiling_assault/SWEEP.tsv
BANKED = [
    ("M4", 16, 1, 97, Fraction(675629394531, 10 ** 9), "675.629394531"),
    ("M2", 16, 2, 97, None, "9.38720703125"),
    ("M2", 16, 2, 193, None, "2.591796875"),
]

ok1 = True
for fam, N, kappa, p, _f, banked_str in BANKED:
    if fam == "M4":
        rows = Z.rows_M4(N, p)
    else:
        rows = Z.rows_M2(N, kappa, p)
    d = Z.cell(rows, p)
    tm = d["TMASS"]
    # exact banked comparison: banked printed value is exact in binary
    # (TMASS is a dyadic rational with denominator 2^N)
    banked = Fraction(banked_str)
    match = (tm == banked)
    zfr = Fraction(tm) * p ** kappa / (1 << N)
    floor_ok = zfr >= 1
    tight2 = zfr <= 2
    ok1 &= match and floor_ok
    print(f"{fam} N={N} kappa={kappa} p={p}")
    print(f"   TMASS       = {float(tm):.12f}   banked {banked_str}"
          f"   EXACT MATCH: {match}")
    print(f"   ZFRATIO     = {float(zfr):.12f}  (Z*p^kappa/2^N)")
    print(f"   Z-FLOOR ok  = {floor_ok}   within-2x = {tight2}")
print(f"E1 VERDICT: all banked TMASS replayed exactly and Z-FLOOR holds: {ok1}")

print()
print("=" * 70)
print("E2  banked band-analogue exact count (F7-A2, q=97)")
print("=" * 70)

CORE = (HERE / "scratch_e22_core.py").read_text()
CENS = (HERE / "scratch_e22_census.py").read_text()
CENS = re.sub(r"^import modal\s*$", "", CENS, flags=re.M)
CENS = re.sub(r"^app = modal\.App.*$", "", CENS, flags=re.M)
CENS = re.sub(r"^image = .*$", "", CENS, flags=re.M)
CENS = re.sub(r"^@app\.\w+\(.*\)\s*$", "", CENS, flags=re.M)


def cell_at(q, spec):
    ns = {"__name__": "e22_core", "__file__": "/tmp/x/e22_core.py"}
    exec(CORE, ns)
    ns["P"] = q
    mod = types.ModuleType("e22_core")
    mod.__dict__.update(ns)
    sys.modules["e22_core"] = mod
    ns2 = {"__name__": "e22_census", "__file__": "/tmp/x/e22_census.py"}
    exec(CENS, ns2)
    ns2["P"] = q
    n, k, sigma, layout, scalar = spec
    return ns2["exact_cell"](n, k, sigma, layout, scalar)


SPEC = (16, 8, 1, "cyclic_step_1", "linear")
BANKED_E2 = {97: (109, 4, 0), 113: (95, 4, 0), 193: (56, 4, 0)}
ok2 = True
for q, (ch_b, pl_b, unc_b) in BANKED_E2.items():
    cell = cell_at(q, SPEC)
    cc = cell.get("class_counts", {})
    ch = sum(cc.get(c, 0) for c in ("full_petal", "mixed_petal"))
    pl = cc.get("planted", 0)
    unc = cell.get("unclassified", 0)
    good = (ch, pl, unc) == (ch_b, pl_b, unc_b)
    ok2 &= good
    print(f"q={q:>5}  challengers={ch:>4} (banked {ch_b})  planted={pl} "
          f"(banked {pl_b})  unclassified={unc} (banked {unc_b})  "
          f"list_size={cell['list_size']}  MATCH={good}")
print(f"E2 VERDICT: banked band-analogue counts reproduced exactly: {ok2}")
print()
print(f"ESCAPE TESTS PASS: {ok1 and ok2}")
