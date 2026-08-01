#!/usr/bin/env python3
"""Univariate exact router for zero-loop 433 common cells 13 and 14."""

import argparse
import importlib.util
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]


def load(name, relative):
    specification = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


BASE = load(
    "zero_loop_atlas",
    "experiments/prize_resolution/rate_half_kb_zero_loop_433_common_atlas.py",
)
COMMON = load(
    "common_router",
    "experiments/prize_resolution/rate_half_kb_zero_loop_433_cell0_router.py",
)
P = BASE.PRIME
BRANCHES = ("minus", "plus")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def polynomial(expression, variables):
    numerator = sp.cancel(expression).as_numer_denom()[0]
    return sp.Poly(numerator, *variables, modulus=P).as_expr()


def strip_guard(expression, variables, r, b=None):
    factors = (r, r - 1, r + 1, r**2 + 1)
    if b is not None and b in variables:
        factors += (b,)
    return BASE.BASE.strip_factors(
        polynomial(expression, variables), factors, variables
    )


def evaluate(expression, substitutions):
    numerator, denominator = sp.cancel(expression).as_numer_denom()
    denominator_value = int(denominator.subs(substitutions)) % P
    if denominator_value == 0:
        raise ZeroDivisionError
    return (
        int(numerator.subs(substitutions))
        * pow(denominator_value, -1, P)
    ) % P


def base_root_gcd(polynomial_value, variable):
    value = sp.Poly(polynomial_value, variable, modulus=P).monic()
    frobenius = COMMON.power_x_mod(P, value, variable)
    return sp.gcd(
        value, frobenius - sp.Poly(variable, variable, modulus=P)
    ).monic()


def univariate_lost(coefficient, constant, variable):
    common = sp.gcd(
        sp.Poly(coefficient, variable, modulus=P),
        sp.Poly(constant, variable, modulus=P),
    )
    if common.degree() <= 0:
        return (), (common.degree(), 0)
    roots = base_root_gcd(common, variable)
    return COMMON.linear_roots(roots, variable), (common.degree(), roots.degree())


def compile_branch(cell, epsilon_1, epsilon_2, branch):
    require(cell in (13, 14) and branch in BRANCHES, "route")
    (t, r, c, b), equations, _, _ = BASE.compile_cell(
        cell, epsilon_1, epsilon_2, strip_fast=True
    )
    x = sp.symbols("x")
    sign = 1 if cell == 13 else -1
    numerator = (r - 1)**2 if branch == "minus" else (r + 1)**2
    denominator = (r + 1)**2 if branch == "minus" else (r - 1)**2
    c_value = sign * b * numerator / denominator
    substituted = []
    for equation in equations:
        expression = (
            equation.subs(t**4, x**2).subs(t**3, t*x).subs(t**2, x)
        )
        substituted.append(
            polynomial(expression.subs(c, c_value), (t, x, r, b))
        )
    require(substituted[0] == 0, "product branch")

    p1 = substituted[1]
    require(sp.degree(p1, x) == 1, "x linearity")
    x_coefficient = strip_guard(sp.diff(p1, x), (r, b), r, b)
    x_constant = strip_guard(p1.subs(x, 0), (r, b), r, b)
    x_lost = COMMON.base_points((x_coefficient, x_constant), r, b)
    x_value = sp.cancel(-p1.subs(x, 0) / sp.diff(p1, x))

    q2 = strip_guard(substituted[2].subs(x, x_value), (t, r, b), r, b)
    if sp.degree(q2, b) == 0:
        obstruction = sp.Poly(q2, r, modulus=P).monic()
        obstruction_roots = base_root_gcd(obstruction, r)
        return {
            "kind": "guarded_empty",
            "symbols": (t, r, c, b, x),
            "c": c_value,
            "x": x_value,
            "x_lost": x_lost,
            "obstruction": obstruction,
            "obstruction_roots": obstruction_roots,
        }
    require(sp.degree(q2, b) == 1 and sp.degree(q2, t) == 0, "b linearity")
    b_coefficient = sp.diff(q2, b)
    b_constant = q2.subs(b, 0)
    b_lost = univariate_lost(b_coefficient, b_constant, r)
    b_value = sp.cancel(-b_constant / b_coefficient)

    q3 = strip_guard(
        substituted[3].subs(x, x_value).subs(b, b_value),
        (t, r), r,
    )
    require(sp.degree(q3, t) == 1, "t linearity")
    t_coefficient = sp.diff(q3, t)
    t_constant = q3.subs(t, 0)
    t_lost = univariate_lost(t_coefficient, t_constant, r)
    t_value = sp.cancel(-t_constant / t_coefficient)

    x_value = sp.cancel(x_value.subs(b, b_value))
    t_numerator, t_denominator = t_value.as_numer_denom()
    x_numerator, x_denominator = x_value.as_numer_denom()
    residual = sp.Poly(
        sp.expand(t_numerator**2 * x_denominator
                  - x_numerator * t_denominator**2),
        r, modulus=P,
    )
    for factor in (r, r - 1, r + 1, r**2 + 1):
        factor_poly = sp.Poly(factor, r, modulus=P)
        while sp.rem(residual, factor_poly).is_zero:
            residual = sp.exquo(residual, factor_poly)
    residual = residual.monic()
    roots = base_root_gcd(residual, r)
    return {
        "kind": "finite",
        "symbols": (t, r, c, b, x),
        "c": c_value,
        "x": x_value,
        "b": b_value,
        "t": t_value,
        "x_lost": x_lost,
        "b_lost": b_lost,
        "t_lost": t_lost,
        "residual": residual,
        "root_gcd": roots,
    }


