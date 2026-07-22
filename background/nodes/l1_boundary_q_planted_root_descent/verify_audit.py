#!/usr/bin/env python3
"""Mutation audit for the boundary-Q planted-root descent."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            row["determinant_identity"] is True,
            row["d_divides_n1"] is True,
            row["planted_in_every_support"] is True,
            row["planted_values_retained"] is True,
            row["residual_root_free"] is True,
            row["locator_drop"] == row["r"],
            row["dimension_drop"] == row["r"],
            row["depth_before"] == row["depth_after"],
            row["rigid_count"] <= 1,
            row["owner_subsets"] == 1,
            row["smoothness_claimed"] is False,
            row["standard_q_claimed"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "r": 3,
        "determinant_identity": True,
        "d_divides_n1": True,
        "planted_in_every_support": True,
        "planted_values_retained": True,
        "residual_root_free": True,
        "locator_drop": 3,
        "dimension_drop": 3,
        "depth_before": 7,
        "depth_after": 7,
        "rigid_count": 1,
        "owner_subsets": 1,
        "smoothness_claimed": False,
        "standard_q_claimed": False,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "determinant_identity": False,
        "d_divides_n1": False,
        "planted_in_every_support": False,
        "planted_values_retained": False,
        "residual_root_free": False,
        "locator_drop": 2,
        "dimension_drop": 2,
        "depth_after": 6,
        "rigid_count": 2,
        "owner_subsets": 8,
        "smoothness_claimed": True,
        "standard_q_claimed": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_BOUNDARY_Q_PLANTED_ROOT_DESCENT_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
