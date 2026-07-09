#!/usr/bin/env python3
"""One-parameter forms for the two loose collision branches."""

from __future__ import annotations

import sympy as sp

from f3_h3_repeat_loose_lambda_slope_collisions import (
    A,
    B,
    EXPECTED_LAMBDA_COORDINATE,
    NONTRIVIAL_LAMBDA_COORDINATE,
)


D = A**2 + A + 1

BRANCHES = {
    "A": {
        "representative": ("L_a", "1/b"),
        "b_formula": A * (A + 1) / D,
    },
    "B": {
        "representative": ("L_a", "-1/(1+b)"),
        "b_formula": -(2 * A**2 + 2 * A + 1) / D,
    },
}


def numerator_after_substitution(poly: sp.Expr, b_formula: sp.Expr) -> sp.Expr:
    num, _ = sp.together(poly.subs(B, b_formula)).as_numer_denom()
    return sp.factor(num)


def check_parametrizations() -> None:
    for label, data in BRANCHES.items():
        representative = data["representative"]
        b_formula = data["b_formula"]
        divisor = EXPECTED_LAMBDA_COORDINATE[representative]
        coefficient = sp.factor(sp.diff(divisor, B))
        if coefficient != D:
            raise AssertionError((label, representative, coefficient, D))
        if numerator_after_substitution(divisor, b_formula) != 0:
            raise AssertionError((label, representative, b_formula, divisor))


def secondary_pullbacks(label: str) -> dict[tuple[str, str], sp.Expr]:
    b_formula = BRANCHES[label]["b_formula"]
    return {
        key: numerator_after_substitution(EXPECTED_LAMBDA_COORDINATE[key], b_formula)
        for key in sorted(NONTRIVIAL_LAMBDA_COORDINATE)
    }


def check_finite_fields() -> None:
    for p in (5, 7, 11, 13, 17, 97):
        for a_value in range(p):
            d_value = (a_value * a_value + a_value + 1) % p
            if d_value == 0:
                continue
            for label, data in BRANCHES.items():
                representative = data["representative"]
                if label == "A":
                    b_value = a_value * (a_value + 1) * pow(d_value, -1, p) % p
                else:
                    b_value = -(2 * a_value * a_value + 2 * a_value + 1) * pow(d_value, -1, p) % p
                value = int(EXPECTED_LAMBDA_COORDINATE[representative].subs({A: a_value, B: b_value})) % p
                if value != 0:
                    raise AssertionError((p, label, a_value, b_value, representative, value))


def main() -> None:
    print("h=3 repeat loose collision-branch parametrization")
    print(f"D = {sp.factor(D)}")
    check_parametrizations()
    for label, data in BRANCHES.items():
        representative = data["representative"]
        b_formula = sp.factor(data["b_formula"])
        print(f"branch_{label}: representative={representative} b={b_formula}")
        print(f"branch_{label}_secondary_pullbacks:")
        for key, pullback in secondary_pullbacks(label).items():
            if key == representative:
                continue
            print(f"  {key[0]}={key[1]} -> {sp.factor(pullback)}")
    check_finite_fields()
    print("finite parametrization guardrails verified over p=5,7,11,13,17,97")
    print("H3_REPEAT_LOOSE_COLLISION_BRANCH_PARAMETRIZATION_PASS")


if __name__ == "__main__":
    main()
