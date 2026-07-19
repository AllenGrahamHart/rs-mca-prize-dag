#!/usr/bin/env python3
"""Integrity check for the banked A=[0,1,48] census JSON."""

from __future__ import annotations

import json
from pathlib import Path


RESULT_PATH = Path(
    "critical/nodes/u1_x4_direct_column_budget/notes/"
    "f3_h3_core_0148_census_results.json"
)

EXPECTED = [
    ([0, 1, 48, 2, 31, 63], [207073]),
    ([0, 1, 48, 2, 51, 95], [207073]),
    ([0, 1, 48, 4, 31, 63], [40897]),
    ([0, 1, 48, 4, 47, 90], [49537]),
    ([0, 1, 48, 6, 31, 63], [18913]),
    ([0, 1, 48, 6, 47, 88], [12289]),
    ([0, 1, 48, 12, 31, 63], [30817]),
    ([0, 1, 48, 12, 47, 82], [1857217]),
    ([0, 1, 48, 14, 47, 80], [300673]),
    ([0, 1, 48, 16, 31, 63], [10177]),
    ([0, 1, 48, 16, 47, 78], [26682529]),
    ([0, 1, 48, 20, 47, 74], [12097]),
    ([0, 1, 48, 22, 47, 72], [1033441]),
    ([0, 1, 48, 24, 47, 70], [1033441]),
    ([0, 1, 48, 26, 47, 68], [12097]),
    ([0, 1, 48, 30, 47, 64], [26682529]),
    ([0, 1, 48, 31, 32, 63], [10177]),
    ([0, 1, 48, 31, 36, 63], [30817]),
    ([0, 1, 48, 31, 42, 63], [18913]),
    ([0, 1, 48, 31, 44, 63], [40897]),
    ([0, 1, 48, 31, 46, 63], [207073]),
    ([0, 1, 48, 31, 50, 63], [207073]),
    ([0, 1, 48, 31, 52, 63], [40897]),
    ([0, 1, 48, 31, 54, 63], [18913]),
    ([0, 1, 48, 31, 60, 63], [30817]),
    ([0, 1, 48, 31, 63, 64], [10177]),
    ([0, 1, 48, 31, 63, 80], [10177]),
    ([0, 1, 48, 31, 63, 84], [30817]),
    ([0, 1, 48, 31, 63, 90], [18913]),
    ([0, 1, 48, 31, 63, 92], [40897]),
    ([0, 1, 48, 31, 63, 94], [207073]),
    ([0, 1, 48, 32, 47, 62], [300673]),
    ([0, 1, 48, 34, 47, 60], [1857217]),
    ([0, 1, 48, 40, 47, 54], [12289]),
    ([0, 1, 48, 42, 47, 52], [49537]),
    ([0, 1, 48, 45, 47, 49], [74209]),
    ([0, 1, 48, 50, 51, 95], [207073]),
]


def main() -> None:
    data = json.loads(RESULT_PATH.read_text())
    if data["core"] != [0, 1, 48]:
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
    print("H3_CORE_0148_CENSUS_CHECK_PASS")


if __name__ == "__main__":
    main()
