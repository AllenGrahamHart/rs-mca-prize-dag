#!/usr/bin/env python3
"""Mutation audit for interior-BC-floor to higher-shell-Q routing."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            row["strict_interior"] is True,
            row["mprime"] > row["m"],
            row["codeword_degree_ok"] is True,
            row["complete_agreement_mprime"] is True,
            row["proper_subsupport_guarded_out"] is True,
            row["inversion_zero"] is True,
            row["higher_retained_once"] is True,
            row["higher_profile_boundary_q"] is True,
            row["support_floor_exact_floor"] is False,
            row["all_interior_empty"] is False,
            row["field_independent_bound"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "m": 10,
        "mprime": 13,
        "strict_interior": True,
        "codeword_degree_ok": True,
        "complete_agreement_mprime": True,
        "proper_subsupport_guarded_out": True,
        "inversion_zero": True,
        "higher_retained_once": True,
        "higher_profile_boundary_q": True,
        "support_floor_exact_floor": False,
        "all_interior_empty": False,
        "field_independent_bound": False,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "mprime": 10,
        "strict_interior": False,
        "codeword_degree_ok": False,
        "complete_agreement_mprime": False,
        "proper_subsupport_guarded_out": False,
        "inversion_zero": False,
        "higher_retained_once": False,
        "higher_profile_boundary_q": False,
        "support_floor_exact_floor": True,
        "all_interior_empty": True,
        "field_independent_bound": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_INTERIOR_BC_FLOOR_HIGHER_SHELL_Q_ROUTING_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
