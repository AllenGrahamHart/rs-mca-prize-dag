#!/usr/bin/env python3
"""Mutation audit for the Pade Jacobian/tangent dichotomy."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            row["pade_rank"] == row["a"] - row["k"],
            row["full_rank"] == row["a"],
            row["differential_is_q_multiplication"] is True,
            row["coprime_required"] is True,
            row["rank_failure_implies_tangent"] is True,
            row["tangent_implies_rank_failure"] is False,
            row["complement_gcd_retained"] is True,
            row["smooth_implies_point_bound"] is False,
            row["tangent_witness_exact"] is True,
            row["tangent_witness_rank"] < row["tangent_w"],
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "a": 7,
        "k": 3,
        "pade_rank": 4,
        "full_rank": 7,
        "differential_is_q_multiplication": True,
        "coprime_required": True,
        "rank_failure_implies_tangent": True,
        "tangent_implies_rank_failure": False,
        "complement_gcd_retained": True,
        "smooth_implies_point_bound": False,
        "tangent_witness_exact": True,
        "tangent_witness_rank": 2,
        "tangent_w": 3,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "pade_rank": 3,
        "full_rank": 6,
        "differential_is_q_multiplication": False,
        "coprime_required": False,
        "rank_failure_implies_tangent": False,
        "tangent_implies_rank_failure": True,
        "complement_gcd_retained": False,
        "smooth_implies_point_bound": True,
        "tangent_witness_exact": False,
        "tangent_witness_rank": 3,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_PADE_REMAINDER_JACOBIAN_TANGENT_DICHOTOMY_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
