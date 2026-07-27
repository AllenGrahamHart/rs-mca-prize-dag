#!/usr/bin/env python3
"""Independent audit of the N=256 V=64 endpoint synthesis."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e32_endpoint_exclusion"
EXPECTED = {
    "e1_n256_s16_e32_profile_08_light_template_exclusion",
    "e1_n256_s16_e32_profile_351_light_template_exclusion",
    "e1_n256_s16_e32_profile_47_exact_norm_exclusion",
}


def main() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    incoming = {
        edge["from"]
        for edge in dag["edges"]
        if edge["to"] == NODE and edge.get("kind", "req") == "req"
    }
    profile_parent = "e1_n256_s16_e32_profile_parity_diameter_reduction"
    assert incoming == EXPECTED | {profile_parent}
    assert all(nodes[node]["status"] == "PROVED" for node in incoming | {NODE})

    statements = {
        node: (ROOT / nodes[node]["refs"][0]).read_text()
        for node in EXPECTED
    }
    assert "zero vectors" in statements["e1_n256_s16_e32_profile_08_light_template_exclusion"]
    assert "1392<1517" in statements["e1_n256_s16_e32_profile_351_light_template_exclusion"]
    assert "15*N_max < 2^250" in statements["e1_n256_s16_e32_profile_47_exact_norm_exclusion"]
    assert "0 < V <= 62" in (ROOT / nodes[NODE]["refs"][0]).read_text()

    print(
        "E1_N256_S16_E32_ENDPOINT_EXCLUSION_AUDIT_PASS "
        "incoming=4 profiles=3 frontier=62"
    )


if __name__ == "__main__":
    main()
