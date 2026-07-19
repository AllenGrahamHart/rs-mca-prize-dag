#!/usr/bin/env python3
"""Verify the exceptional-only reciprocal Bezout normalization."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_reciprocal_bezout_normalization"
DEPENDENCY = "rate_half_ca_hankel_a1_core_one_exceptional_only_reciprocal_resultant_descent"
CONSUMER = "rate_half_band_closure"


def coefficient_profile_check() -> None:
    profiles = 0
    for e in range(3, 256):
        r = 2 * e + 1
        d_0 = 8 * e + 7
        assert d_0 - r - 1 == 6 * e + 5
        assert r + (d_0 - r - 1) == d_0 - 1
        assert (r - 1) + (d_0 - r) == d_0 - 1
        profiles += 1
    assert profiles == 253


def bezout_fixture() -> None:
    p = 1013
    inv_two = pow(2, -1, p)

    # q_inf=(t-2)(t-5), P_cl=t-3,
    # Delta=t/2-2, a_minus=-1/2.
    def q_inf(t: int) -> int:
        return (t - 2) * (t - 5) % p

    def p_cl(t: int) -> int:
        return (t - 3) % p

    def delta(t: int) -> int:
        return (inv_two * t - 2) % p

    a_minus = -inv_two % p
    for t in range(32):
        assert (p_cl(t) * delta(t) + q_inf(t) * a_minus) % p == 1

    for root in (2, 5):
        assert q_inf(root) == 0
        assert p_cl(root) != 0
        assert delta(root) == pow(p_cl(root), -1, p)

    assert any(
        (p_cl(t) * (delta(t) + 1) + q_inf(t) * a_minus) % p != 1
        for t in range(8)
    )


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
        "P_cl Delta_inf+E q_bar a_minus=1",
        "gcd(Delta_inf,E q_bar)=1",
        "Delta_inf(tau)=P_cl(tau)^(-1)",
        "not a free coefficient",
    ):
        assert marker in statement
    for marker in (
        "X^(D_0-1)",
        "Since the coefficient of this",
        "q_r a_minus+q_(r-1)a_top",
        "Both factors are nonzero",
    ):
        assert marker in proof


def main() -> None:
    coefficient_profile_check()
    bezout_fixture()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_RECIPROCAL_BEZOUT_PASS "
        "profiles=253 fixture_points=32 roots=2 mutation=1"
    )


if __name__ == "__main__":
    main()
