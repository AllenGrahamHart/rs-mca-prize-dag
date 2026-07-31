#!/usr/bin/env python3
"""Verify the 442 q-orientation lift."""

import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_q_orientation_lift"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("exactly two" in statement and "(KB4Q-3)" in statement, "claim")
    require("connected tree" in proof and "survival" in (NODE / "audit.md").read_text(), "scope")
    require("nonclaim" in contract and "remain open" in statement, "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_product_q_weld",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_exceptional_product_classifier",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    # For arbitrary target signs alpha,beta, two of eight orientation triples
    # solve s_ab*s_ac=alpha and s_ab*s_bc=beta.
    for alpha, beta in itertools.product((-1, 1), repeat=2):
        solutions = [
            signs for signs in itertools.product((-1, 1), repeat=3)
            if signs[0] * signs[1] == alpha and signs[0] * signs[2] == beta
        ]
        require(len(solutions) == 2, f"orientation count {alpha}/{beta}")
        require(solutions[0] == tuple(-value for value in solutions[1]), "global pair")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_Q_ORIENTATION_PASS "
        "target_signs=4 orientations_each=2 common_k=realized"
    )


if __name__ == "__main__":
    main()
