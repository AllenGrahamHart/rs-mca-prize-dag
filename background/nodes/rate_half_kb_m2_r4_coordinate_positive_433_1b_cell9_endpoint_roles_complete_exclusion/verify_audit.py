#!/usr/bin/env python3
"""Independent scope and partition audit for endpoint composition."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"


def main():
    replay = json.loads((EXP / "rate_half_kb_positive_433_1b_cell9_endpoint_replay_result.json").read_text())
    generic = json.loads((EXP / "rate_half_kb_positive_433_1b_cell9_endpoint_residual_result.json").read_text())
    base = json.loads((EXP / "rate_half_kb_positive_433_1b_cell9_kernel_null_residual_result.json").read_text())
    source_rows = {(tuple(row["epsilon"]), row["endpoint"]):
                   (row["generic_point_count"], row["kernel_null_point_count"])
                   for row in replay["rows"]}
    if len(source_rows) != 8 or set(source_rows.values()) != {(4, 2)}:
        raise RuntimeError("source partition")
    generic_labels = {
        (tuple(row["epsilon"]), row["endpoint"], tuple(row["sigma"]),
         item["point_index"], item["pairing_index"])
        for row in generic["rows"] for item in row["rows"] if item["unit"]
    }
    base_labels = {
        (tuple(row["epsilon"]), row["point_index"], tuple(row["sigma"]),
         item["xi_index"], item["pairing_index"])
        for row in base["rows"] for item in row["rows"]
        if item["unit"] and item["xi_index"] in (5, 6)
    }
    if len(generic_labels) != 1920 or len(base_labels) != 960:
        raise RuntimeError("endpoint composition ledger")
    contract = (NODE / "claim_contract.md").read_text()
    if "other five outside roles" not in contract or "Complete cell `9`" not in contract:
        raise RuntimeError("scope fence")
    print("audit=ok endpoint_labels=30")


if __name__ == "__main__":
    main()
