#!/usr/bin/env python3
"""Verify the corrected conditional K3 orientation composition."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
PREMISES = {
    "rate_half_kb_active_balanced_core_component_bridge",
    "rate_half_kb_m2_r4_coordinate_positive_complete_payment",
    "rate_half_kb_m2_r4_diagonal_source_line_remaining_payment",
    "rate_half_kb_m2_r4_diagonal_source_cover_payment",
    "rate_half_kb_m2_r8_trivial_stabilizer_payment",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    manifest = json.loads((NODE / "node.json").read_text())
    node = manifest["node"]
    require(node["status"] == "CONDITIONAL" and node["gate"] == "all",
            "conditional all-gate")
    require({row["from"] for row in manifest["requires"]} == PREMISES,
            "exact premise set")
    require("U_geometry=U_source_line+U_source_cover+U_trivial" in
            node["statement"], "exact geometry identity")
    require("(m,r,delta)=(2,8,1)" in node["statement"],
            "trivial-stabilizer branch")
    print("PASS corrected K3 orientation composition premises=5")


if __name__ == "__main__":
    main()
