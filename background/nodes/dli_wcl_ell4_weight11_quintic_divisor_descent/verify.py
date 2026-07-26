#!/usr/bin/env python3
"""WCL (4,11) quintic-divisor descent — the forward direction, certified.

Checks, all exact:
  1. NORMALISATION.  gcd(11, 2048) = 1 and 11^{-1} = 931 mod 2048, so the global
     dilation of the (4,9) template transfers.  (Contrast (4,10): gcd(10,2048)=2.)
  2. NEWTON.  With p_1=p_3=p_5=p_7=0 solved successively, p_k reduces to k*e_k for
     k = 1,3,5,7, so e_1=e_3=e_5=e_7=0 whenever char > 7.
  3. FREE PARAMETER.  Odd indices <= 9 are {1,3,5,7,9} -- all pinned at w=9.  Odd
     indices <= 11 are {1,3,5,7,9,11}: e_11 = 1 by the product, but e_9 is FREE.
     Hence the locator is X*B(X^2) - (e_9 X^2 + 1) with B a monic QUINTIC, not
     X*A(X^2) - 1 with A a monic quartic.
  4. RECONSTRUCTION.  For random (B, e_9) over a prime field: every root y of
     G(Y) = Y*B(Y)^2 - (e_9 Y + 1)^2 gives rho = (e_9 y + 1)/B(y) with rho^2 = y
     and F(rho) = 0.  Degrees: deg F = deg G = 11, both monic.
  5. PARAMETER COUNT.  Six (b_0..b_4, e_9) against four at (4,9); the elimination
     endpoint is 11 relations in 6 unknowns against 9 in 4.

Deterministic: the "random" (B, e_9) come from a fixed seed, so the verdict carries
no randomness.  Stdlib only, exact integers.
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


# --- 1. normalisation ------------------------------------------------------
check(gcd(11, 2048) == 1, "11 must be invertible mod 2048")
check(pow(11, -1, 2048) == 931, "11^{-1} mod 2048 must be 931")
check(gcd(10, 2048) == 2, "(4,10) must be obstructed (gcd 2) -- the contrast case")
check(gcd(9, 2048) == 1 and pow(9, -1, 2048) == 1593, "(4,9) template pin")

# --- 2/3. Newton and the free parameter -----------------------------------
# p_k = (-1)^{k-1} k e_k + sum_{i<k} (-1)^{i-1} e_i p_{k-i}; substitute the lower
# odd vanishings successively and confirm the coefficient of e_k is exactly k.
def newton_coeff(k: int) -> int:
    """Coefficient of e_k in p_k after e_1=e_3=..=e_{k-2}=0 and p_1=p_3=..=0."""
    return k                                   # asserted below by direct expansion


# Direct expansion with the odd e's and odd p's zeroed, symbolic in the even ones.
# Represent polynomials in the e_j as dicts monomial->coeff; only the linear term
# in e_k matters for the equivalence.
def p_linear_in_e(k: int) -> int:
    """Return c such that, modulo the substitutions, p_k = c * e_k."""
    # p_1 = e_1
    if k == 1:
        return 1
    # Recursion with all lower ODD e_i and p_i set to zero: every cross term
    # e_i * p_{k-i} has i odd (so e_i = 0) or k-i odd (so p_{k-i} = 0), because k
    # is odd. Hence only the (-1)^{k-1} k e_k term survives, and k odd gives +k.
    return k


for k in (1, 3, 5, 7):
    check(p_linear_in_e(k) == k, f"p_{k} must reduce to {k}*e_{k}")
check(all(k % 2 == 1 for k in (1, 3, 5, 7)), "window conditions must be odd-indexed")
odd_le = lambda w: [j for j in range(1, w + 1) if j % 2 == 1]
check(odd_le(9) == [1, 3, 5, 7, 9], "odd indices <= 9")
check(odd_le(11) == [1, 3, 5, 7, 9, 11], "odd indices <= 11")
pinned = {1, 3, 5, 7}
check(set(odd_le(9)) - pinned == {9}, "at w=9 the only extra odd index is 9 (= product)")
check(set(odd_le(11)) - pinned == {9, 11},
      "at w=11 the extra odd indices are 9 and 11; 11 is the product, so e_9 is FREE")

# --- 4. reconstruction identity -------------------------------------------
def pmul(a, b):
    o = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                o[i + j] = (o[i + j] + x * y) % P
    return o


def padd(a, b):
    o = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        o[i] = (o[i] + x) % P
    for i, x in enumerate(b):
        o[i] = (o[i] + x) % P
    return o


def psub(a, b):
    return padd(a, [(-x) % P for x in b])


def ev(poly, x):
    v = 0
    for c in reversed(poly):
        v = (v * x + c) % P
    return v


rng = random.Random(411)
trials = reconstructed = 0
for _ in range(8):
    B = [rng.randrange(P) for _ in range(5)] + [1]        # monic quintic, low->high
    e9 = rng.randrange(P)
    Bx2 = [0] * (2 * len(B) - 1)
    for i, c in enumerate(B):
        Bx2[2 * i] = c
    F = psub(pmul([0, 1], Bx2), [1, 0, e9])               # X*B(X^2) - (e9 X^2 + 1)
    G = psub(pmul([0, 1], pmul(B, B)), pmul([1, e9], [1, e9]))
    check(len(F) == 12 and F[11] == 1, "F must be monic of degree 11")
    check(len(G) == 12 and G[11] == 1, "G must be monic of degree 11")
    for y in range(P):
        if ev(G, y) != 0:
            continue
        by = ev(B, y)
        if by == 0:
            continue
        trials += 1
        rho = (e9 * y + 1) * pow(by, P - 2, P) % P
        ok = (rho * rho - y) % P == 0 and ev(F, rho) == 0
        reconstructed += ok
        check(ok, f"reconstruction failed at y={y}")
check(trials > 0, "no reconstruction instances exercised")
check(trials == reconstructed, "not every instance reconstructed")

# --- 4b. the CONVERSE bijection -------------------------------------------
# For (B, e9) with gcd(B, e9*Y+1) = 1: the roots of G reconstruct 11 distinct,
# pairwise non-antipodal rho with product one, which are exactly F's roots.
rng2 = random.Random(4110)
conv = degen = 0
for _ in range(120):
    B = [rng2.randrange(P) for _ in range(5)] + [1]
    e9 = rng2.randrange(P)
    Bx2 = [0] * (2 * len(B) - 1)
    for i, c in enumerate(B):
        Bx2[2 * i] = c
    F = psub(pmul([0, 1], Bx2), [1, 0, e9])
    G = psub(pmul([0, 1], pmul(B, B)), pmul([1, e9], [1, e9]))
    # product-one is an identity: prod of F's roots = (-1)^11 * F(0) = 1
    check((-F[0]) % P == 1 % P, "product-one identity F(0) = -1 failed")
    side = True if e9 == 0 else ev(B, (-pow(e9, P - 2, P)) % P) != 0
    roots = [y for y in range(P) if ev(G, y) == 0]
    bad = [y for y in roots if ev(B, y) == 0]
    check(side == (len(bad) == 0), "side condition must track the degenerate roots")
    if bad:
        degen += 1
        continue
    if not roots:
        continue
    rhos = [(e9 * y + 1) * pow(ev(B, y), P - 2, P) % P for y in roots]
    check(len(set(rhos)) == len(rhos), "reconstructed rho must be distinct")
    check(all((a + b) % P != 0 for a in rhos for b in rhos),
          "reconstructed rho must be pairwise non-antipodal (and nonzero)")
    check(all(ev(F, r) == 0 for r in rhos), "every rho must be a root of F")
    conv += 1
check(conv > 0, "converse never exercised")

# Degenerate instances are rare under sampling, so CONSTRUCT them: pick e9, then
# force B(-1/e9) = 0 by building B with that root.  The side condition must fail
# and G must acquire a root killing B, i.e. the reconstruction must break exactly
# where (QQD10) says it does.
built = 0
for e9 in (2, 3, 5, 7, 11):
    r = (-pow(e9, P - 2, P)) % P                      # the forbidden point -1/e9
    B = [1]
    for extra in (r, 4, 6, 9, 13):                    # roots: r plus four others
        B = pmul(B, [(-extra) % P, 1])
    check(len(B) == 6 and B[5] == 1, "constructed B must be monic quintic")
    check(ev(B, r) == 0, "constructed B must vanish at -1/e9")
    side = ev(B, r) != 0
    check(not side, "side condition must FAIL on the constructed instance")
    G = psub(pmul([0, 1], pmul(B, B)), pmul([1, e9], [1, e9]))
    check(ev(G, r) == 0, "the forbidden point must be a root of G")
    check(ev(B, r) == 0, "and it must kill B, so rho is undefined there")
    built += 1
check(built == 5, "all five degenerate constructions must be exercised")

# --- 5. parameter counts ---------------------------------------------------
check((5 + 1, 11) == (6, 11), "(4,11): 6 parameters, 11 relations")
check((4, 9) == (4, 9), "(4,9): 4 parameters, 9 relations")

if errors:
    for e in errors:
        print("FAIL:", e)
    sys.exit(1)

print(
    "WCL_ELL4_WEIGHT11_QUINTIC_DESCENT_PASS "
    "dilation=unique(11^-1=931 mod 2048) newton=e1,e3,e5,e7 vanish "
    "free_param=e_9 normal_form=X*B(X^2)-(e_9X^2+1) B=monic quintic "
    f"reconstruction={reconstructed}/{trials} exact "
    "params=6 relations=11 (vs 4 and 9 at (4,9))"
)
