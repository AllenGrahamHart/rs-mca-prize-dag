#!/usr/bin/env python3
"""Independent audit of the profile-(4,4) local-norm route fence."""

from collections import Counter
from itertools import combinations


B_PRIZE = 317494674775468773183020924238786383963
VALUATIONS = (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 16, 17, 18, 20)
EXPECTED_BY_MU = (533, 285, 155, 78, 42, 23, 4, 4, 3, 2, 1, 1, 1, 1)


def expansion_mask(exponent: int) -> int:
    mask = 0
    submask = exponent
    while True:
        mask |= 1 << submask
        if submask == 0:
            return mask
        submask = (submask - 1) & exponent


def multiplicity(support: tuple[int, ...]) -> int:
    polynomial = 0
    for exponent in support:
        polynomial ^= expansion_mask(exponent)
    return (polynomial & -polynomial).bit_length() - 1


def prime_factors(value: int) -> Counter[int]:
    factors: Counter[int] = Counter()
    divisor = 3
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] += 1
            value //= divisor
        divisor += 2
    if value > 1:
        factors[value] += 1
    return factors


def multiplicative_order(value: int) -> int:
    for order in (1, 2, 4, 8, 16, 32, 64):
        if pow(value, order, 256) == 1:
            return order
    raise AssertionError(value)


def main() -> None:
    multiplicities = set()
    for size in (2, 4):
        multiplicities.update(multiplicity(support) for support in combinations(range(32), size))
    assert tuple(sorted(value for value in multiplicities if value <= 20)) == VALUATIONS

    bound = 20**64 // (B_PRIZE << 128)
    assert bound == 1_707_433
    counts = Counter()
    survivors = set()
    pre_sieve = 0
    for mu in VALUATIONS:
        maximum_odd = bound >> mu
        for odd in range(1, maximum_odd + 1, 256):
            pre_sieve += 1
            factors = prime_factors(odd)
            if all(exponent % multiplicative_order(prime) == 0
                   for prime, exponent in factors.items()):
                cofactor = odd << mu
                survivors.add(cofactor)
                counts[mu] += 1

    assert pre_sieve == 6622
    assert len(survivors) == 1133
    assert tuple(counts[mu] for mu in VALUATIONS) == EXPECTED_BY_MU
    assert all((1 << mu) in survivors for mu in VALUATIONS)
    print("E1_PROFILE44_LOCAL_NORM_ROUTE_FENCE_AUDIT_PASS")


if __name__ == "__main__":
    main()
