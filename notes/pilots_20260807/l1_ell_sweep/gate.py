#!/usr/bin/env python3
"""E0: the PREREG P2 replication gate.  NOTHING downstream is reported
unless every line here says PASS.

Targets of record:
  LAYOUT-B n=16 ell=2 consec/geom5 = 43 / 33      (census result md:37-38)
  LAYOUT-B n=32 ell=2 consec/geom5 = 2879 / 2857  (census result md:39-40)
     + agreement histograms 17:2871,18:8 / 17:2850,18:7
     + core histograms 2:93,3:2786 / 1:3,2:98,3:2756
  LAYOUT-A n=24 consec ell=2,3,4   = 475 / 8135 / 20942  (round-21 REPORT.md:52)
  LAYOUT-A n=16 consec ell=2,3     = 36 / 0     (this session's d3 replay)
  BOX at every cell == the PREREG R1 closed form.
"""
import sys
import numpy as np

sys.path.insert(0, "notes/pilots_20260807/l1_ell_sweep")
from sweep_engine import build, run, consec, geom5, mindeg_word  # noqa: E402
from cf_cells import shells                                       # noqa: E402

P = 97
ok = True


def gate(n, ell, lay, want, hist_agr=None, hist_a=None, mode="consec"):
    global ok
    c = build(n, P, ell, lay)
    cv = consec(c.t, P) if mode == "consec" else geom5(c.t, P)
    res, _ = run(c, [cv])
    d = res[0]
    N = shells(n, ell)
    boxcf = sum(N.values())
    good = (d["RET"] == want) and (d["BOX"] == boxcf)
    if hist_agr is not None:
        good &= d["hist_agr"] == hist_agr
    if hist_a is not None:
        good &= d["hist_a"] == hist_a
    ok &= good
    print(f"  {'PASS' if good else '*** FAIL ***'}  n={n} ell={ell} "
          f"LAYOUT-{lay} {mode:6s} t={c.t} b={c.b} Lam={c.Lam}  "
          f"BOX={d['BOX']:,} (closed form {boxcf:,})  FILT={d['FILT']:,}  "
          f"RET={d['RET']:,} (want {want:,})  agr={d['hist_agr']} "
          f"a={d['hist_a']}")
    return d


print("=" * 96)
print("E0  REPLICATION GATE (PREREG P2)")
print("=" * 96)
gate(16, 2, "B", 43, {9: 43}, {2: 6, 3: 37})
gate(16, 2, "B", 33, {9: 33}, {1: 1, 2: 8, 3: 24}, mode="geom5")
gate(16, 2, "A", 36)
# SELF-CORRECTION (post-gate, adjudicated by brute.py, a third code path
# that solves the Vandermonde system directly): d3_ell_sweep.py prints 0
# here, which is WRONG.  At b=0 its m = a+nb-om is 0 on the whole r=1
# shell, and `R = set(drop[:m-1])` then becomes `drop[:-1]` -- Python's
# negative slice -- so it deletes all but the last core point instead of
# nothing.  The true value is 100 (engine and brute agree, including
# a={2:16,3:30,4:54}).  No banked number is affected: every cell quoted
# in the round-21 REPORT/addendum has b=1, where m>=1 and the slice is
# correct.
gate(16, 3, "A", 100, {9: 100}, {2: 16, 3: 30, 4: 54})
gate(24, 2, "A", 475)
gate(24, 3, "A", 8135)
gate(24, 4, "A", 20942)
gate(32, 2, "B", 2879, {17: 2871, 18: 8}, {2: 93, 3: 2786})
gate(32, 2, "B", 2857, {17: 2850, 18: 7}, {1: 3, 2: 98, 3: 2756}, mode="geom5")

print()
print("=" * 96)
print("E0b  mindeg cross-check: LAYOUT-B n=32 ell=2 must give a5's "
      "c_i = x_i^2 - x_bg^2 up to scale (a5_scale32.py:186-188)")
print("=" * 96)
c = build(32, P, 2, "B")
md, deg = mindeg_word(c)
xbg2 = int(c.xs[c.bgs[0]]) ** 2 % P
a5 = np.array([(int(c.xs[pr[0]]) ** 2 - xbg2) % P for pr in c.petals],
              dtype=np.int64)
ratios = {int(m) * pow(int(a), P - 2, P) % P
          for m, a in zip(md, a5) if a % P}
same = len(ratios) == 1 and all(a % P for a in a5)
ok &= same
print(f"  mindeg  = {md.tolist()}   deg U = {deg}  (k+1 = {c.k+1})")
print(f"  a5 word = {a5.tolist()}")
print(f"  {'PASS' if same else '*** FAIL ***'}  scale ratios {ratios}")

print()
print("GATE:", "ALL PASS" if ok else "*** FAILED -- report nothing downstream ***")
sys.exit(0 if ok else 1)
