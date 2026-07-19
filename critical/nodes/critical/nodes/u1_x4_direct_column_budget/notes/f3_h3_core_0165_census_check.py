#!/usr/bin/env python3
"""Integrity check for the banked A=[0,1,65] census JSON."""

from __future__ import annotations

import json
from pathlib import Path


RESULT_PATH = Path(
    "critical/nodes/u1_x4_direct_column_budget/notes/"
    "f3_h3_core_0165_census_results.json"
)

EXPECTED = [
    ([0, 1, 65, 5, 53, 73], [37633]),
    ([0, 1, 65, 7, 55, 77], [67777]),
    ([0, 1, 65, 11, 22, 70], [207073]),
    ([0, 1, 65, 13, 23, 71], [67777]),
    ([0, 1, 65, 13, 61, 89], [37633]),
    ([0, 1, 65, 16, 64, 95], [10177]),
    ([0, 1, 65, 23, 28, 76], [40897]),
    ([0, 1, 65, 25, 29, 77], [37633]),
    ([0, 1, 65, 29, 31, 79], [20929]),
    ([0, 1, 65, 31, 32, 80], [10177]),
    ([0, 1, 65, 37, 41, 85], [37633]),
    ([0, 1, 65, 38, 43, 86], [207073]),
    ([0, 1, 65, 44, 55, 92], [40897]),
    ([0, 1, 65, 47, 61, 95], [20929]),
]


def main() -> None:
    data = json.loads(RESULT_PATH.read_text())
    if data["core"] != [0, 1, 65]:
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
    print("H3_CORE_0165_CENSUS_CHECK_PASS")


if __name__ == "__main__":
    main()
