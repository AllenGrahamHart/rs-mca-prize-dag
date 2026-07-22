#!/usr/bin/env python3
"""Mutation audit for the exact-shell prefix/Hankel bridge contract."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            row["a"] > row["k"],
            row["w"] == row["a"] - row["k"],
            row["xsize"] == row["d"] + row["w"] + 1,
            row["prefix_count"] == row["w"],
            row["local_count"] == row["w"],
            row["monic_diagonal"] is True,
            row["exact_core_guard"] is True,
            row["exact_noncore_guard"] is True,
            row["raw_subsupports_removed"] is True,
            row["toy_q_auto_consumed"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "a": 9,
        "k": 5,
        "w": 4,
        "d": 3,
        "xsize": 8,
        "prefix_count": 4,
        "local_count": 4,
        "monic_diagonal": True,
        "exact_core_guard": True,
        "exact_noncore_guard": True,
        "raw_subsupports_removed": True,
        "toy_q_auto_consumed": False,
    }
    assert valid(row)
    mutations = {
        "a": 5,
        "w": 3,
        "xsize": 7,
        "prefix_count": 3,
        "local_count": 3,
        "monic_diagonal": False,
        "exact_core_guard": False,
        "exact_noncore_guard": False,
        "raw_subsupports_removed": False,
        "toy_q_auto_consumed": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_EXACT_SHELL_PREFIX_HANKEL_BRIDGE_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
