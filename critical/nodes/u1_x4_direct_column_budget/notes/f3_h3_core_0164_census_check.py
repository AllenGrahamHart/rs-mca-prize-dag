#!/usr/bin/env python3
"""Integrity check for the banked A=[0,1,64] census JSON."""

from __future__ import annotations

import json
from pathlib import Path


RESULT_PATH = Path(
    "critical/nodes/u1_x4_direct_column_budget/notes/"
    "f3_h3_core_0164_census_results.json"
)

EXPECTED = [
    ([0, 1, 64, 2, 50, 68], [12289]),
    ([0, 1, 64, 2, 62, 80], [12289]),
    ([0, 1, 64, 4, 60, 80], [37633]),
    ([0, 1, 64, 6, 19, 67], [18913]),
    ([0, 1, 64, 6, 54, 76], [20929]),
    ([0, 1, 64, 6, 58, 80], [67777]),
    ([0, 1, 64, 7, 55, 78], [18913]),
    ([0, 1, 64, 8, 9, 89], [37633]),
    ([0, 1, 64, 8, 41, 57], [37633]),
    ([0, 1, 64, 9, 56, 89], [37633]),
    ([0, 1, 64, 10, 54, 80], [67777]),
    ([0, 1, 64, 12, 32, 77], [207073]),
    ([0, 1, 64, 12, 52, 80], [37633]),
    ([0, 1, 64, 12, 60, 88], [37633]),
    ([0, 1, 64, 13, 61, 90], [30817]),
    ([0, 1, 64, 14, 50, 80], [12289]),
    ([0, 1, 64, 14, 62, 92], [27361]),
    ([0, 1, 64, 15, 63, 94], [207073]),
    ([0, 1, 64, 20, 26, 74], [27361]),
    ([0, 1, 64, 26, 38, 80], [27361]),
    ([0, 1, 64, 28, 30, 78], [67777]),
    ([0, 1, 64, 28, 36, 80], [37633]),
    ([0, 1, 64, 30, 34, 80], [20929]),
    ([0, 1, 64, 33, 34, 81], [10177]),
    ([0, 1, 64, 36, 40, 84], [37633]),
    ([0, 1, 64, 37, 42, 85], [30817]),
    ([0, 1, 64, 38, 44, 86], [12289]),
    ([0, 1, 64, 41, 56, 57], [37633]),
    ([0, 1, 64, 45, 58, 93], [40897]),
    ([0, 1, 64, 74, 80, 86], [27361]),
    ([0, 1, 64, 76, 80, 84], [37633]),
    ([0, 1, 64, 78, 80, 82], [20929]),
]


def main() -> None:
    data = json.loads(RESULT_PATH.read_text())
    if data["core"] != [0, 1, 64]:
        raise AssertionError(data["core"])
    if data["total_shapes"] != 129766:
        raise AssertionError(data["total_shapes"])
    if data["norm_exception_count"] != 1074:
        raise AssertionError(data["norm_exception_count"])
    if data["activation_exception_count"] != 32:
        raise AssertionError(data["activation_exception_count"])
    got = [
        (rec["shape"], rec["activation_primes"])
        for rec in data["activation_exceptions"]
    ]
    if got != EXPECTED:
        raise AssertionError(got)
    print("H3_CORE_0164_CENSUS_CHECK_PASS")


if __name__ == "__main__":
    main()
