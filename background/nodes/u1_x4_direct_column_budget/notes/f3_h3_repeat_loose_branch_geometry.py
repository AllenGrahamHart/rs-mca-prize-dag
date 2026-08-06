#!/usr/bin/env python3
"""Shared geometry of the two loose collision branches."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from f3_h3_repeat_loose_branch_slope_maps import branch_b_value, branch_slope_map
from f3_h3_repeat_loose_collision_branch_parametrization import BRANCHES, D
from f3_h3_repeat_loose_lambda_slope_collisions import A
from f3_h3_repeat_loose_normalized_system import normalized_reciprocal_multipliers


@dataclass(frozen=True)
class BranchGeometry:
    label: str
    b_formula: sp.Expr
    derivative_numerator: sp.Expr
    derivative_denominator: sp.Expr
    distinctness_product: sp.Expr
    derivative_distinctness_multiplicity: int


def primitive_factor(poly: sp.Expr) -> sp.Expr:
    primitive = sp.primitive(sp.Poly(sp.factor(poly), A, domain=sp.QQ).as_expr())[1]
    return sp.factor(primitive)


def factor_multiplicity(poly: sp.Expr, factor: sp.Expr) -> int:
    remaining = sp.Poly(poly, A, domain=sp.QQ)
    divisor = sp.Poly(factor, A, domain=sp.QQ)
    multiplicity = 0
    while True:
        quotient, remainder = sp.div(remaining, divisor)
        if remainder.as_expr() != 0:
            return multiplicity
        remaining = quotient
        multiplicity += 1


def reciprocal_multipliers(label: str) -> tuple[sp.Expr, ...]:
    b_formula = BRANCHES[label]["b_formula"]
    return (
        sp.Integer(1),
        A,
        b_formula,
        -(1 + A),
        -(1 + b_formula),
        -(A + b_formula),
    )


def distinctness_product(label: str) -> sp.Expr:
    multipliers = reciprocal_multipliers(label)
    product = sp.Integer(1)
    for i, left in enumerate(multipliers):
        for right in multipliers[i + 1 :]:
            numerator, _ = sp.together(left - right).as_numer_denom()
            product *= numerator
    return primitive_factor(product)


def branch_geometry(label: str) -> BranchGeometry:
    b_formula = BRANCHES[label]["b_formula"]
    derivative = sp.diff(b_formula, A)
    numerator, denominator = sp.together(derivative).as_numer_denom()
    numerator = primitive_factor(numerator)
    denominator = primitive_factor(denominator)
    product = distinctness_product(label)
    if sp.factor(denominator - D**2) != 0:
        raise AssertionError((label, denominator, D**2))
    return BranchGeometry(
        label=label,
        b_formula=sp.factor(b_formula),
        derivative_numerator=numerator,
        derivative_denominator=denominator,
        distinctness_product=product,
        derivative_distinctness_multiplicity=factor_multiplicity(product, numerator),
    )


def shared_slope_matches() -> dict[str, str]:
    branch_a = dict(branch_slope_map("A").expressions)
    branch_b = dict(branch_slope_map("B").expressions)
    matches: dict[str, str] = {}
    for left_name, left_expression in branch_a.items():
        for right_name, right_expression in branch_b.items():
            numerator, _ = sp.together(left_expression - right_expression).as_numer_denom()
            if sp.factor(numerator) == 0:
                matches[left_name] = right_name
                break
    expected = {
        "C_1": "C_1",
        "C_a": "C_a",
        "C_b": "C_1b",
        "C_1a": "C_1a",
        "C_1b": "C_b",
        "L_b": "L_b",
    }
    if matches != expected:
        raise AssertionError((matches, expected))
    return matches


def valid_branch_parameter(label: str, a_value: int, p: int) -> bool:
    b_value = branch_b_value(label, a_value, p)
    if b_value is None:
        return False
    q_values = normalized_reciprocal_multipliers(a_value, b_value, p)
    if not all(q_values):
        return False
    if len(set(q_values)) != 6:
        return False
    if (1 + a_value + b_value) % p == 0:
        return False
    return True


def finite_guardrails() -> dict[str, int]:
    primes = (5, 7, 11, 13, 17, 97)
    checked = 0
    for p in primes:
        for a_value in range(p):
            a_b = branch_b_value("A", a_value, p)
            b_b = branch_b_value("B", a_value, p)
            if a_b is not None and b_b is not None and (a_b + b_b + 1) % p != 0:
                raise AssertionError((p, a_value, a_b, b_b, "complement failed"))
            for label in ("A", "B"):
                if not valid_branch_parameter(label, a_value, p):
                    continue
                checked += 1
                if (2 * a_value + 1) % p == 0:
                    raise AssertionError((p, label, a_value, "active ramification"))
    return {"primes": len(primes), "checked": checked}


def branch_geometry_summary() -> dict[str, int]:
    geometries = {label: branch_geometry(label) for label in ("A", "B")}
    if sp.factor(BRANCHES["A"]["b_formula"] + BRANCHES["B"]["b_formula"] + 1) != 0:
        raise AssertionError("branch complement identity failed")
    if {label: row.derivative_distinctness_multiplicity for label, row in geometries.items()} != {
        "A": 1,
        "B": 1,
    }:
        raise AssertionError(geometries)
    matches = shared_slope_matches()
    guardrails = finite_guardrails()
    return {
        "shared_slope_maps": len(matches),
        "branch_a_private_slope_maps": 8 - len(matches),
        "branch_b_private_slope_maps": 8 - len(matches),
        "active_finite_ramification_points": 0,
        "finite_checks": guardrails["checked"],
    }


def main() -> None:
    print("h=3 repeat loose branch geometry")
    print(f"shared D={sp.factor(D)}")
    if sp.factor(BRANCHES["A"]["b_formula"] + BRANCHES["B"]["b_formula"] + 1) != 0:
        raise AssertionError("branch complement identity failed")
    print("branch_complement: b_B(a) = -1 - b_A(a)")
    for label in ("A", "B"):
        row = branch_geometry(label)
        print(f"branch_{label}: b={row.b_formula}")
        print(
            f"  derivative=({row.derivative_numerator})/({row.derivative_denominator}) "
            f"distinctness_multiplicity={row.derivative_distinctness_multiplicity}"
        )
        print(f"  distinctness_product={row.distinctness_product}")
    matches = shared_slope_matches()
    print("shared_unique_slope_maps:")
    for left, right in matches.items():
        print(f"  branch_A.{left} = branch_B.{right}")
    print("private_unique_slope_maps: branch_A={C_ab,L_ab}; branch_B={C_ab,L_ab}")
    summary = branch_geometry_summary()
    print(
        "finite_guardrails: "
        f"checked={summary['finite_checks']} "
        f"active_finite_ramification_points={summary['active_finite_ramification_points']}"
    )
    print("H3_REPEAT_LOOSE_BRANCH_GEOMETRY_PASS")


if __name__ == "__main__":
    main()
