#!/usr/bin/env python3
"""Mutation audit for the received-word barycentric Q scope fence."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            row["a"] > row["k"],
            row["moment_count"] == row["a"] - row["k"],
            row["complete_locator_derivative"] is True,
            row["zero_equivalence"] is True,
            row["same_locator_prefix"] is True,
            row["different_received_prefix"] is True,
            row["exchange_defect"] != 0,
            row["exact_shell_visible"] is True,
            row["direct_q_import"] is False,
            row["nonlinear_transport_excluded"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "a": 3,
        "k": 2,
        "moment_count": 1,
        "complete_locator_derivative": True,
        "zero_equivalence": True,
        "same_locator_prefix": True,
        "different_received_prefix": True,
        "exchange_defect": 4,
        "exact_shell_visible": True,
        "direct_q_import": False,
        "nonlinear_transport_excluded": False,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "a": 2,
        "moment_count": 2,
        "complete_locator_derivative": False,
        "zero_equivalence": False,
        "same_locator_prefix": False,
        "different_received_prefix": False,
        "exchange_defect": 0,
        "exact_shell_visible": False,
        "direct_q_import": True,
        "nonlinear_transport_excluded": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_RECEIVED_WORD_BARYCENTRIC_Q_SCOPE_FENCE_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
