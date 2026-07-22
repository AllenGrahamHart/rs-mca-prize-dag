#!/usr/bin/env python3
"""Mutation audit for cofactor-depth accounting and scope guards."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            row["e"] < row["k"],
            row["d"] == row["w"] + row["e"],
            row["cofactor_count"] == row["q"] ** row["e"],
            row["ambient_cancels"] is True,
            row["image_factor_retained"] is True,
            row["integer_loss_lt_qe"] is True,
            row["depth_uniform_q_proved"] is False,
            row["f2_ladder_is_depth_transfer"] is False,
            row["e_ge_k_paid"] is False,
            row["route_fence_is_counterexample"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "e": 3,
        "k": 6,
        "w": 4,
        "d": 7,
        "q": 17,
        "cofactor_count": 4913,
        "ambient_cancels": True,
        "image_factor_retained": True,
        "integer_loss_lt_qe": True,
        "depth_uniform_q_proved": False,
        "f2_ladder_is_depth_transfer": False,
        "e_ge_k_paid": False,
        "route_fence_is_counterexample": False,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "e": 6,
        "d": 6,
        "cofactor_count": 4912,
        "ambient_cancels": False,
        "image_factor_retained": False,
        "integer_loss_lt_qe": False,
        "depth_uniform_q_proved": True,
        "f2_ladder_is_depth_transfer": True,
        "e_ge_k_paid": True,
        "route_fence_is_counterexample": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_COFACTOR_DEPTH_BUDGET_CANCELLATION_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
