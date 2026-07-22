#!/usr/bin/env python3
"""Mutation audit for the decorated shift-pair compiler."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            row["ordered_count"] == row["z"] * (row["z"] - 1),
            row["d"] == row["a"] - row["g"],
            row["w"] == row["a"] - row["k"],
            row["g"] <= row["k"] - 1,
            row["residual_degree"] <= row["d"] - row["w"] - 1,
            row["cross_coprime"] is True,
            row["e"] <= row["w"],
            row["primitive_multiplicity"] == 1,
            row["common_gcd_routed"] is True,
            row["support_pair_bound_proved"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "z": 5,
        "ordered_count": 20,
        "a": 10,
        "k": 6,
        "g": 5,
        "d": 5,
        "w": 4,
        "residual_degree": 0,
        "cross_coprime": True,
        "e": 4,
        "primitive_multiplicity": 1,
        "common_gcd_routed": True,
        "support_pair_bound_proved": False,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "ordered_count": 10,
        "d": 4,
        "w": 3,
        "g": 6,
        "residual_degree": 1,
        "cross_coprime": False,
        "e": 5,
        "primitive_multiplicity": 2,
        "common_gcd_routed": False,
        "support_pair_bound_proved": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_GROWING_COFACTOR_DECORATED_SHIFT_PAIR_COMPILER_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
