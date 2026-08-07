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
    guard = "f2_consumer_guard_depth_reconciliation"
    stale_object = "f2_admissible_object"

    assert nodes[close]["status"] == "TARGET"
    assert nodes[reduction]["status"] == "PROVED"
    assert nodes[myerson]["status"] == "TARGET"
    assert nodes[alarm]["status"] == "REFUTED"
    assert nodes[class_alarm]["status"] == "REFUTED"
    assert nodes[floor]["status"] == "PROVED"
    assert nodes[minus]["status"] == "PROVED"
    assert nodes[ambient]["status"] == "PROVED"
    assert nodes[guard]["status"] == "PROVED"
    # wave-48 repin (coordinator): canonical f2_admissible_object is PROVED (the
    # five-class object of record); the REFUTED pin dated from a transient branch
    # state that this wave reconciled to canonical.
    assert nodes[stale_object]["status"] == "PROVED"
    assert "plus branch" in nodes[reduction]["statement"].lower()
    assert (reduction, close, "ev") in edges
    assert (myerson, close, "ev") in edges
    assert (alarm, close, "ev") in edges
    assert (class_alarm, close, "ev") in edges
    assert (floor, close, "ev") in edges
    assert (minus, close, "ev") in edges
    assert (ambient, close, "ev") in edges
    assert (guard, close, "ev") in edges
    assert "generated-field guard" in nodes[close]["statement"].lower()
    assert (myerson, close, "req") not in edges
    exact_slice = "u2c_exact_slice_extras_budget"
    route_cut = "x4_exact_slice_f2_guard_route_cut"
    assert nodes[exact_slice]["status"] == "TARGET"
    assert nodes[route_cut]["status"] == "PROVED"
    assert (close, "u2c_giant_tnull_dichotomy", "req") not in edges
    assert (close, "u2c_giant_tnull_dichotomy", "ev") in edges
    # wave-48 repin (coordinator): the born-red declaration rewired this pair —
    # the dichotomy now supplies evidence TO the slice budget (ev), not the reverse req.
    assert ("u2c_giant_tnull_dichotomy", exact_slice, "ev") in edges
    assert (route_cut, exact_slice, "ev") in edges
    print("F2_ROUTE_SCOPE_REPAIR_PASS statuses=12/12 edges=13/13")


if __name__ == "__main__":
    main()
