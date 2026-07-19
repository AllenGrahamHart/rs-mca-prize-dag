#!/usr/bin/env python3
"""Integrity check for the banked A=[0,1,45] census JSON."""

from __future__ import annotations

import json
from pathlib import Path


RESULT_PATH = Path(
    "critical/nodes/u1_x4_direct_column_budget/notes/"
    "f3_h3_core_0145_census_results.json"
)

EXPECTED = [
    ([0, 1, 45, 4, 41, 85], [37633]),
    ([0, 1, 45, 5, 57, 92], [37633]),
    ([0, 1, 45, 8, 57, 84], [37633]),
    ([0, 1, 45, 12, 85, 88], [37633]),
    ([0, 1, 45, 13, 44, 77], [207073]),
    ([0, 1, 45, 38, 53, 56], [15937]),
    ([0, 1, 45, 46, 47, 94], [207073]),
]


def main() -> None:
    data = json.loads(RESULT_PATH.read_text())
    if data["core"] != [0, 1, 45]:
        raise AssertionError(data["core"])
    if data["total_shapes"] != 129766:
        raise AssertionError(data["total_shapes"])
    if data["norm_exception_count"] != 1113:
        raise AssertionError(data["norm_exception_count"])
    if data["activation_exception_count"] != 7:
        raise AssertionError(data["activation_exception_count"])
    got = [
        (rec["shape"], rec["activation_primes"])
        for rec in data["activation_exceptions"]
    ]
    if got != EXPECTED:
        raise AssertionError(got)
    print("H3_CORE_0145_CENSUS_CHECK_PASS")


if __name__ == "__main__":
    main()
