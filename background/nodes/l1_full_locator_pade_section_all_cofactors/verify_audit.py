#!/usr/bin/env python3
"""Mutation audit for the all-cofactor full-locator Pade section."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            row["d"] == row["e"] + row["w"],
            row["zero_equations"] == row["w"],
            row["full_locator_retained"] is True,
            row["reciprocal_continues_past_a"] is True,
            row["cofactor_recoverable"] is True,
            row["gcd_guard_retained"] is True,
            row["below_cap_size"] == row["q"] ** row["k"],
            row["above_cap_size_claimed"] is False,
            row["transversality_proved"] is False,
            row["formal_density_promoted"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "e": 7,
        "w": 4,
        "d": 11,
        "k": 6,
        "q": 17,
        "zero_equations": 4,
        "full_locator_retained": True,
        "reciprocal_continues_past_a": True,
        "cofactor_recoverable": True,
        "gcd_guard_retained": True,
        "below_cap_size": 24137569,
        "above_cap_size_claimed": False,
        "transversality_proved": False,
        "formal_density_promoted": False,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "d": 10,
        "zero_equations": 3,
        "full_locator_retained": False,
        "reciprocal_continues_past_a": False,
        "cofactor_recoverable": False,
        "gcd_guard_retained": False,
        "below_cap_size": 24137568,
        "above_cap_size_claimed": True,
        "transversality_proved": True,
        "formal_density_promoted": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_FULL_LOCATOR_PADE_SECTION_ALL_COFACTORS_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
