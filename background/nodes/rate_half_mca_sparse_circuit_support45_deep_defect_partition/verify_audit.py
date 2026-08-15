#!/usr/bin/env python3
"""Independent combinatorial audit of the deep defect partition."""

from __future__ import annotations

import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    need(p["source_supports"] == [4, 5], "supports")
    other = 1
    for count in (9, 8, 5, 4, 3, 2):
        other *= count
    need(other == 8640, "other product")
    checked = 0
    for kprime in range(46, 55):
        q = kprime - 10
        pairs = [(s4, s5) for s4 in range(q + 1) for s5 in range(q + 1)]
        joint = [pair for pair in pairs if sum(pair) < q]
        row = p["rows"][str(kprime)]
        need(len(pairs) == row["exact_pair_count"], "pairs")
        need(len(joint) == row["joint_eligible_pair_count"], "joint")
        need(len(pairs) - len(joint) == row["nonjoint_pair_count"], "nonjoint")
        need(row["raw_leaf_count"] == len(pairs) * other, "leaves")
        checked += len(pairs)
    print(
        "RATE_HALF_MCA_SPARSE_CIRCUIT_SUPPORT45_DEEP_DEFECT_PARTITION_AUDIT_PASS "
        f"pairs={checked} rows=9"
    )


if __name__ == "__main__":
    main()
