#!/usr/bin/env python3
"""Mutation audit for the tangent Hasse root-pinning census."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            row["double_root_iff"] is True,
            row["hasse_characteristic_safe"] is True,
            row["rank"] == min(row["k"], 2 * row["r"]),
            row["fiber_exponent"] == max(row["k"] - 2 * row["r"], 0),
            row["exact_gcd_owner"] is True,
            row["subset_overcount"] is False,
            row["full_rank"] == row["a"] - row["r"],
            row["pade_corank"] <= min(row["w"], row["r"]),
            row["raw_sum_is_row_sharp"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "double_root_iff": True,
        "hasse_characteristic_safe": True,
        "k": 7,
        "r": 2,
        "rank": 4,
        "fiber_exponent": 3,
        "exact_gcd_owner": True,
        "subset_overcount": False,
        "a": 9,
        "full_rank": 7,
        "w": 5,
        "pade_corank": 2,
        "raw_sum_is_row_sharp": False,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "double_root_iff": False,
        "hasse_characteristic_safe": False,
        "rank": 5,
        "fiber_exponent": 2,
        "exact_gcd_owner": False,
        "subset_overcount": True,
        "full_rank": 8,
        "pade_corank": 3,
        "raw_sum_is_row_sharp": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_TANGENT_HASSE_ROOT_PINNING_CENSUS_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
