#!/usr/bin/env python3
"""d1_prices.py -- rh_farca_upper (round 32), D1 route pricing.

Exact integer arithmetic for every threshold quoted in the report.
Stdlib only.  Run under: tools/ramguard tiny -- python3 <this>
"""
from math import isqrt, lgamma, log

LOG2 = log(2.0)


def lg(x):
    return log(x) / LOG2


def lgbinom(n, m):
    return (lgamma(n + 1) - lgamma(m + 1) - lgamma(n - m + 1)) / LOG2


out = []
P = out.append

n = 1 << 41
k = 1 << 40
R = n - k
sigma = 1 << 34
a = k + sigma
r = n - a
P("== razor row ==")
P(f"n            = {n}")
P(f"k            = {k}")
P(f"R = n-k      = {R}")
P(f"sigma        = {sigma}")
P(f"a = k+sigma  = {a}")
P(f"r = n-a      = {r}   (= 2^40-2^34 : {r == (1<<40)-(1<<34)})")
P(f"r+1          = {r+1}  = 2^{lg(r+1):.4f}")
P(f"a/n          = {a}/{n} = {a/n!r}")
P(f"R/2          = {R//2}")
P(f"R-r          = {R-r}   (= 2^34 : {R-r == sigma}) = a-k")
P(f"2r-R+1       = {2*r-R+1}  (= 2^40-2^35+1 : {2*r-R+1 == (1<<40)-(1<<35)+1})")
P(f"2a-n         = {2*a-n}   (= 2^35 : {2*a-n == (1<<35)})")
P(f"3n/4         = {3*n//4}  ; a < 3n/4 : {a < 3*n//4}")

P("")
P("== PR-A : wide pencil / unique-decoding radius ==")
P(f"pencil shape (R-r) x (r+1) = {R-r} x {r+1}")
P(f"rows < cols (wide, full column rank IMPOSSIBLE) : {(R-r) < (r+1)}")
P(f"r > R/2 : {r > R/2}   (r/R = {r/R!r})")
P(f"unique-decoding radius (d-1)/2 = R/2 = {R//2}; "
  f"a >= n-R/2 <=> a >= {n-R//2} = 3n/4 : {n-R//2 == 3*n//4}")

P("")
P("== PR-B : the literal (MI1)/(MI2) reading in the wide regime ==")
rho_max = R - r
A_min = R + 1 - 2 * rho_max
P(f"rho <= min(R-r, r+1) = {rho_max}")
P(f"A = R+1-2rho >= {A_min} (= 2r-R+1 : {A_min == 2*r-R+1})")
P(f"A_min > rho_max  (so (MI1) (A+s)e<=d<=rho forces e=0) : {A_min > rho_max}")
P(f"literal e=0 branch would give T <= rho <= {rho_max} = 2^{lg(rho_max):.1f}")
P(f"LB1 floor r+1 = {r+1}")
P(f"CLASH FACTOR (r+1)/(R-r) = {(r+1)/(R-r)!r}   [PR-B window 62.9-63.1]")
P(f"e=0 forced iff rho < (R+1)/3 = {(R+1)/3!r}; R-r-1 = {R-r-1} < that : "
  f"{(R-r-1) < (R+1)/3}")

P("")
P("== PR-C : route (a), list instruments ==")
sq_nk = isqrt(n * k)
sq_nk1 = isqrt(n * (k - 1))
P(f"sqrt(nk)      = {sq_nk}  (2^40.5 = {2.0**40.5!r})")
P(f"sqrt(n(k-1))  = {sq_nk1}")
P(f"Johnson agreement threshold sqrt(nk)/n = {sq_nk/n!r} (1/sqrt2 = 0.70710678)")
P(f"worst-case anchored agreement 2a-n = {2*a-n}")
P(f"k / (2a-n)    = {k//(2*a-n)} exactly ({k/(2*a-n)!r})   [PR-C(i): 32]")
P(f"sqrt(nk)/(2a-n) = {sq_nk/(2*a-n)!r}   [PR-C(ii): 2^5.5 = {2.0**5.5!r}]")
P(f"best-case anchored agreement a = {a}; sqrt(nk)/a = {sq_nk/a!r}"
  f"   [PR-C(iii) window 1.3924-1.3925]")
P(f"a < k? {a < k}   (agreement above dimension, so k-subset counting is "
  f"non-void ONLY at anchor error weight s <= a-k = {a-k})")
P(f"2a-n < k : {2*a-n < k}  -> C(2a-n, k) = 0, the k-subset ratio bound is VOID")

P("")
P("== PR-D : second-level (core) Fisher ==")
P(f"core cap (column-farness)      a-1 = {a-1}")
P(f"core Fisher threshold sqrt(n(k-1)) = {sq_nk1}")
P(f"ratio threshold/(a-1) = {sq_nk1/(a-1)!r}   [PR-D window 1.3924-1.3925]")
P(f"dead even at the MAXIMAL core : {(a-1)**2 < n*(k-1)}")
P(f"revives exactly at a-1 > sqrt(n(k-1)) i.e. a > {sq_nk1+1} = "
  f"{ (sq_nk1+1)/n!r } n")

P("")
P("== PR-E : two maximal cores ==")
P(f"2(a-1) = {2*(a-1)} <= n + (k-1) = {n+k-1} : {2*(a-1) <= n+k-1}")
P(f"threshold a <= (n+k+1)/2 = {(n+k+1)/2!r} = 3n/4 + 1/2 : "
  f"{(n+k+1)/2 == 3*n/4 + 0.5}")

P("")
P("== PR-F : UB-NEAR (stratification by radius) ==")
rp = R // 2 - 2
P(f"safe inner radius r' = R/2-2 = {rp}; bound r'+1 = {rp+1} = "
  f"2^{lg(rp+1):.4f}")
P(f"agreement floor of the near stratum n-r' = {n-rp} = 3n/4+2 : "
  f"{n-rp == 3*n//4+2}")
P(f"margin to 2^128 : {128 - lg(rp+1)!r} bits   [PR-F window 88.9-89.1]")

P("")
P("== PR-G : cell regime ratio rho_cell = C(n,n-a)/q^(a-k-1) ==")
for lgq in (128, 167, 216, 255):
    P(f"  log2 q = {lgq}: log2 rho_cell = "
      f"{lgbinom(n, r) - lgq*(a-k-1)!r}")
P(f"log2 C(n,a) = {lgbinom(n, a)!r}")

P("")
P("== PR-I : the a-set counting bound ==")
P(f"T <= C(n,a) = 2^{lgbinom(n,a)!r}  vs the quoted 2^216 : "
  f"worse by 2^{lgbinom(n,a)-216!r}")

P("")
P("== LB1-C admissibility (replay of round 31) ==")
for lgq in (128, 129, 167, 255):
    P(f"  log2 q = {lgq}: (a-k-1)*log2 q - n = {(a-k-1)*lgq - n}")

P("")
P("== budgets ==")
P(f"2^128 = {1<<128}")
P(f"margin of UB-DEFICIENT (T <= R-r-1 = {R-r-1}) below 2^128 : "
  f"{128 - lg(R-r-1)!r} bits")
P(f"drop demanded across one unit of agreement: "
  f"B_ca^far(a-1) >= 2^216 -> B_ca^far(a) <= 2^128 : {216-128} bits")

print("\n".join(out))
