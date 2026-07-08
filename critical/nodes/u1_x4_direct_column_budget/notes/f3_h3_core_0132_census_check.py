#!/usr/bin/env python3
"""Integrity check for the banked A=[0,1,32] census JSON."""

from __future__ import annotations

import json
from pathlib import Path


RESULT_PATH = Path(
    "critical/nodes/u1_x4_direct_column_budget/notes/"
    "f3_h3_core_0132_census_results.json"
)

EXPECTED = [
    ([0, 1, 32, 2, 33, 81], [10177]),
    ([0, 1, 32, 2, 36, 50], [20929]),
    ([0, 1, 32, 5, 42, 53], [40897]),
    ([0, 1, 32, 8, 36, 84], [37633]),
    ([0, 1, 32, 11, 54, 59], [207073]),
    ([0, 1, 32, 12, 56, 60], [37633]),
    ([0, 1, 32, 17, 65, 66], [10177]),
    ([0, 1, 32, 18, 66, 68], [20929]),
    ([0, 1, 32, 20, 42, 90], [67777]),
    ([0, 1, 32, 20, 68, 72], [37633]),
    ([0, 1, 32, 21, 69, 74], [40897]),
    ([0, 1, 32, 24, 44, 92], [37633]),
    ([0, 1, 32, 26, 74, 84], [67777]),
    ([0, 1, 32, 27, 75, 86], [207073]),
]


def main() -> None:
    data = json.loads(RESULT_PATH.read_text())
    if data["core"] != [0, 1, 32]:
        raise AssertionError(data["core"])
    if data["total_shapes"] != 129766:
        raise AssertionError(data["total_shapes"])
    if data["norm_exception_count"] != 957:
        raise AssertionError(data["norm_exception_count"])
    if data["activation_exception_count"] != 14:
        raise AssertionError(data["activation_exception_count"])
    got = [
        (rec["shape"], rec["activation_primes"])
        for rec in data["activation_exceptions"]
    ]
    if got != EXPECTED:
        raise AssertionError(got)
    print("H3_CORE_0132_CENSUS_CHECK_PASS")


if __name__ == "__main__":
    main()
