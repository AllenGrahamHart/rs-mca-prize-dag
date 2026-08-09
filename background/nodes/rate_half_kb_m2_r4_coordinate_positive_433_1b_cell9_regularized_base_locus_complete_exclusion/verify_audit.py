#!/usr/bin/env python3
"""Independent label audit for the all-role base-locus census."""

import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
RESULT = ROOT / "experiments/prize_resolution/rate_half_kb_positive_433_1b_cell9_kernel_null_residual_result.json"


def main():
    payload = json.loads(RESULT.read_text())
    systems = set()
    programs = set()
    for row in payload["rows"]:
        prefix = (tuple(row["epsilon"]), row["point_index"], tuple(row["sigma"]))
        programs.add(row["program_sha256"])
        for item in row["rows"]:
            key = (*prefix, item["xi_index"], item["pairing_index"])
            if key in systems or not item["unit"]:
                raise RuntimeError("duplicate or nonunit system")
            systems.add(key)
    expected = {
        (source, point, lane, xi, matching)
        for source in itertools.product((-1, 1), repeat=2)
        for point in range(2)
        for lane in itertools.product((-1, 1), repeat=2)
        for xi in range(7) for matching in range(15)
    }
    if systems != expected or not programs or any(len(value) != 64
                                                   for value in programs):
        raise RuntimeError("census coverage or transcript hash")
    print(f"audit=ok systems=3360 program_digests={len(programs)}")


if __name__ == "__main__":
    main()
