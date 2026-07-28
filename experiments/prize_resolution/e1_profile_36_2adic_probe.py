#!/usr/bin/env python3
"""Enumerate the low 2-adic multiplicities for six odd coefficients."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


LIMIT = 2013
B_PRIZE = 317494674775468773183020924238786383963


def multiplicity_at_one(residues: tuple[int, ...]) -> int:
    """Return ord_(X+1) of sum X^r over F_2, for residues below 16."""
    for derivative in range(16):
        if sum(comb(r, derivative) for r in residues) % 2:
            return derivative
    return 16


def admissible_cofactors(multiplicities: set[int]) -> list[int]:
    values = set()
    for mu in multiplicities:
        if not 1 <= mu <= 10:
            continue
        odd = 1
        while (1 << mu) * odd <= LIMIT:
            values.add((1 << mu) * odd)
            odd += 256
    # The residue-degree rule excludes 1026=2*3^3*19.
    values.discard(1026)
    return sorted(values)


def taylor_lower(x: Fraction, degree: int) -> Fraction:
    return sum(x**j / factorial(j) for j in range(degree + 1))


def taylor_upper(x: Fraction, degree: int) -> Fraction:
    lower = taylor_lower(x, degree)
    next_term = x ** (degree + 1) / factorial(degree + 1)
    ratio = x / (degree + 2)
    assert ratio < 1
    return lower + next_term / (1 - ratio)


def variance_windows(cofactors: list[int]) -> dict[int, tuple[int, int, int]]:
    windows = {}
    for cofactor in cofactors:
        target = Fraction(18**64, cofactor * B_PRIZE * 2**128)
        for variance in range(4, 2269, 2):
            x = Fraction(8 * variance, 405)
            lower_degree = next(
                (
                    degree
                    for degree in range(0, 80)
                    if taylor_lower(x, degree) > target
                ),
                None,
            )
            if lower_degree is None:
                continue
            previous = variance - 2
            previous_x = Fraction(8 * previous, 405)
            upper_degree = next(
                degree
                for degree in range(max(0, previous_x.numerator // previous_x.denominator), 100)
                if previous_x < degree + 2
                and taylor_upper(previous_x, degree) <= target
            )
            windows[cofactor] = (variance, lower_degree, upper_degree)
            break
    return windows


def main() -> None:
    counts: Counter[tuple[int, int]] = Counter()
    witnesses: dict[int, tuple[int, ...]] = {}
    multiplicities = set()

    # Modulo (X+1)^16, X^16=1. Six distinct exponents therefore leave an
    # even parity support of size 0, 2, 4, or 6 in Z/16Z. The zero support
    # has multiplicity at least 16 and is recorded separately.
    counts[(0, 16)] = 1
    multiplicities.add(16)
    witnesses[16] = ()
    for weight in (2, 4, 6):
        for residues in combinations(range(16), weight):
            mu = multiplicity_at_one(residues)
            counts[(weight, mu)] += 1
            multiplicities.add(mu)
            witnesses.setdefault(mu, residues)

    low = sorted(mu for mu in multiplicities if mu <= 10)
    high = sorted(mu for mu in multiplicities if mu > 10)
    cofactors = admissible_cofactors(multiplicities)
    windows = variance_windows(cofactors)

    print(f"low_multiplicities={low}")
    print(f"high_multiplicities={high}")
    print(f"cofactors={cofactors}")
    for cofactor, (onset, lower_degree, upper_degree) in windows.items():
        print(
            f"window m={cofactor}: onset={onset} "
            f"lower_degree={lower_degree} previous_upper_degree={upper_degree}"
        )
    for mu in sorted(witnesses):
        print(f"witness mu={mu}: {witnesses[mu]}")
    for key in sorted(counts):
        print(f"count parity_weight={key[0]} mu={key[1]}: {counts[key]}")

    assert low == [1, 2, 3, 4, 5, 6, 8, 9, 10]
    assert cofactors == [2, 4, 8, 16, 32, 64, 256, 512, 514, 1024, 1028, 1538]
    print("E1_PROFILE_36_2ADIC_PROBE_PASS")


if __name__ == "__main__":
    main()
