#!/usr/bin/env python3
"""Verify the cell-4 exceptional scale-chart exclusion."""

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "cell4_exceptional_scale_chart_exclusion"
)
FACTOR_FILE = "rate_half_kb_positive_433_1a_cell4_exceptional_scale_factor_result.json"
FACTOR_HASH = "9bf203fb4c0260ea391cf4f7b5d874d6a256c1d48d51d4a33a0a3823331458dc"
PLANE_HASH = "26cc881846361a6f85d270dc436784991109f67982122b40cc4bbf75235e410e"
PRIME = 2130706433
ROOTS = [0, 1, 16711679, 2113994754, 2130706432]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell4-exceptional-scale-factor-v1",
            "factor schema")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME,
            "factor completion")
    require(result["source_plane_sha256"] == PLANE_HASH, "plane hash chain")
    require([row["t"] for row in result["linear_roots"]] == ROOTS,
            "linear root census")
    require({row["name"] for row in result["rows"]} == {
        "r_denominator", "c_denominator", "denominator_scale",
        "common_projective_scale", "plane_leading_coefficient",
        "projected_common_scale",
    }, "scale census")
    cubic_count = 0
    for row in result["rows"]:
        require(sum(factor["total_degree"]*factor["multiplicity"]
                    for factor in row["factorization"]) == row["degrees"][1],
                f"factor degree {row['name']}")
        for factor in row["factorization"]:
            require(factor["total_degree"] in (1, 3), "factor degree class")
            if factor["total_degree"] == 3:
                cubic_count += 1
                require("root" not in factor, "cubic root fence")
    require(cubic_count == 2, "irreducible cubic census")
    require(pow(16711679, 2, PRIME) == PRIME-1, "deployed square root of -1")
    for root in ROOTS:
        guard = root*(1-root*root)*(1+root*root) % PRIME
        require(guard == 0, f"guard root {root}")


def main():
    path = EXPERIMENTS / FACTOR_FILE
    require(hashlib.sha256(path.read_bytes()).hexdigest() == FACTOR_HASH,
            "factor artifact hash")
    verify_payload(json.loads(path.read_text()))

    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement and
            "does not exclude the main genus-one chart" in statement,
            "statement status and nonclaim")
    require("only `F_2130706433`" in contract and "nonclaim" in contract,
            "contract field and nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    parents = (
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_cell4_genus1_plane_kernel_reduction",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient",
    )
    for parent in parents:
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print("positive 433-1a cell-4 exceptional scale charts verified")


if __name__ == "__main__":
    main()
