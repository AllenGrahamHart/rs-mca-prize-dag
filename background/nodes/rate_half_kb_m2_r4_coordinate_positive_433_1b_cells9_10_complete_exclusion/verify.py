#!/usr/bin/env python3
"""Verify complete duplicate-role composition for cells 9 and 10."""

import hashlib
import json
from pathlib import Path
import subprocess

NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = ROOT / "experiments/prize_resolution" / (
    "rate_half_kb_positive_433_1b_cells9_10_duplicate_role_transport.py"
)
SCRIPT_SHA256 = "a562de03d52fedad25a9670b492283107b96fab6e4d689f32ff53345e7723f13"
EXPECTED = (
    "RATE_HALF_KB_POSITIVE_433_1B_CELLS9_10_TRANSPORT_PASS "
    "common_rows=20 target_lanes=4 labels=420 systems=1680"
)
CELL9 = "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_complete_exclusion"
TRANSPORT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_cells9_10_duplicate_role_transport"
RANKDROP = "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_complete_exclusion"
PARENTS = {CELL9, TRANSPORT, RANKDROP}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def validate(statuses):
    require(
        statuses == {identifier: "PROVED" for identifier in PARENTS},
        "proved logical parents",
    )


def main():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_SHA256,
            "transport custody")
    process = subprocess.run(
        ["python3", str(SCRIPT)], capture_output=True, text=True, timeout=10
    )
    require(process.returncode == 0 and process.stdout.strip() == EXPECTED
            and not process.stderr, "transport replay")
    manifests = {
        identifier: json.loads(
            (ROOT / "background/nodes" / identifier / "node.json").read_text()
        )["node"]
        for identifier in PARENTS
    }
    validate({identifier: item["status"] for identifier, item in manifests.items()})
    require(
        "105 raw cell-9 direct labels" in manifests[CELL9]["closure"]
        and "cell 9" in manifests[CELL9]["statement"],
        "cell-9 premise",
    )
    own = json.loads((NODE / "node.json").read_text())
    require({item["from"] for item in own["requires"]} == PARENTS,
            "exact parent set")
    require(own["node"]["status"] == "PROVED"
            and "[9,10]" in own["node"]["closure"], "complete orbit status")
    print("PASS cells 9-10 complete: principal=1680 rankdrop=excluded")


if __name__ == "__main__":
    main()
