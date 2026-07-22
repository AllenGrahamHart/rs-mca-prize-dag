#!/usr/bin/env python3
"""Mutation audit for root-free rational-Q projective packing."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            row["nonempty"] is True,
            row["projective_dimension"] == row["d"],
            row["codimension"] == row["w"],
            row["gcd_trivial"] is True,
            row["infinity_split"] == 0,
            row["full_intersection"] is True,
            row["max_pair_intersection"] <= row["d"] - 1,
            row["count"] <= row["packing_bound"],
            row["fixed_d_paid"] is True,
            row["sublinear_d_subexponential"] is True,
            row["linear_d_paid"] is False,
            row["reserve_condition_retained"] is True,
            row["average_normalized"] is False,
            row["finite_reserve_fit"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "d": 2,
        "w": 5,
        "nonempty": True,
        "projective_dimension": 2,
        "codimension": 5,
        "gcd_trivial": True,
        "infinity_split": 0,
        "full_intersection": True,
        "max_pair_intersection": 1,
        "count": 10,
        "packing_bound": 10,
        "fixed_d_paid": True,
        "sublinear_d_subexponential": True,
        "linear_d_paid": False,
        "reserve_condition_retained": True,
        "average_normalized": False,
        "finite_reserve_fit": False,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "projective_dimension": 3,
        "codimension": 4,
        "gcd_trivial": False,
        "infinity_split": 1,
        "full_intersection": False,
        "max_pair_intersection": 2,
        "count": 11,
        "fixed_d_paid": False,
        "sublinear_d_subexponential": False,
        "linear_d_paid": True,
        "reserve_condition_retained": False,
        "average_normalized": True,
        "finite_reserve_fit": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_ROOTFREE_RATIONAL_Q_PROJECTIVE_PACKING_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
