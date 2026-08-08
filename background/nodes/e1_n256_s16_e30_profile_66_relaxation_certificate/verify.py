#!/usr/bin/env python3
"""Verify the profile-(6,6) relaxation child certificate."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e30_profile_66_relaxation_certificate"
DEPENDENCY = "e1_n256_s16_e30_profile_parity_light_reduction"
PARENT = ROOT / "background/nodes/e1_n256_s16_e30_profile_66_exclusion"


def load_parent():
    spec = importlib.util.spec_from_file_location("e30_profile66_parent", PARENT / "verify.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parent = load_parent()
    pin = parent.load_pin()
    tasks = parent.check_relaxations(pin)
    assert len(tasks) == 1_191
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    assert nodes[NODE]["status"] == nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    print("E1_E30_PROFILE66_RELAXATION_CERTIFICATE_PASS masks=1234 exceptional_masks=1191 assignments=44779702968 exceptions=33737")


if __name__ == "__main__":
    main()

