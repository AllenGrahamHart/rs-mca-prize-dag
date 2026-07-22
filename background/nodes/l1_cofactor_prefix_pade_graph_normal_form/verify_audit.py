#!/usr/bin/env python3
"""Mutation audit for the cofactor-prefix Pade graph normal form."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            row["e"] < row["k"],
            row["d"] == row["w"] + row["e"],
            row["graph_size"] == row["q"] ** row["e"],
            row["free_coordinates"] == row["e"],
            row["dependent_coordinates"] == row["w"],
            row["cofactor_recoverable"] is True,
            row["distinct_targets"] is True,
            row["gcd_guard_retained"] is True,
            row["transversality_proved"] is False,
            row["e_ge_k_paid"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "e": 3,
        "k": 6,
        "w": 4,
        "d": 7,
        "q": 17,
        "graph_size": 4913,
        "free_coordinates": 3,
        "dependent_coordinates": 4,
        "cofactor_recoverable": True,
        "distinct_targets": True,
        "gcd_guard_retained": True,
        "transversality_proved": False,
        "e_ge_k_paid": False,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "e": 6,
        "d": 6,
        "graph_size": 4912,
        "free_coordinates": 4,
        "dependent_coordinates": 3,
        "cofactor_recoverable": False,
        "distinct_targets": False,
        "gcd_guard_retained": False,
        "transversality_proved": True,
        "e_ge_k_paid": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_COFACTOR_PREFIX_PADE_GRAPH_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
