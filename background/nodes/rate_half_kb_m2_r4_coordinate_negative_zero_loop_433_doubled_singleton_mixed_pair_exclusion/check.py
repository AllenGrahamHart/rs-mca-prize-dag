#!/usr/bin/env python3
"""Shared exact row checker for the zero-loop 433 cell-0 exclusion."""

import importlib.util
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
ROUTER = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_zero_loop_433_cell0_router.py"
)
SPEC = importlib.util.spec_from_file_location("router", ROUTER)
ROUTER_MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ROUTER_MODULE)
P = ROUTER_MODULE.PRIME
GUARD_POINTS = ((0, P-1), (1, 1), (P-1, 0))


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def check_row(epsilon_1, epsilon_2, expected_root_gcd,
              expected_q_points, expected_q_stats):
    router = ROUTER_MODULE
    route = router.compile_route(epsilon_1, epsilon_2)
    y, b = route["variables"]

    square_gcd = sp.Poly(route["square_gcd"], y, b, modulus=P).monic()
    expected_square_gcd = sp.Poly(
        route["x_denominator"]*(y*y-1), y, b, modulus=P
    ).monic()
    require(square_gcd == expected_square_gcd, "cleared square gcd")

    basis_count, eliminant, root_gcd = router.generic_certificate(route)
    require(basis_count == 6, "generic basis count")
    require(eliminant.degree() == 20, "generic eliminant degree")
    expected = sp.Poly(expected_root_gcd, b, modulus=P).monic()
    require(root_gcd == expected, "base-root gcd")
    b_roots = router.linear_roots(root_gcd, b)
    require(router.reconstruct(
        epsilon_1, epsilon_2, b_roots, route=route
    ) == (), "projected packet replay")

    branches = router.branch_certificates(route)
    for name in ("c_lost", "x_lost"):
        points, _ = branches[name]
        require(points == GUARD_POINTS, f"{name} points")
    q_points, q_stats = branches["q_singular"]
    require(q_points == expected_q_points, "singular-q points")
    require(q_stats == expected_q_stats, "singular-q stats")
    for b_value, y_value in q_points:
        if (b_value, y_value) in GUARD_POINTS:
            continue
        substitutions = {b: b_value, y: y_value}
        require(router.evaluate(route["x_denominator"], substitutions) == 0,
                "extra singular point denominator")
        require(router.evaluate(route["x_numerator"], substitutions) != 0,
                "extra singular point numerator")
    return basis_count, len(b_roots), len(q_points)
