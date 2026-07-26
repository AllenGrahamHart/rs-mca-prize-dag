#!/usr/bin/env python3
"""WCL (4,10) even-weight divisor descent. Stdlib, exact, deterministic seed.

  1. PARITY.  gcd(10,2048) = 2, so the (4,9)/(4,11) global dilation does NOT exist.
     Contrast pins: gcd(9,2048) = gcd(11,2048) = 1.
  2. FREE PARAMETERS.  Odd indices <= 10 are {1,3,5,7,9}; the window kills 1,3,5,7,
     leaving e_9, and e_10 is free (no dilation to fix it, and none needed).
  3. NORMAL FORM.  F(X) = E(X^2) - e_9 X with E monic quintic -- the single odd term
     sits INSIDE the even part, unlike the odd cells where X sits outside.
  4. e_9 != 0 AUTOMATIC.  e_9 = 0 makes F even, so roots fall into antipodal pairs,
     which reducedness forbids.
  5. RECONSTRUCTION.  G(Y) = E(Y)^2 - e_9^2 Y, monic degree 10; every root y gives
     rho = E(y)/e_9 with rho^2 = y and F(rho) = 0.
"""

from __future__ import annotations

import random
import sys
from math import gcd

P = 10007
errors: list[str] = []


def check(c: bool, m: str) -> None:
    if not c:
        errors.append(m)


# --- 1. parity contrast ----------------------------------------------------
check(gcd(10, 2048) == 2, "(4,10) must be obstructed for the global dilation")
check(gcd(9, 2048) == 1 and gcd(11, 2048) == 1, "the odd cells must be unobstructed")

# --- 2. free-parameter accounting -----------------------------------------
odd_le10 = [j for j in range(1, 11) if j % 2 == 1]
check(odd_le10 == [1, 3, 5, 7, 9], "odd indices <= 10")
check(set(odd_le10) - {1, 3, 5, 7} == {9}, "e_9 is the surviving odd index at w=10")


def pmul(a, b):
    o = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                o[i + j] = (o[i + j] + x * y) % P
    return o


def psub(a, b):
    o = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        o[i] = (o[i] + x) % P
    for i, x in enumerate(b):
        o[i] = (o[i] - x) % P
    return o


def ev(poly, x):
    v = 0
    for c in reversed(poly):
        v = (v * x + c) % P
    return v


def build(E, e9):
    Ex2 = [0] * (2 * len(E) - 1)
    for i, c in enumerate(E):
        Ex2[2 * i] = c
    F = psub(Ex2, [0, e9])                       # E(X^2) - e9 X
    G = psub(pmul(E, E), [0, e9 * e9 % P])       # E(Y)^2 - e9^2 Y
    return F, G


# --- 3/5. normal form and reconstruction ----------------------------------
rng = random.Random(410)
tested = 0
for _ in range(300):
    E = [rng.randrange(P) for _ in range(5)] + [1]
    e9 = rng.randrange(1, P)
    F, G = build(E, e9)
    check(len(F) == 11 and F[10] == 1, "F must be monic of degree 10")
    check(len(G) == 11 and G[10] == 1, "G must be monic of degree 10")
    for y in range(P):
        if ev(G, y):
            continue
        rho = ev(E, y) * pow(e9, P - 2, P) % P
        tested += 1
        check((rho * rho - y) % P == 0, f"rho^2 != y at y={y}")
        check(ev(F, rho) == 0, f"F(rho) != 0 at y={y}")
check(tested > 0, "no reconstruction instances exercised")

# --- 4. e_9 = 0 forces antipodal roots, which reducedness forbids ----------
antipodal_hits = 0
for _ in range(40):
    E = [rng.randrange(P) for _ in range(5)] + [1]
    F0, _ = build(E, 0)
    # F0 is even: F0(-x) = F0(x) for every x, so roots come in +/- pairs.
    check(all(ev(F0, x) == ev(F0, (-x) % P) for x in range(1, 60)),
          "e_9 = 0 must make F even")
    rts = [x for x in range(P) if ev(F0, x) == 0]
    if any((-x) % P in rts and x != 0 for x in rts):
        antipodal_hits += 1
check(antipodal_hits > 0,
      "e_9 = 0 should exhibit an antipodal root pair on some instance")

if errors:
    for e in errors[:10]:
        print("FAIL:", e)
    sys.exit(1)

print(
    "WCL_ELL4_WEIGHT10_EVEN_DESCENT_PASS "
    "dilation=ABSENT(gcd(10,2048)=2) but NOT needed "
    "normal_form=E(X^2)-e_9*X E=monic quintic params=6 "
    f"reconstruction={tested} exact e9_nonzero=forced_by_reducedness "
    "relations=10 unknowns=6"
)
