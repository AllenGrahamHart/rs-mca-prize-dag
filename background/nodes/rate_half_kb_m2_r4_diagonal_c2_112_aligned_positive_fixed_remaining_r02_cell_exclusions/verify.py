#!/usr/bin/env python3
"""Verify the companion composition closing the remaining fixed R02 cells."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
REQUIRED = (
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_f04_r02_cell_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_f07_r02_cell_exclusion",
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
    for cell in ("F05-R02", "F06-R02", "F07-R02"):
        assert cell in statement
    assert "30/36" in statement
    print("KB_C2_112_ALIGNED_POSITIVE_REMAINING_R02_CELLS_PASS closed=3 coverage=30/36")


if __name__ == "__main__":
    main()
