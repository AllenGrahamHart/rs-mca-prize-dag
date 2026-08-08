#!/usr/bin/env python3
"""D1(b) + D1(c) probes.  tools/ramguard local -- python3 ...
  PROBE-1  composite boundary walk (CATCH-Z6: DECLARED probes, NOT admissible
           cells; they cannot falsify Z-CEILING, they locate the gate)
  PROBE-2  the general-F_p-subspace scope probe (P2c)
  PROBE-3  Lambda relaxation inside the negacyclic family (P2b, boundary probe)
  PROBE-4  exhaustive p-free count at n = 30 vs the banked CZ-M count formula
"""
import itertools, math, os, sys, time
from fractions import Fraction
from math import comb
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zcore import *   # noqa


def next_prime_cong(lo, m):
    q = lo + ((1 - lo) % m)
    while True:
        if is_prime(q):
            return q
        q += m


print("=" * 104)
print("PROBE-1 -- COMPOSITE boundary walk (DECLARED CATCH-Z6 probes; NOT admissible cells).")
print("           registered: CRATIO -> PFMASS(n) as p -> inf; PFMASS(2^a*3) = (5/4)^{L/3}")
print("=" * 104)
print("%5s %4s %12s %9s %11s %10s %11s %11s" %
      ("n=2L", "L", "p", "SIGMA", "TMASS", "CRATIO", "PFMASS", "(PFMASS+H)/(1+H)"))
for (n, plo) in [(12, 1 << 6), (12, 1 << 10), (12, 1 << 14), (12, 1 << 18), (12, 1 << 22),
                 (24, 1 << 14), (24, 1 << 18), (24, 1 << 20), (24, 1 << 22),
                 (18, 1 << 18), (36, 1 << 22), (20, 1 << 18), (30, 1 << 18)]:
    L = n // 2
    p = next_prime_cong(plo, n)
    pf, cnt, sh = pfree_mass(n)
    t = time.time()
    d = cell(rows_M4(L, p), p)
    H = Fraction((1 << L) - 1, p)
    pred = float((pf + H) / (1 + H))
    print("%5d %4d %12d %9.3f %11.6f %10.6f %11.6f %11.6f   [%.1fs]" %
          (n, L, p, d["SIGMA"], d["TMASSf"], d["CRATIO"], float(pf), pred, time.time() - t))
    check("PROBE-1 TMASS >= PFMASS(n) at (n=%d, p=%d)" % (n, p), d["TMASS"] >= pf,
          "TMASS %.6f >= PFMASS %.6f" % (d["TMASSf"], float(pf)))
    if H < Fraction(1, 100):
        check("PROBE-1 CRATIO == (PFMASS+H)/(1+H) to 1%% at (n=%d, p=%d)" % (n, p),
              abs(d["CRATIO"] - pred) < 0.01 * pred, "measured %.6f predicted %.6f" % (d["CRATIO"], pred))

