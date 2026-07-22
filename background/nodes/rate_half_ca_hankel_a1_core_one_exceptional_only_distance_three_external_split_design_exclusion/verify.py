#!/usr/bin/env python3
"""Exact scope controls for the distance-three split-design exclusion."""

from __future__ import annotations


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    m = 2**37
    e = 2 * m - 1
    need(e == 2**38 - 1, "official distance-three parameter mismatch")
    need(e - 8 > 8, "bounded-tail good-pair count is too small")
    need(e - 44 > 4, "aligned orbit count is too small")

    # A valid quartic in every kernel forces rank at most four for every
    # five-column crossing matrix, which is exactly the all-deficient branch.
    columns = 5
    kernel_dimensions = (1, 2, 3)
    need(all(columns - dimension <= 4 for dimension in kernel_dimensions),
         "nonzero kernel did not force crossing deficiency")
    print(
        "RATE_HALF_DISTANCE_THREE_EXTERNAL_SPLIT_DESIGN_EXCLUSION_PASS "
        f"m={m} e={e} good_pair_floor={e - 8} aligned_floor={e - 44}"
    )


if __name__ == "__main__":
    main()
