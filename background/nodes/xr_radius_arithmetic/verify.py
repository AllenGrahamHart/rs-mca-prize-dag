#!/usr/bin/env python3
"""Verifier for xr_radius_arithmetic.
(1) exact corridor edge t* at L=log2 q=255.9, n=2^41 -> reproduces the QX.14/15
    table; s*=t*-1 (never s*=1). (2) ball profile N_s=C(j,s)C(n-j,s) exhaustive +
    Vandermonde sum_s N_s=C(n,j). (3) plateau onset c(s,t)=min(s,t-1) at s=t-1.
Stdlib only; runs <1s."""
from math import lgamma, log, comb
from itertools import combinations
LN2 = log(2)

def log2C(n, j):
    if j < 0 or j > n: return float("-inf")
    return (lgamma(n + 1) - lgamma(j + 1) - lgamma(n - j + 1)) / LN2

def corridor_edge(n, k, L):
    # smallest t with t*L >= log2 C(n, n-k-t) + 128
    lo, hi = 1, n - k - 1
    while lo < hi:
        t = (lo + hi) // 2
        if L * t >= log2C(n, n - k - t) + 128: hi = t
        else: lo = t + 1
    return lo

def ball_profile_exhaustive(n, j):
    """directly count co-supports at each exchange distance s from a fixed j-set,
    compare to C(j,s)C(n-j,s); return True iff exact for all s. (small n)"""
    T0 = set(range(j))
    from collections import Counter
    cnt = Counter()
    for T in combinations(range(n), j):
        s = j - len(T0 & set(T))   # |T\T0| = exchange distance
        cnt[s] += 1
    for s in range(0, j + 1):
        if cnt[s] != comb(j, s) * comb(n - j, s):
            return False
    # Vandermonde: total = C(n,j)
    return sum(cnt.values()) == comb(n, j)

if __name__ == "__main__":
    ok = True
    # (1) exact table
    n, L = 2**41, 255.9
    TARGET = {2: 8592912739, 4: 7014660390, 8: 4722556392, 16: 2943177800}
    print("(1) corridor edge t* and reach s*=t*-1 at L=255.9, n=2^41:")
    for denom, tref in TARGET.items():
        k = n // denom
        tstar = corridor_edge(n, k, L)
        sstar = tstar - 1
        match = (tstar == tref)
        never1 = (sstar > 1)
        ok &= match and never1
        print(f"    rate 1/{denom:<2d}: t*={tstar} (ref {tref}) match={match}  "
              f"s*={sstar}  s*>1(never s*=1):{never1}")

    # (2) ball profile + Vandermonde, exhaustive on toys
    print("(2) ball profile N_s=C(j,s)C(n-j,s) + Vandermonde sum=C(n,j):")
    for (nn, jj) in [(8, 3), (9, 4), (10, 4), (7, 2)]:
        good = ball_profile_exhaustive(nn, jj)
        ok &= good
        print(f"    n={nn} j={jj}: exhaustive N_s match & Vandermonde: {good}")

    # (3) plateau onset: c(s,t)=min(s,t-1) reaches max t-1 exactly at s=t-1
    print("(3) plateau onset c(s,t)=min(s,t-1):")
    plok = True
    for t in range(2, 20):
        c = [min(s, t - 1) for s in range(0, 2 * t)]
        # max value t-1 first attained at s=t-1
        first = next(s for s, v in enumerate(c) if v == t - 1)
        if first != t - 1 or max(c) != t - 1: plok = False
    ok &= plok
    print(f"    plateau reached at s=t-1 for all t in [2,20): {plok}")

    assert ok
    print("ALL PASS")
