#!/usr/bin/env python3
"""Check the rate-half ordinary-list scope repair and its DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE_ID = "rate_half_list_adjacent_crossing"
CONSUMER = "list_adjacency_closing"
FLOOR = "rate_half_cyclic_rotated_prefix_floor"
SAFE_ANCHOR = "rate_half_list_integer_johnson_safe_anchor"
LOW_BUDGET = "rate_half_list_low_budget_exact_crossing"


def main() -> int:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    packet = ROOT / "critical" / "nodes" / NODE_ID
    statement = (packet / "statement.md").read_text()
    consumer = (
        ROOT / "critical" / "nodes" / CONSUMER / "conditional.md"
    ).read_text()
    floor_statement = (
        ROOT / "critical" / "nodes" / FLOOR / "statement.md"
    ).read_text()

    incoming = sorted(
        (edge["from"], edge.get("kind"))
        for edge in dag["edges"]
        if edge["to"] == NODE_ID
    )
    outgoing_req = sorted(
        edge["to"]
        for edge in dag["edges"]
        if edge["from"] == NODE_ID and edge.get("kind") == "req"
    )
    old_floor_consumer = sorted(
        edge.get("kind")
        for edge in dag["edges"]
        if edge["from"] == FLOOR and edge["to"] == CONSUMER
    )

    checks = [
        ("node_exists", NODE_ID in nodes),
        ("node_is_target", nodes[NODE_ID]["status"] == "TARGET"),
        ("floor_is_proved", nodes[FLOOR]["status"] == "PROVED"),
        ("safe_anchor_is_proved", nodes[SAFE_ANCHOR]["status"] == "PROVED"),
        ("low_budget_is_proved", nodes[LOW_BUDGET]["status"] == "PROVED"),
        (
            "brackets_are_evidence",
            incoming == [(FLOOR, "ev"), (SAFE_ANCHOR, "ev"), (LOW_BUDGET, "ev")],
        ),
        ("direct_consumer", outgoing_req == [CONSUMER]),
        ("floor_remains_parent_requirement", old_floor_consumer == ["req"]),
        ("consumer_names_new_leaf", NODE_ID in consumer),
        ("statement_pins_ordinary_object", "L_1(a)" in statement and "m=1" in statement),
        ("statement_pins_threshold", "B*=floor(q/2^128)" in statement),
        (
            "statement_pins_razor_lower_bound",
            "17,179,869,184" in statement and "k+2^34" in statement,
        ),
        (
            "statement_pins_safe_anchor",
            "a_IJ(C)" in statement and "1554944255988" in statement,
        ),
        (
            "statement_pins_exact_low_budgets",
            "B* in {1,2}" in statement and "a_L(C)=3n/4" in statement,
        ),
        ("floor_disclaims_safe_side", "no safe-side list claim" in floor_statement),
        (
            "packet_complete",
            all(
                (packet / name).is_file()
                for name in [
                    "statement.md",
                    "attack.md",
                    "frontier.md",
                    "claim_contract.md",
                    "dependency_subdag.md",
                ]
            ),
        ),
    ]

    result = {
        "node": NODE_ID,
        "status": "PASS" if all(ok for _, ok in checks) else "FAIL",
        "checks": [{"name": name, "ok": ok} for name, ok in checks],
        "nonclaim": "Budgets one and two are exact; the adjacent crossing remains open for B*>=3.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
