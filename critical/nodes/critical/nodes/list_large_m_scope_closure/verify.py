#!/usr/bin/env python3
"""Audit the arbitrary-arity list compiler and its DAG wiring.

The general projection theorem is proved in the packet. This script checks
that the conditional node consumes exactly the base crossing and that theorem.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE_ID = "list_large_m_scope_closure"
THEOREM_ID = "list_subsqrt_interleaving_collapse"


def main() -> int:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    incoming_req = sorted(
        edge["from"]
        for edge in dag["edges"]
        if edge["to"] == NODE_ID and edge.get("kind") == "req"
    )
    outgoing_req = sorted(
        edge["to"]
        for edge in dag["edges"]
        if edge["from"] == NODE_ID and edge.get("kind") == "req"
    )

    packet = ROOT / "critical" / "nodes" / NODE_ID
    conditional = (packet / "conditional.md").read_text()
    theorem_statement = (
        ROOT / "critical" / "nodes" / THEOREM_ID / "statement.md"
    ).read_text()
    theorem_proof = (
        ROOT / "critical" / "nodes" / THEOREM_ID / "proof.md"
    ).read_text()

    checks = [
        ("node_exists", NODE_ID in nodes),
        ("node_is_conditional", nodes[NODE_ID]["status"] == "CONDITIONAL"),
        ("theorem_is_proved", nodes[THEOREM_ID]["status"] == "PROVED"),
        (
            "exact_req_inputs",
            incoming_req
            == ["list_adjacency_closing", "list_subsqrt_interleaving_collapse"],
        ),
        ("direct_consumer_is_list_grand", outgoing_req == ["list_grand"]),
        ("conditional_names_theorem", THEOREM_ID in conditional),
        ("conditional_uses_base_instance", "m=1" in conditional),
        ("conditional_pins_threshold", "B*" in conditional and "2^256" in conditional),
        ("theorem_states_general_bound", "L(q-1)/(q-L)" in theorem_statement),
        ("proof_has_collision_count", "q^(m-2)" in theorem_proof),
        ("proof_has_diagonal_lower", "Diagonal lower bound" in theorem_proof),
        (
            "packet_complete",
            all(
                (packet / name).is_file()
                for name in [
                    "statement.md",
                    "conditional.md",
                    "attack.md",
                    "frontier.md",
                    "dependency_subdag.md",
                ]
            ),
        ),
    ]

    result = {
        "node": NODE_ID,
        "status": "PASS" if all(ok for _, ok in checks) else "FAIL",
        "checks": [{"name": name, "ok": ok} for name, ok in checks],
        "nonclaim": (
            "This audit checks wiring and proof pins; the human-readable packet "
            "contains the general theorem proof."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
