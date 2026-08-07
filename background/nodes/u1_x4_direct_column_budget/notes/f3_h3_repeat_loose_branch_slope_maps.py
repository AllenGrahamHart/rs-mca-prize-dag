#!/usr/bin/env python3
"""Explicit slope maps for the two loose collision branches."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from f3_h3_repeat_loose_affine_slope_compiler import coordinate_slopes, lambda_slopes
from f3_h3_repeat_loose_collision_branch_parametrization import BRANCHES, D
from f3_h3_repeat_loose_lambda_slope_collisions import A, B
from f3_h3_repeat_loose_normalized_system import normalized_reciprocal_multipliers


SLOPE_EXPRESSIONS = {
    "C_1": sp.Integer(1),
    "C_a": 1 / A,
    "C_b": 1 / B,
    "C_1a": -1 / (1 + A),
    "C_1b": -1 / (1 + B),
    "C_ab": -1 / (A + B),
    "L_a": 1 + 1 / A - 1 / (1 + A),
    "L_b": 1 + 1 / B - 1 / (1 + B),
    "L_ab": 1 / A + 1 / B - 1 / (A + B),
}


@dataclass(frozen=True)
class BranchSlopeMap:
    label: str
    duplicate: tuple[str, str]
    expressions: tuple[tuple[str, sp.Expr], ...]
    max_num_degree: int
    max_den_degree: int


def branch_b_formula(label: str) -> sp.Expr:
    return BRANCHES[label]["b_formula"]


def raw_branch_slopes(label: str) -> tuple[tuple[str, sp.Expr], ...]:
    b_formula = branch_b_formula(label)
    return tuple(
        (name, sp.factor(sp.together(expression.subs(B, b_formula))))
        for name, expression in SLOPE_EXPRESSIONS.items()
    )


def unique_branch_slopes(label: str) -> tuple[tuple[str, sp.Expr], ...]:
    unique: list[tuple[str, sp.Expr]] = []
    for name, expression in raw_branch_slopes(label):
        if not any(sp.factor(sp.together(expression - old).as_numer_denom()[0]) == 0 for _, old in unique):
            unique.append((name, expression))
    return tuple(unique)


def degree_pair(expression: sp.Expr) -> tuple[int, int]:
    numerator, denominator = sp.together(expression).as_numer_denom()
    return sp.degree(numerator, A), sp.degree(denominator, A)


def branch_slope_map(label: str) -> BranchSlopeMap:
    raw = raw_branch_slopes(label)
    duplicates = []
    for i, (left_name, left) in enumerate(raw):
        for right_name, right in raw[i + 1 :]:
            if sp.factor(sp.together(left - right).as_numer_denom()[0]) == 0:
                duplicates.append((left_name, right_name))
    expected_duplicate = ("C_b", "L_a") if label == "A" else ("C_1b", "L_a")
    if duplicates != [expected_duplicate]:
        raise AssertionError((label, duplicates, expected_duplicate))
    unique = unique_branch_slopes(label)
    if len(unique) != 8:
        raise AssertionError((label, unique))
    degrees = [degree_pair(expression) for _, expression in unique]
    return BranchSlopeMap(
        label=label,
        duplicate=expected_duplicate,
        expressions=unique,
        max_num_degree=max(num for num, _ in degrees),
        max_den_degree=max(den for _, den in degrees),
    )


def eval_expression_mod(expression: sp.Expr, a_value: int, p: int) -> int | None:
    numerator, denominator = sp.together(expression).as_numer_denom()
    den_value = int(denominator.subs(A, a_value)) % p
    if den_value == 0:
        return None
    num_value = int(numerator.subs(A, a_value)) % p
    return num_value * pow(den_value, -1, p) % p


def branch_b_value(label: str, a_value: int, p: int) -> int | None:
    d_value = (a_value * a_value + a_value + 1) % p
    if d_value == 0:
        return None
    if label == "A":
        return a_value * (a_value + 1) * pow(d_value, -1, p) % p
    return -(2 * a_value * a_value + 2 * a_value + 1) * pow(d_value, -1, p) % p


def check_finite_fields() -> None:
    slope_names = tuple(SLOPE_EXPRESSIONS)
    for p in (5, 7, 11, 13, 17, 97):
        for label in BRANCHES:
            branch = dict(raw_branch_slopes(label))
            for a_value in range(p):
                b_value = branch_b_value(label, a_value, p)
                if b_value is None:
                    continue
                q_values = normalized_reciprocal_multipliers(a_value, b_value, p)
                if not all(q_values):
                    continue
                if len(set(q_values)) != 6:
                    continue
                if (1 + a_value + b_value) % p == 0:
                    continue
                raw_values = coordinate_slopes(a_value, b_value, p) + lambda_slopes(a_value, b_value, p)
                for name, expected in zip(slope_names, raw_values):
                    value = eval_expression_mod(branch[name], a_value, p)
                    if value is None:
                        raise AssertionError((p, label, a_value, name, "unexpected pole"))
                    if value != expected:
                        raise AssertionError((p, label, a_value, b_value, name, value, expected))


def main() -> None:
    print("h=3 repeat loose branch slope maps")
    print(f"shared D={sp.factor(D)}")
    for label in BRANCHES:
        data = branch_slope_map(label)
        b_formula = sp.factor(branch_b_formula(label))
        print(f"branch_{label}: b={b_formula} duplicate={data.duplicate}")
        print(
            f"branch_{label}_degree_budget: "
            f"unique_slopes={len(data.expressions)} "
            f"max_num_degree={data.max_num_degree} max_den_degree={data.max_den_degree}"
        )
        for name, expression in data.expressions:
            numerator_degree, denominator_degree = degree_pair(expression)
            print(
                f"  {name}: {sp.factor(expression)} "
                f"(num_deg={numerator_degree}, den_deg={denominator_degree})"
            )
    check_finite_fields()
    print("finite slope-map guardrails verified over p=5,7,11,13,17,97")
    print("H3_REPEAT_LOOSE_BRANCH_SLOPE_MAPS_PASS")


if __name__ == "__main__":
    main()
