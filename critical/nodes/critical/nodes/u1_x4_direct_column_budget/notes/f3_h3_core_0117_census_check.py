#!/usr/bin/env python3
"""Integrity check for the banked A=[0,1,17] census JSON."""

from __future__ import annotations

import json
from pathlib import Path


RESULT_PATH = Path(
    "critical/nodes/u1_x4_direct_column_budget/notes/"
    "f3_h3_core_0117_census_results.json"
)

EXPECTED = [
    ([0, 1, 17, 5, 25, 86], [32833]),
    ([0, 1, 17, 10, 45, 63], [15361]),
    ([0, 1, 17, 15, 74, 93], [15361]),
    ([0, 1, 17, 22, 41, 85], [32833]),
]


def main() -> None:
    data = json.loads(RESULT_PATH.read_text())
    if data["core"] != [0, 1, 17]:
        raise AssertionError(data["core"])
    if data["total_shapes"] != 129766:
        raise AssertionError(data["total_shapes"])
    if data["norm_exception_count"] != 1228:
        raise AssertionError(data["norm_exception_count"])
    if data["activation_exception_count"] != 4:
        raise AssertionError(data["activation_exception_count"])
    got = [
        (rec["shape"], rec["activation_primes"])
        for rec in data["activation_exceptions"]
    ]
    if got != EXPECTED:
        raise AssertionError(got)
    print("H3_CORE_0117_CENSUS_CHECK_PASS")


if __name__ == "__main__":
    main()
