#!/usr/bin/env python3
"""Verify the exact cell-9 six-chart tower packet."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
RESULT = ROOT / "experiments/prize_resolution" / (
    "rate_half_kb_positive_433_1b_cell9_four_basis_tower_result.json"
)
SOURCE = ROOT / "experiments/prize_resolution" / (
    "rate_half_kb_positive_433_1b_cell9_global_common_result.json"
)
EXPECTED_SHA256 = "8cf1f6a2bd3d1bc7204b803e5795bbeb9d7d82f9d563bc6602a5b3d57d67818b"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    node = json.loads((NODE / "node.json").read_text())
    require(node["node"]["status"] == "PROVED", "node status")
    require(hashlib.sha256(RESULT.read_bytes()).hexdigest() == EXPECTED_SHA256,
            "tower packet hash")
    payload = json.loads(RESULT.read_text())
    require(payload["field"] == 2130706433, "field")
    require(payload["source_structure_sha256"]
            == hashlib.sha256(SOURCE.read_bytes()).hexdigest(), "source hash")
    expected = set(itertools.product((-1, 1), (-1, 1), (2, 3), (4, 5, 6)))
    rows = {
        (*row["epsilon"], row["b_row_index"], row["c_row_index"]): row
        for row in payload["rows"]
    }
    require(set(rows) == expected and len(payload["rows"]) == 24,
            "complete chart keys")
    for row in rows.values():
        require(row["status"] == "COMPLETE" and row["exact"], "exact row")
        require(row["kernel_dimension"] == row["tower_dimension"] == 1,
                "curve dimensions")
        require(row["b_cover_complete"] and row["c_cover_complete"],
                "cover completeness")
        require(row["remainders"] == ["0"] * 7, "seven reductions")
        require(row["base"]["degrees"][0] == 2, "quadratic t relation")
        require(row["b_relation"]["degrees"][1] == 2,
                "quadratic b relation")
        require(row["c_relation"]["degrees"][0] == 1,
                "linear c relation")
    print("PASS cell-9 six-chart four-basis cover: signs=4 charts=24")


if __name__ == "__main__":
    main()
