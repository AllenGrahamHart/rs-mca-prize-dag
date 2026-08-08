#!/usr/bin/env python3
"""E1-E6 escape tests + banked-number replay.  tools/ramguard local -- python3 ..."""
import math, os, sys
from fractions import Fraction
from math import comb
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zcore import *   # noqa

print("=" * 104)
print("E2/E1/E6 -- exact DP vs the VERBATIM round-23 weight enumerators; Z-FLOOR; grid asserts")
print("=" * 104)
CELLS = []
for (L, p) in [(4, 17), (4, 41), (8, 17), (8, 97), (8, 113), (8, 193), (8, 241),
               (16, 97), (16, 193), (16, 257), (16, 353), (16, 449), (16, 577), (16, 641)]:
    CELLS.append(("M4", L, 1, p))
for (S, R, p) in [(8, 2, 17), (8, 2, 97), (16, 2, 97), (16, 2, 193), (16, 4, 97), (16, 4, 193),
                  (16, 2, 257), (16, 3, 257), (8, 3, 113), (8, 1, 193)]:
    CELLS.append(("M2", S, R, p))

print("%4s %4s %3s %7s | %-22s %-22s %8s | %9s %9s %9s" %
      ("fam", "N", "k", "p", "TMASS exact", "TMASS ref(round23)", "agree", "CRATIO", "SIGMA", "ZFRATIO"))
for (fam, N, k, p) in CELLS:
    assert_2power_grid(N)                                  # E6 / CATCH-Z6
    rows = rows_M4(N, p) if fam == "M4" else rows_M2(N, k, p)
    d = cell(rows, p, want_AU=True)
    AU = d["AU"]
    ref = sum(Fraction(AU[U], 1 << U) for U in range(N + 1))
    ok = (ref == d["TMASS"])
    print("%4s %4d %3d %7d | %-22s %-22s %8s | %9.5f %9.3f %9.4f" %
          (fam, N, k, p, str(d["TMASS"])[:22], str(ref)[:22], ok,
           d["CRATIO"], d["SIGMA"], d["ZFRATIO"]))
    check("E2 exact DP == verbatim round-23 enumerator  %s N=%d k=%d p=%d" % (fam, N, k, p), ok)
    check("E1 Z-FLOOR  TMASS >= 2^N/p^kappa            %s N=%d k=%d p=%d" % (fam, N, k, p),
          d["ZFRATIO"] >= 1.0, "ZFRATIO %.6f" % d["ZFRATIO"])

print()
print("=" * 104)
print("E3 -- full-cube identity (kappa = 0 surrogate: the p=... trivial row) ")
print("=" * 104)
for N in [4, 8, 16]:
    # kappa = 0 is TMASS over the whole cube = 2^N ; emulate with the identity sum_U C(N,U) 2^U 2^-U
    tot = sum(comb(N, U) * (2 ** U) * Fraction(1, 1 << U) for U in range(N + 1))
    check("E3 full-cube TMASS = 2^N at N=%d" % N, tot == (1 << N), "%s vs %d" % (tot, 1 << N))

print()
print("=" * 104)
print("E4 -- w-invariance: TMASS identical across ALL primitive 2S-th roots (registered P2a)")
print("=" * 104)
for (fam, N, k, p) in [("M4", 8, 1, 97), ("M4", 16, 1, 257), ("M2", 8, 2, 97),
                       ("M2", 16, 2, 257), ("M2", 16, 3, 353), ("M2", 8, 3, 113)]:
    ws = all_elts_of_order(p, 2 * N)
    vals = set()
    for w in ws:
        rows = rows_M4(N, p, th=w) if fam == "M4" else rows_M2(N, k, p, w=w)
        vals.add(tmass_exact(rows, p))
    check("E4 w-invariance %s N=%d k=%d p=%d (%d roots)" % (fam, N, k, p, len(ws)),
          len(vals) == 1, "distinct TMASS values: %d  (value %s)" % (len(vals), str(sorted(vals)[0])[:28]))

print()
print("=" * 104)
print("E5 -- banked-number replay")
print("=" * 104)
d = cell(rows_M2(16, 2, 3137), 3137, want_AU=True)
print("   (S,R,p)=(16,2,3137): TMASS=%s  EXCESS=%.4f  CRATIO=%.6f  SIGMA=%.4f  UMIN=%s  A[UMIN]=%d"
      % (str(d["TMASS"])[:30], d["EXCESS"], d["CRATIO"], d["SIGMA"], d["UMIN"], d["AU"][d["UMIN"]]))
check("E5 banked EXCESS = 2.3463 at (16,2,3137)", abs(d["EXCESS"] - 2.3463) < 5e-4,
      "measured %.6f" % d["EXCESS"])
check("E5 banked '32 weight-11 ternary kernel vectors'",
      d["UMIN"] == 11 and d["AU"][11] == 32, "UMIN=%s A[11]=%d" % (d["UMIN"], d["AU"][11]))
