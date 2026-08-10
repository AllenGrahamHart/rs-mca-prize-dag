#!/usr/bin/env python3
"""d1_exact.py -- rh_overlap_cap (round 31).

Exact integer / Fraction replay of every razor-scale number this round
quotes.  No floats enter a load-bearing comparison; floats appear only
in printed diagnostics (marked).

Objects, stated once so the report can quote them:

  C = RS[F_q, D, k], n = |D| = 2^41, k = 2^40, a = k + sigma, r = n-a.
  A received pair (f1,f2) is COLUMN-FAR at radius r iff for EVERY pair
  of codewords (p0,p1) the common agreement
       |Agr(f1,p0) cap Agr(f2,p1)|  <=  n-r-1 = a-1.
  (definition read off d2_sunflower.py:108-112 and
   rate_half_ca_hankel_split_pencil_equivalence/statement.md:28-34)
  A slope lam is CA-BAD iff dist(f1+lam f2, C) <= r; A_lam is its
  agreement set with a chosen witness, |A_lam| >= a.
"""
from fractions import Fraction
import math

L2 = lambda x: math.log(x, 2)          # DIAGNOSTIC float only

n = 2 ** 41
k = 2 ** 40
SIG = 2 ** 34
a = k + SIG
r = n - a

print("=" * 74)
print("RAZOR ROW  n=2^41  k=2^40  sigma=2^34")
print("=" * 74)
print("  n            = %d" % n)
print("  k            = %d" % k)
print("  a  = k+2^34  = %d" % a)
print("  r  = n-a     = %d   (= 2^40-2^34: %s)" % (r, r == 2 ** 40 - 2 ** 34))
print("  2a-n         = %d   (= 2^35: %s)" % (2 * a - n, 2 * a - n == 2 ** 35))

# ---------------------------------------------------------------- the caps
theta_star = Fraction(a * a, n)
assert theta_star.denominator == 1
theta_star = int(theta_star)
THETA_ALG = k - 1                      # round-29's cap (MDS codeword agreement)
THETA_FAR = a - 1                      # the cap that actually applies (col-far)

print()
print("--- the three caps ---")
print("  THETA_STAR = a^2/n            = %d   (= 2^39+2^34+2^27: %s)"
      % (theta_star, theta_star == 2 ** 39 + 2 ** 34 + 2 ** 27))
print("  THETA_ALG  = k-1  (round-29)  = %d" % THETA_ALG)
print("  THETA_FAR  = a-1  (this round)= %d" % THETA_FAR)
print("  THETA_FAR - THETA_ALG         = %d   (= 2^34: %s)"
      % (THETA_FAR - THETA_ALG, THETA_FAR - THETA_ALG == 2 ** 34))

GAP_ALG = THETA_ALG - theta_star
GAP_FAR = THETA_FAR - theta_star
BRACKET = 3 * n // 4 - a
print()
print("--- gaps, and T5's ratio ---")
print("  GAP_ALG = (k-1) - a^2/n       = %d" % GAP_ALG)
print("  GAP_FAR = (a-1) - a^2/n       = %d   (= 2^39-2^27-1: %s)"
      % (GAP_FAR, GAP_FAR == 2 ** 39 - 2 ** 27 - 1))
print("  BRACKET = 3n/4 - a            = %d" % BRACKET)
print("  GAP_ALG / BRACKET             = %s  (~%.6f)  <- T5's 0.999748"
      % (Fraction(GAP_ALG, BRACKET), GAP_ALG / BRACKET))
print("  GAP_FAR / BRACKET             = %s  (~%.6f)  <- with the right cap"
      % (Fraction(GAP_FAR, BRACKET), GAP_FAR / BRACKET))
print("  RATIO_CAP = (k-1)/(a^2/n)     = %.6f" % (THETA_ALG / theta_star))
print("  RATIO_FAR = (a-1)/(a^2/n)     = %.6f" % (THETA_FAR / theta_star))

# ------------------------------------------------- do they end together?
# GAP_ALG(a) = 0  at  a = floor(sqrt(n(k-1)))+1 ; BRACKET(a) = 0 at 3n/4.
lo, hi = k, n
while lo < hi:                          # least a with a^2 > n(k-1)
    mid = (lo + hi) // 2
    if mid * mid > n * (k - 1):
        hi = mid
    else:
        lo = mid + 1
