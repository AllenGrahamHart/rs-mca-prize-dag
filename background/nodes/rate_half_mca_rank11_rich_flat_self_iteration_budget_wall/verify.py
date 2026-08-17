#!/usr/bin/env python3
"""Exact primary replay of the rich-flat self-iteration method wall."""

from math import comb

N, K, M = 2_097_152, 1_048_576, 1_116_048
A, C0 = 1_114_501, 131_850
LOW = 206_105_684_094_104_220
OUTSIDE = N - A
R1 = 8_147_918


def fall(x: int, r: int) -> int:
    out = 1
    for i in range(r):
        out *= x - i
    return out


def rq(q: int) -> int:
    if q == 1:
        return R1
    return OUTSIDE * (comb(N - K + q, q) // comb(A - K + q, q))


def charge(q: int, delta: int) -> int:
    p = 10 - q
    return (fall(M, p) // delta**p) * rq(q)


def two_rung(q: int) -> tuple[int, int, int]:
    return min(
        (charge(q, d) + charge(q + 1, C0 + 1 - d), d, C0 + 1 - d)
        for d in range(1, C0 + 1)
    )


assert [rq(q) // OUTSIDE for q in range(2, 11)] == [
    252, 4023, 63993, 1017785, 16187098,
    257439730, 4094265120, 65113370815, 1035519360730,
]
payable = [
    (C0 - d, d, charge(1, d) + charge(2, d))
    for d in range(1, C0 + 1)
    if charge(1, d) + charge(2, d) <= LOW
]
assert max(payable) == (42_452, 89_398, 206_103_676_871_467_496)
assert LOW - max(payable)[2] == 2_007_222_636_724
assert charge(1, 89_397) + charge(2, 89_397) - LOW == 17_108_854_816_460

one = two_rung(1)
two = two_rung(2)
assert one == (2_539_543_014_780_268_202, 64_305, 67_546)
assert two == (3_232_479_920_013_973_566, 66_671, 65_180)
assert one[0] - LOW == 2_333_437_330_686_163_982
assert two[0] - LOW == 3_026_374_235_919_869_346
print("RANK11_RICH_FLAT_SELF_ITERATION_WALL_OK", one[0], two[0])
