#!/usr/bin/env python3
"""Integrity check for the banked A=[0,1,31] census JSON."""

from __future__ import annotations

import json
from pathlib import Path


RESULT_PATH = Path(
    "critical/nodes/u1_x4_direct_column_budget/notes/"
    "f3_h3_core_0131_census_results.json"
)

EXPECTED = [
    ([0, 1, 31, 13, 18, 43], [27361]),
    ([0, 1, 31, 17, 80, 82], [10177]),
    ([0, 1, 31, 19, 78, 85], [27361]),
    ([0, 1, 31, 46, 47, 80], [10177]),
]


def main() -> None:
    data = json.loads(RESULT_PATH.read_text())
    if data["core"] != [0, 1, 31]:
        raise AssertionError(data["core"])
    if data["total_shapes"] != 129766:
        raise AssertionError(data["total_shapes"])
    if data["norm_exception_count"] != 1070:
        raise AssertionError(data["norm_exception_count"])
    if data["activation_exception_count"] != 4:
        raise AssertionError(data["activation_exception_count"])
    got = [
        (rec["shape"], rec["activation_primes"])
        for rec in data["activation_exceptions"]
    ]
    if got != EXPECTED:
        raise AssertionError(got)
    print("H3_CORE_0131_CENSUS_CHECK_PASS")


if __name__ == "__main__":
    main()
