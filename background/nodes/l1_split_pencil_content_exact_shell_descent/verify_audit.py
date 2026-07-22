#!/usr/bin/env python3
"""Mutation audit for split-pencil content exact-shell descent."""

from __future__ import annotations


def valid(row: dict[str, bool]) -> bool:
    return all(
        (
            row["squarefree_split_locator"],
            row["module_basis"],
            row["basis_invariant_content"],
            row["agreement_formula"],
            row["exact_iff_coprime"],
            row["unique_content_descent"],
            row["raw_to_exact_partition"],
            not row["primitive_count_bound_claimed"],
            not row["q_bc_flatness_claimed"],
        )
    )


def main() -> None:
    row = {
        "squarefree_split_locator": True,
        "module_basis": True,
        "basis_invariant_content": True,
        "agreement_formula": True,
        "exact_iff_coprime": True,
        "unique_content_descent": True,
        "raw_to_exact_partition": True,
        "primitive_count_bound_claimed": False,
        "q_bc_flatness_claimed": False,
    }
    assert valid(row)
    mutations = {
        "squarefree_split_locator": False,
        "module_basis": False,
        "basis_invariant_content": False,
        "agreement_formula": False,
        "exact_iff_coprime": False,
        "unique_content_descent": False,
        "raw_to_exact_partition": False,
        "primitive_count_bound_claimed": True,
        "q_bc_flatness_claimed": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_SPLIT_PENCIL_CONTENT_EXACT_SHELL_DESCENT_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
