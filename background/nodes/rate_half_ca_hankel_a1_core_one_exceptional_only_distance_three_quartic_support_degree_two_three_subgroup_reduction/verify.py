#!/usr/bin/env python3
"""Exact checks for the quartic degree-two/three subgroup reduction."""

from __future__ import annotations

import runpy
from pathlib import Path


SOURCE = (
    Path(__file__).resolve().parents[1]
    / "rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_official_trigonal_subgroup_exclusion"
    / "verify.py"
)


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def normal_form_choice(
    leading: tuple[int, int],
    constant: tuple[int, int],
    prime: int,
) -> tuple[tuple[int, int], tuple[int, int]]:
    choices = [
        (left, right)
        for left in range(prime)
        for right in range(prime)
        if left or right
    ]
    r = next(
        pair
        for pair in choices
        if (pair[0] * leading[0] + pair[1] * leading[1]) % prime == 0
    )
    s = next(
        pair
        for pair in choices
        if (pair[0] * leading[0] + pair[1] * leading[1]) % prime
        and (pair[0] * constant[0] + pair[1] * constant[1]) % prime
        and (pair[0] * r[1] - pair[1] * r[0]) % prime
    )
    return s, r


def check_normal_forms() -> int:
    prime = 5
    nonzero = [
        (left, right)
        for left in range(prime)
        for right in range(prime)
        if left or right
    ]
    checks = 0
    for leading in nonzero:
        for constant in nonzero:
            s, r = normal_form_choice(leading, constant, prime)
            need((r[0] * leading[0] + r[1] * leading[1]) % prime == 0,
                 "denominator leading term did not cancel")
            need((s[0] * leading[0] + s[1] * leading[1]) % prime != 0,
                 "numerator lost cubic degree")
            need((s[0] * constant[0] + s[1] * constant[1]) % prime != 0,
                 "numerator constant term vanished")
            need((s[0] * r[1] - s[1] * r[0]) % prime != 0,
                 "target transformation became singular")
            checks += 1
    return checks


def main() -> None:
    # Replay the coefficient, corner, torus-change, and graph classifier used
    # by the general cubic normal form.
    source = runpy.run_path(str(SOURCE))
    source["main"]()

    n_value = 1 << 41
    e_value = (1 << 38) - 1
    degree_two_pairs = e_value - 40
    degree_three_pairs = e_value - 85
    need(
        32**3 * n_value**2 < (2 * degree_two_pairs) ** 3,
        "degree-two graph margin failed",
    )
    need(
        1440**3 * n_value**2 < (2 * degree_three_pairs) ** 3,
        "degree-three irreducible margin failed",
    )
    need(
        32**3 * n_value**2 < degree_three_pairs**3,
        "degree-three graph margin failed",
    )
    need(pow(2, 41, 3) == 2, "power-two subgroup unexpectedly has 3-torsion")

    normal_forms = check_normal_forms()
    print(
        "RATE_HALF_DISTANCE_THREE_QUARTIC_SUPPORT_DEGREE_TWO_THREE_PASS "
        f"degree_two_pairs={degree_two_pairs} "
        f"degree_three_pairs={degree_three_pairs} normal_forms={normal_forms} "
        "degree_three_excluded=True degree_two_tail=40"
    )


if __name__ == "__main__":
    main()
