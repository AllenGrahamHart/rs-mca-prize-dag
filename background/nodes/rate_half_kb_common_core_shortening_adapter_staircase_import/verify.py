#!/usr/bin/env python3
"""Exact replay of the PR #1163 staircase walls at the official KoalaBear
row. Pure integer arithmetic; every displayed constant is recomputed.

RAMGUARD_TIMEOUT: `tools/ramguard tiny -- python3 ...` (seconds).
"""

from fractions import Fraction
from math import comb

N, K, M = 2097152, 1048576, 1116048
D = M - K
R = N - K
T = N - M
B_STAR = 274980728111395087

assert (D, R, T) == (67472, 1048576, 981104)

# 1. degree-18 interface wall: survives exactly through c = 4130
assert 32 * M - 17 * N == 61952


def r_min(c):
    return -((-32 * (M - c)) // (N - c))  # ceil(32(m-c)/(n-c))


assert 32 * (M - 4130) > 17 * (N - 4130)
assert 32 * (M - 4131) < 17 * (N - 4131)
assert r_min(4130) == 18
assert r_min(4131) == 17
assert r_min(K - 1) == 3

# 2. fixed-core compiler cells: fits s <= 2, first fails at s = 3


def b_cell(s):
    return min(comb(R + s, D + s), comb(R + s, s + 1))


assert b_cell(1) == 549756338176
assert b_cell(2) == 192154133857304576
assert b_cell(3) == 50372197381489643749376
assert B_STAR - b_cell(1) == 274980178355056911
assert B_STAR - b_cell(2) == 82826594254090511
assert b_cell(3) - B_STAR == 50371922400761532354289
assert b_cell(2) <= B_STAR < b_cell(3)

# 3. direction-separated boundary: J_13 < B_* < J_14


def j_s(s):
    prod = Fraction(1)
    for i in range(s + 1):
        prod *= Fraction(R + i, D + i)
    return prod.numerator // prod.denominator


assert j_s(13) == 47876303026096432
assert j_s(14) == 743896698428332665
assert j_s(13) < B_STAR < j_s(14)

# 4. Jo shortening-transfer wall at the first degree-drop core c = 4131
c = 4131
top, bot = comb(N, c), comb(M, c)
assert top > B_STAR * bot
mult = -((-top) // bot)  # ceil
assert mult.bit_length() == 3765
assert len(str(mult)) == 1134

# 5. staged shortening telescopes: the multiplier is invariant under staging
for c1 in (1, 64, 2048):
    c2 = c - c1
    staged = Fraction(comb(N, c1), comb(M, c1)) \
        * Fraction(comb(N - c1, c2), comb(M - c1, c2))
    assert staged == Fraction(top, bot)

print("KB_COMMON_CORE_STAIRCASE_WALLS_OK",
      "c_wall=4131", "s_cell_fail=3", "J13<B*<J14",
      "jo_bits=", mult.bit_length())
