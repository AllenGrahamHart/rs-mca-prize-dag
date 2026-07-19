#!/usr/bin/env python3
"""Integrity check for the banked A=[0,1,49] census JSON."""

from __future__ import annotations

import json
from pathlib import Path


RESULT_PATH = Path(
    "critical/nodes/u1_x4_direct_column_budget/notes/"
    "f3_h3_core_0149_census_results.json"
)

EXPECTED = [
    ([0, 1, 49, 2, 46, 47], [207073]),
    ([0, 1, 49, 2, 46, 95], [207073]),
    ([0, 1, 49, 3, 34, 66], [207073]),
    ([0, 1, 49, 5, 34, 66], [40897]),
    ([0, 1, 49, 7, 34, 66], [18913]),
    ([0, 1, 49, 7, 50, 93], [49537]),
    ([0, 1, 49, 9, 50, 91], [12289]),
    ([0, 1, 49, 13, 34, 66], [30817]),
    ([0, 1, 49, 15, 50, 85], [1857217]),
    ([0, 1, 49, 17, 34, 66], [10177]),
    ([0, 1, 49, 17, 50, 83], [300673]),
    ([0, 1, 49, 19, 50, 81], [26682529]),
    ([0, 1, 49, 23, 50, 77], [12097]),
    ([0, 1, 49, 25, 50, 75], [1033441]),
    ([0, 1, 49, 27, 50, 73], [1033441]),
    ([0, 1, 49, 29, 50, 71], [12097]),
    ([0, 1, 49, 33, 34, 66], [10177]),
    ([0, 1, 49, 33, 50, 67], [26682529]),
    ([0, 1, 49, 34, 37, 66], [30817]),
    ([0, 1, 49, 34, 43, 66], [18913]),
    ([0, 1, 49, 34, 45, 66], [40897]),
    ([0, 1, 49, 34, 47, 66], [207073]),
    ([0, 1, 49, 34, 51, 66], [207073]),
    ([0, 1, 49, 34, 53, 66], [40897]),
    ([0, 1, 49, 34, 55, 66], [18913]),
    ([0, 1, 49, 34, 61, 66], [30817]),
    ([0, 1, 49, 34, 65, 66], [10177]),
    ([0, 1, 49, 34, 66, 81], [10177]),
    ([0, 1, 49, 34, 66, 85], [30817]),
    ([0, 1, 49, 34, 66, 91], [18913]),
    ([0, 1, 49, 34, 66, 93], [40897]),
    ([0, 1, 49, 34, 66, 95], [207073]),
    ([0, 1, 49, 35, 50, 65], [300673]),
    ([0, 1, 49, 37, 50, 63], [1857217]),
    ([0, 1, 49, 43, 50, 57], [12289]),
    ([0, 1, 49, 45, 50, 55], [49537]),
    ([0, 1, 49, 48, 50, 52], [74209]),
]


def main() -> None:
    data = json.loads(RESULT_PATH.read_text())
    if data["core"] != [0, 1, 49]:
        raise AssertionError(data["core"])
    if data["total_shapes"] != 129766:
        raise AssertionError(data["total_shapes"])
    if data["norm_exception_count"] != 1067:
        raise AssertionError(data["norm_exception_count"])
    if data["activation_exception_count"] != 37:
        raise AssertionError(data["activation_exception_count"])
    got = [
        (rec["shape"], rec["activation_primes"])
        for rec in data["activation_exceptions"]
    ]
    if got != EXPECTED:
        raise AssertionError(got)
    print("H3_CORE_0149_CENSUS_CHECK_PASS")


if __name__ == "__main__":
    main()
