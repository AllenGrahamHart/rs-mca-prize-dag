#!/usr/bin/env python3
"""Integrity check for the banked A=[0,1,86] census JSON."""

from __future__ import annotations

import json
from pathlib import Path


RESULT_PATH = Path(
    "critical/nodes/u1_x4_direct_column_budget/notes/"
    "f3_h3_core_0186_census_results.json"
)

EXPECTED = [
    ([0, 1, 86, 2, 8, 22], [69313]),
    ([0, 1, 86, 37, 50, 51], [30817]),
    ([0, 1, 86, 37, 60, 71], [30817]),
]


def main() -> None:
    data = json.loads(RESULT_PATH.read_text())
    if data["core"] != [0, 1, 86]:
        raise AssertionError(data["core"])
    if data["total_shapes"] != 129766:
        raise AssertionError(data["total_shapes"])
    if data["norm_exception_count"] != 1110:
        raise AssertionError(data["norm_exception_count"])
    if data["activation_exception_count"] != 3:
        raise AssertionError(data["activation_exception_count"])
    got = [
        (rec["shape"], rec["activation_primes"])
        for rec in data["activation_exceptions"]
    ]
    if got != EXPECTED:
        raise AssertionError(got)
    print("H3_CORE_0186_CENSUS_CHECK_PASS")


if __name__ == "__main__":
    main()
