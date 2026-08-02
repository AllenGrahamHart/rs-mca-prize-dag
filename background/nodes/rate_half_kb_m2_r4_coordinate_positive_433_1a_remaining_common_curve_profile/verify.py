#!/usr/bin/env python3
"""Verify the seven-orbit deployed common curve profile."""

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "remaining_common_curve_profile"
)
RESULT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_remaining_common_saturation_result.json"
)
RESULT_SHA256 = "56be2226b9777e68f25f7535a1be49dc933e6a6f346ab6a6b7f558ba90d5776d"
EXPECTED = {
    0: ("[0]", 7),
    3: ("[3,6]", 23),
    4: ("[4,7]", 24),
    9: ("[9,10]", 23),
    11: ("[11]", 26),
    12: ("[12,13]", 29),
    14: ("[14]", 31),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-remaining-common-saturation-v1",
            "schema")
    rows = {row["cell"]: row for row in payload["rows"]}
    require(set(rows) == set(EXPECTED), "representatives")
    for cell, (orbit, size) in EXPECTED.items():
        row = rows[cell]
        require(row["cell_orbit"] == orbit, f"cell {cell} orbit")
        require(row["field"] == 2130706433, f"cell {cell} field")
        require(row["epsilon"] == [-1, -1], f"cell {cell} signs")
        require(row["status"] == "COMPLETE", f"cell {cell} completion")
        require(row["chart_unit"] is False and row["full_unit"] is False,
                f"cell {cell} proper ideals")
        expected_stdout = (
            f"BEGIN_CHART\n1\n{size}\nCHART_UNIT=0\nEND_CHART\n"
            f"BEGIN_FULL\n1\n{size}\nFULL_UNIT=0\nEND_FULL\n"
        )
        require(row["stdout"] == expected_stdout, f"cell {cell} transcript")
        require(row["stderr"] == "", f"cell {cell} stderr")
        require(row["guard_shape"] == {"degree": 28, "terms": 60},
                f"cell {cell} guard")


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("Krull\ndimension one" in statement or
            "Krull dimension one" in statement, "dimension claim")
    require("does not prove" in statement and "rational point" in statement,
            "rational-point fence")
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
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_cell1_2_common_root_sign_orbit_exclusion",
    )
    for parent in parents:
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print("positive 433-1a remaining common curve profile verified")


if __name__ == "__main__":
    main()
