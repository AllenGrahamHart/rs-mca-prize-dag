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

    assert nodes[close]["status"] == "TARGET"
    assert nodes[reduction]["status"] == "PROVED"
    assert nodes[myerson]["status"] == "TARGET"
    assert nodes[alarm]["status"] == "REFUTED"
    assert nodes[class_alarm]["status"] == "REFUTED"
    assert "plus branch" in nodes[reduction]["statement"].lower()
    assert (reduction, close, "ev") in edges
    assert (myerson, close, "ev") in edges
    assert (alarm, close, "ev") in edges
    assert (class_alarm, close, "ev") in edges
    assert (myerson, close, "req") not in edges
    assert (close, "u2c_giant_tnull_dichotomy", "req") in edges
    print("F2_ROUND18_CRITICAL_ROUTE_REPAIR_PASS statuses=5/5 edges=6/6")


if __name__ == "__main__":
    main()
