#!/usr/bin/env python3
"""Exact official incidence checks for the aligned Pade residual."""

from __future__ import annotations


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def aligned_lower(e: int, tail: int, orbit_count: int, h: int) -> int:
    block_rows = 2 * e + 1
    numerator = h * (orbit_count - block_rows) - 2 * tail * orbit_count
    denominator = h - 2 * tail
    return (numerator + denominator - 1) // denominator


def branch(
    e: int,
    tail: int,
    orbit_loss: int,
    class_lower: int,
    alignment_loss: int,
) -> tuple[int, int, int, int]:
    orbit_count = 3 * e - orbit_loss
    first_aligned = aligned_lower(e, tail, orbit_count, class_lower)
    first_cap = 2 * (3 * e - class_lower) // first_aligned
    near_full_aligned = aligned_lower(e, tail, orbit_count, e - 6)
    second_cap = 2 * (3 * e - (e - 6)) // near_full_aligned
    final_aligned = aligned_lower(e, tail, orbit_count, e - 4)
    need(first_cap <= 6, "first incidence pass did not reach degree six")
    need(second_cap <= 4, "second incidence pass did not reach degree four")
    need(final_aligned >= e - alignment_loss, "alignment count drifted")
    return first_aligned, first_cap, second_cap, e - final_aligned


def main() -> None:
    e = 2**38 - 1
    antipodal = branch(e, 6, 8, 172410, 33)
    reciprocal = branch(e, 8, 11, 2128, 44)
    need(antipodal[3] == 33, "antipodal exact alignment loss drifted")
    need(reciprocal[3] == 44, "reciprocal exact alignment loss drifted")
    print(
        "RATE_HALF_DISTANCE_THREE_PADE_ALIGNED_RESIDUAL_PASS "
        f"antipodal={antipodal} reciprocal={reciprocal} degree_range=1..4"
    )


if __name__ == "__main__":
    main()
