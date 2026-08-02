#!/usr/bin/env python3
"""Verify the cell-0 common lex basis and rational witnesses."""

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "cell0_common_lex_rational_witness"
)
RESULT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_cell0_common_triangle_result.json"
)
RESULT_SHA256 = "fc3f3d0318a8c32a5d1b36856b181946fa8cb68994340efddc07c82faa7c2926"
STDOUT_SHA256 = "1fff68a6f062e105011e37b0bddedc481036769e09d4cf25d11b33605ee5fb72"
POINTS = (
    {"t": 2, "r": 2063859717, "c": 572859116, "b": 1547071505},
    {"t": 2, "r": 2063859717, "c": 396175561, "b": 583634934},
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell0-common-triangle-v1",
            "schema")
    result = payload["result"]
    require(result["status"] == "COMPLETE", "completion")
    require(result["field"] == 2130706433 and result["cell"] == 0,
            "scope")
    require(result["epsilon"] == [-1, -1], "signs")
    require(result["program_sha256"] ==
            "1bf15a82ab89d9cb309de4151354f36370ff27af8e6ec9aa826fe1db1913e413",
            "program hash")
    stdout = result["stdout"]
    require(hashlib.sha256(stdout.encode()).hexdigest() == STDOUT_SHA256,
            "stdout hash")
    require("BEGIN_BLOCK_SUMMARY\n1\n7\n" in stdout, "block profile")
    require("BEGIN_LEX_SUMMARY\n1\n4\n" in stdout, "lex profile")
    for equation in (
        "GP[1]=b2-6b+1",
        "GP[2]=ct4-16711679c-1056997377bt4-8355839bt2+1065353216b+1056997377t4-8355839t2-1065353216",
        "GP[3]=cb-33423356ct2-3c+16711680bt2-16711679b-16711680t2-16711679",
        "GP[4]=r+16711679t2",
    ):
        require(equation in stdout, f"lex equation {equation[:5]}")
    require(result["stderr"] == "", "Singular stderr")

    witnesses = result["rational_witnesses"]
    require(len(witnesses) == 2, "witness count")
    for observed, expected in zip(witnesses, POINTS):
        require(all(observed[key] == value for key, value in expected.items()),
                "witness coordinates")
        require(observed["valid"] is True, "witness validity")
        require(observed["equation_values"] == [0] * 6, "minor values")
        require(len(observed["guard_values"]) == 20 and
                all(observed["guard_values"]), "guard values")


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("two deployed rational common points" in statement, "claim")
    require("does not prove" in statement and "outside record" in statement,
            "scope fence")
    require("nonclaim" in contract, "contract fence")

    result_bytes = RESULT.read_bytes()
    require(hashlib.sha256(result_bytes).hexdigest() == RESULT_SHA256,
            "result hash")
    verify_payload(json.loads(result_bytes))

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    parents = (
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_remaining_common_curve_profile",
    )
    for parent in parents:
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print("positive 433-1a cell-0 common lex rational witness verified")


if __name__ == "__main__":
    main()
