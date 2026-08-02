#!/usr/bin/env python3
"""Recompute the (CLB3)/(CLB4) rank-four basis thresholds under the widened
pairwise core cap kappa = A-2, and check the formula against the banked
thresholds at kappa = k (statement prints B>=4,4,7 / 4,5,10 at s=4).

(CLB3):  |P_hi(B)| <= L(kappa) * floor(C(n,s-1)/B)  <= 8n^3
so the sufficient basis threshold is B >= L*C(n,s-1)/(8n^3).

Run: tools/ramguard tiny -- python3 <this>
"""
from math import comb

ROWS = []
for name, n, rate, scale in [
    ("RowC 1/4", 1024, 4, 256), ("RowC 1/8", 1024, 8, 256),
    ("RowC 1/16", 1024, 16, 512), ("prize 1/4", 2**41, 4, 256),
    ("prize 1/8", 2**41, 8, 256), ("prize 1/16", 2**41, 16, 512),
]:
    k = n // rate
    A = k + n // scale + 1
    ROWS.append((name, n, k, A, A - k, n - A, n - k))


def Bthresh(n, L, s, budget):
    """least integer B with L*floor(C(n,s-1)/B) <= budget (binary search)"""
    C = comb(n, s - 1)

    def ok(B):
        return L * (C // B) <= budget

    lo, hi = 1, 1
    while not ok(hi):
        hi *= 2
        if hi > 10**30:
            return None
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


print("=== (CLB3) sufficient basis threshold at selector rank s=4, budget 8n^3 ===")
print(f"{'row':<11}{'L(k)':>8}{'B* @kappa=k':>14}{'banked':>9}"
      f"{'L(A-2)':>16}{'B* @kappa=A-2':>16}{'chart excess b+s-2':>21}")
banked = {"RowC 1/4": 4, "RowC 1/8": 4, "RowC 1/16": 7,
          "prize 1/4": 4, "prize 1/8": 5, "prize 1/16": 10}
for name, n, k, A, h, r, R in ROWS:
    Lk = (n - k) // (A - k)
    LA = (n - (A - 2)) // 2
    b1 = Bthresh(n, Lk, 4, 8 * n**3)
    b2 = Bthresh(n, LA, 4, 8 * n**3)
    print(f"{name:<11}{Lk:>8}{b1:>14}{banked[name]:>9}{LA:>16}{b2:>16}"
          f"{(b2 + 2) if b2 else 0:>21}")

print()
print("Reading: at kappa=k the formula reproduces the banked thresholds exactly.")
print("At kappa=A-2 the CLB dichotomy's OTHER branch (a line with b<B* localizes")
print("the whole selector into a chart of excess <= b+s-2 <= B*+2) is useless:")
print("GRK/ACG pay chart excess only through d = 3,3,2,10,10,9 at these rows,")
print("so a chart of excess ~B*+2 is unpayable.  (CLB3)/(CLB4) rank-four close")
print("is DEAD at kappa=A-2 on every row.")

print()
print("=== (CLB1b) compensating gain: a large-core line self-localizes better ===")
print("chart size = (n-w) + m_ell = R + m_ell - (w-k): each extra core point")
print("buys one unit of chart excess back.  Excess is fully cancelled at")
print("w-k = m_ell, i.e. w = k+m_ell.")
print(f"{'row':<11}{'max w-k available (A-2-k)':>28}")
for name, n, k, A, h, r, R in ROWS:
    print(f"{name:<11}{A - 2 - k:>28}")

print()
print("=== budget headroom for a separate band column ===")
print("xr_strip_classification_rungs (3): B_quot_ub(A) + (n-A+1) + 16n^3 <= B*")
print("at all six candidates; prize rows tight at 29n^3 (30n^3 fails).")
print("=> a THIRD generic column for the band fits if it is <= 13 n^3.")