def reconstruct(cell, epsilon_1, epsilon_2, branch, route=None):
    route = route or compile_branch(cell, epsilon_1, epsilon_2, branch)
    if route["kind"] != "finite":
        return (), ()
    t, r, c, b, _ = route["symbols"]
    (_, _, _, _), original, guard, _ = BASE.compile_cell(
        cell, epsilon_1, epsilon_2
    )
    packets = []
    candidates = []
    for r_value in COMMON.linear_roots(route["root_gcd"], r):
        substitutions = {r: r_value}
        try:
            b_value = evaluate(route["b"], substitutions)
            substitutions[b] = b_value
            values = {
                b: b_value,
                c: evaluate(route["c"], substitutions),
                r: r_value,
                t: evaluate(route["t"], substitutions),
            }
        except ZeroDivisionError:
            candidates.append((r_value, "denominator"))
            continue
        residuals = tuple(int(value.subs(values)) % P for value in original)
        guarded = int(guard.subs(values)) % P != 0
        candidates.append((r_value, residuals, guarded))
        if not any(residuals) and guarded:
            packets.append(tuple(values[symbol] for symbol in (b, c, r, t)))
    return tuple(packets), tuple(candidates)


def audit_route(route):
    t, r, c, b, _ = route["symbols"]
    x_points, x_stats = route["x_lost"]
    require(
        all(b_value == 0 and r_value in (1, P - 1)
            for b_value, r_value in x_points),
        "x lost guard",
    )
    if route["kind"] == "guarded_empty":
        roots = COMMON.linear_roots(route["obstruction_roots"], r)
        require(
            roots and all(root * root % P == P - 1 for root in roots),
            "opposite-sign obstruction",
        )
        return {"x": (x_points, x_stats), "obstruction": roots}
    require(not route["b_lost"][0], "b lost")
    require(not route["t_lost"][0], "t lost")
    return {
        "x": (x_points, x_stats),
        "b": route["b_lost"],
        "t": route["t_lost"],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cell", type=int, choices=(13, 14), required=True)
    parser.add_argument("--epsilon-1", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--epsilon-2", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--branch", choices=BRANCHES, required=True)
    arguments = parser.parse_args()
    route = compile_branch(
        arguments.cell, arguments.epsilon_1, arguments.epsilon_2,
        arguments.branch,
    )
    packets, candidates = reconstruct(
        arguments.cell, arguments.epsilon_1, arguments.epsilon_2,
        arguments.branch, route,
    )
    audit = audit_route(route)
    if route["kind"] == "finite":
        detail = (
            f"residual={route['residual'].degree()} "
            f"base_r={route['root_gcd'].degree()} packets={len(packets)}"
        )
    else:
        detail = (
            f"obstruction={route['obstruction'].degree()} "
            f"base_r={route['obstruction_roots'].degree()} packets=0"
        )
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_CELL1314_ROUTE "
        f"cell={arguments.cell} eps={arguments.epsilon_1},{arguments.epsilon_2} "
        f"branch={arguments.branch} kind={route['kind']} {detail} "
        f"candidates={len(candidates)} x_lost={len(audit['x'][0])}",
        flush=True,
    )
    print(f"packets={packets}", flush=True)


if __name__ == "__main__":
    main()
