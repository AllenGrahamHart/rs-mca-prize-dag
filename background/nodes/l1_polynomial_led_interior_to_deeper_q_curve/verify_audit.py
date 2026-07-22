#!/usr/bin/env python3
"""Mutation audit for polynomial-led interior deeper-Q decomposition."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            row["e"] >= 1,
            row["e"] <= row["k"],
            row["triangular_cofactor"] is True,
            row["recursive_locator"] is True,
            row["injective_curve"] is True,
            row["exact_union"] is True,
            row["guard_retained"] is True,
            row["ambient_cancels"] is True,
            row["additive_slices"] == row["base_power_e"],
            row["nonconstant_basis_claimed"] is False,
            row["above_cap_claimed"] is False,
            row["q_bound_proved"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "e": 2,
        "k": 5,
        "triangular_cofactor": True,
        "recursive_locator": True,
        "injective_curve": True,
        "exact_union": True,
        "guard_retained": True,
        "ambient_cancels": True,
        "additive_slices": 49,
        "base_power_e": 49,
        "nonconstant_basis_claimed": False,
        "above_cap_claimed": False,
        "q_bound_proved": False,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "e": 6,
        "triangular_cofactor": False,
        "recursive_locator": False,
        "injective_curve": False,
        "exact_union": False,
        "guard_retained": False,
        "ambient_cancels": False,
        "additive_slices": 48,
        "nonconstant_basis_claimed": True,
        "above_cap_claimed": True,
        "q_bound_proved": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_POLYNOMIAL_LED_INTERIOR_TO_DEEPER_Q_CURVE_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
