#!/usr/bin/env python3
"""Mutation audit for the deep exact-shell Johnson closure."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    denominator = row["m"] ** 2 - row["n"] * (row["k"] - 1)
    return all(
        (
            2 * row["m"] > row["n"] + row["k"] - 1,
            denominator > 0,
            row["pair_intersection"] == row["k"] - 1,
            row["tail_charged_once"] is True,
            row["tail_bound"] == row["n"] ** 2,
            row["field_independent"] is True,
            row["band_closed"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "n": 20,
        "k": 8,
        "m": 14,
        "pair_intersection": 7,
        "tail_charged_once": True,
        "tail_bound": 400,
        "field_independent": True,
        "band_closed": False,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "m": 13,
        "pair_intersection": 8,
        "tail_charged_once": False,
        "tail_bound": 8000,
        "field_independent": False,
        "band_closed": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_DEEP_EXACT_SHELL_JOHNSON_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
