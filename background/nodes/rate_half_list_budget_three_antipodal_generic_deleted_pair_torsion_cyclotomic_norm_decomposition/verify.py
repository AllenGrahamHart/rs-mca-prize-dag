#!/usr/bin/env python3
"""Verify the exact Jacobi/Chebyshev cyclotomic-norm decomposition."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
NODE = (
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_"
    "torsion_cyclotomic_norm_decomposition"
)
DEPENDENCY = (
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_"
    "even_jacobi_norm_router"
)
CONSUMER = "rate_half_list_adjacent_crossing"


def norm_checks() -> int:
    w, z, theta = sp.symbols("w z theta")
    theta_modulus = sp.Poly(theta * theta - 2, theta, domain=sp.QQ)

    def reduce_theta(expression: sp.Expr) -> sp.Expr:
        polynomial = sp.Poly(sp.expand(expression), theta, domain=sp.QQ)
        return sp.rem(polynomial, theta_modulus).as_expr()

    checked = 0
    mutation_tripped = False
    for m in (1, 2, 4, 8):
        jacobi = sp.jacobi(m, sp.Rational(-1, 4), sp.Rational(-1, 2), w)
        lifted = sp.cancel(z**m * jacobi.subs(w, (z + z**-1) / 2))
        assert sp.Poly(lifted, z).degree() == 2 * m
        assert sp.expand(lifted - z ** (2 * m) * lifted.subs(z, z**-1)) == 0

        r_minus = sp.resultant(jacobi, sp.chebyshevt(2 * m, w), w)
        r_plus = sp.resultant(jacobi, sp.chebyshevu(2 * m - 1, w), w)
        top_norm = sp.resultant(sp.cyclotomic_poly(8 * m, z), lifted, z)
        plus_modulus = sp.div(z ** (4 * m) - 1, z * z - 1, z)[0]
        plus_norm = sp.resultant(plus_modulus, lifted, z)
        scalar = 2 ** (2 * m * (2 * m - 1))

        assert sp.cancel(r_minus * r_minus - scalar * top_norm) == 0
        assert sp.cancel(r_plus * r_plus - scalar * plus_norm) == 0

        tower = sp.Rational(1)
        trace_product = sp.Rational(1)
        trace_polynomial_product = sp.Integer(1)
        order = 4
        trace_degree = 1
        levels = 0
        while order <= 4 * m:
            level_norm = sp.resultant(sp.cyclotomic_poly(order, z), lifted, z)
            trace_polynomial = sp.chebyshevt(trace_degree, w)
            trace_resultant = sp.resultant(jacobi, trace_polynomial, w)
            assert sp.cancel(
                level_norm
                - trace_resultant * trace_resultant
                / 2 ** (2 * m * (trace_degree - 1))
            ) == 0
            tower *= level_norm
            trace_product *= trace_resultant
            trace_polynomial_product *= trace_polynomial
            order *= 2
            trace_degree *= 2
            levels += 1
        assert sp.cancel(tower - plus_norm) == 0
        assert sp.expand(
            sp.chebyshevu(2 * m - 1, w)
            - 2 * m * trace_polynomial_product
        ) == 0
        assert sp.cancel(r_plus - (2 * m) ** m * trace_product) == 0
        assert levels == m.bit_length()

        t_m = sp.chebyshevt(m, w)
        split_minus = sp.resultant(jacobi, theta * t_m - 1, w)
        split_plus = sp.resultant(jacobi, theta * t_m + 1, w)
        assert reduce_theta(r_minus - split_minus * split_plus) == 0
        conjugate = split_minus.subs(theta, -theta)
        assert reduce_theta(
            split_minus * conjugate - (-1) ** m * r_minus
        ) == 0

        if sp.cancel(r_minus * r_minus - 2 * scalar * top_norm) != 0:
            mutation_tripped = True
        checked += 1
    assert mutation_tripped
    return checked


def official_order_check() -> None:
    m = 1 << 35
    assert 8 * m == 1 << 38
    assert 4 * m == 1 << 37
    orders = []
    order = 4
    while order <= 4 * m:
        orders.append(order)
        order *= 2
    assert len(orders) == 36
    assert orders[0] == 1 << 2 and orders[-1] == 1 << 37


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    proof = (here / "proof.md").read_text()
    for marker in (
        "H_M(z)=z^M J((z+z^(-1))/2)",
        "R_-^2=2^(2M(2M-1))",
        "36`-level tower",
        "R_+=(2M)^M",
        "Norm_(K/Q)(S_-)=(-1)^M R_-",
        "official characteristic is absent from either norm",
    ):
        assert marker in statement
    for marker in (
        "z^(4M)+1=Phi_(8M)(z)",
        "z notin {+1,-1}",
        "Multiplicativity of the resultant",
        "U_(2M-1)=2^(s+1)",
        "This is `(TCN10)`",
        "sigma(S_-)=(-1)^M S_+",
        "orders in `(TCN3)` and `(TCN5)`",
    ):
        assert marker in proof


def main() -> None:
    checked = norm_checks()
    official_order_check()
    packet_check()
    print(
        "RATE_HALF_DELETED_PAIR_TORSION_CYCLOTOMIC_NORM_PASS "
        f"exact_orders={checked} official_plus_levels=36 mutation=1"
    )


if __name__ == "__main__":
    main()