print()
print("P3c HEADLINE (boundary probe): least composite n whose p-free mass alone breaks CRATIO > 2")
for n in [12, 24, 48]:
    pf, cnt, sh = pfree_mass(n)
    print("   n=%3d  L=%3d  RELDIM=%2d  |PFREE|=%6d  PFMASS=%.6f = (5/4)^%d   sup_p CRATIO = PFMASS %s 2"
          % (n, n // 2, sh, cnt, float(pf), (n // 2) // 3, ">" if pf > 2 else "<="))
p24 = next_prime_cong(1 << 22, 24)
d24 = cell(rows_M4(12, p24), p24, want_AU=True)
check("P3c composite n=24 exhibits CRATIO > 2 at p=%d" % p24, d24["CRATIO"] > 2.0,
      "CRATIO = %.6f (TMASS = %s, PFMASS = 625/256 = 2.44140625)" % (d24["CRATIO"], d24["TMASS"]))
print("   n=24 exhibit: p=%d  TMASS=%s=%.8f  CRATIO=%.8f  UMIN=%d  A[3]=%d"
      % (p24, d24["TMASS"], d24["TMASSf"], d24["CRATIO"], d24["UMIN"], d24["AU"][3]))

print()
print("=" * 104)
print("PROBE-2 -- SCOPE PROBE (P2c): a GENERAL F_p-subspace, L = span{(1,1,...,1)}")
print("           2-power N, admissible p -- but NOT an admissible parity row.")
print("=" * 104)
print("%4s %8s | %14s %14s %10s %10s" % ("N", "p", "TMASS(exact)", "closed form", "HEUR", "CRATIO"))
for (N, p) in [(4, 17), (8, 257), (16, 65537), (16, 257), (16, 97), (32, 193)]:
    tm = tmass_exact([[1] * N], p)
    cf = sum(Fraction(comb(N, U) * comb(U, U // 2), 1 << U) for U in range(0, N + 1, 2))
    H = Fraction((1 << N) - 1, p)
    cr = float(tm / (1 + H))
    print("%4d %8d | %14.6f %14.6f %10.6f %10.4f" % (N, p, float(tm), float(cf), float(1 + H), cr))
    check("PROBE-2 all-ones TMASS = sum_U C(N,U)C(U,U/2)2^-U (p-INDEPENDENT) at N=%d p=%d" % (N, p),
          tm == cf, "%s" % tm)
tm8 = tmass_exact([[1] * 8], 257)
cr8 = float(tm8 / (1 + Fraction(255, 257)))
check("P2c registered CRATIO = 25.23 +- 0.05 at N=8, p=257", abs(cr8 - 25.23) < 0.05,
      "REGISTERED 25.23 ; measured %.4f (TMASS = %s)" % (cr8, tm8))
print("   => on GENERAL F_p-subspaces CRATIO is unbounded (grows like p at fixed N):")
for p in (97, 257, 65537, 16777259):
    tm = tmass_exact([[1] * 8], p) if p < 1 << 20 else Fraction(0)
    if tm == 0:
        tm = sum(Fraction(comb(8, U) * comb(U, U // 2), 1 << U) for U in range(0, 9, 2))
    print("      N=8  p=%9d  CRATIO = %.4f" % (p, float(tm / (1 + Fraction(255, p)))))

print()
print("=" * 104)
print("PROBE-3 -- LAMBDA RELAXATION (P2b, boundary probe): all all-odd Lambda of size R")
print("           (CATCH-19B still honoured: 0 not in Lambda).  Consecutive = the cell of record.")
print("=" * 104)
print("%4s %3s %7s | %11s %11s %11s | %s" %
      ("S", "R", "p", "consecutive", "max over Lam", "min over Lam", "argmax Lambda"))
for (S, R, p) in [(16, 2, 257), (16, 2, 193), (16, 2, 353), (16, 2, 97),
                  (8, 2, 97), (8, 2, 241), (8, 3, 241), (16, 3, 353)]:
    w = elt_of_order(p, 2 * S)
    odds = [l for l in range(1, 2 * S, 2)]
    bestv = -1
    worstv = 9e9
    bestl = None
    for lam in itertools.combinations(odds, R):
        rws = [[pow(w, l * e, p) for e in range(S)] for l in lam]
        tm = tmass_exact(rws, p)
        H = Fraction((1 << S) - 1, p ** R)
        cr = float(tm / (1 + H))
        if cr > bestv:
            bestv = cr
            bestl = lam
        worstv = min(worstv, cr)
    con = cell(rows_M2(S, R, p), p)["CRATIO"]
    print("%4d %3d %7d | %11.6f %11.6f %11.6f | %s" % (S, R, p, con, bestv, worstv, list(bestl)))
    check("PROBE-3 max CRATIO over all all-odd Lambda < 2 at (S=%d,R=%d,p=%d)" % (S, R, p),
          bestv < 2.0, "max %.6f (consecutive %.6f)" % (bestv, con))

print()
print("=" * 104)
print("PROBE-4 -- exhaustive p-free ternary count at n = 30 vs banked CZ-M count 3^{n/2-phi(n)}-1")
print("=" * 104)
n = 30
h = n // 2
ph = cyclotomic(n)
d = len(ph) - 1


def reduce_mod(v):
    a = list(v) + [0] * 0
    for t in range(len(a) - 1, d - 1, -1):
        c = a[t]
        if c:
            for s in range(d + 1):
                a[t - d + s] -= c * ph[s]
    return tuple(a[:d])


A = {}
for f in itertools.product((0, 1, -1), repeat=7):
    r = reduce_mod(list(f) + [0] * (h - 7))
    A.setdefault(r, []).append(sum(1 for x in f if x))
tot = 0
mass = Fraction(0)
for f in itertools.product((0, 1, -1), repeat=h - 7):
    r = reduce_mod([0] * 7 + list(f))
    key = tuple(-x for x in r)
    if key in A:
        wb = sum(1 for x in f if x)
        for wa in A[key]:
            tot += 1
            mass += Fraction(1, 1 << (wa + wb))
lat, latc, sh = pfree_mass(n)
print("   n=30: EXHAUSTIVE over all 3^15 ternary vectors ->  |PFREE| = %d,  PFMASS = %s = %.6f"
      % (tot, mass, float(mass)))
print("         lattice-{0,+-1}-combination search           ->  %d,  %s" % (latc, lat))
print("         banked CZ-M count formula 3^{n/2-phi(n)}     ->  %d" % 3 ** sh)
check("PROBE-4 exhaustive == lattice search at n=30", tot == latc and mass == lat)
check("PROBE-4 banked CZ-M count 3^{n/2-phi(n)}-1 reproduces at n=30",
      tot - 1 == 3 ** sh - 1, "exhaustive %d nonzero vs CZ-M %d" % (tot - 1, 3 ** sh - 1))

sys.exit(summary())
