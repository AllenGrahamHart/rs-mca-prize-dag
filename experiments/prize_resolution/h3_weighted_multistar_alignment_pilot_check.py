#!/usr/bin/env python3
"""Check the pinned H3 weighted-multistar alignment pilot."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


RESULT = Path(__file__).with_name("h3_weighted_multistar_alignment_pilot_result.json")
INPUT = Path(__file__).with_name("h3_low_distance_ideal_star_alignment_pilot_result.json")
EXPECTED_SHA256 = "2408b1acef2362143e33c6a61099384600bcdc78624a621c8d387f8e9d0e5c63"
EXPECTED = {
    32: (18, 4, 32, 5, 8),
    64: (162, 67, 542, 7, 8),
}


def main() -> None:
    raw = RESULT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256
    rows = json.loads(raw)["results"]
    source = {
        row["order"]: set(row["aligned_ideal_star_primes"])
        for row in json.loads(INPUT.read_text())["results"]
    }
    assert [row["order"] for row in rows] == [32, 64]
    for row in rows:
        survivors = row["weighted_multistar_primes"]
        observed = (
            row["input_two_leaf_primes"],
            len(survivors),
            row["surviving_fiber_count"],
            row["maximum_small_fiber"],
            row["maximum_weighted_degree"],
        )
        assert observed == EXPECTED[row["order"]]
        assert survivors == sorted(set(survivors))
        assert set(survivors) < source[row["order"]]
        assert row["complete"] is True
    print(
        "H3_WEIGHTED_MULTISTAR_ALIGNMENT_PILOT_CHECK_PASS "
        f"n32=18/4 n64=162/67 sha256={EXPECTED_SHA256}"
    )


if __name__ == "__main__":
    main()
