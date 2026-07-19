#!/usr/bin/env python3
"""Verify the core-one zero-weld quartic boundary packet."""

from __future__ import annotations

import json
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_zero_weld_quartic_boundary"
DEPENDENCY = "rate_half_ca_hankel_a1_core_one_two_sided_complement_weld"
CONSUMER = "rate_half_band_closure"


def official_degree_check() -> None:
    m = 1 << 37
    e = 2 * m - 1
    assert e % 5 == 3
    for residual_e in (0, 1, e // 5):
        dominant_e = e - residual_e
        r = 2 * dominant_e + 1
        assert gcd(dominant_e, r) == 1
        full_remainder = 4 * residual_e + 1
        assert 0 < full_remainder < dominant_e
        assert (4 * e + 1) % dominant_e == full_remainder
        clean_remainder = 4 * residual_e
        assert 0 <= clean_remainder < dominant_e
        assert (4 * e) % dominant_e == clean_remainder
        if residual_e:
            assert clean_remainder

    r = 2 * e + 1
    clean_degree = 4 * e
    domain_degree = clean_degree * r // e
    residual_domain = 8 * e + 7
    assert domain_degree == 8 * e + 4 == 4 * r
    assert residual_domain - domain_degree == 3
    assert (domain_degree - r, clean_degree - e) == (3 * r, 3 * e)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    assert f"background/nodes/{NODE}/statement.md" in nodes[CONSUMER]["refs"]

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md", "dependency_subdag.md",
        "audit.md", "result.md", "verify.py", "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    packet = (base / "statement.md").read_text() + (base / "proof.md").read_text()
    for marker in (
        "b=0",
        "D_*=1",
        "F(U,V)-G_0(X)=Q_*(U,V;X)V_0(U,V;X)",
        "deg G_0=8e+4",
        "deg V_0=(6e+3,3e)",
        "K!=0",
    ):
        assert marker in packet


def main() -> None:
    official_degree_check()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_ZERO_WELD_QUARTIC_BOUNDARY_PASS "
        "survivor=b0,D1 omitted_domain_factors=3"
    )


if __name__ == "__main__":
    main()
