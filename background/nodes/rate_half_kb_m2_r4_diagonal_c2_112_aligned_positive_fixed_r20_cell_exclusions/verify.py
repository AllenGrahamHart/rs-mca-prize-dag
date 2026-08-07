#!/usr/bin/env python3
"""Verify the composition closing all four fixed R20 cells."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
REQUIRED = (
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r02_r20_rank_drop_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r02_r20_quadratic_branch_reduction",
    "rate_half_kb_m2_r4_diagonal_c2_112_fixed_literal_r20_generic_cubic_replay",
    "rate_half_kb_m2_r4_diagonal_c2_112_fixed_literal_companion_inversion_transport",
    "rate_half_kb_m2_r4_diagonal_c2_112_fixed_literal_cubic_full_j_route_exclusions",
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r20_degree12_branch_exclusion",
)


def main() -> None:
    node = json.loads((HERE / "node.json").read_text())
    assert tuple(edge["from"] for edge in node["requires"]) == REQUIRED
    for node_id in REQUIRED:
        parent = json.loads((HERE.parent / node_id / "node.json").read_text())
        assert parent["node"]["status"] == "PROVED"
    statement = node["node"]["statement"]
    for cell in ("F04-R20", "F05-R20", "F06-R20", "F07-R20"):
        assert cell in statement
    assert "34/36" in statement
    print("KB_C2_112_ALIGNED_POSITIVE_FIXED_R20_CELLS_PASS closed=4 coverage=34/36")


if __name__ == "__main__":
    main()
