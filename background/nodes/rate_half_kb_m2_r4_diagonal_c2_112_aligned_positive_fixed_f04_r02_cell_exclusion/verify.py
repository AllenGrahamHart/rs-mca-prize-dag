#!/usr/bin/env python3
"""Verify the dependency scope of the F04-R02 literal-cell closure."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
REQUIRED = (
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r02_r20_rank_drop_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r02_r20_quadratic_branch_reduction",
    "rate_half_kb_m2_r4_diagonal_c2_112_f04_cubic_full_j_route_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_f04_r02_degree12_branch_exclusion",
)


def main() -> None:
    node = json.loads((HERE / "node.json").read_text())
    assert node["node"]["status"] == "PROVED"
    assert tuple(edge["from"] for edge in node["requires"]) == REQUIRED
    for node_id in REQUIRED:
        dependency = json.loads((HERE.parent / node_id / "node.json").read_text())
        assert dependency["node"]["status"] == "PROVED"
    assert "F04-R02" in node["node"]["statement"]
    assert "No literal transport" in node["node"]["statement"]
    print("KB_C2_112_ALIGNED_POSITIVE_F04_R02_CELL_EXCLUSION_PASS coverage=27/36")


if __name__ == "__main__":
    main()
