#!/usr/bin/env python3
"""Verify the exceptional-only unit-resultant collapse."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_unit_resultant_collapse"
DEPENDENCY = "rate_half_ca_hankel_a1_core_one_exceptional_only_two_sided_resultant_saturation"
CONSUMER = "rate_half_band_closure"


def exponent_check() -> None:
    profiles = 0
    for e in range(3, 256):
        r = 2 * e + 1
        d_0 = 8 * e + 7
        n_x = d_0 - 1
        for m in (0, r // 2, r - 1):
            assert (m + n_x + 1) + 1 == m + d_0 + 1
            assert (m + n_x) + 1 == m + d_0
        assert n_x + r == 10 * e + 7
        profiles += 1
    assert profiles == 253


def scalar_fixture() -> None:
    p = 1013
    c_x, exceptional, q_bar = 17, 19, 23
    n_x, m = 22, 4
    a = exceptional * q_bar % p
    res_b = c_x * q_bar % p
    res_w = (
        pow(c_x, -1, p)
        * pow(exceptional, m + n_x + 1, p)
        * pow(q_bar, m + n_x, p)
    ) % p
    assert res_w * res_b % p == pow(a, m + n_x + 1, p)

    broken = res_b * exceptional % p
    assert res_w * broken % p != pow(a, m + n_x + 1, p)


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
        "Res_X(Q,B_1)=c_X q_bar",
        "E^(m+n_X+1) q_bar^(m+n_X)",
        "If `v_inf!=0`",
        "single degree-`e-1` form",
    ):
        assert marker in statement
    for marker in (
        "D_0-n_X=1",
        "a^(m+D_0)",
        "leading-coefficient correction",
    ):
        assert marker in proof


def main() -> None:
    exponent_check()
    scalar_fixture()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_UNIT_RESULTANT_PASS "
        "profiles=253 degree_branches=3 fixture=1 mutation=1"
    )


if __name__ == "__main__":
    main()
