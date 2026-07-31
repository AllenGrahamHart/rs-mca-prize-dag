#!/usr/bin/env python3
"""Verify the 442 complete-edge skeleton classifier."""

import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_complete_edge_skeleton_classifier"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("(m_DE,m_DF,m_EF)=(1,2,2)" in statement, "claim")
    require("third root" in proof and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
        "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_antipodal_label_classifier",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    solutions = []
    for r in itertools.product(range(3), repeat=3):
        if sum(r) != 2:
            continue
        for internal in itertools.product(range(3), repeat=3):
            if sum(internal) != 5:
                continue
            m01, m02, m12 = internal
            degrees = (m01+m02, m01+m12, m02+m12)
            if all(degrees[i] == 4-r[i] for i in range(3)):
                solutions.append((r, internal))
    expected = {
        ((1, 1, 0), (1, 2, 2)),
        ((1, 0, 1), (2, 1, 2)),
        ((0, 1, 1), (2, 2, 1)),
    }
    require(set(solutions) == expected, "ordered skeletons")
    require(all(sorted(r) == [0, 1, 1] for r, _ in solutions),
            "colored split")
    require(all(sorted(values) == [1, 2, 2] for _, values in solutions),
            "internal profile")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_SKELETON_PASS "
        "ordered=3 orbit_types=1 colored=C-D,C-E internal=1,2,2"
    )


if __name__ == "__main__":
    main()
