#!/usr/bin/env python3
"""Verify the conditional K3 allocation interface."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
PREMISES = {
    "rate_half_kb_m2_r4_coordinate_positive_complete_payment",
    "rate_half_kb_m2_r4_k3_orientation_assembly",
    "rate_half_kb_v4_balanced_core_allocation_definition",
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
    require("joint unpaid reserve is not a K3-only allocation" in
            node["statement"], "joint-reserve fence")
    print("PASS K3 conditional allocation interface")


if __name__ == "__main__":
    main()
