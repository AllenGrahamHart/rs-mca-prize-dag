#!/usr/bin/env python3
"""Verify the profile-(6,6) actual-vector census child."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e30_profile_66_actual_census_certificate"
DEPENDENCY = "e1_n256_s16_e30_profile_66_relaxation_certificate"
PARENT = ROOT / "background/nodes/e1_n256_s16_e30_profile_66_exclusion"


def load_parent():
    spec = importlib.util.spec_from_file_location("e30_profile66_parent_actual", PARENT / "verify.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parent = load_parent()
    pin = parent.load_pin()
    tasks = parent.check_relaxations(pin)
    primitive = parent.check_actual(pin, tasks)
    assert len(primitive) == 1_232
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    assert nodes[NODE]["status"] == nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    print("E1_E30_PROFILE66_ACTUAL_CENSUS_CERTIFICATE_PASS templates=1191 vectors=23638891776 profile=240672 exceptional=6244 primitive=1232")


if __name__ == "__main__":
    main()

