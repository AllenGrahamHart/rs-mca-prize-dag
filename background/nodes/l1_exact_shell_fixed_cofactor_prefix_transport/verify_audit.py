#!/usr/bin/env python3
"""Mutation audit for fixed-cofactor locator-prefix transport."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            row["a"] <= row["h"],
            row["e"] == row["h"] - row["a"],
            row["w"] == row["a"] - row["k"],
            row["depth"] == min(row["a"], row["w"] + row["e"]),
            row["leading_cofactor_fixed"] is True,
            row["cofactor_count"] == row["q"] ** row["e"],
            row["gcd_guard_retained"] is True,
            row["scalar_exactness_automatic"] is True,
            row["growing_e_paid"] is False,
            row["locator_q_proved"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "a": 10,
        "h": 13,
        "k": 6,
        "e": 3,
        "w": 4,
        "depth": 7,
        "q": 17,
        "cofactor_count": 4913,
        "leading_cofactor_fixed": True,
        "gcd_guard_retained": True,
        "scalar_exactness_automatic": True,
        "growing_e_paid": False,
        "locator_q_proved": False,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "a": 14,
        "e": 2,
        "w": 3,
        "depth": 6,
        "cofactor_count": 4912,
        "leading_cofactor_fixed": False,
        "gcd_guard_retained": False,
        "scalar_exactness_automatic": False,
        "growing_e_paid": True,
        "locator_q_proved": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_EXACT_SHELL_FIXED_COFACTOR_PREFIX_TRANSPORT_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