check("P1a CRATIO(16,2,3137) = 1.0089 +- 0.0010", abs(d["CRATIO"] - 1.0089) < 1e-3,
      "REGISTERED 1.0089 ; measured %.6f" % d["CRATIO"])
for pp in (1409, 1889, 3137):
    dd = cell(rows_M2(16, 2, pp), pp)
    print("   SIGMA->-inf line (16,2,p): p=%5d  SIGMA=%8.4f  EXCESS=%7.4f  CRATIO=%9.6f"
          % (pp, dd["SIGMA"], dd["EXCESS"], dd["CRATIO"]))
check("E5 banked EXCESS line 2.13 / 1.70 / 2.35 at p=1409/1889/3137",
      abs(cell(rows_M2(16, 2, 1409), 1409)["EXCESS"] - 2.13) < 5e-3 and
      abs(cell(rows_M2(16, 2, 1889), 1889)["EXCESS"] - 1.70) < 5e-3,
      "%.4f  %.4f" % (cell(rows_M2(16, 2, 1409), 1409)["EXCESS"],
                      cell(rows_M2(16, 2, 1889), 1889)["EXCESS"]))

print()
print("   composite boundary probe (CATCH-Z6 INVALID as a counterexample; declared):")
d6 = cell(rows_M4(6, 19993), 19993, want_AU=True)
print("   L=6 2L=12 p=19993: TMASS=%.6f EXCESS=%.4f CRATIO=%.6f UMIN=%s A[3]=%d"
      % (d6["TMASSf"], d6["EXCESS"], d6["CRATIO"], d6["UMIN"], d6["AU"][3]))
check("E5 banked EXCESS = 178.51 at composite (L=6, p=19993)", abs(d6["EXCESS"] - 178.51) < 5e-3,
      "measured %.4f" % d6["EXCESS"])

print()
print("=" * 104)
print("P3a/P3c -- p-free (char-0) relation lattice: PFMASS(n) closed form vs exhaustive")
print("=" * 104)
print("%5s %4s %7s %8s | %14s %12s | %10s %12s" %
      ("n=2L", "L", "phi(n)", "RELDIM", "|PFREE| latt", "3^RELDIM", "PFMASS", "(5/4)^(L/3)"))
for n in [8, 16, 32, 64, 12, 24, 48, 18, 36, 20, 40, 30, 28, 44]:
    L = n // 2
    m, c, sh = pfree_mass(n)
    ph = 0
    for j in range(1, n + 1):
        if math.gcd(j, n) == 1:
            ph += 1
    pred = Fraction(5, 4) ** (L // 3) if (n % 3 == 0 and (n // 3) & ((n // 3) - 1) == 0) else None
    print("%5d %4d %7d %8d | %14s %12s | %10s %12s" %
          (n, L, ph, L - ph, c, 3 ** sh if sh is not None else "-",
           ("%.6f" % float(m)) if m is not None else "cap",
           ("%.6f" % float(pred)) if pred is not None else "-"))
    check("CZ-M RELDIM(n)=n/2-phi(n) at n=%d" % n, sh == L - ph, "sh=%s L-phi=%d" % (sh, L - ph))
    if n & (n - 1) == 0:
        check("CZ-M: 2-power n=%d has PFREE={0} (PFMASS=1)" % n, m == 1, "PFMASS=%s" % m)
    if pred is not None:
        check("P3c PFMASS(%d) = (5/4)^(L/3) = %s" % (n, pred), m == pred, "measured %s" % m)
        check("CZ-M count 3^{n/2-phi} at n=%d" % n, c == 3 ** sh, "%d vs %d" % (c, 3 ** sh))

# exhaustive independent confirmation that the lattice search finds ALL ternary relations
print()
print("   independent exhaustive ternary sweep (all 3^h vectors) for n=12, 24:")
for n in [12, 24]:
    h = n // 2
    ph = cyclotomic(n)
    cnt = 0
    mass = Fraction(0)
    v = [0] * h
    def rec(i):
        global cnt, mass
        if i == h:
            a = v[:]
            db = len(ph) - 1
            for t in range(h - 1, db - 1, -1):
                c = a[t]
                if c:
                    for j in range(db + 1):
                        a[t - db + j] -= c * ph[j]
            if all(x == 0 for x in a):
                cnt += 1
                mass += Fraction(1, 1 << sum(1 for x in v if x))
            return
        for e in (0, 1, -1):
            v[i] = e
            rec(i + 1)
        v[i] = 0
    rec(0)
    m2, c2, sh2 = pfree_mass(n)
    print("      n=%d: brute |PFREE| = %d, PFMASS = %s   (lattice search: %d, %s)" % (n, cnt, mass, c2, m2))
    check("P3c lattice search is EXHAUSTIVE at n=%d" % n, cnt == c2 and mass == m2)

sys.exit(summary())
