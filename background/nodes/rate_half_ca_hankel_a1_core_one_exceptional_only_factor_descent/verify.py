#!/usr/bin/env python3
"""Verify the core-one exceptional-only factor descent."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_factor_descent"
DEPENDENCY = "rate_half_ca_hankel_a1_core_one_active_partition_incidence_reconstruction"
CONSUMER = "rate_half_band_closure"


def degree_ledger_check() -> None:
    for e in range(3, 256):
        d_0 = 8 * e + 7
        r = 2 * e + 1
        deg_p_x = d_0 - 1
        deg_q_0 = r - 1
        deg_h = deg_p_x - deg_q_0
        deg_a = d_0 - r - 1
        assert deg_h == d_0 - r
        assert deg_h == deg_a + 1


def scalar_descent_fixture() -> None:
    p = 101
    q, exceptional, w, b_1, j, p_cl, p_x = 7, 3, 5, 4, 6, 8, 11
    inv_q = pow(q, -1, p)
    k_1 = (w * b_1 - 1) * inv_q % p
    a_1 = (p_x - p_cl * exceptional * b_1) * inv_q % p
    b = (q * j + exceptional * b_1) % p
    a = (a_1 - p_cl * j) % p
    k = (w * j + exceptional * k_1) % p
    product = p_cl * exceptional % p
    v = (product - p_x * w) * inv_q % p

    assert (q * v + p_x * w) % p == product
    assert (q * a + p_cl * b) % p == p_x
    assert (w * b - exceptional) % p == q * k % p
    assert (q * a_1 + product * b_1) % p == p_x
    assert (w * b_1 - 1) % p == q * k_1 % p
    assert (v * b_1 + a_1) % p == (-p_x * k_1) % p

    broken_b = (b + 1) % p
    assert (q * a + p_cl * broken_b) % p != p_x


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
        "b=0,       D_*=1,       c=z=1",
        "q_0=Q(gamma_0;X) | P_X",
        "B=QJ+E B_1",
        "W B_1-1=Q K_1",
        "deg_X A_1=D_0-r",
        "not the already-excluded",
    ):
        assert marker in statement
    for marker in (
        "gcd(E,Q)=1",
        "A_1+VB_1+P_XK_1=0",
        "cannot be imported",
    ):
        assert marker in proof


def main() -> None:
    degree_ledger_check()
    scalar_descent_fixture()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_FACTOR_DESCENT_PASS "
        "profiles=253 fixture=1 mutation=1"
    )


if __name__ == "__main__":
    main()
