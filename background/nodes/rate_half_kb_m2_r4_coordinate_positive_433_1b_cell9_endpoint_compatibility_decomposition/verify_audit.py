#!/usr/bin/env python3
"""Independent set-partition audit for the endpoint replay."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
RESULT = ROOT / "experiments/prize_resolution/rate_half_kb_positive_433_1b_cell9_endpoint_replay_result.json"


def key(point):
    return tuple(point[name] for name in ("r", "t", "b", "c"))


def main():
    rows = json.loads(RESULT.read_text())["rows"]
    by_sign = {}
    for row in rows:
        generic = {key(point) for point in row["generic_points"]}
        base = {key(point) for point in row["kernel_null_points"]}
        if len(generic) != 4 or len(base) != 2 or generic & base:
            raise RuntimeError("non-disjoint 4+2 decomposition")
        if not all(point["guard_nonzero"]
                   for point in [*row["generic_points"],
                                 *row["kernel_null_points"]]):
            raise RuntimeError("guard failure")
        sign = tuple(row["epsilon"])
        previous = by_sign.setdefault(sign, base)
        if previous != base:
            raise RuntimeError("BF/CF base loci differ")
    if len(rows) != 8 or len(by_sign) != 4:
        raise RuntimeError("incomplete replay")
    statement = (NODE / "statement.md").read_text()
    if "excludes no target lift" not in statement:
        raise RuntimeError("scope marker missing")
    print("audit=ok endpoint_rows=8 split=4+2")


if __name__ == "__main__":
    main()
