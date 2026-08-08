#!/usr/bin/env python3
"""Verify the exact disjoint 36-cell aligned-positive census."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODES = ROOT / "background" / "nodes"
TARGETS = ("R02", "R11", "R20")

SUPPLIERS = {
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_companion_inversion_transport": {
        f"{source}-{target}"
        for source in ("F00", "F01")
        for target in TARGETS
    },
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_f02_f03_upstream_import": {
        f"{source}-{target}"
        for source in ("F02", "F03")
        for target in TARGETS
    },
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_balanced_quadratic_branch_reduction": {
        f"{source}-R11" for source in ("F04", "F05", "F06", "F07")
    },
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_remaining_r02_cell_exclusions": {
        f"{source}-R02" for source in ("F04", "F05", "F06", "F07")
    },
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r20_cell_exclusions": {
        f"{source}-R20" for source in ("F04", "F05", "F06", "F07")
    },
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_moving_ten_cell_upstream_import": {
        "M00-R02", "M00-R11", "M00-R20",
        "M01-R02", "M01-R20",
        "M02-R02", "M02-R20",
        "M03-R02", "M03-R11", "M03-R20",
    },
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_moving_upstream_review_gate": {
        "M01-R11", "M02-R11",
    },
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


registry = {
    f"{source}-{target}"
    for source in (
        "F00", "F01", "F02", "F03", "F04", "F05", "F06", "F07",
        "M00", "M01", "M02", "M03",
    )
    for target in TARGETS
}
seen: set[str] = set()
for node_id, cells in SUPPLIERS.items():
    manifest = json.loads((NODES / node_id / "node.json").read_text())
    require(manifest["node"]["status"] == "PROVED", f"supplier {node_id}")
    require(not seen.intersection(cells), f"overlap at {node_id}")
    seen.update(cells)

require(len(registry) == 36, "registry size")
require(seen == registry, f"coverage missing={sorted(registry-seen)} extra={sorted(seen-registry)}")
manifest = json.loads((Path(__file__).parent / "node.json").read_text())
require(manifest["node"]["status"] == "PROVED", "aggregate status")
require(
    {row["from"] for row in manifest["requires"]} == set(SUPPLIERS),
    "aggregate requirements",
)

print("KB_C2_112_ALIGNED_POSITIVE_36_CELL_COVERAGE_PASS suppliers=7 cells=36")
