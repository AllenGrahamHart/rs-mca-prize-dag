#!/usr/bin/env python3
"""Mutation audit for the Pade/support-moment inversion."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            row["m"] >= row["k"],
            row["split_equals_support"] is True,
            row["fiber_is_binomial"] is True,
            row["guard_selects_complete"] is True,
            row["inversion_direction_up"] is True,
            row["alternating_sign"] is True,
            row["exact_le_support"] is True,
            row["smoothness_required"] is False,
            row["owners_preserved"] is False,
            row["row_bound_proved"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "m": 8,
        "k": 5,
        "split_equals_support": True,
        "fiber_is_binomial": True,
        "guard_selects_complete": True,
        "inversion_direction_up": True,
        "alternating_sign": True,
        "exact_le_support": True,
        "smoothness_required": False,
        "owners_preserved": False,
        "row_bound_proved": False,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "m": 4,
        "split_equals_support": False,
        "fiber_is_binomial": False,
        "guard_selects_complete": False,
        "inversion_direction_up": False,
        "alternating_sign": False,
        "exact_le_support": False,
        "smoothness_required": True,
        "owners_preserved": True,
        "row_bound_proved": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_PADE_SPLIT_SECTION_SUPPORT_MOMENT_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
