#!/usr/bin/env python3
"""Audit the scope composition for cell-4 xi3/xi4 pairings 7/10."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
DIRECT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell4_xi3_pairing7_quadratic_resultant_signfree_exclusion"
)
XI_TRANSPORT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "universal_xi4_xi3_outside_role_transport"
)
MATCHING_TRANSPORT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell4_parallel_de_matching_orbit_quotient"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    manifest = json.loads((NODE / "node.json").read_text())
    dependencies = {row["from"] for row in manifest["requires"]}
    require(dependencies == {DIRECT, XI_TRANSPORT, MATCHING_TRANSPORT},
            "exact three-parent composition")
    require(manifest["node"]["status"] == "PROVED", "proved manifest")
    require("64 raw atlas cases" in manifest["node"]["statement"],
            "raw-case accounting")

    direct = json.loads((
        ROOT / "background/nodes" / DIRECT / "node.json"
    ).read_text())["node"]
    xi_transport = json.loads((
        ROOT / "background/nodes" / XI_TRANSPORT / "node.json"
    ).read_text())["node"]
    matching_transport = json.loads((
        ROOT / "background/nodes" / MATCHING_TRANSPORT / "node.json"
    ).read_text())["node"]
    require({direct["status"], xi_transport["status"],
             matching_transport["status"]} == {"PROVED"},
            "all parents proved")
    require("pairing-7 exclusion" in direct["closure"],
            "direct matching scope")
    require("every common role cell" in xi_transport["closure"],
            "transport role-cell scope")
    require("105-to-60" in matching_transport["closure"],
            "matching transport scope")

    result = (NODE / "result.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    audit = (NODE / "audit.md").read_text()
    require("97/105" in result and "cell-4 labels live           8" in result,
            "updated cell-4 ledger")
    require("Two cell-4 matching-exchange pairs remain" in frontier,
            "retained frontier")
    require("four labels" in audit and "4*4" in audit,
            "label multiplicity discipline")
    print("audit=ok cell=4 xi=3,4 pairings=7,10 raw_cases=64 parents=3")


if __name__ == "__main__":
    main()
