#!/usr/bin/env python3
"""Verify the repaired F2 critical-route wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def main() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    close = "f2_conditional_close"
    reduction = "f2_admissible_direct_sum_grs_reduction"
    myerson = "f2_growing_order_myerson"
    alarm = "f2_all_admissible_o1_mass_bound"
    class_alarm = "f2_all_admissible_direct_sum_grs_reduction"
    floor = "f2_weighted_kernel_collision_floor"
    minus = "f2_minus_branch_coupled_negacyclic_reduction"
    ambient = "f2_generated_field_ambient_invariance"
    stale_object = "f2_admissible_object"

    assert nodes[close]["status"] == "TARGET"
    assert nodes[reduction]["status"] == "PROVED"
    assert nodes[myerson]["status"] == "TARGET"
    assert nodes[alarm]["status"] == "REFUTED"
    assert nodes[class_alarm]["status"] == "REFUTED"
    assert nodes[floor]["status"] == "PROVED"
    assert nodes[minus]["status"] == "PROVED"
    assert nodes[ambient]["status"] == "PROVED"
    assert nodes[stale_object]["status"] == "REFUTED"
    assert "plus branch" in nodes[reduction]["statement"].lower()
    assert (reduction, close, "ev") in edges
    assert (myerson, close, "ev") in edges
    assert (alarm, close, "ev") in edges
    assert (class_alarm, close, "ev") in edges
    assert (floor, close, "ev") in edges
    assert (minus, close, "ev") in edges
    assert (ambient, close, "ev") in edges
    assert (myerson, close, "req") not in edges
    assert (close, "u2c_giant_tnull_dichotomy", "req") in edges
    print("F2_CRITICAL_ROUTE_REPAIR_PASS statuses=9/9 edges=9/9")


if __name__ == "__main__":
    main()
