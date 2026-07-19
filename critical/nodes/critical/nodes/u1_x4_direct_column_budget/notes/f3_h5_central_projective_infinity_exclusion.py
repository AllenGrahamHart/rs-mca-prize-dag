#!/usr/bin/env python3
"""Projective-infinity exclusion for the h=5 central fixed scheme."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

import sympy as sp

from f3_h5_central_infinity_flag import (
    coefficient_prime_bound,
    fixed_equation_tops,
    monomial_support,
    restricted_inner_data,
)
from f3_h5_central_slice_quadratic_normal_form import SLICE_TOP, slice_graph_components


OFFICIAL_MIN_CHARACTERISTIC = 2**13 + 1
VARIABLE_ORDER = {str(variable): index for index, variable in enumerate(SLICE_TOP)}


@dataclass(frozen=True)
class InfinityBranch:
    zero_variables: tuple[str, ...]
    active_variables: tuple[str, ...]
    top_supports: tuple[tuple[str, ...], ...]
    forced_zero_options: tuple[tuple[str, ...], ...]
    max_coefficient_prime: int


def sort_variables(variables: set[str] | tuple[str, ...]) -> tuple[str, ...]:
    return tuple(sorted(variables, key=lambda variable: VARIABLE_ORDER[variable]))


def minimal_hitting_sets(supports: tuple[tuple[str, ...], ...]) -> tuple[tuple[str, ...], ...]:
    """Return inclusion-minimal coordinate vanishings hitting every monomial."""
    support_sets = [set(support) for support in supports]
    if any(not support for support in support_sets):
        return ()

    universe = sort_variables(set().union(*support_sets))
    minimal: list[set[str]] = []
    for size in range(1, len(universe) + 1):
        for combo in combinations(universe, size):
            combo_set = set(combo)
            if not all(combo_set & support for support in support_sets):
                continue
            if any(previous <= combo_set for previous in minimal):
                continue
            minimal = [previous for previous in minimal if not combo_set <= previous]
            minimal.append(combo_set)
    return tuple(sort_variables(option) for option in minimal)


def branch_at(graph: tuple[sp.Expr, ...], zero_variables: tuple[str, ...]) -> InfinityBranch:
    active_variables, _, _ = restricted_inner_data(graph, zero_variables)
    tops = fixed_equation_tops(graph, zero_variables)
    top_expressions = tuple(expression for expression, _ in tops)
    supports = tuple(monomial_support(expression, active_variables) for expression in top_expressions)
    max_prime = coefficient_prime_bound(top_expressions, active_variables)
    if max_prime >= OFFICIAL_MIN_CHARACTERISTIC:
        raise AssertionError(("coefficient prime reaches official range", zero_variables, max_prime))
    return InfinityBranch(
        zero_variables=zero_variables,
        active_variables=tuple(str(variable) for variable in active_variables),
        top_supports=supports,
        forced_zero_options=minimal_hitting_sets(supports),
        max_coefficient_prime=max_prime,
    )


def infinity_descent_tree() -> tuple[tuple[InfinityBranch, ...], tuple[tuple[str, ...], ...]]:
    graph = slice_graph_components()
    branches: list[InfinityBranch] = []
    terminal_leaves: list[tuple[str, ...]] = []
    seen: set[tuple[str, ...]] = set()

    def descend(zero_variables: tuple[str, ...]) -> None:
        if len(zero_variables) == len(SLICE_TOP):
            terminal_leaves.append(zero_variables)
            return
        if zero_variables in seen:
            return
        seen.add(zero_variables)
        branch = branch_at(graph, zero_variables)
        branches.append(branch)
        if not branch.forced_zero_options:
            raise AssertionError(("uncovered infinity branch", branch))
        for option in branch.forced_zero_options:
            next_zero = sort_variables(set(zero_variables) | set(option))
            if next_zero == zero_variables:
                raise AssertionError(("non-progressing infinity branch", branch, option))
            descend(next_zero)

    descend(())
    return tuple(branches), tuple(terminal_leaves)


def projective_infinity_exclusion_summary() -> dict[str, int]:
    branches, terminal_leaves = infinity_descent_tree()
    actual_tree = {
        branch.zero_variables: branch.forced_zero_options for branch in branches
    }
    expected_tree = {
        (): (("l9",),),
        ("l9",): (("l7",), ("l8",)),
        ("l7", "l9"): (("l8",),),
        ("l7", "l8", "l9"): (("l6",),),
        ("l8", "l9"): (("l6",),),
        ("l6", "l8", "l9"): (("l7",),),
    }
    if actual_tree != expected_tree:
        raise AssertionError(actual_tree)
    if terminal_leaves != (
        ("l6", "l7", "l8", "l9"),
        ("l6", "l7", "l8", "l9"),
    ):
        raise AssertionError(terminal_leaves)
    max_support_size = max(len(support) for branch in branches for support in branch.top_supports)
    max_prime = max(branch.max_coefficient_prime for branch in branches)
    return {
        "variables": len(SLICE_TOP),
        "branches": len(branches),
        "terminal_leaves": len(terminal_leaves),
        "forced_edges": sum(len(branch.forced_zero_options) for branch in branches),
        "max_support_size": max_support_size,
        "max_coefficient_prime": max_prime,
        "official_min_characteristic": OFFICIAL_MIN_CHARACTERISTIC,
    }


def main() -> None:
    summary = projective_infinity_exclusion_summary()
    print("h=5 central projective-infinity exclusion")
    for branch in infinity_descent_tree()[0]:
        print(
            f"zero={branch.zero_variables or ('-',)} "
            f"active={branch.active_variables} "
            f"top_supports={branch.top_supports} "
            f"forced_zero_options={branch.forced_zero_options}"
        )
    print(
        "summary: "
        f"variables={summary['variables']} "
        f"branches={summary['branches']} "
        f"forced_edges={summary['forced_edges']} "
        f"terminal_leaves={summary['terminal_leaves']} "
        f"max_support_size={summary['max_support_size']} "
        f"max_coeff_prime={summary['max_coefficient_prime']} "
        f"< official_min_char={summary['official_min_characteristic']}"
    )
    print("Every projective-infinity branch descends to all slice coordinates zero.")
    print("H5_CENTRAL_PROJECTIVE_INFINITY_EXCLUSION_PASS")


if __name__ == "__main__":
    main()
