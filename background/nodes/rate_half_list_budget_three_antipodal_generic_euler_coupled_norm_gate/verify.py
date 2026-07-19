#!/usr/bin/env python3
"""Verify the generic Euler coupled-norm gate."""

from __future__ import annotations

from math import gcd
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_euler_coupled_norm_gate"
DEPENDENCY = "rate_half_list_budget_three_antipodal_generic_euler_cubic_norm_gate"
CONSUMER = "rate_half_list_adjacent_crossing"


def exact_fixture_check() -> None:
    # V=Y^2+1, U=T=Y, d=-1: N_U=N_T=N_Q=1.
    v_degree = 2
    n_u = n_t = n_q = 1
    d_value = -1
    assert n_q == n_u**4
    assert n_t * n_u**3 == (-d_value) ** v_degree
    assert n_t**4 * n_q**3 == d_value ** (4 * v_degree)
    assert 2**4 * n_q**3 != d_value ** (4 * v_degree)


def character_check() -> None:
    for q_value, expected in ((5, {1}), (7, {1, 2, 4}), (13, {1, 3, 9})):
        fourth_powers = {pow(value, 4, q_value) for value in range(1, q_value)}
        assert fourth_powers == expected
        g_value = gcd(4, q_value - 1)
        classified = {
            value
            for value in range(1, q_value)
            if pow(value, (q_value - 1) // g_value, q_value) == 1
        }
        assert classified == fourth_powers


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "N_Q=N_U^4", "N_T N_U^3=(-d)^v", "N_Q in (F^*)^4",
        "N_T^4 N_Q^3=d^(4v)", "g_4=gcd(4,q-1)", "not sufficient",
    ):
        assert marker in statement


def main() -> None:
    exact_fixture_check()
    character_check()
    packet_check()
    print(
        "RATE_HALF_ANTIPODAL_GENERIC_EULER_COUPLED_NORM_PASS "
        "characters=2 coupling=exact eliminated=N_U"
    )


if __name__ == "__main__":
    main()
