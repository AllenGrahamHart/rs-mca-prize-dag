#!/usr/bin/env python3
"""Integrity check for the banked A=[0,1,52] census JSON."""

from __future__ import annotations

import json
from pathlib import Path


RESULT_PATH = Path(
    "critical/nodes/u1_x4_direct_column_budget/notes/"
    "f3_h3_core_0152_census_results.json"
)

EXPECTED = [
    ([0, 1, 52, 3, 50, 51], [207073]),
    ([0, 1, 52, 5, 40, 92], [37633]),
    ([0, 1, 52, 9, 12, 85], [37633]),
    ([0, 1, 52, 12, 56, 93], [37633]),
    ([0, 1, 52, 13, 40, 89], [37633]),
    ([0, 1, 52, 20, 53, 84], [207073]),
    ([0, 1, 52, 41, 44, 59], [15937]),
]


def main() -> None:
    data = json.loads(RESULT_PATH.read_text())
    if data["core"] != [0, 1, 52]:
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
    print("H3_CORE_0152_CENSUS_CHECK_PASS")


if __name__ == "__main__":
    main()
