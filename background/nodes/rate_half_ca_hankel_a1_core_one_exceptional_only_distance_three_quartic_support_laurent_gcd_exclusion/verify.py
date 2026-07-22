#!/usr/bin/env python3
"""Exact margins for the Laurent-end Corvaja--Zannier exclusion."""

from __future__ import annotations


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    n_value = 1 << 41
    e_value = (1 << 38) - 1
    p_floor = 1 << 167
    ordered = 2 * (e_value - 148)
    genus_bound = 4
    support_bound = 12
    chi_bound = support_bound + 2 * genus_bound - 2
    need(chi_bound == 18, "Euler-characteristic ledger changed")

    first_cube_constant = 27 * (2 * 3 * 3 * chi_bound)
    need(first_cube_constant == 27 * 324, "gcd first-term constant changed")
    need(
        first_cube_constant * n_value**2 < ordered**3,
        "Corvaja--Zannier first term missed the official margin",
    )
    need(
        108 * n_value**2 < p_floor * ordered,
        "Corvaja--Zannier characteristic term missed the official margin",
    )
    need(n_value % 2 == 0 and p_floor > n_value, "differential guard failed")

    support = {(3, 1), (2, 2), (1, 3), (2, 1), (1, 2), (1, 1), (0, 0)}
    anchor = (0, 0)
    need(
        any(
            left[0] * right[1] != left[1] * right[0]
            for left in support
            for right in support
            if left != anchor and right != anchor
        ),
        "Laurent support became one-dimensional",
    )
    print(
        "RATE_HALF_DISTANCE_THREE_QUARTIC_SUPPORT_LAURENT_GCD_PASS "
        f"genus_bound={genus_bound} support_bound={support_bound} "
        f"chi_bound={chi_bound} first_cube_constant={first_cube_constant} "
        "characteristic_coefficient=108 laurent_branch_excluded=True"
    )


if __name__ == "__main__":
    main()
