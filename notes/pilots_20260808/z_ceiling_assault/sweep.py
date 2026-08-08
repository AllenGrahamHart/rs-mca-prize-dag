#!/usr/bin/env python3
"""D1/D2 -- the exhaustive 2-POWER-grid census.  tools/ramguard local -- python3 ...

Emits notes/pilots_20260808/z_ceiling_assault/SWEEP.tsv with one line per cell:
  fam  N  kappa  p  SIGMA  TMASS(float)  CRATIO  EXCESS  H
Every cell asserts CATCH-Z6 (2N a 2-power) and CATCH-19B (0 not in Lambda).
"""
import math, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zcore import *   # noqa

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SWEEP.tsv")
STAGE = sys.argv[1] if len(sys.argv) > 1 else "all"

# (fam, N, kappa, PMAX)  -- PMAX chosen so cost ~ 2*h*min(3^h,p)*3 stays bounded
PLAN_M4 = [(4, 1 << 20), (8, 1 << 20), (16, 1 << 16), (32, 20000), (64, 20000), (128, 6000)]
PLAN_M2 = [(8, 1, 1 << 18), (8, 2, 1 << 16), (8, 3, 20000), (8, 4, 20000),
           (16, 1, 1 << 16), (16, 2, 20000), (16, 3, 20000), (16, 4, 20000),
           (32, 1, 20000), (32, 2, 700)]

PMAXALL = max([q for _, q in PLAN_M4] + [q for _, _, q in PLAN_M2])
t0 = time.time()
PR = primes_upto(PMAXALL)
sys.stderr.write("sieve %d primes in %.1fs\n" % (len(PR), time.time() - t0))

rows_out = []
best = {}


def do(fam, N, k, p):
    rows = rows_M4(N, p) if fam == "M4" else rows_M2(N, k, p)
    d = cell(rows, p)
    key = (fam, N, k)
    if key not in best or d["CRATIO"] > best[key]["CRATIO"]:
        best[key] = d
    rows_out.append("%s\t%d\t%d\t%d\t%.6f\t%.12g\t%.12g\t%.12g\t%.12g" %
                    (fam, N, k, p, d["SIGMA"], d["TMASSf"], d["CRATIO"], d["EXCESS"], d["H"]))
    assert d["ZFRATIO"] >= 1.0 - 1e-12, ("E1 Z-FLOOR VIOLATION", fam, N, k, p, d["ZFRATIO"])
    return d


print("=" * 104)
print("SWEEP-1 -- family M4 (kappa = 1, Lambda = {1}), 2-POWER grid, ALL p == 1 mod 2L below PMAX")
print("=" * 104)
print("%4s %9s %7s | %9s %9s | %-28s %9s" %
      ("N", "PMAX", "#cells", "maxCRATIO", "at p", "SIGMA at argmax", "minCRATIO"))
for (L, pmax) in PLAN_M4:
    assert_2power_grid(L)
    t = time.time()
    n = 0
    lo = 9e9
    for p in PR:
        if p >= pmax:
            break
        if p <= 2 * L or (p - 1) % (2 * L):
            continue
        d = do("M4", L, 1, p)
        lo = min(lo, d["CRATIO"])
        n += 1
    b = best[("M4", L, 1)]
    print("%4d %9d %7d | %9.6f %9d | SIGMA=%8.3f  H=%10.4g       %9.6f   [%.1fs]" %
          (L, pmax, n, b["CRATIO"], b["p"], b["SIGMA"], b["H"], lo, time.time() - t))

print()
print("=" * 104)
print("SWEEP-2 -- family M2 (negacyclic GRS of record, Lambda = {1,3,..,2R-1}), 2-POWER grid")
print("=" * 104)
print("%4s %4s %9s %7s | %9s %9s | %-28s %9s" %
      ("S", "R", "PMAX", "#cells", "maxCRATIO", "at p", "SIGMA at argmax", "minCRATIO"))
for (S, R, pmax) in PLAN_M2:
    assert_2power_grid(S)
    t = time.time()
    n = 0
    lo = 9e9
    for p in PR:
        if p >= pmax:
            break
        if p <= 2 * S or (p - 1) % (2 * S):
            continue
        if min(3 ** (S // 2), p ** R) > 4_000_000:
            continue
        d = do("M2", S, R, p)
        lo = min(lo, d["CRATIO"])
        n += 1
    if n == 0:
        print("%4d %4d %9d %7d | (no feasible cell)" % (S, R, pmax, n))
        continue
    b = best[("M2", S, R)]
    print("%4d %4d %9d %7d | %9.6f %9d | SIGMA=%8.3f  H=%10.4g       %9.6f   [%.1fs]" %
          (S, R, pmax, n, b["CRATIO"], b["p"], b["SIGMA"], b["H"], lo, time.time() - t))

with open(OUT, "w") as f:
    f.write("fam\tN\tkappa\tp\tSIGMA\tTMASS\tCRATIO\tEXCESS\tH\n")
    f.write("\n".join(rows_out) + "\n")

print()
print("=" * 104)
gm = max(best.values(), key=lambda d: d["CRATIO"])
gk = [k for k, v in best.items() if v is gm][0]
print("TOTAL CELLS SWEPT: %d      GLOBAL max CRATIO = %.6f  at  %s N=%d kappa=%d p=%d (SIGMA=%.3f)" %
      (len(rows_out), gm["CRATIO"], gk[0], gk[1], gk[2], gm["p"], gm["SIGMA"]))
print("REGISTERED FALSIFIER (CRATIO > 2): %s" % ("TRIPPED" if gm["CRATIO"] > 2 else "NOT tripped"))
print("Round-23 banked record C <= 1.2610 :  %s" %
      ("EXCEEDED (%.6f)" % gm["CRATIO"] if gm["CRATIO"] > 1.2610 else "not exceeded"))
print("=" * 104)
