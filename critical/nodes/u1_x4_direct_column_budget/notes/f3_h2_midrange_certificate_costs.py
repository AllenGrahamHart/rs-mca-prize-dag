#!/usr/bin/env python3
"""Exact h=2 finite-midrange certificate-cost table."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


ENERGY_CONSTANT_OPTIMIZED = 22111
THRESHOLD = Fraction(ENERGY_CONSTANT_OPTIMIZED, 8) ** 2
INTEGER_COVERAGE_START = THRESHOLD.numerator // THRESHOLD.denominator + 1
SHARD_UNIT = 2**26
OFFICIAL_EXPONENTS = range(13, 42)
FEASIBLE_SHARD_LIMIT = 2000


@dataclass(frozen=True)
class Row:
    exponent: int
    h: int
    ordered_differences: int
    shards: int
    status: str


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


def row_for_exponent(exponent: int) -> Row:
    h = 2**exponent
    ordered = h * (h - 1)
    shards = ceil_div(ordered, SHARD_UNIT)
    if h >= INTEGER_COVERAGE_START:
        status = "theorem"
    elif shards < FEASIBLE_SHARD_LIMIT:
        status = "feasible_exact_census"
    else:
        status = "residual_midrange"
    return Row(exponent, h, ordered, shards, status)


def main() -> None:
    rows = [row_for_exponent(exponent) for exponent in OFFICIAL_EXPONENTS]
    feasible = [row.exponent for row in rows if row.status == "feasible_exact_census"]
    residual = [row.exponent for row in rows if row.status == "residual_midrange"]
    theorem = [row.exponent for row in rows if row.status == "theorem"]

    expected_feasible = list(range(13, 19))
    expected_residual = list(range(19, 23))
    expected_theorem = list(range(23, 42))
    if feasible != expected_feasible:
        raise AssertionError(("feasible", feasible, expected_feasible))
    if residual != expected_residual:
        raise AssertionError(("residual", residual, expected_residual))
    if theorem != expected_theorem:
        raise AssertionError(("theorem", theorem, expected_theorem))

    print(f"optimized threshold = {THRESHOLD}")
    print(f"integer theorem coverage starts at h = {INTEGER_COVERAGE_START}")
    print(f"ordered-difference shard unit = {SHARD_UNIT}")
    print(" exp        h        ordered_differences   shards  status")
    for row in rows:
        print(
            f"{row.exponent:4d} {row.h:9d} {row.ordered_differences:26d}"
            f" {row.shards:8d}  {row.status}"
        )
    print("feasible exact-census exponents:", ",".join(map(str, feasible)))
    print("residual midrange exponents:", ",".join(map(str, residual)))
    print("theorem-covered exponents:", f"{theorem[0]}..{theorem[-1]}")
    print("H2_MIDRANGE_CERTIFICATE_COSTS_PASS")


if __name__ == "__main__":
    main()
