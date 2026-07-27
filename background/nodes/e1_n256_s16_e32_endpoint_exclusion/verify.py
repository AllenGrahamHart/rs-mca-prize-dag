#!/usr/bin/env python3
"""Verify the N=256 square-mass-16 V=64 endpoint exclusion."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e32_endpoint_exclusion"
PROFILE = "e1_n256_s16_e32_profile_parity_diameter_reduction"
CHILDREN = (
    "e1_n256_s16_e32_profile_08_light_template_exclusion",
    "e1_n256_s16_e32_profile_351_light_template_exclusion",
    "e1_n256_s16_e32_profile_47_exact_norm_exclusion",
)
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
EXPECTED_PIN = {
    "profile_08_file": "background/nodes/e1_n256_s16_e32_profile_08_light_template_exclusion/statement.md",
    "profile_08_file_sha256": "4a0905c72bef38ee729958da52150ebd4222a7972c114f0d873bf537ca10fe2b",
    "profile_351_file": "background/nodes/e1_n256_s16_e32_profile_351_light_template_exclusion/statement.md",
    "profile_351_file_sha256": "0b387bbc48dcecda916904df2a5b589fb98fb41399e4b618108923811c29d23c",
    "profile_47_file": "background/nodes/e1_n256_s16_e32_profile_47_exact_norm_exclusion/statement.md",
    "profile_47_file_sha256": "fe335329382779e00b0f1329f6aa4890aaeed45feaeba3b6573ba9035416503e",
    "profile_reduction_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/statement.md",
    "profile_reduction_file_sha256": "2c775ba148a35987157c2ce170dbc18b4a338f194cd990b304904e8726ed4edd",
}


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]

    reduction = (ROOT / pin["profile_reduction_file"]).read_text()
    assert "(4,7), (0,8), (3,5,1)" in reduction
    assert "is either zero or two" in reduction

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == nodes[PROFILE]["status"] == "PROVED"
    assert (PROFILE, NODE, "req") in edges
    for child in CHILDREN:
        assert nodes[child]["status"] == "PROVED"
        assert (child, NODE, "req") in edges
    required_into_node = {source for source, target, kind in edges if target == NODE and kind == "req"}
    assert required_into_node == {PROFILE, *CHILDREN}
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "0<V<=62" in nodes[NODE]["statement"]
    assert all(profile in nodes[NODE]["statement"] for profile in ("(4,7)", "(0,8)", "(3,5,1)"))

    print(
        "E1_N256_S16_E32_ENDPOINT_EXCLUSION_PASS "
        "profiles=3 exclusions=3 frontier=62 mutations=4"
    )


if __name__ == "__main__":
    main()
