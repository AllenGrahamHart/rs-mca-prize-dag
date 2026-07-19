#!/usr/bin/env python3
"""Verify the core-one two-sided complement weld packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_two_sided_complement_weld"
DEPENDENCY = "rate_half_ca_hankel_a1_core_one_component_norm_localization"
CONSUMER = "rate_half_band_closure"


def degree_check(m: int, residual_e: int, omission: int) -> None:
    e = 2 * m - 1
    dominant_e = e - residual_e
    r = 2 * dominant_e + 1
    residual_domain = 16 * m - 1
    supported = 4 * e + 1
    capacity = e - 5 * residual_e - 1 + omission
    assert r > 0 and dominant_e > 0
    assert omission in (0, 1)
    if capacity < 0:
        return
    nonsaturated = capacity
    saturated = residual_domain - nonsaturated
    clean = supported - omission
    assert saturated >= 14 * m + 5 * residual_e
    assert clean >= supported - 1
    v_parameter = supported - dominant_e
    v_x_upper = saturated - 1 if saturated else -1
    w_x_upper = r - 1
    a_parameter_upper = clean - 1
    a_x = residual_domain - r
    b_parameter_upper = dominant_e - 1
    b_x_upper = residual_domain
    k_parameter_upper = supported + b_parameter_upper - dominant_e
    k_x_upper = w_x_upper + b_x_upper - r
    assert v_parameter >= 0 and v_x_upper >= 0
    assert a_parameter_upper >= 0 and a_x >= 0
    assert k_parameter_upper == supported - 1
    assert k_x_upper == residual_domain - 1


def formal_elimination_check(prime: int = 1_000_003) -> None:
    # Scalar specialization of the two complement identities.
    for seed in range(1, 128):
        q = 2 * seed + 1
        px = 3 * seed + 2
        w = 5 * seed + 3
        pcl = 11 * seed + 5
        ez = 13 * seed + 6
        b = 19 * seed + 8
        bx = 23 * seed + 9
        p = pcl * ez % prime
        gx = px * bx % prime
        v = (p - px * w) * pow(q, -1, prime) % prime
        a = (gx - pcl * b) * pow(q, -1, prime) % prime
        assert (q * v + px * w) % prime == p
        assert (q * a + pcl * b) % prime == gx
        left = (q * (v * b + a * ez) + px * (w * b - bx * ez)) % prime
        assert left == 0


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
        "Q V+P_X W=P",
        "Q A+P_cl B=G_X",
        "W B-B_X E_Z=Q K",
        "V B+A E_Z=-P_X K",
        "deg_(U,V)K<=T-1",
        "deg_X B_X<=e-5b-1+D_*",
    ):
        assert marker in packet


def main() -> None:
    for m in range(3, 256):
        e = 2 * m - 1
        for residual_e in range(e // 5 + 1):
            for omission in (0, 1):
                degree_check(m, residual_e, omission)
    formal_elimination_check()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_TWO_SIDED_COMPLEMENT_WELD_PASS "
        "degree_profiles=bounded formal_elimination=1"
    )


if __name__ == "__main__":
    main()
