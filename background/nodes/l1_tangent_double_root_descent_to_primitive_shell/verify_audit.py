#!/usr/bin/env python3
"""Mutation audit for exact tangent descent."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            row["uses_exact_gcd"] is True,
            row["uses_d_squared"] is True,
            row["n_prime"] == row["n"] - row["r"],
            row["k_prime"] == row["k"] - 2 * row["r"],
            row["a_prime"] == row["a"] - row["r"],
            row["e_prime"] == row["e"] - row["r"],
            row["w_prime"] == row["w"] + row["r"],
            row["reduced_primitive"] is True,
            row["punctured_smooth"] is False,
            row["owner_sum_closed"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "uses_exact_gcd": True,
        "uses_d_squared": True,
        "n": 20,
        "k": 10,
        "a": 13,
        "e": 5,
        "w": 3,
        "r": 2,
        "n_prime": 18,
        "k_prime": 6,
        "a_prime": 11,
        "e_prime": 3,
        "w_prime": 5,
        "reduced_primitive": True,
        "punctured_smooth": False,
        "owner_sum_closed": False,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "uses_exact_gcd": False,
        "uses_d_squared": False,
        "n_prime": 17,
        "k_prime": 8,
        "a_prime": 12,
        "e_prime": 4,
        "w_prime": 4,
        "reduced_primitive": False,
        "punctured_smooth": True,
        "owner_sum_closed": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_TANGENT_DOUBLE_ROOT_DESCENT_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
