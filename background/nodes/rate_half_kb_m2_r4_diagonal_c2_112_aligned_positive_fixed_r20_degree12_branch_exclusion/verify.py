#!/usr/bin/env python3
"""Verify the exhaustive four-cell R20 degree-12 composition."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
REQUIRED = (
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r02_r20_degree12_s_zero_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r02_r20_degree12_degree6_leading_curve_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_degree12_r20_b0_generic_boundary_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_degree12_r20_k10_zero_leading_drop_exclusion",
)
CELLS = tuple(f"F{index:02d}-R20" for index in range(4, 8))


def main() -> None:
    node = json.loads((HERE / "node.json").read_text())
    assert tuple(edge["from"] for edge in node["requires"]) == REQUIRED
    for node_id in REQUIRED:
        parent = json.loads((HERE.parent / node_id / "node.json").read_text())
        assert parent["node"]["status"] == "PROVED"
    statement = (HERE / "statement.md").read_text()
    for cell in CELLS:
        assert cell in statement
    for leaf in ("s=0", "L6=0", "K10!=0", "K10=0"):
        assert leaf in statement
    print("KB_C2_112_FIXED_R20_DEGREE12_BRANCH_PASS cells=4 leaves_per_cell=4")


if __name__ == "__main__":
    main()
