#!/usr/bin/env python3
"""S3 orbits of lambda-coordinate collision divisors."""

from __future__ import annotations

import sympy as sp

from f3_h3_repeat_loose_lambda_slope_collisions import (
    A,
    B,
    EXPECTED_LAMBDA_COORDINATE,
    NONTRIVIAL_LAMBDA_COORDINATE,
)


U, V = sp.symbols("u v")

S3_ACTIONS = {
    "e": (A, B),
    "swap": (B, A),
    "a-first": (1 / A, B / A),
    "a-first-swap": (B / A, 1 / A),
    "b-first": (1 / B, A / B),
    "b-first-swap": (A / B, 1 / B),
}

EXPECTED_ORBITS = [
    frozenset(
        (
            ("L_a", "1/b"),
            ("L_b", "1/a"),
            ("L_ab", "1"),
        )
    ),
    frozenset(
        (
            ("L_a", "-1/(1+b)"),
            ("L_a", "-1/(a+b)"),
            ("L_b", "-1/(1+a)"),
            ("L_b", "-1/(a+b)"),
            ("L_ab", "-1/(1+a)"),
            ("L_ab", "-1/(1+b)"),
        )
    ),
]


def numerator_after_action(poly: sp.Expr, action: tuple[sp.Expr, sp.Expr]) -> sp.Expr:
    temp = poly.subs({A: U, B: V})
    pulled = temp.subs({U: action[0], V: action[1]})
    num, _ = sp.together(pulled).as_numer_denom()
    return sp.factor(num)


def canonical(poly: sp.Expr) -> sp.Expr:
    primitive = sp.primitive(sp.Poly(sp.factor(poly), A, B, domain=sp.QQ).as_expr())[1]
    result = sp.Poly(primitive, A, B, domain=sp.QQ)
    leading = result.terms()[0][1]
    return sp.factor(result.as_expr() / leading)


def divisor_lookup() -> dict[sp.Expr, tuple[str, str]]:
    lookup: dict[sp.Expr, tuple[str, str]] = {}
    for key in NONTRIVIAL_LAMBDA_COORDINATE:
        lookup[canonical(EXPECTED_LAMBDA_COORDINATE[key])] = key
    return lookup


def orbit_from(seed: tuple[str, str], lookup: dict[sp.Expr, tuple[str, str]]) -> frozenset[tuple[str, str]]:
    poly = EXPECTED_LAMBDA_COORDINATE[seed]
    orbit: set[tuple[str, str]] = set()
    for action_name, action in S3_ACTIONS.items():
        transformed = canonical(numerator_after_action(poly, action))
        if transformed not in lookup:
            raise AssertionError((seed, action_name, transformed, "not a registered divisor"))
        orbit.add(lookup[transformed])
    return frozenset(orbit)


def check_orbits() -> list[frozenset[tuple[str, str]]]:
    lookup = divisor_lookup()
    seen: set[tuple[str, str]] = set()
    orbits: list[frozenset[tuple[str, str]]] = []
    for seed in sorted(NONTRIVIAL_LAMBDA_COORDINATE):
        if seed in seen:
            continue
        orbit = orbit_from(seed, lookup)
        orbits.append(orbit)
        seen.update(orbit)
    if set(orbits) != set(EXPECTED_ORBITS):
        raise AssertionError((orbits, EXPECTED_ORBITS))
    if seen != NONTRIVIAL_LAMBDA_COORDINATE:
        raise AssertionError((seen, NONTRIVIAL_LAMBDA_COORDINATE))
    return orbits


def main() -> None:
    print("h=3 repeat loose collision-orbit compiler")
    print("S3 action on (a,b): (a,b),(b,a),(1/a,b/a),(b/a,1/a),(1/b,a/b),(a/b,1/b)")
    orbits = check_orbits()
    for index, orbit in enumerate(sorted(orbits, key=lambda items: (len(items), sorted(items))), start=1):
        representative = sorted(orbit)[0]
        polynomial = sp.factor(EXPECTED_LAMBDA_COORDINATE[representative])
        labels = ", ".join(f"{left}={right}" for left, right in sorted(orbit))
        print(f"orbit_{index}: size={len(orbit)} representative={representative} divisor={polynomial}")
        print(f"orbit_{index}_members: {labels}")
    print("nine lambda-coordinate collision divisors quotient to two S3 branch types")
    print("H3_REPEAT_LOOSE_COLLISION_ORBIT_COMPILER_PASS")


if __name__ == "__main__":
    main()
