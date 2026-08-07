#!/usr/bin/env python3
"""Verify the proved-dependency composition covering all eight routes."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
REQUIRED = (
    "rate_half_kb_m2_r4_diagonal_c2_112_f04_cubic_full_j_route_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_fixed_literal_full_j_log_router_replay",
    "rate_half_kb_m2_r4_diagonal_c2_112_fixed_literal_full_j_log_denominator_branch_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_fixed_literal_full_j_log_guarded_numerator_exclusions",
    "rate_half_kb_m2_r4_diagonal_c2_112_fixed_literal_companion_inversion_transport",
)


def main() -> None:
    node = json.loads((HERE / "node.json").read_text())
    assert node["node"]["status"] == "PROVED"
    assert tuple(edge["from"] for edge in node["requires"]) == REQUIRED
    for node_id in REQUIRED:
        dependency = json.loads((HERE.parent / node_id / "node.json").read_text())
        assert dependency["node"]["status"] == "PROVED"
    statement = node["node"]["statement"]
    for assignment in ("F04", "F05", "F06", "F07"):
        assert assignment in statement
    assert "all eight routes" in statement
    assert "No rank-drop" in statement
    print("KB_C2_112_FIXED_LITERAL_CUBIC_FULL_J_ROUTES_PASS routes=8")


if __name__ == "__main__":
    main()
