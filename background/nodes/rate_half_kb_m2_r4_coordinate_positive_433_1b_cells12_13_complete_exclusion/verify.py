#!/usr/bin/env python3
"""Verify complete duplicate-role composition for cells 12 and 13."""

import hashlib
import json
from pathlib import Path
import subprocess


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = ROOT / "experiments/prize_resolution" / (
    "rate_half_kb_positive_433_1b_cells12_13_duplicate_role_transport.py"
)
SCRIPT_SHA256 = "fd626431946cf538f6ada57b6b56df1b9adce15778923ebdb31a02e5cafbe97d"
EXPECTED = (
    "RATE_HALF_KB_POSITIVE_433_1B_CELLS12_13_TRANSPORT_PASS "
    "common_rows=20 target_lanes=4 labels=420 systems=1680"
)
PARENTS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell12_complete_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cells12_13_duplicate_role_transport",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_complete_exclusion",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_SHA256,
            "transport custody")
    process = subprocess.run(
        ["python3", str(SCRIPT)], capture_output=True, text=True, timeout=10
    )
    require(process.returncode == 0 and process.stdout.strip() == EXPECTED
            and not process.stderr, "transport replay")
    manifests = {
        node_id: json.loads((ROOT / "background/nodes" / node_id / "node.json").read_text())["node"]
        for node_id in PARENTS
    }
    require(all(item["status"] == "PROVED" for item in manifests.values()),
            "proved logical parents")
    require("all 105 generic outside labels" in
            manifests["rate_half_kb_m2_r4_coordinate_positive_433_1b_cell12_complete_exclusion"]["closure"],
            "cell-12 premise")
    own = json.loads((NODE / "node.json").read_text())
    require({item["from"] for item in own["requires"]} == PARENTS,
            "exact parent set")
    require(own["node"]["status"] == "PROVED"
            and "[12,13]" in own["node"]["closure"], "complete orbit status")
    print("PASS cells 12-13 complete: principal=1680 rankdrop=excluded")


if __name__ == "__main__":
    main()
