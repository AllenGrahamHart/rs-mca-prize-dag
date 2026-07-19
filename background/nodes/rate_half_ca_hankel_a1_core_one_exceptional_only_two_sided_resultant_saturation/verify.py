#!/usr/bin/env python3
"""Verify the exceptional-only two-sided resultant ledger."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_two_sided_resultant_saturation"
DEPENDENCY = "rate_half_ca_hankel_a1_core_one_exceptional_only_infinity_coefficient_rigidity"
CONSUMER = "rate_half_band_closure"


def exponent_check() -> None:
    profiles = 0
    for e in range(3, 256):
        t = 4 * e + 1
        d_0 = 8 * e + 7
        n_x = d_0 - 1
        r = 2 * e + 1
        assert t - e == 3 * e + 1
        assert n_x - r == 6 * e + 5
        assert n_x - r + 1 == 6 * e + 6
        assert t * r - 1 == e * n_x
        assert e + (t - e) == t
        assert r + (n_x - r) == n_x
        profiles += 1
    assert profiles == 253


def multiplicity_fixture() -> None:
    # e=2 toy exponent ledger: T=9, r=5, n_X=22, with one exceptional
    # column of degree four. The identities test multiplicities, not field
    # existence of the official biform.
    e, t, r, n_x = 2, 9, 5, 22
    q_column_degrees = [r] * (t - 1) + [r - 1]
    assert sum(q_column_degrees) == e * n_x
    a_column_degrees = [n_x - r] * (t - 1) + [n_x - r + 1]
    assert sum(a_column_degrees) == (t - e) * n_x


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
        "Res_t(P,Q)=c_t P_X^e",
        "Res_t(P,A_1)=c_t^(-1) P_X^(T-e)",
        "Res_X(P_X,Q)=c_X P_cl^r E^(r-1)",
        "Res_X(P_X,V)=c_X^(-1) P_cl^(n_X-r) E^(n_X-r+1)",
        "no unrecorded residual factor",
    ):
        assert marker in statement
    for marker in (
        "Q(gamma;x_0)!=0",
        "Tr-1=e n_X",
        "minus one is precisely",
    ):
        assert marker in proof


def main() -> None:
    exponent_check()
    multiplicity_fixture()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_RESULTANT_SATURATION_PASS "
        "profiles=253 directions=2 complements=2"
    )


if __name__ == "__main__":
    main()
