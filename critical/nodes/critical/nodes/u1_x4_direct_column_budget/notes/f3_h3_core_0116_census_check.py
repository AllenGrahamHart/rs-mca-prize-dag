#!/usr/bin/env python3
"""Integrity check for the banked A=[0,1,16] census JSON."""

from __future__ import annotations

import json
from pathlib import Path


RESULT_PATH = Path(
    "critical/nodes/u1_x4_direct_column_budget/notes/"
    "f3_h3_core_0116_census_results.json"
)

EXPECTED = [
    ([0, 1, 16, 8, 9, 41], [37633]),
    ([0, 1, 16, 8, 41, 57], [1416317953]),
    ([0, 1, 16, 8, 57, 89], [37633]),
    ([0, 1, 16, 9, 41, 56], [37633]),
    ([0, 1, 16, 9, 56, 89], [1416317953]),
    ([0, 1, 16, 24, 52, 75], [20161]),
    ([0, 1, 16, 56, 57, 89], [37633]),
]


def main() -> None:
    data = json.loads(RESULT_PATH.read_text())
    if data["core"] != [0, 1, 16]:
        raise AssertionError(data["core"])
    if data["total_shapes"] != 129766:
        raise AssertionError(data["total_shapes"])
    if data["norm_exception_count"] != 1275:
        raise AssertionError(data["norm_exception_count"])
    if data["activation_exception_count"] != 7:
        raise AssertionError(data["activation_exception_count"])
    got = [
        (rec["shape"], rec["activation_primes"])
        for rec in data["activation_exceptions"]
    ]
    if got != EXPECTED:
        raise AssertionError(got)
    print("H3_CORE_0116_CENSUS_CHECK_PASS")


if __name__ == "__main__":
    main()
