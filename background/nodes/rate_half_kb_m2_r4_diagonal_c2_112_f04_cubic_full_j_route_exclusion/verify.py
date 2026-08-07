#!/usr/bin/env python3
"""Verify the dependency scope of the F04 cubic/full-J composition."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
REQUIRED = (
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r02_r20_quadratic_branch_reduction",
    "rate_half_kb_m2_r4_diagonal_c2_112_full_j_log_derivative_branch_router",
    "rate_half_kb_m2_r4_diagonal_c2_112_full_j_log_denominator_branch_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_full_j_log_guarded_numerator_branch_exclusion",
)


def main() -> None:
    node = json.loads((HERE / "node.json").read_text())
    assert node["node"]["status"] == "PROVED"
    assert tuple(edge["from"] for edge in node["requires"]) == REQUIRED
    for node_id in REQUIRED:
        dependency = json.loads((HERE.parent / node_id / "node.json").read_text())
        assert dependency["node"]["status"] == "PROVED"
    statement = (HERE / "statement.md").read_text()
    assert "F04-R02" in statement and "F04-R20" in statement
    assert "degree-12" not in node["node"]["closure"]
    print("KB_C2_112_F04_CUBIC_FULL_J_ROUTE_EXCLUSION_PASS targets=R02,R20")


if __name__ == "__main__":
    main()
