#!/usr/bin/env python3
"""Verify the dependency scope of the direct F07-R02 cell closure."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
REQUIRED = (
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r02_r20_rank_drop_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_fixed_literal_r02_generic_cubic_replay",
    "rate_half_kb_m2_r4_diagonal_c2_112_fixed_literal_cubic_full_j_route_exclusions",
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r02_degree12_branch_exclusion",
)


def main() -> None:
    node = json.loads((HERE / "node.json").read_text())
    assert node["node"]["status"] == "PROVED"
    assert tuple(edge["from"] for edge in node["requires"]) == REQUIRED
    for node_id in REQUIRED:
        dependency = json.loads((HERE.parent / node_id / "node.json").read_text())
        assert dependency["node"]["status"] == "PROVED"
    statement = node["node"]["statement"]
    assert "F07-R02" in statement
    assert "No companion transport" in statement
    print("KB_C2_112_ALIGNED_POSITIVE_F07_R02_CELL_EXCLUSION_PASS")


if __name__ == "__main__":
    main()
