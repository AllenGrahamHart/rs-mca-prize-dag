#!/usr/bin/env python3
"""Verify the deployed cells-1/2 common root-sign orbit exclusion."""

import hashlib
import json
import subprocess
import sys
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "cell1_2_common_root_sign_orbit_exclusion"
)
RESULT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_cell12_common_saturation_result.json"
)
RESULT_SHA256 = "be8efeb8259350ba555da81fcf52251c38b7ee20a1e674a36630af96f5d2400a"
PROGRAMS = {
    (-1, -1): "4a3c4f07305a18b43c59768f00187d4416732819e095f6020d358679fb741221",
    (-1, 1): "e03faa46f10c0353443a06f050722a295e57c929402fc2903c33fca2f8b20784",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell12-common-saturation-v1",
            "schema")
    rows = {tuple(row["epsilon"]): row for row in payload["rows"]}
    require(set(rows) == set(PROGRAMS), "two sign classes")
    for signs, program_hash in PROGRAMS.items():
        row = rows[signs]
        require(row["field"] == 2130706433 and row["cell"] == 1, "row scope")
        require(row["sign_product"] == signs[0] * signs[1], "sign product")
        require(row["matching"] == [[1, 3], [2, 4]], "matching")
        require(row["status"] == "COMPLETE", "completion")
        require(row["chart_unit"] is True and row["full_unit"] is True,
                "unit ideals")
        require(row["program_sha256"] == program_hash, "program hash")
        require(row["guard_shape"] == {"degree": 28, "terms": 60},
                "guard shape")
        require(row["stdout"] ==
                "BEGIN_CHART\n-1\n1\nCHART_UNIT=1\nEND_CHART\n"
                "BEGIN_FULL\n-1\n1\nFULL_UNIT=1\nEND_FULL\n",
                "Singular transcript")
        require(row["stderr"] == "", "Singular stderr")


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("all eight common rows" in statement, "closure")
    require("leaves exactly seven" in statement and
            "unclosed common symmetry representatives" in statement,
            "remaining frontier")
    require("nonclaim" in contract, "scope fence")

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
    )
    for parent in parents:
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    symmetry = ROOT / (
        "experiments/prize_resolution/"
        "check_rate_half_kb_positive_433_1a_common_root_sign_symmetry.py"
    )
    completed = subprocess.run(
        [sys.executable, str(symmetry)], cwd=ROOT, check=True,
        capture_output=True, text=True,
    )
    require("exact_orbits=10" in completed.stdout, "symmetry replay")
    print("positive 433-1a cells 1/2 common orbit exclusion verified")


if __name__ == "__main__":
    main()
