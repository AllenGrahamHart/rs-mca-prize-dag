#!/usr/bin/env python3
"""WCL descent normalisation: the odd/even parity dichotomy (2026-07-26).

Route-selection theorem for the ten open zero-event cells. Stdlib, exact.

The proved `dli_wcl_ell4_weight9_quartic_divisor_descent` normalises a weight-w
relation by a GLOBAL dilation: with rho_i = s_i omega^{e_i}, omega of exact order
N, and a_w = prod_i rho_i, it takes

    lambda = a_w^{-(w^{-1} mod N)} in mu_N

so that the normalised roots lambda*rho_i have product one. At (4,9): N = 2048 and
9^{-1} = 1593 mod 2048.

LEMMA.  The root order is N_ell = 512*ell (512, 1024, 2048 at ell = 1, 2, 4), a
power of two.  Hence w is invertible mod N_ell **iff w is odd**, and:

  * w ODD  -> the global dilation exists and is UNIQUE; the (4,9) normalisation
              transfers verbatim.
  * w EVEN -> w is a zero divisor mod N_ell.  The equation lambda^w = a_w^{-1} has
              exactly g = gcd(w, N_ell) solutions when solvable, and is solvable
              only when a_w^{-1} is a g-th power in mu_N -- an index-g obstruction.
              The global normalisation is therefore UNAVAILABLE.

Consequences for the board:

    ODD  (global dilation transfers) : (1,5) (1,7) (2,7) (2,9) (4,9) (4,11)
    EVEN (obstructed, index g)       : (1,6) g=2   (4,10) g=2
                                       (1,8) g=8   (2,8)  g=8

So (1,8) and (2,8) carry an index-EIGHT obstruction, four times worse than (1,6)
and (4,10) -- they are structurally the hardest of the even cells, independently of
their census sizes.

The two CLOSED ell=2 cells already exhibit the workaround: both (2,5) and (2,6)
were closed by SUB-TUPLE normalisation (the pair-quadratic and triple-cubic
routers), which fixes a selected sub-tuple rather than the global product and so
never needs w invertible. That is the pattern an even-weight descent must follow.
"""

from __future__ import annotations

import sys
from math import gcd

OPEN = [(1, 5), (1, 6), (1, 7), (1, 8), (2, 7), (2, 8), (2, 9),
        (4, 9), (4, 10), (4, 11)]
CLOSED = [(2, 5), (2, 6)]

EXPECTED_ODD = {(1, 5), (1, 7), (2, 7), (2, 9), (4, 9), (4, 11)}
EXPECTED_EVEN_INDEX = {(1, 6): 2, (1, 8): 8, (2, 8): 8, (4, 10): 2}
EXPECTED_N = {1: 512, 2: 1024, 4: 2048}
PINNED_INVERSES = {(2, 5): 205, (1, 5): 205, (1, 7): 439, (2, 7): 439,
                   (2, 9): 569, (4, 9): 1593, (4, 11): 931}

errors: list[str] = []


def check(c: bool, m: str) -> None:
    if not c:
        errors.append(m)


for ell, N in EXPECTED_N.items():
    check(N == 512 * ell, f"root order drift at ell={ell}")
    check(N & (N - 1) == 0, f"N_ell={N} must be a power of two for the argument")

odd, even = set(), {}
for ell, w in OPEN + CLOSED:
    N = EXPECTED_N[ell]
    g = gcd(w, N)
    check((g == 1) == (w % 2 == 1),
          f"({ell},{w}): invertibility mod a 2-power must coincide with w odd")
    if g == 1:
        inv = pow(w, -1, N)
        check(inv * w % N == 1, f"({ell},{w}): bad inverse")
        if (ell, w) in PINNED_INVERSES:
            check(inv == PINNED_INVERSES[(ell, w)],
                  f"({ell},{w}): inverse {inv} != pinned {PINNED_INVERSES[(ell,w)]}")
        if (ell, w) in OPEN:
            odd.add((ell, w))
    else:
        # lambda^w = a^{-1} in the cyclic group mu_N has g solutions when solvable,
        # and the solvable set is the index-g subgroup of g-th powers.
        sols = sum(1 for x in range(N) if (w * x) % N == 0)
        check(sols == g, f"({ell},{w}): expected {g} dilations, found {sols}")
        if (ell, w) in OPEN:
            even[(ell, w)] = g

check(odd == EXPECTED_ODD, f"odd-cell set drift: {sorted(odd)}")
check(even == EXPECTED_EVEN_INDEX, f"even-cell index drift: {even}")
check(max(even.values()) == 8, "the worst even obstruction should be index 8")
check({c for c, g in even.items() if g == 8} == {(1, 8), (2, 8)},
      "index-8 cells should be exactly (1,8) and (2,8)")

# The (4,9) pin the lemma is calibrated against.
check(pow(9, -1, 2048) == 1593, "(4,9) inverse must be 1593 mod 2048")

if errors:
    for e in errors:
        print("FAIL:", e)
    sys.exit(1)

print(
    "DESCENT_PARITY_DICHOTOMY_PASS "
    f"odd_cells={len(odd)} (global dilation transfers) "
    f"even_cells={len(even)} obstructed "
    f"index2={sorted(c for c,g in even.items() if g==2)} "
    f"index8={sorted(c for c,g in even.items() if g==8)} "
    "=> even-weight descents need sub-tuple normalisation, as in the closed (2,6)"
)
