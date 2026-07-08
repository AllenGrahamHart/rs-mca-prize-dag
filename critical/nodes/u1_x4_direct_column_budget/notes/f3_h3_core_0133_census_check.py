#!/usr/bin/env python3
"""Integrity check for the banked A=[0,1,33] census JSON."""

from __future__ import annotations

import json
from pathlib import Path


RESULT_PATH = Path(
    "critical/nodes/u1_x4_direct_column_budget/notes/"
    "f3_h3_core_0133_census_results.json"
)

EXPECTED = [
    ([0, 1, 33, 3, 34, 82], [207073]),
    ([0, 1, 33, 4, 39, 52], [40897]),
    ([0, 1, 33, 5, 35, 83], [27361]),
    ([0, 1, 33, 7, 36, 84], [30817]),
    ([0, 1, 33, 8, 41, 88], [37633]),
    ([0, 1, 33, 8, 88, 89], [37633]),
    ([0, 1, 33, 9, 37, 85], [37633]),
    ([0, 1, 33, 11, 17, 23], [27361]),
    ([0, 1, 33, 11, 53, 59], [12289]),
    ([0, 1, 33, 12, 55, 60], [30817]),
    ([0, 1, 33, 13, 17, 21], [37633]),
    ([0, 1, 33, 13, 57, 61], [37633]),
    ([0, 1, 33, 15, 17, 19], [20929]),
    ([0, 1, 33, 16, 63, 64], [10177]),
    ([0, 1, 33, 17, 35, 95], [12289]),
    ([0, 1, 33, 17, 37, 93], [37633]),
    ([0, 1, 33, 17, 39, 91], [67777]),
    ([0, 1, 33, 17, 43, 87], [67777]),
    ([0, 1, 33, 17, 45, 85], [37633]),
    ([0, 1, 33, 17, 47, 83], [12289]),
    ([0, 1, 33, 17, 59, 71], [27361]),
    ([0, 1, 33, 17, 61, 69], [37633]),
    ([0, 1, 33, 17, 63, 67], [20929]),
    ([0, 1, 33, 19, 42, 90], [18913]),
    ([0, 1, 33, 19, 67, 69], [67777]),
    ([0, 1, 33, 20, 65, 85], [207073]),
    ([0, 1, 33, 21, 43, 91], [20929]),
    ([0, 1, 33, 23, 71, 77], [27361]),
    ([0, 1, 33, 29, 47, 95], [12289]),
    ([0, 1, 33, 30, 78, 91], [18913]),
    ([0, 1, 33, 40, 41, 56], [37633]),
    ([0, 1, 33, 40, 56, 89], [37633]),
]


def main() -> None:
    data = json.loads(RESULT_PATH.read_text())
    if data["core"] != [0, 1, 33]:
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
    print("H3_CORE_0133_CENSUS_CHECK_PASS")


if __name__ == "__main__":
    main()