a_john = lo
lo, hi = k, n
while lo < hi:                          # least a with a^2/n >= a-1, i.e. GAP_FAR<=0
    mid = (lo + hi) // 2
    if mid * mid >= n * (mid - 1):
        hi = mid
    else:
        lo = mid + 1
a_far0 = lo
print()
print("--- 'they end together' (T5) tested ---")
print("  GAP_ALG vanishes at a = %d   (sigma = %d, a/n ~ %.7f)"
      % (a_john, a_john - k, a_john / n))
print("  GAP_FAR vanishes at a = %d   (a/n ~ %.7f)  [n-1 = %d]"
      % (a_far0, a_far0 / n, n - 1))
print("  BRACKET vanishes at a = %d = 3n/4" % (3 * n // 4))
print("  3n/4 - a_john                 = %d" % (3 * n // 4 - a_john))
print("  sigma_john                    = %d" % (a_john - k))
print("  GAP_ALG(3n/4) = %d   (already NEGATIVE: %s)"
      % ((k - 1) - (3 * n // 4) ** 2 // n, (k - 1) - (3 * n // 4) ** 2 // n < 0))
# the exact identity behind the 0.999748 coincidence
s = SIG
ident = BRACKET - 1 - Fraction(s * s, 2 * k)
print("  identity GAP_ALG = BRACKET - 1 - sigma^2/(2k):  %s  ->  %s"
      % (ident, ident == GAP_ALG))
print("  sigma^2/(2k) = %d (= 2^27: %s)"
      % (s * s // (2 * k), s * s // (2 * k) == 2 ** 27))

# ------------------------------------------------- T3 numbers, replayed
print()
print("--- T3 (Fisher / Corradi) replay ---")
for name, th in [("theta = n/4", n // 4), ("theta = a^2/n - 1", theta_star - 1)]:
    val = Fraction(a - th, theta_star - th)
    print("  %-20s  #slopes <= %s = %d   margin %.4f bits"
          % (name, val, int(val), 128 - L2(int(val))))
print("  a(n-a)/n + 1 = %d   (matches theta*-1 bound: %s)"
      % (a * (n - a) // n + 1, a * (n - a) // n + 1 == int(Fraction(a - (theta_star - 1), 1))))
print("  average pairwise overlap of M sets = a^2/n - a(n-a)/(n(M-1)) < a^2/n")
print("     => Fisher is TIGHT; the cap is STRONGER than the list bound.")

# -------------------------------------------- T1(iv) monotonicity in e
print()
print("--- T1(iv): m_P <= (n-e)/(a-e), monotone INCREASING in e ---")
for lab, e in [("e = 2a-n (minimal core)", 2 * a - n),
               ("e = a^2/n (Fisher edge)", theta_star),
               ("e = a-1   (maximal core)", a - 1)]:
    m = Fraction(n - e, a - e)
    print("  %-26s e=%-16d m_P <= %s = %d" % (lab, e, m, int(m)))
print("  1 + n/a = %s ~ %.5f" % (1 + Fraction(n, a), 1 + n / a))

# --------------------------------- when can T3's hypothesis hold at all?
# a - e_P = s + t_P - r  (anchor-pencil (AP2)/(AP3) coordinates), and
# t_P <= r, so a - e_P <= s.  T3 needs a - e_P > a - a^2/n = a(n-a)/n.
s_thresh = a * (n - a) // n
print()
print("--- exact emptiness test for T3's hypothesis ---")
print("  a - a^2/n = a(n-a)/n = %d   (= 2^39-2^27: %s)"
      % (s_thresh, s_thresh == 2 ** 39 - 2 ** 27))
print("  T3 needs EVERY bad slope's error weight s > %d" % s_thresh)
print("  admissible s range is [1, r] = [1, %d]" % r)
print("  s/r threshold = a/n = %s = %.7f  -> T3 dead on %.4f%% of the range"
      % (Fraction(a, n), a / n, 100 * a / n))
print("  equivalently: one bad slope of agreement >= n - %d = %d kills T3"
      % (s_thresh, n - s_thresh))
print("  n - a(n-a)/n = 3n/4 + 2^27 : %s" % (n - s_thresh == 3 * n // 4 + 2 ** 27))

# ------------------------------------------- the maximal-core pencil
print()
print("--- the maximal-core pencil (D1 extremal structure) ---")
print("  |E| = a-1 = %d   |T| = n-a+1 = r+1 = %d" % (a - 1, n - a + 1))
print("  slopes  M = n-a+1 = %d = 2^%.4f" % (n - a + 1, L2(n - a + 1)))
print("  every pairwise overlap = a-1 = %d" % (a - 1))
print("  T1(iv) at e=a-1 gives m_P <= n-a+1 = %d  -> TIGHT" % (n - a + 1))
print("  budget margin: 128 - log2(M) = %.4f bits" % (128 - L2(n - a + 1)))
# union bound (all integers; q >= 2^255 used conservatively)
LOGQ = 255                              # conservative: 2^255.9 < q < 2^256
bad_log2 = n - SIG * LOGQ               # log2( 2^n * q^{k-a} ) upper bound
print("  union bound  log2( #(U0,U1) * q^{k-a} ) <= n - sigma*log2 q")
print("     = %d - %d*%d = %d  (= -(2^41-2^34): %s)"
      % (n, SIG, LOGQ, bad_log2, bad_log2 == -(2 ** 41 - 2 ** 34)))
print("     bad fraction < 2^%d  ==> a good lambda-assignment EXISTS" % bad_log2)

# ------------------------------------------------- second-level Fisher
print()
print("--- second level (cores inside A_lam0) ---")
core_min = 2 * a - n
print("  |E_i| >= 2a-n = %d ; ground set a = %d" % (core_min, a))
print("  second-level Fisher threshold (2a-n)^2/a = %s ~ 2^%.4f"
      % (Fraction(core_min * core_min, a), L2(core_min * core_min / a)))
print("  a/(2a-n) = %s = %.1f  (disjoint cores would give t <= 32)"
      % (Fraction(a, 2 * a - n), a / (2 * a - n)))
print("  MDS cap on core-core overlap = k-1 = %d -> factor %.1f short"
      % (k - 1, (k - 1) / (core_min * core_min / a)))
print("  first level is short by only a factor %.4f" % (THETA_FAR / theta_star))

# ------------------------------------------------------- the scale ladder
print()
print("=" * 74)
print("SCALE LADDER (rate 1/2, n_s = 2 k_s, a = k_s + s)")
print("=" * 74)
print("  cell            k-1   a^2/n     GAP_ALG    a-1  GAP_FAR  RATIO_CAP")
cells = [(8, 4, 5), (8, 4, 6), (8, 4, 7), (10, 5, 6), (12, 6, 7),
         (16, 8, 9), (16, 8, 10), (16, 8, 11)]
for (ns, ks, aa) in cells:
    ts = Fraction(aa * aa, ns)
    print("  (%2d,%2d,%2d)   %5d  %8s  %8s  %5d  %8s   %.4f"
          % (ns, ks, aa, ks - 1, ts, ks - 1 - ts, aa - 1, aa - 1 - ts,
             (ks - 1) / ts))
print()
print("  smallest rate-1/2 dimension with GAP_ALG > 0 (s=1):")
for ks in range(3, 12):
    ns, aa = 2 * ks, ks + 1
    ok = ks * ks - 2 * ks - 2 * ks * 1 - 1 > 0
    print("     k=%2d : k^2-2k-2ks-s^2 = %5d  -> %s"
          % (ks, ks * ks - 2 * ks - 2 * ks - 1, "POSITIVE" if ok else "negative"))
print()
print("  RATIO_CAP closed form 2k(k-1)/(k+s)^2 at razor: %.6f  (matches: %s)"
      % (2 * k * (k - 1) / (a * a) * 1.0,
         Fraction(2 * k * (k - 1), a * a) == Fraction(THETA_ALG, theta_star)))
print("  union-bound budget sigma*log2(q) - n at each cell decides whether the")
print("  maximal-core pencil is FORCED to exist; at the razor it is (above).")
print("=" * 74)
