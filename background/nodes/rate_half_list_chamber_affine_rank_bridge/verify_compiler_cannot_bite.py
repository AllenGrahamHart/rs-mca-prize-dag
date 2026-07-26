#!/usr/bin/env python3
"""THE BRIDGE QUESTION, ANSWERED — negatively (2026-07-26).

At the official rate-1/2 razor row the GF rank-flat list compiler CANNOT exclude a
four-codeword configuration, at any affine rank, any generalized weights, any b.
Therefore no chamber->(d_1..d_s,b) transport can ever make it bite, the Convergence
Ledger's S3 promotion test can never fire, and H1 is permanently ev-wired.

Inputs, all previously established:
  * b = 0.  (Two independent routes: Codex's budget-three common-mismatch zero,
    unconditional in all six incidence types and all thirteen chambers; and this
    node's own (CZB) route in the s=2/Ddir=6 branch.)  b = 0 MINIMISES every
    denominator factor d_j - t + b, so it is the compiler's best case.
  * s in {2,3}.  (s=1 excluded: no three list members are collinear.)
  * d_1 in {R+1, R+2}.  The razor bracket forces every pairwise difference to have
    weight K+1 or K+2, and d_1 is the minimum weight of the direction code.
  * s=2 forces d_2 = n - z with z in {733007751849, 733007751850}  (PROGRESS 4).

Cap:  |L_A| <= floor( d_s^{under s} / prod_j (d_j - t + b) ),  t = n - m.

Result:
  s=2, at the pinned d_2 : cap = 4 exactly (exact value 64/15) -- equals the
                           quadruple size, so no exclusion.
  s=3, minimised over the ENTIRE admissible region: cap = 6 -- never below 4.

Exact rational arithmetic; the floor is applied only at the end.
"""

from __future__ import annotations

import sys
from fractions import Fraction

N = 2**41
K = 2**40
R = N - K
M = 3 * N // 4 - 1
T = N - M                                  # = n/4 + 1
D1_CHOICES = (R + 1, R + 2)                # razor bracket
Z_PINNED = (733007751849, 733007751850)    # PROGRESS 4

EXPECTED_S2_CAP = 4
EXPECTED_S3_MIN_CAP = 6

errors: list[str] = []


def check(c: bool, m: str) -> None:
    if not c:
        errors.append(m)


def cap2(d1: int, d2: int) -> Fraction:
    return Fraction(d2 * (d2 - 1), (d1 - T) * (d2 - T))


def cap3(d1: int, d2: int, d3: int) -> Fraction:
    return Fraction(d3 * (d3 - 1) * (d3 - 2), (d1 - T) * (d2 - T) * (d3 - T))


def floor_of(f: Fraction) -> int:
    return f.numerator // f.denominator


def ternary_min(f, lo: int, hi: int) -> int:
    while hi - lo > 2:
        a = lo + (hi - lo) // 3
        b = hi - (hi - lo) // 3
        lo, hi = (lo, b) if f(a) <= f(b) else (a, hi)
    return min(range(lo, hi + 1), key=f)


# --- s = 2, at the pinned d_2 ---------------------------------------------
s2 = set()
for z in Z_PINNED:
    d2 = N - z
    for d1 in D1_CHOICES:
        check(d1 < d2, f"d_1={d1} must be below d_2={d2}")
        c = floor_of(cap2(d1, d2))
        s2.add(c)
        check(c >= 4, f"s=2 cap {c} < 4 at z={z}, d_1={d1} -- would EXCLUDE; recheck")
check(s2 == {EXPECTED_S2_CAP}, f"s=2 cap drift: {sorted(s2)}")

# --- s = 3, minimised over the whole admissible region --------------------
# d_2 = d_3 - 1 maximises (d_2 - t) subject to d_2 < d_3, so it minimises the cap
# for any fixed (d_1, d_3); then minimise over d_3 and over the two d_1 choices.
best = None
for d1 in D1_CHOICES:
    f = lambda x, _d1=d1: cap3(_d1, x - 1, x)
    x = ternary_min(f, d1 + 2, N)
    for cand in range(max(d1 + 2, x - 2), min(N, x + 2) + 1):
        v = f(cand)
        if best is None or v < best[0]:
            best = (v, d1, cand - 1, cand)
s3_min = floor_of(best[0])
check(s3_min == EXPECTED_S3_MIN_CAP, f"s=3 minimum cap drift: {s3_min}")
check(s3_min >= 4, "s=3 minimum cap dropped below 4 -- the compiler would bite; recheck")

# Spot-check that d_2 = d_3 - 1 really is optimal for a sample of d_3.
for d3 in (R + 5, 3 * N // 4, 7 * N // 8, N):
    for d1 in D1_CHOICES:
        if d3 <= d1 + 1:
            continue
        base = cap3(d1, d3 - 1, d3)
        for d2 in (d1 + 1, (d1 + d3) // 2):
            if d1 < d2 < d3:
                check(cap3(d1, d2, d3) >= base,
                      f"d_2 = d_3-1 is not optimal at d_3={d3}, d_1={d1}")

if errors:
    for e in errors:
        print("FAIL:", e)
    sys.exit(1)

v, d1b, d2b, d3b = best
print(
    "COMPILER_CANNOT_BITE_PASS "
    f"s2_cap={EXPECTED_S2_CAP}(exact {cap2(D1_CHOICES[0], N-Z_PINNED[0])}) "
    f"s3_min_cap={s3_min}(exact {v}, at d1={d1b} d2={d2b} d3={d3b}) "
    "=> cap >= 4 at every reachable configuration; the rank-flat compiler can "
    "NEVER exclude four codewords at this row, so no chamber transport can make "
    "it bite and H1 is permanently ev-wired"
)
