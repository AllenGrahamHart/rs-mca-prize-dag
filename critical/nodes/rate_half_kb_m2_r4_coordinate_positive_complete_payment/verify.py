#!/usr/bin/env python3
"""Verify the exact conditional positive-coordinate composition."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
FIXED_EVIDENCE = {
    "rate_half_kb_m2_r4_coordinate_positive_residual_loop_workboard",
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_o0b_complete_route_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_raw_workboard_complete_exclusion",
}
PREMISE = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    own = json.loads((NODE / "node.json").read_text())
    require(own["node"]["status"] == "CONDITIONAL"
            and own["node"]["gate"] == "all", "conditional all-gate")
    require({row["from"] for row in own["requires"]} == {PREMISE},
            "exact open premise")
    manifests = {identifier: json.loads(
        (ROOT / "background/nodes" / identifier / "node.json").read_text()
    )["node"] for identifier in FIXED_EVIDENCE}
    remaining = json.loads(
        (ROOT / "critical/nodes" / PREMISE / "node.json").read_text()
    )["node"]
    require(all(manifests[item]["status"] == "PROVED"
                for item in FIXED_EVIDENCE), "proved fixed evidence")
    require(remaining["status"] in {"TARGET", "PROVED"},
            "live remaining-route premise")
    require("thirteen" in manifests[
        "rate_half_kb_m2_r4_coordinate_positive_residual_loop_workboard"
    ]["statement"], "13-route census")
    print("PASS positive-coordinate conditional payment: U_positive=U_remaining")


if __name__ == "__main__":
    main()
