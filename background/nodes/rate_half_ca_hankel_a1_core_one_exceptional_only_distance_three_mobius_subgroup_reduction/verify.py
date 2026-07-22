#!/usr/bin/env python3
"""Exact arithmetic checks for the official Mobius subgroup reduction."""

from __future__ import annotations


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    n = 1 << 41
    e = (1 << 38) - 1
    ordered_pairs = 2 * e

    require(n > 100, "subgroup is below the theorem threshold")

    # N < p^(3/4)/3 for every p>2^167, checked without real arithmetic.
    require((3 * n) ** 4 < (1 << 167) ** 3, "curve-bound field margin failed")

    # Compare C*N^(2/3) with 2e by cubing both positive sides.
    require((32**3) * (n**2) < ordered_pairs**3, "curve bound does not exclude")
    require(32 * (1 << 28) < ordered_pairs, "coarse power-of-two margin failed")

    prime = 1009
    subgroup_order = 16
    generator = pow(11, (prime - 1) // subgroup_order, prime)
    subgroup = {pow(generator, index, prime) for index in range(subgroup_order)}
    require(len(subgroup) == subgroup_order, "toy subgroup has wrong order")

    antipodal = {(-x) % prime for x in subgroup}
    require(antipodal == subgroup, "antipodal involution left the subgroup")

    c = next(iter(subgroup))
    inversion = {c * pow(x, prime - 2, prime) % prime for x in subgroup}
    require(inversion == subgroup, "constant-product involution left the subgroup")

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_"
        "DISTANCE_THREE_MOBIUS_SUBGROUP_REDUCTION_PASS "
        f"N={n} ordered={ordered_pairs} general_lt_2^33=1 special=2"
    )


if __name__ == "__main__":
    main()
