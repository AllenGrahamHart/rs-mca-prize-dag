#!/usr/bin/env python3
"""Audit the scope composition for the cell-4 xi4 pairing-0 corollary."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
DIRECT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell4_xi3_pairing0_reciprocal_square_exclusion"
)
TRANSPORT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "universal_xi4_xi3_outside_role_transport"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    manifest = json.loads((NODE / "node.json").read_text())
    dependencies = {row["from"] for row in manifest["requires"]}
    require(dependencies == {DIRECT, TRANSPORT}, "exact two-parent composition")
    require(manifest["node"]["status"] == "PROVED", "proved manifest")
    require("16 raw atlas cases" in manifest["node"]["statement"],
            "raw-case accounting")

    direct = json.loads((
        ROOT / "background/nodes" / DIRECT / "node.json"
    ).read_text())["node"]
    transport = json.loads((
        ROOT / "background/nodes" / TRANSPORT / "node.json"
    ).read_text())["node"]
    require(direct["status"] == transport["status"] == "PROVED",
            "both parents proved")
    require("xi3 pairing-0" in direct["closure"], "direct matching scope")
    require("every common role cell" in transport["closure"],
            "transport role-cell scope")

    result = (NODE / "result.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    audit = (NODE / "audit.md").read_text()
    require("77 of 105 labels paid and 28 live" in result,
            "updated cell-4 ledger")
    require("matching indices 1 through 14" in frontier,
            "retained frontier")
    require("does not multiply by the three" in " ".join(audit.lower().split()),
            "branch multiplicity discipline")
    print("audit=ok cell=4 xi=4 pairing=0 raw_cases=16 parents=2")


if __name__ == "__main__":
    main()
