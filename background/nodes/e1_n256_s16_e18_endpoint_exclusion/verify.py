#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
NODE = "e1_n256_s16_e18_endpoint_exclusion"
DEPENDENCIES = {
    "e1_n256_s16_e18_profile_parity_light_reduction",
    "e1_n256_s16_e18_six_profile_exclusion",
}
TARGETS = {"e1_official_prime_exception_control", "unsafe_crossing_family_instantiation"}
PROFILES = {"(6,3)", "(2,4)", "(5,1,1)", "(1,2,1)", "(0,0,2)", "(2,0,0,1)"}


def main() -> None:
    pin = json.loads((HERE / "source_pin.json").read_text())
    texts = []
    for key, value in pin.items():
        if key.endswith("_file"):
            path = ROOT / value
            assert hashlib.sha256(path.read_bytes()).hexdigest() == pin[key + "_sha256"]
            texts.append(path.read_text())
    assert all(any(profile in text for text in texts) for profile in PROFILES)
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert all(nodes[dependency]["status"] == "PROVED" for dependency in DEPENDENCIES)
    assert {source for source, target, kind in edges if target == NODE and kind == "req"} == DEPENDENCIES
    assert all((NODE, target, "ev") in edges for target in TARGETS)
    assert "0<V<=34" in nodes[NODE]["statement"]
    assert all(profile in nodes[NODE]["statement"] for profile in PROFILES)
    print(
        "E1_N256_S16_E18_ENDPOINT_EXCLUSION_PASS "
        "profiles=6 exclusions=6 frontier=34 mutations=2"
    )


if __name__ == "__main__":
    main()
