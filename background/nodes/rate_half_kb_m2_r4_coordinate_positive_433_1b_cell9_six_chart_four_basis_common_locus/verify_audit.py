#!/usr/bin/env python3
"""Audit chart coherence and scope for the cell-9 tower node."""

import ast
import copy
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
RESULT = ROOT / "experiments/prize_resolution" / (
    "rate_half_kb_positive_433_1b_cell9_four_basis_tower_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def check(payload):
    require(len(payload["rows"]) == 24, "row count")
    for epsilon in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
        rows = [row for row in payload["rows"] if tuple(row["epsilon"]) == epsilon]
        require(len(rows) == 6, "six charts per sign")
        require(len({row["base"]["sha256"] for row in rows}) == 1,
                "common t relation")
        for b_index in (2, 3):
            require(len({row["b_relation"]["sha256"] for row in rows
                         if row["b_row_index"] == b_index}) == 1,
                    "coherent b chart")
        for c_index in (4, 5, 6):
            require(len({row["c_relation"]["sha256"] for row in rows
                         if row["c_row_index"] == c_index}) == 1,
                    "coherent c chart")
        require(all(row["b_cover_complete"] and row["c_cover_complete"]
                    for row in rows), "complete chart cover")


def main():
    ast.parse((NODE / "verify.py").read_text())
    payload = json.loads(RESULT.read_text())
    check(payload)
    hostile = copy.deepcopy(payload)
    hostile["rows"][0]["b_cover_complete"] = False
    try:
        check(hostile)
    except RuntimeError:
        pass
    else:
        raise RuntimeError("hostile cover mutation survived")
    contract = (NODE / "claim_contract.md").read_text()
    require("Any source cut" in contract and "Prize claim" in contract,
            "scope markers")
    print("PASS cell-9 tower audit: coherent_charts=24 hostile=detected")


if __name__ == "__main__":
    main()
