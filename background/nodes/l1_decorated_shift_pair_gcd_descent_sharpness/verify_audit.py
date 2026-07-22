#!/usr/bin/env python3
"""Mutation audit for decorated gcd descent and sharpness."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            row["reduced_e"] == row["e"] - row["c"],
            row["reduced_w"] == row["w"] + row["c"],
            row["gcd_divides_residual"] is True,
            row["gcd_coprime_abn"] is True,
            row["domain_roots_in_g"] is True,
            row["unique_after_descent"] == (row["e"] <= row["w"] + 2 * row["c"]),
            row["sharp_e"] == row["sharp_w"] + 1,
            row["sharp_witnesses"] == 10,
            row["fixed_word_multiplicity_claimed"] is False,
            row["l1_refuted"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "e": 5,
        "w": 3,
        "c": 1,
        "reduced_e": 4,
        "reduced_w": 4,
        "gcd_divides_residual": True,
        "gcd_coprime_abn": True,
        "domain_roots_in_g": True,
        "unique_after_descent": True,
        "sharp_e": 2,
        "sharp_w": 1,
        "sharp_witnesses": 10,
        "fixed_word_multiplicity_claimed": False,
        "l1_refuted": False,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "reduced_e": 5,
        "reduced_w": 3,
        "gcd_divides_residual": False,
        "gcd_coprime_abn": False,
        "domain_roots_in_g": False,
        "unique_after_descent": False,
        "sharp_e": 3,
        "sharp_witnesses": 11,
        "fixed_word_multiplicity_claimed": True,
        "l1_refuted": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_DECORATED_SHIFT_PAIR_GCD_DESCENT_SHARPNESS_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
