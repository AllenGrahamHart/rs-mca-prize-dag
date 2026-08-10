#!/usr/bin/env python3
"""Verify the logical shape of the conditional K3 budget composition."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
PREMISES = {
    "rate_half_kb_m2_r4_coordinate_positive_complete_payment",
    "rate_half_kb_m2_r4_k3_orientation_assembly",
    "rate_half_kb_m2_r4_k3_allocation_inequality",
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
    require("U_K3=U_positive+U_geometry" in node["statement"],
            "exact ledger identity")
    print("PASS K3 conditional budget-ledger composition")


if __name__ == "__main__":
    main()
