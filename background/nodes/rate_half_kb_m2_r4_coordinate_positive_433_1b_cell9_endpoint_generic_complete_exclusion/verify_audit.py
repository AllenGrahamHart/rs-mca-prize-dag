#!/usr/bin/env python3
"""Independent Cartesian audit of generic endpoint systems."""

import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
RESULT = ROOT / "experiments/prize_resolution/rate_half_kb_positive_433_1b_cell9_endpoint_residual_result.json"


def main():
    payload = json.loads(RESULT.read_text())
    keys = set()
    systems = set()
    for row in payload["rows"]:
        prefix = (tuple(row["epsilon"]), row["endpoint"], tuple(row["sigma"]))
        if prefix in keys:
            raise RuntimeError("duplicate lane")
        keys.add(prefix)
        for item in row["rows"]:
            key = (*prefix, item["point_index"], item["pairing_index"])
            if key in systems or not item["unit"]:
                raise RuntimeError("duplicate or nonunit system")
            systems.add(key)
    if len(keys) != 32 or len(systems) != 1920:
        raise RuntimeError("incomplete Cartesian ledger")
    expected_tail = set(itertools.product(range(4), range(15)))
    for prefix in keys:
        if {key[-2:] for key in systems if key[:-2] == prefix} != expected_tail:
            raise RuntimeError("point/matching gap")
    print("audit=ok lanes=32 systems=1920")


if __name__ == "__main__":
    main()
