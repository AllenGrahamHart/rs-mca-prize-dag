#!/usr/bin/env python3
"""Mutation audit for the balanced shifted-lattice reduction."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            2 * row["m"] <= row["n"] + row["k"] - 1,
            row["omega"] == row["n"] - row["m"],
            row["w"] == row["m"] - row["k"],
            row["degree_sum"] == row["n"] - row["k"] + 1,
            row["near_exact_empty"] is True,
            row["near_support_empty"] is False,
            row["near_agreement"] >= row["m"] + 1,
            row["balanced_min"] == row["w"] + 1,
            row["pencil_dimension"] == row["omega"] - row["w"] + 1,
            row["guard_retained"] is True,
            row["row_bound_proved"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "n": 20,
        "k": 8,
        "m": 13,
        "omega": 7,
        "w": 5,
        "degree_sum": 13,
        "near_exact_empty": True,
        "near_support_empty": False,
        "near_agreement": 14,
        "balanced_min": 6,
        "pencil_dimension": 3,
        "guard_retained": True,
        "row_bound_proved": False,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "m": 14,
        "omega": 8,
        "w": 4,
        "degree_sum": 12,
        "near_exact_empty": False,
        "near_support_empty": True,
        "near_agreement": 13,
        "balanced_min": 5,
        "pencil_dimension": 2,
        "guard_retained": False,
        "row_bound_proved": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_EXACT_SHELL_BALANCED_LATTICE_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
