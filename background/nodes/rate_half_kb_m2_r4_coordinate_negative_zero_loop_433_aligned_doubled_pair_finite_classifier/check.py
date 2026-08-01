#!/usr/bin/env python3
"""Shared exact checker for the zero-loop 433 cell-2 classifier."""

import importlib.util
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
ROUTER_PATH = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_zero_loop_433_cell0_router.py"
)
SPEC = importlib.util.spec_from_file_location("router", ROUTER_PATH)
ROUTER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ROUTER)
P = ROUTER.PRIME
GUARD_POINTS = ((0,0),(1,P-1),(P-1,1))


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def check_row(epsilon_1, epsilon_2, expected_basis,
              expected_eliminant_degree, expected_root_gcd,
              expected_packets, expected_q_points, expected_q_stats):
    route = ROUTER.compile_route(epsilon_1, epsilon_2, cell_index=2)
    y, b = route["variables"]
    square_gcd = sp.Poly(route["square_gcd"], y, b, modulus=P).monic()
    expected_square = sp.Poly(
        route["x_denominator"]*(y*y-1), y, b, modulus=P
    ).monic()
    require(square_gcd == expected_square, "cleared square gcd")
    basis_count, eliminant, root_gcd = ROUTER.generic_certificate(route)
    require(basis_count == expected_basis, "basis count")
    require(eliminant.degree() == expected_eliminant_degree,
            "eliminant degree")
    require(root_gcd == sp.Poly(expected_root_gcd,b,modulus=P).monic(),
            "root gcd")
    b_roots = ROUTER.linear_roots(root_gcd, b)
    packets = ROUTER.reconstruct(
        epsilon_1, epsilon_2, b_roots, route=route, cell_index=2
    )
    require(packets == expected_packets, "packet replay")

    branches = ROUTER.branch_certificates(route)
    for name in ("c_lost","x_lost"):
        require(branches[name][0] == GUARD_POINTS, f"{name} points")
    q_points, q_stats = branches["q_singular"]
    require(q_points == expected_q_points, "q points")
    require(q_stats == expected_q_stats, "q stats")
    for b_value, y_value in q_points:
        if b_value in (0,1,P-1) or y_value in (0,1,P-1):
            continue
        substitutions = {b:b_value,y:y_value}
        require(ROUTER.evaluate(route["x_denominator"],substitutions) == 0,
                "false q denominator")
        require(ROUTER.evaluate(route["x_numerator"],substitutions) != 0,
                "false q numerator")
    return len(b_roots), len(packets)
