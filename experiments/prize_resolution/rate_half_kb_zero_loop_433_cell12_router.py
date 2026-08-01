#!/usr/bin/env python3
"""Exact two-branch router for zero-loop 433 common cell 12."""

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
BRANCHES = ("cy", "cdivy")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def polynomial(expression, variables):
    numerator = sp.cancel(expression).as_numer_denom()[0]
    return sp.Poly(numerator, *variables, modulus=P).as_expr()


def strip_guard(expression, variables, b, y):
    return BASE.BASE.strip_factors(
        polynomial(expression, variables),
        (b, y, y - 1, y + 1),
        variables,
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


def compile_branch(epsilon_1, epsilon_2, branch):
    require(branch in BRANCHES, "branch")
    (t, r, c, b), equations, _, _ = BASE.compile_cell(
        12, epsilon_1, epsilon_2, strip_fast=True
    )
    x, y = sp.symbols("x y")
    parity = tuple(
        COMMON.parity_reduce(equation, t, r, x, y, c, b)
        for equation in equations
    )
    c_value = b * y if branch == "cy" else b / y
    substituted = tuple(
        polynomial(equation.subs(c, c_value), (t, r, x, y, b))
        for equation in parity
    )
    require(substituted[0] == 0, "product branch")

    p1 = substituted[1]
    require(sp.degree(p1, x) == 1, "x linearity")
    x_coefficient = sp.diff(p1, x)
    x_constant = p1.subs(x, 0)
    x_value = sp.cancel(-x_constant / x_coefficient)

    q2 = strip_guard(substituted[2].subs(x, x_value), (t, r, y, b), b, y)
    require(sp.degree(q2, r) == 1 and sp.degree(q2, t) == 0, "r linearity")
    r_coefficient = sp.diff(q2, r)
    r_constant = q2.subs(r, 0)
    r_value = sp.cancel(-r_constant / r_coefficient)

    q3 = strip_guard(
        substituted[3].subs(x, x_value).subs(r, r_value),
        (t, y, b), b, y,
    )
    require(sp.degree(q3, t) == 1, "t linearity")
    t_coefficient = sp.diff(q3, t)
    t_constant = q3.subs(t, 0)
    t_value = sp.cancel(-t_constant / t_coefficient)

    r_numerator, r_denominator = r_value.as_numer_denom()
    t_numerator, t_denominator = t_value.as_numer_denom()
    x_numerator, x_denominator = x_value.as_numer_denom()
    r_square = sp.Poly(
        sp.expand(r_numerator**2 - y * r_denominator**2),
        y, b, modulus=P,
    )
    t_square = sp.Poly(
        sp.expand(t_numerator**2 * x_denominator
                  - x_numerator * t_denominator**2),
        y, b, modulus=P,
    )
    common = sp.gcd(r_square, t_square)
    r_residual = r_square.exquo(common)
    t_residual = t_square.exquo(common)
    basis = sp.groebner(
        (r_residual.as_expr(), t_residual.as_expr()),
        y, b, order="lex", method="f5b", modulus=P,
    )
    require(basis.is_zero_dimensional, "zero-dimensional generic branch")
    eliminants = [
        entry.as_expr() for entry in basis.polys
        if sp.degree(entry.as_expr(), y) == 0
    ]
    require(len(eliminants) == 1, "b eliminant")
    eliminant = sp.Poly(eliminants[0], b, modulus=P)
    while eliminant.eval(0) == 0:
        eliminant = eliminant.exquo(sp.Poly(b, b, modulus=P))
    eliminant = eliminant.monic()
    roots = base_root_gcd(eliminant, b)

    lost = {
        "x": COMMON.base_points(
            (
                strip_guard(x_coefficient, (y, b), b, y),
                strip_guard(x_constant, (y, b), b, y),
            ),
            y, b,
        ),
        "r": COMMON.base_points(
            (r_coefficient, r_constant), y, b
        ),
        "t": COMMON.base_points(
            (t_coefficient, t_constant), y, b
        ),
    }
    return {
        "symbols": (t, r, c, b, x, y),
        "c": c_value,
        "x": x_value,
        "r": r_value,
        "t": t_value,
        "r_residual": r_residual,
        "t_residual": t_residual,
        "basis_count": len(basis.polys),
        "eliminant": eliminant,
        "root_gcd": roots,
        "lost": lost,
        "r_linear": (r_coefficient, r_constant),
    }


def reconstruct(epsilon_1, epsilon_2, branch, route=None):
    route = route or compile_branch(epsilon_1, epsilon_2, branch)
    t, r, c, b, _, y = route["symbols"]
    (_, _, _, _), original, guard, _ = BASE.compile_cell(
        12, epsilon_1, epsilon_2
    )
    packets = []
    candidates = []
    for b_value in COMMON.linear_roots(route["root_gcd"], b):
        r_special = sp.Poly(
            route["r_residual"].as_expr().subs(b, b_value), y, modulus=P
        )
        t_special = sp.Poly(
            route["t_residual"].as_expr().subs(b, b_value), y, modulus=P
        )
        y_polynomial = sp.gcd(r_special, t_special).monic()
        y_roots = COMMON.linear_roots(base_root_gcd(y_polynomial, y), y)
        for y_value in y_roots:
            substitutions = {b: b_value, y: y_value}
            try:
                values = {
                    b: b_value,
                    c: evaluate(route["c"], substitutions),
                    r: evaluate(route["r"], substitutions),
                    t: evaluate(route["t"], substitutions),
                }
            except ZeroDivisionError:
                candidates.append((b_value, y_value, "denominator"))
                continue
            residuals = tuple(int(value.subs(values)) % P for value in original)
            guarded = int(guard.subs(values)) % P != 0
            candidates.append((b_value, y_value, residuals, guarded))
            if not any(residuals) and guarded:
                packets.append(tuple(values[symbol] for symbol in (b, c, r, t)))
    return tuple(packets), tuple(candidates)


def audit_lost(route):
    _, _, _, b, _, y = route["symbols"]
    x_points, x_stats = route["lost"]["x"]
    r_points, r_stats = route["lost"]["r"]
    t_points, t_stats = route["lost"]["t"]
    require(not x_points, "x lost points")
    require(all(y_value in (1, P - 1) for b_value, y_value in r_points),
            "r lost guard")
    r_coefficient, r_constant = route["r_linear"]
    for b_value, y_value in t_points:
        if b_value in (0, 1, P - 1) or y_value in (0, 1, P - 1):
            continue
        substitutions = {b: b_value, y: y_value}
        require(
            int(r_coefficient.subs(substitutions)) % P == 0
            and int(r_constant.subs(substitutions)) % P != 0,
            "t projection is not false on prior r row",
        )
    return {
        "x": (x_points, x_stats),
        "r": (r_points, r_stats),
        "t": (t_points, t_stats),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--epsilon-1", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--epsilon-2", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--branch", choices=BRANCHES, required=True)
    arguments = parser.parse_args()
    route = compile_branch(arguments.epsilon_1, arguments.epsilon_2, arguments.branch)
    packets, candidates = reconstruct(
        arguments.epsilon_1, arguments.epsilon_2, arguments.branch, route
    )
    lost = audit_lost(route)
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_CELL12_ROUTE "
        f"eps={arguments.epsilon_1},{arguments.epsilon_2} "
        f"branch={arguments.branch} basis={route['basis_count']} "
        f"eliminant={route['eliminant'].degree()} "
        f"base_b={route['root_gcd'].degree()} packets={len(packets)} "
        f"candidates={len(candidates)} lost="
        f"{len(lost['x'][0])},{len(lost['r'][0])},{len(lost['t'][0])}",
        flush=True,
    )
    print(f"packets={packets}", flush=True)


if __name__ == "__main__":
    main()
