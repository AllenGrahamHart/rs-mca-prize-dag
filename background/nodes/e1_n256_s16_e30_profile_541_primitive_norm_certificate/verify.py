#!/usr/bin/env python3
"""Verify the profile-(5,4,1) primitive norm child."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e30_profile_541_primitive_norm_certificate"
DEPENDENCY = "e1_n256_s16_e30_profile_541_actual_census_certificate"
PARENT = ROOT / "background/nodes/e1_n256_s16_e30_profile_541_exclusion"


def load_parent():
    spec = importlib.util.spec_from_file_location("e30_profile541_parent_norm", PARENT / "verify.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parent = load_parent()
    pin = json.loads((PARENT / "source_pin.json").read_text())
    orbits = parent.check_orbits(json.loads((ROOT / pin["orbit_result_file"]).read_text()))
    production = json.loads((ROOT / pin["relaxation_result_file"]).read_text())
    audit = json.loads((ROOT / pin["relaxation_audit_result_file"]).read_text())
    masks = parent.check_relaxations(production, audit)
    tasks = [orbits[mask][0] for mask in sorted(masks)]
    actual = json.loads((ROOT / pin["actual_result_file"]).read_text())
    actual_audit = json.loads((ROOT / pin["actual_audit_result_file"]).read_text())
    primitive = parent.check_actual(actual, actual_audit, tasks)
    norms = json.loads((ROOT / pin["norm_result_file"]).read_text())
    parent.check_norms(norms, primitive)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    assert nodes[NODE]["status"] == nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    print("E1_E30_PROFILE541_PRIMITIVE_NORM_CERTIFICATE_PASS vectors=86 distinct=42 max_bits=247")


if __name__ == "__main__":
    main()

