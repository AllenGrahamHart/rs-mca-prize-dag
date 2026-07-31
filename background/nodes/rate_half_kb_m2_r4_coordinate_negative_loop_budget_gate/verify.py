#!/usr/bin/env python3
"""Verify the negative common-K loop-budget gate."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("ell_K<=2" in statement and "(KBNL-2)" in statement, "claim")
    require("deg A_1<=2" in proof and "q_kappa B_2(kappa)=0" in proof, "proof")
    require("nonclaim" in contract and "does not exclude" in statement, "scope")
    require("no search" in (NODE / "source_evidence.md").read_text(), "source")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    parent = "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler"
    require((parent, NODE_ID, "req") in edges, "dependency")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    parent_skeletons = (
        (0, 1, 0, 2, 2, 0),
        (1, 1, 0, 1, 1, 1),
        (1, 1, 1, 2, 0, 0),
        (0, 0, 0, 2, 2, 1),
        (1, 0, 0, 1, 1, 2),
        (1, 0, 1, 2, 0, 1),
        (1, 1, 1, 1, 1, 0),
    )
    survivors = tuple(value for value in parent_skeletons if sum(value[:3]) <= 2)
    require(len(survivors) == 5, "five survivors")
    require(sorted(sum(value[:3]) for value in survivors) == [0, 1, 1, 2, 2], "loop strata")
    require(all(value in statement for value in (
        "(0,1,0;2,2,0)", "(1,1,0;1,1,1)", "(0,0,0;2,2,1)",
        "(1,0,0;1,1,2)", "(1,0,1;2,0,1)",
    )), "printed census")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_LOOP_BUDGET_PASS "
        "parent=7 survivors=5 loop_strata=0,1,1,2,2"
    )


if __name__ == "__main__":
    main()
