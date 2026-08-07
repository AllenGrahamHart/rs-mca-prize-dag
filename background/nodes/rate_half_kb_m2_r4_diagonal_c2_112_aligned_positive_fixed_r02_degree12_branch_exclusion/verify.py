#!/usr/bin/env python3
"""Verify the logical composition of all four R02 degree-12 closes."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
NODES = HERE.parent
REQUIRED = (
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r02_r20_degree12_s_zero_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r02_r20_degree12_degree6_leading_curve_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_degree12_b0_k8_nonzero_f_p6_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_degree12_k8_branch_cover",
)
CELLS = tuple(f"F{index:02d}-R02" for index in range(4, 8))


def main() -> None:
    parents = {}
    for node_id in REQUIRED:
        payload = json.loads((NODES / node_id / "node.json").read_text())
        assert payload["node"]["id"] == node_id
        assert payload["node"]["status"] == "PROVED"
        parents[node_id] = payload

    for cell in CELLS:
        assert cell in parents[REQUIRED[2]]["node"]["statement"]
        assert cell in parents[REQUIRED[3]]["node"]["statement"]

    statement = (HERE / "statement.md").read_text()
    for cell in CELLS:
        assert cell in statement
    for label in ("s=0", "L6=0", "K8!=0", "K8=0, K10!=0", "K8=K10=0"):
        assert label in statement

    node = json.loads((HERE / "node.json").read_text())
    assert {edge["from"] for edge in node["requires"]} == set(REQUIRED)
    print(
        "KB_C2_112_FIXED_R02_DEGREE12_BRANCH_EXCLUSION_PASS "
        "cells=4 leaves_per_cell=5 requirements=4"
    )


if __name__ == "__main__":
    main()
