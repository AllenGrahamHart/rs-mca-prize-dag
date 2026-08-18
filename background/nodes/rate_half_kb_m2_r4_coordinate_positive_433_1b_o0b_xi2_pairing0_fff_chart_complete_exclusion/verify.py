#!/usr/bin/env python3
"""Verify the logical FFF chart aggregate."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
PARENTS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_xi2_pairing0_fff_generic_root_dichotomy",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_xi2_pairing0_fff_exceptional_fiber_exclusion",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def validate(statuses):
    require(statuses == {identifier: "PROVED" for identifier in PARENTS},
            "proved parent partition")


def main():
    statuses = {
        identifier: json.loads(
            (ROOT / "background/nodes" / identifier / "node.json").read_text()
        )["node"]["status"] for identifier in PARENTS
    }
    validate(statuses)
    own = json.loads((NODE / "node.json").read_text())
    require({row["from"] for row in own["requires"]} == PARENTS,
            "exact parent set")
    require(own["node"]["status"] == "PROVED" and
            "all-finite" in own["node"]["closure"], "aggregate status")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_XI2_PAIRING0_FFF_"
          "CHART_COMPLETE_VERIFY_PASS generic=1 exceptional=14")


if __name__ == "__main__":
    main()
