#!/usr/bin/env python3
"""Verify complete duplicate-role composition for cells 5 and 8."""

import hashlib
import json
from pathlib import Path
import subprocess

NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = ROOT / "experiments/prize_resolution" / (
    "rate_half_kb_positive_433_1b_cells5_8_duplicate_role_transport.py"
)
SCRIPT_SHA256 = "c234d6bac6d8b12e802cd70b5dd9383777b5e4c6075603a5aebcc1b50a7d2ec5"
EXPECTED = (
    "RATE_HALF_KB_POSITIVE_433_1B_CELLS5_8_TRANSPORT_PASS "
    "common_rows=20 target_lanes=4 labels=420 systems=1680"
)
CELL5 = "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell5_complete_exclusion"
TRANSPORT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_cells5_8_duplicate_role_transport"
RANKDROP = "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_complete_exclusion"
PARENTS = {CELL5, TRANSPORT, RANKDROP}


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
        "105 raw cell-5" in manifests[CELL5]["closure"],
        "cell-5 premise",
    )
    own = json.loads((NODE / "node.json").read_text())
    require({item["from"] for item in own["requires"]} == PARENTS,
            "exact parent set")
    require(own["node"]["status"] == "PROVED"
            and "[5,8]" in own["node"]["closure"], "complete orbit status")
    print("PASS cells 5-8 complete: principal=1680 rankdrop=excluded")


if __name__ == "__main__":
    main()
