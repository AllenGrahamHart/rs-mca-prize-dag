# Coordinator note (2026-08-07, round 22): d3_ell_sweep.py is UNSAFE outside b = 1 cells

Round-22 l1_ell_sweep found two failure modes in this dir's
d3_ell_sweep.py (lines 84-86, the drop[:m-1] filter):
- b >= 2: the filter tests vanishing on a k-point set (stronger
  than membership) — UNDER-counts.
- b = 0: the r = 1 shell has m = 0 and drop[:-1] deletes all but
  the last core point — its printed "n=16 ell=3 -> retained 0" is
  WRONG (true value 100, confirmed by two independent code paths).
NO banked number is affected: every round-21 number of record
(n=24 ell=2,3,4: 475/8,135/20,942; the n=16/32/64 gate cells) is a
b = 1 cell, and the n=16 ell=3 zero was never quoted in REPORT.md
or the node addendum. Do not re-run d3_ell_sweep.py at any b = 0
or b >= 2 cell; use round-22's sweep_engine.py (exact
necessary-and-sufficient existence test, validated three-path).
Source: notes/pilots_20260807/l1_ell_sweep/ (report section 2).
