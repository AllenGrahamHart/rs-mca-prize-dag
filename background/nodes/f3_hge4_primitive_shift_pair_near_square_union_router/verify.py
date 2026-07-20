#!/usr/bin/env python3
"""Verify the HGE4 near-square union router contract and arithmetic."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_primitive_shift_pair_near_square_union_router"
DEPENDENCY = "f3_hge4_primitive_shift_pair_orbit_aggregate_router"
CONSUMER = "f3_hge4_norm_gate_count"


def arithmetic_check() -> None:
    for n in (16, 32, 64, 2**13, 2**20):
        for h in range(2, min(n // 2, 20) + 1):
            pair_candidates = comb(n - 1, h - 1) * comb(n - h, h)
            union_candidates = comb(n - 1, 2 * h - 1)
            assert pair_candidates == union_candidates * comb(2 * h - 1, h - 1)

    # Free and antipodal-swap orbit bookkeeping.
    for free in range(8):
        for swap in range(8):
            for h in range(2, 12):
                ordered_orbits = 2 * free + swap
                anchored_unions = 2 * h * free + h * swap
                assert anchored_unions == h * ordered_orbits
                assert ordered_orbits <= 2 * (free + swap)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join(
        (base / name).read_text() for name in required if name.endswith(".md")
    )
    for marker in (
        "S_U(X)^2-D_U(X)=d_U^2 in F_p^*",
        "O_h^prim=2V_h^free+V_h^swap",
        "A_h^union=2hV_h^free+hV_h^swap=hO_h^prim",
        "sum_(h=4)^H_max A_h^union/h<=14n^2",
        "A_h^union<=7000h max(1,B_h)",
        "binom(2h-1,h-1)",
        "not a primitive union",
    ):
        assert marker in text


def main() -> None:
    arithmetic_check()
    packet_check()
    print(
        "F3_HGE4_PRIMITIVE_SHIFT_PAIR_NEAR_SQUARE_UNION_ROUTER_PASS "
        "candidate_identity=checked"
    )


if __name__ == "__main__":
    main()
