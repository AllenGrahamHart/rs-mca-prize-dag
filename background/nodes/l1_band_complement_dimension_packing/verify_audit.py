#!/usr/bin/env python3
"""Mutation audit for L1 band complement-dimension packing."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            row["band"] is True,
            row["s"] >= 1,
            row["vector_dimension"] == row["s"] + 1,
            row["projective_dimension"] == row["s"],
            row["first_coordinate_injective"] is True,
            row["complete_supports"] is True,
            row["max_complement_intersection"] <= row["s"] - 1,
            row["count"] <= row["packing_bound"],
            row["sublinear_subexponential"] is True,
            row["reserve_condition_retained"] is True,
            row["linear_s_paid"] is False,
            row["deep_double_charged"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "band": True,
        "s": 3,
        "vector_dimension": 4,
        "projective_dimension": 3,
        "first_coordinate_injective": True,
        "complete_supports": True,
        "max_complement_intersection": 2,
        "count": 9,
        "packing_bound": 9,
        "sublinear_subexponential": True,
        "reserve_condition_retained": True,
        "linear_s_paid": False,
        "deep_double_charged": False,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "band": False,
        "s": 0,
        "vector_dimension": 3,
        "projective_dimension": 4,
        "first_coordinate_injective": False,
        "complete_supports": False,
        "max_complement_intersection": 3,
        "count": 10,
        "sublinear_subexponential": False,
        "reserve_condition_retained": False,
        "linear_s_paid": True,
        "deep_double_charged": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_BAND_COMPLEMENT_DIMENSION_PACKING_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
