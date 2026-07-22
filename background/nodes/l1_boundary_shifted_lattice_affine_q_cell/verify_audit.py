#!/usr/bin/env python3
"""Mutation audit for the boundary affine Q cell."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            row["d1"] == row["w"] + 1,
            row["d2"] == row["omega"],
            row["b_degree"] == 0,
            row["a_degree"] == row["omega"] - row["w"] - 1,
            row["infinity_exact"] <= 1,
            row["affine_injective"] is True,
            row["guard_retained"] is True,
            row["w1_one_is_prefix"] is True,
            row["nonconstant_is_fixed_column"] is False,
            row["interior_included"] is False,
            row["q_bound_proved"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "w": 4,
        "omega": 9,
        "d1": 5,
        "d2": 9,
        "b_degree": 0,
        "a_degree": 4,
        "infinity_exact": 1,
        "affine_injective": True,
        "guard_retained": True,
        "w1_one_is_prefix": True,
        "nonconstant_is_fixed_column": False,
        "interior_included": False,
        "q_bound_proved": False,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "d1": 6,
        "d2": 8,
        "b_degree": 1,
        "a_degree": 5,
        "infinity_exact": 2,
        "affine_injective": False,
        "guard_retained": False,
        "w1_one_is_prefix": False,
        "nonconstant_is_fixed_column": True,
        "interior_included": True,
        "q_bound_proved": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_BOUNDARY_SHIFTED_LATTICE_AFFINE_Q_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
