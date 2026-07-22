#!/usr/bin/env python3
"""Mutation audit for the XR P-A top-level claim contract."""

from __future__ import annotations


def valid(row: dict[str, int | bool | str | tuple[int, ...]]) -> bool:
    return all(
        (
            row["status"] == "TARGET",
            row["currency"] == "distinct_slopes",
            row["a1_budget_factor"] == 8,
            row["a2_budget_factor"] == 16,
            row["a2_combined"] is True,
            row["moment_is_target"] is False,
            row["a1_open"] == (5, 5, 5, 17, 17, 15),
            row["a2_open"] == (5, 4, 4, 4, 4, 4),
            row["p_a1_proved"] is False,
            row["p_a2_proved"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool | str | tuple[int, ...]] = {
        "status": "TARGET",
        "currency": "distinct_slopes",
        "a1_budget_factor": 8,
        "a2_budget_factor": 16,
        "a2_combined": True,
        "moment_is_target": False,
        "a1_open": (5, 5, 5, 17, 17, 15),
        "a2_open": (5, 4, 4, 4, 4, 4),
        "p_a1_proved": False,
        "p_a2_proved": False,
    }
    if not valid(row):
        raise AssertionError("control rejected")
    mutations: dict[str, int | bool | str | tuple[int, ...]] = {
        "status": "PROVED",
        "currency": "collision_moment",
        "a1_budget_factor": 16,
        "a2_budget_factor": 8,
        "a2_combined": False,
        "moment_is_target": True,
        "a1_open": (5, 5, 5, 12, 12, 11),
        "a2_open": (5, 5, 5, 5, 5, 5),
        "p_a1_proved": True,
        "p_a2_proved": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    if caught != len(mutations):
        raise AssertionError((caught, len(mutations)))
    print(f"XR_HIGHCORE_COLLISION_COUNT_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
