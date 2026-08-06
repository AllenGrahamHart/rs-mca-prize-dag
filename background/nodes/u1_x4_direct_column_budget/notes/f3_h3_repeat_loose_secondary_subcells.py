#!/usr/bin/env python3
"""Secondary subcell compiler for one-parameter loose collision branches."""

from __future__ import annotations

from dataclasses import dataclass
from functools import cache

import sympy as sp

from f3_h3_repeat_loose_branch_slope_maps import (
    branch_b_value,
    eval_expression_mod,
    raw_branch_slopes,
)
from f3_h3_repeat_loose_collision_branch_parametrization import (
    BRANCHES,
    D,
    secondary_pullbacks,
)
from f3_h3_repeat_loose_lambda_slope_collisions import A
from f3_h3_repeat_loose_normalized_system import normalized_reciprocal_multipliers


STRUCTURAL_FACTORS = (A, A + 1, D)


@dataclass(frozen=True)
class SecondaryRow:
    label: str
    collision: tuple[str, str]
    raw_pullback: sp.Expr
    residual: sp.Expr
    residual_degree: int


def strip_structural_factors(poly: sp.Expr) -> sp.Expr:
    result = sp.Poly(sp.factor(poly), A, domain=sp.QQ).as_expr()
    for structural in STRUCTURAL_FACTORS:
        factor_poly = sp.Poly(structural, A, domain=sp.QQ)
        while True:
            quotient, remainder = sp.div(sp.Poly(result, A, domain=sp.QQ), factor_poly)
            if remainder.as_expr() != 0:
                break
            result = quotient.as_expr()
    primitive = sp.primitive(sp.Poly(sp.factor(result), A, domain=sp.QQ).as_expr())[1]
    return sp.factor(primitive)


@cache
def secondary_rows(label: str) -> tuple[SecondaryRow, ...]:
    representative = BRANCHES[label]["representative"]
    rows: list[SecondaryRow] = []
    for collision, pullback in secondary_pullbacks(label).items():
        if collision == representative:
            continue
        residual = strip_structural_factors(pullback)
        rows.append(
            SecondaryRow(
                label=label,
                collision=collision,
                raw_pullback=sp.factor(pullback),
                residual=residual,
                residual_degree=sp.degree(residual, A),
            )
        )
    return tuple(rows)


@cache
def residual_product(label: str) -> sp.Expr:
    product = sp.Integer(1)
    for row in secondary_rows(label):
        product *= row.residual
    return sp.factor(product)


def residual_degree(label: str) -> int:
    return sp.degree(residual_product(label), A)


def residual_value(product: sp.Expr, a_value: int, p: int) -> int:
    value = int(product.subs(A, a_value)) % p
    return value


def valid_branch_parameter(label: str, a_value: int, p: int) -> bool:
    if a_value % p == 0 or (a_value + 1) % p == 0:
        return False
    if int(D.subs(A, a_value)) % p == 0:
        return False
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


def slope_count(raw_slopes: tuple[tuple[str, sp.Expr], ...], a_value: int, p: int) -> int | None:
    values: list[int] = []
    for _, expression in raw_slopes:
        value = eval_expression_mod(expression, a_value, p)
        if value is None:
            return None
        values.append(value)
    return len(set(values))


def finite_guardrails() -> dict[str, int]:
    primes = (5, 7, 11, 13, 17, 97)
    products = {label: residual_product(label) for label in BRANCHES}
    raw_slopes = {label: raw_branch_slopes(label) for label in BRANCHES}
    checked = 0
    secondary_hits = 0
    clean_eight_slope = 0
    for p in primes:
        for label in BRANCHES:
            for a_value in range(p):
                if not valid_branch_parameter(label, a_value, p):
                    continue
                count = slope_count(raw_slopes[label], a_value, p)
                if count is None:
                    raise AssertionError((p, label, a_value, "unexpected branch pole"))
                checked += 1
                is_secondary = residual_value(products[label], a_value, p) == 0
                if is_secondary:
                    secondary_hits += 1
                    if count > 7:
                        raise AssertionError((p, label, a_value, count, "residual zero but no extra collision"))
                else:
                    clean_eight_slope += 1
                    if count != 8:
                        raise AssertionError((p, label, a_value, count, "expected clean eight-slope branch"))
    return {
        "primes": len(primes),
        "checked": checked,
        "secondary_hits": secondary_hits,
        "clean_eight_slope": clean_eight_slope,
    }


def main() -> None:
    print("h=3 repeat loose secondary subcell compiler")
    print("structural factors stripped: a, a+1, a^2+a+1")
    for label in BRANCHES:
        print(f"branch_{label}:")
        for row in secondary_rows(label):
            print(
                f"  {row.collision[0]}={row.collision[1]}: "
                f"residual={sp.factor(row.residual)} degree={row.residual_degree}"
            )
        print(
            f"branch_{label}_secondary_product_degree={residual_degree(label)} "
            f"product={sp.factor(residual_product(label))}"
        )
    expected = {"A": 24, "B": 29}
    actual = {label: residual_degree(label) for label in BRANCHES}
    if actual != expected:
        raise AssertionError(actual)
    guardrails = finite_guardrails()
    print(
        f"finite_guardrails: primes={guardrails['primes']} "
        f"checked={guardrails['checked']} "
        f"secondary_hits={guardrails['secondary_hits']} "
        f"clean_eight_slope={guardrails['clean_eight_slope']}"
    )
    print("H3_REPEAT_LOOSE_SECONDARY_SUBCELLS_PASS")


if __name__ == "__main__":
    main()
