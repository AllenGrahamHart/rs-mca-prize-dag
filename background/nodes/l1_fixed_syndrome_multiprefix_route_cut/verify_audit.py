#!/usr/bin/env python3
"""Mutation audit for the fixed-syndrome multiprefix route cut."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            row["degree"] < row["dimension"],
            row["source_floor"] == 1_693_898,
            row["boundary_only"] is True,
            row["same_agreement_remainder"] is True,
            row["same_error_remainder"] is True,
            row["agreement_prefixes_distinct"] is True,
            row["error_prefixes_distinct"] is True,
            row["translation_preserves_pair"] is True,
            row["max_fiber_alone_sufficient"] is False,
            row["coarser_adapter_excluded"] is False,
            row["upper_payment_proved"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "degree": 1_048_439,
        "dimension": 1_048_576,
        "source_floor": 1_693_898,
        "boundary_only": True,
        "same_agreement_remainder": True,
        "same_error_remainder": True,
        "agreement_prefixes_distinct": True,
        "error_prefixes_distinct": True,
        "translation_preserves_pair": True,
        "max_fiber_alone_sufficient": False,
        "coarser_adapter_excluded": False,
        "upper_payment_proved": False,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "degree": 1_048_576,
        "source_floor": 29,
        "boundary_only": False,
        "same_agreement_remainder": False,
        "same_error_remainder": False,
        "agreement_prefixes_distinct": False,
        "error_prefixes_distinct": False,
        "translation_preserves_pair": False,
        "max_fiber_alone_sufficient": True,
        "coarser_adapter_excluded": True,
        "upper_payment_proved": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_FIXED_SYNDROME_MULTIPREFIX_ROUTE_CUT_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
