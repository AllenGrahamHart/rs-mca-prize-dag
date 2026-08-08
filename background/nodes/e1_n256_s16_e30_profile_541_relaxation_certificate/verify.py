#!/usr/bin/env python3
"""Verify the profile-(5,4,1) relaxation child certificate."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e30_profile_541_relaxation_certificate"
DEPENDENCY = "e1_n256_s16_e30_profile_parity_light_reduction"
PARENT = ROOT / "background/nodes/e1_n256_s16_e30_profile_541_exclusion"


def load_parent():
    spec = importlib.util.spec_from_file_location("e30_profile541_parent", PARENT / "verify.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parent = load_parent()
    pin = json.loads((PARENT / "source_pin.json").read_text())
    assert pin == parent.EXPECTED_PIN
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]
    orbits = json.loads((ROOT / pin["orbit_result_file"]).read_text())
    atlas = parent.check_orbits(orbits)
    production = json.loads((ROOT / pin["relaxation_result_file"]).read_text())
    audit = json.loads((ROOT / pin["relaxation_audit_result_file"]).read_text())
    masks = parent.check_relaxations(production, audit)
    assert len(atlas) == 1_234 and len(masks) == 321

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    assert nodes[NODE]["status"] == nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    print("E1_E30_PROFILE541_RELAXATION_CERTIFICATE_PASS masks=1234 exceptional_masks=321 assignments=2924654040 exceptions=1456")


if __name__ == "__main__":
    main()

