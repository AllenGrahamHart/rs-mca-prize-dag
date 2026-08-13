#!/usr/bin/env python3
"""Independent exact audit of the rank-10 threshold split."""

from fractions import Fraction
from math import comb, prod


N = 2097152
K = 1048576
M = 1116048
W = 67472
TAIL = N - M
NEAR = 2 * W
BUDGET = 274980728111395087
FIELD = 2130706433 ** 6


def ff(x: int, j: int) -> int:
    return prod(x - i for i in range(j))


def rr(x: int, j: int) -> int:
    return prod(x + i for i in range(j))


def transverse(rank: int, threshold: int) -> int:
    candidates = (
        Fraction(ff(N, rank + 1), M * threshold * rr(W + 1, rank - 1)),
        Fraction(ff(N - K + rank, rank + 1), threshold * rr(W + 1, rank)),
    )
    value = max(candidates)
    return value.numerator // value.denominator


def total(rank: int, threshold: int) -> tuple[int, int, int, int]:
    q = threshold - 1
    residual = W - q
    ordinary = comb(N - K + rank, rank) // comb(residual + rank, rank)
    high = max(
        N // threshold,
        *(transverse(r, threshold) for r in range(1, rank + 1)),
    )
    low = (TAIL + q) * ordinary
    return NEAR + high + low, high, low, ordinary


def main() -> None:
    expected = {
        15: 280660860122827119,
        16: 266373135875296370,
        666: 61871337525323046,
        667: 61871313426765543,
        668: 61871313610314122,
    }
    for threshold, value in expected.items():
        assert total(9, threshold)[0] == value
    optimum = min((total(9, threshold)[0], threshold)
                  for threshold in range(2, W + 1)
                  if total(9, threshold)[3] ** 2 < FIELD)
    assert optimum == (61871313426765543, 667)
    first = next(threshold for threshold in range(2, W + 1)
                 if total(9, threshold)[0] <= BUDGET)
    assert first == 16
    rank_ten = min((total(10, threshold)[0], threshold)
                   for threshold in range(2, W + 1)
                   if total(10, threshold)[3] ** 2 < FIELD)
    assert rank_ten == (1040506078215897711, 876)
    assert rank_ten[0] > BUDGET
    _, high, low, ordinary = total(9, 667)
    assert (high, low, ordinary) == (
        5143522968716559, 56727790457914040, 57781140652
    )
    assert BUDGET - optimum[0] == 213109414684629544
    print(
        "RATE_HALF_MCA_RANK10_MARGIN_INTERLEAVING_SPLIT_PAYMENT_AUDIT_PASS "
        "thresholds=5 optimum=667 first_pay=16 next_rank_unpaid=10"
    )


if __name__ == "__main__":
    main()
