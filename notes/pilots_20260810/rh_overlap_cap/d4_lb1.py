#!/usr/bin/env python3
"""d4_lb1.py -- rh_overlap_cap (round 31).

Exact arithmetic for LB1 (the maximal-core pencil lower bound) and its
consequences.  LB1's sufficient condition is

    2^n * q^{k-a} < 1        (column-farness)          -- (C1)
    q * 2^n * q^{k-a} < 1    (no spurious witness)     -- (C2)

i.e.  n < (a-k-1) * log2 q  covers both.  Everything below is integer
arithmetic on the exponents (log2 q is bounded below by an integer).
"""
from fractions import Fraction

n, k = 2 ** 41, 2 ** 40
SIG = 2 ** 34
a = k + SIG
r = n - a

print("=" * 74)
print("LB1 admissibility:  n < (a-k-1)*log2 q")
print("=" * 74)
print("  n = %d ;  a-k-1 = %d" % (n, a - k - 1))
for lgq in (128, 129, 167, 255, 256):
    lhs = (a - k - 1) * lgq
    print("  log2 q >= %3d :  (a-k-1)*log2 q = %d   margin = %+d   %s"
          % (lgq, lhs, lhs - n, "OK" if lhs > n else "FAILS"))
print("  the widened RH-AC quantifier is q > 2^167 -> LB1 applies with")
print("  margin %d bits at the bottom of the quantifier."
      % ((a - k - 1) * 167 - n))
print("  at the razor slice (log2 q > 255.9) margin = %d (= 2^41-2^34 at 255: %s)"
      % ((a - k - 1) * 255 - n, (a - k) * 255 - n == 2 ** 41 - 2 ** 34))

print()
print("--- LB1 output at the razor row ---")
print("  slopes         M = r+1 = n-a+1 = %d" % (n - a + 1))
print("  every pairwise overlap = a-1 = %d" % (a - 1))
print("  a^2/n                  = %d" % (a * a // n))
print("  ratio (a-1)/(a^2/n)    = %.6f" % ((a - 1) / (a * a // n)))
print("  so the cap 'overlap < a^2/n' is FALSE at sigma = 2^34.")

print()
print("--- is a-1 > a^2/n for the WHOLE open bracket? ---")
print("  a-1 > a^2/n  <=>  a^2 - n a + n < 0.  Roots of x^2-nx+n:")
lo, hi = 2, n
while lo < hi:                          # least a with a^2-na+n >= 0 above n/2
    mid = (lo + hi + 1) // 2
    if mid * mid - n * mid + n < 0:
        lo = mid
    else:
        hi = mid - 1
print("  largest a with a^2-na+n < 0 : %d  (n-1 = %d)" % (lo, n - 1))
for lab, aa in [("bracket bottom k+2^34", k + 2 ** 34),
                ("Johnson point", 1554944255988),
                ("bracket top 3n/4", 3 * n // 4)]:
    print("  %-22s a=%-15d a^2-na+n = %d  (<0: %s)"
          % (lab, aa, aa * aa - n * aa + n, aa * aa - n * aa + n < 0))

print()
print("--- LB1 vs the banked r+1 UPPER bound (minimal_index_budget) ---")
print("  banked: every column-far syndrome pencil has <= r+1 supported")
print("  finite slopes, for N=2^41, R=2^40, r <= R/2-2 = %d" % (2 ** 39 - 2))
for rr in (2 ** 39 - 2, 2 ** 39 - 1, 2 ** 39):
    aa = n - rr
    print("  r = %-14d a = n-r = %-15d  LB1 gives >= %d ; banked <= %s"
          % (rr, aa, rr + 1,
             ("%d  ->  EQUALITY" % (rr + 1)) if rr <= 2 ** 39 - 2
             else ("%d (band_closure:484)  -> EQUALITY" % (rr + 1)
                   if rr == 2 ** 39 else "not proved")))
print("  a = 3n/4 : LB1 >= %d ; the D4-precision-fix budget is 2^39+1 = %d"
      % (n - 3 * n // 4 + 1, 2 ** 39 + 1))
print("  => budget 2^39 is UNATTAINABLE at a = 3n/4 (LB1 exceeds it by 1).")

print()
print("--- THEOREM I' consistency of the LB1 configuration ---")
print("  (xr_band_key_lemma_pencil_mass statement.md:41-46)")
print("  Z_v = E, |Z_v| = a-1 ; u = 0 on E so e(0) = |E| = a-1.")
print("  identity:  sum_z agr(0, w_z) = q e(0) + (n - |Z_v|)")
print("  LB1 side:  (r+1)*a + (q-r-1)*(a-1) = q(a-1) + (r+1)")
print("  q(a-1) + (n - (a-1)) = q(a-1) + (r+1)   ->  n-(a-1) = r+1 : %s"
      % (n - (a - 1) == r + 1))
print("  COROLLARY I.1 floor(n/a) = %d  (a fixed witness serves <= 1 slope)"
      % (n // a))
print("  COROLLARY I.2 needs 2a > n : 2a-n = %d > 0 -> lists pairwise disjoint"
      % (2 * a - n))
print("  LB1 has %d distinct bad slopes with the SAME witness 0 -- consistent"
      % (r + 1))
print("  because v = d_2 has |Z_v| = a-1 zeros, so I' (not I) applies.")

print()
print("--- T3 stratum emptiness, in the banked (AP2)/(AP3) coordinates ---")
print("  anchor_pencil statement.md:33-34 :  r-s+1 <= t <= r ; s+t-r >= 1")
print("  dictionary  e_P = n - s - t  ,  a - e_P = s + t - r  in [1, s]")
s_thr = a * (n - a) // n
print("  T3 needs a - e_P > a - a^2/n = %d for every line" % s_thr)
print("  since a - e_P <= s, EVERY bad slope needs s > %d" % s_thr)
print("  s <= r = %d, so the live window is s in (%d, %d]" % (r, s_thr, r))
print("  fraction of the s-range that survives = (n-a)/n = %s = %.7f"
      % (Fraction(n - a, n), (n - a) / n))
print("  one bad slope at agreement >= n-%d = %d kills T3 outright"
      % (s_thr, n - s_thr))
print("=" * 74)
