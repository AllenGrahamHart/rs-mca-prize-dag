#!/usr/bin/env python3
"""Exact verifier for the generic PMA defect-four obstruction."""

from math import comb


def falling(value: int, count: int) -> int:
    out = 1
    for offset in range(count):
        out *= value - offset
    return out


def is_prime(value: int) -> bool:
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return value >= 2


def expectation_certificate() -> tuple[int, int, int, int]:
    n = 2**16
    k = n // 2
    core_size = k - 1
    length = n - k
    petals = length // 2
    q = 65537**2
    nonzero = q - 1
    hyperplanes = comb(length, 2) + length + 5

    assert n == 65536 and k == 32768 and is_prime(65537)
    assert (q - 1) % n == 0
    assert q > 2 * hyperplanes

    avoidance_numerator = nonzero - 6 - 2 * (petals - 6)
    assert avoidance_numerator > 0
    numerator = (
        comb(core_size, 4)
        * q**4
        * (q - hyperplanes)
        * 2**6
        * comb(petals, 6)
        * avoidance_numerator
    )
    denominator = falling(nonzero, 6) * (nonzero - 6)
    assert numerator > n**6 * denominator

    # Removing the exact defect-set multiplicity destroys the contradiction.
    mutant = numerator // comb(core_size, 4)
    assert mutant < n**6 * denominator
    return numerator // denominator, numerator.bit_length(), denominator.bit_length(), hyperplanes


def owner_geometry() -> tuple[int, int, int]:
    n = 2**16
    k = n // 2
    s_n = n // (32 * 16)
    support_size = k + 1
    eligible = [
        size
        for size in (2**power for power in range(17))
        if k - s_n <= size <= support_size + s_n
    ]
    assert eligible == [k]
    max_coset_hits = k // 2 + 6
    assert k - max_coset_hits > s_n
    assert support_size % 2 == 1
    assert 65537 % 2 == 1

    # Mutation: concentrating the core in one k-coset would enter the owner.
    concentrated_hits = k - 4 + 6
    assert k - min(k, concentrated_hits) <= s_n
    return s_n, max_coset_hits, support_size


def main() -> None:
    mean_floor, numerator_bits, denominator_bits, hyperplanes = expectation_certificate()
    s_n, max_coset_hits, support_size = owner_geometry()
    print(
        "PMA_D4_GENERIC_OBSTRUCTION_PASS "
        f"mean_floor_bits={mean_floor.bit_length()} n6_bits={((2**16)**6).bit_length()} "
        f"numerator_bits={numerator_bits} denominator_bits={denominator_bits} "
        f"hyperplanes={hyperplanes} s_n={s_n} "
        f"max_coset_hits={max_coset_hits} support_size={support_size} mutations=2"
    )


if __name__ == "__main__":
    main()
