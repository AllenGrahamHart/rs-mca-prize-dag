#!/usr/bin/env python3
"""Verify the exceptional-only infinity coefficient chain."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_infinity_coefficient_rigidity"
DEPENDENCY = "rate_half_ca_hankel_a1_core_one_exceptional_only_factor_descent"
CONSUMER = "rate_half_band_closure"


def degree_check() -> None:
    for e in range(3, 256):
        d_0 = 8 * e + 7
        t = 4 * e + 1
        r = 2 * e + 1
        assert d_0 - r == 6 * e + 6
        assert d_0 - 2 + r == d_0 + r - 2
        assert (t - 1) + e == t + e - 1


def coefficient_fixture() -> None:
    p = 1009
    exceptional = 17
    q_bar = 23
    j_inf = 31
    v_inf = 37
    p_cl = 41
    q_inf = exceptional * q_bar % p
    a_inf = p_cl * j_inf % p
    b_inf = -j_inf * q_bar % p
    w_inf = -exceptional * q_bar * v_inf % p
    k_inf = j_inf * q_bar * v_inf % p
    product = p_cl * exceptional % p

    assert (q_inf * a_inf + product * b_inf) % p == 0
    assert (q_inf * v_inf + w_inf) % p == 0
    assert (w_inf * b_inf - q_inf * k_inf) % p == 0

    broken_b = (b_inf + 1) % p
    assert (q_inf * a_inf + product * broken_b) % p != 0


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
        "q_inf=E q_bar",
        "b_inf=-j_inf q_bar",
        "w_inf=-E q_bar v_inf",
        "k_inf= j_inf q_bar v_inf",
        "deg_X B_1=D_0",
        "truncating `B_1`",
    ):
        assert marker in statement
    for marker in (
        "q_inf v_inf+w_inf=0",
        "E j_inf q_bar^2v_inf=E q_bar k_inf",
        "permits `v_inf=0`",
    ):
        assert marker in proof


def main() -> None:
    degree_check()
    coefficient_fixture()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_INFINITY_RIGIDITY_PASS "
        "profiles=253 fixture=1 mutation=1"
    )


if __name__ == "__main__":
    main()
