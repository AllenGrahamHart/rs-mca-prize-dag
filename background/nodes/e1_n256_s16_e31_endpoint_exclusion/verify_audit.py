#!/usr/bin/env python3
"""Independent audit of the N=256 V=62 endpoint synthesis."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e31_endpoint_exclusion"
REDUCTION = "e1_n256_s16_e31_profile_parity_light_reduction"
EXCLUSION = "e1_n256_s16_e31_three_profile_joint_exclusion"


def main() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    incoming = {
        edge["from"]
        for edge in dag["edges"]
        if edge["to"] == NODE and edge.get("kind", "req") == "req"
    }
    assert incoming == {REDUCTION, EXCLUSION}
    assert all(nodes[node]["status"] == "PROVED" for node in incoming | {NODE})

    reduction = (ROOT / nodes[REDUCTION]["refs"][0]).read_text()
    exclusion = (ROOT / nodes[EXCLUSION]["refs"][0]).read_text()
    endpoint = (ROOT / nodes[NODE]["refs"][0]).read_text()
    profiles = {"(3,7)", "(2,5,1)", "(1,3,2)"}
    assert all(profile in reduction for profile in profiles)
    assert all(profile in exclusion for profile in profiles)
    assert "proper-conductor theorem excludes its complement" in exclusion
    assert "0 < V <= 60" in endpoint
    assert "no statement about `V<=60`" in (ROOT / nodes[EXCLUSION]["refs"][2]).read_text()

    print(
        "E1_N256_S16_E31_ENDPOINT_EXCLUSION_AUDIT_PASS "
        "incoming=2 profiles=3 frontier=60"
    )


if __name__ == "__main__":
    main()
