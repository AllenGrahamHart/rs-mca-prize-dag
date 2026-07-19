#!/usr/bin/env python3
"""Check the pinned H3 ideal-star prime-alignment pilot result."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


RESULT = Path(__file__).with_name("h3_low_distance_ideal_star_alignment_pilot_result.json")
INPUT = Path(__file__).with_name("h3_low_distance_ideal_star_gcd_pilot_result.json")
EXPECTED_SHA256 = "6e097c0f7f910be76d09ed4a5557de2cd5ee3aeddcdd01935275b8f16a131a6b"
EXPECTED = {
    32: (103, 18, 88, 5, 10),
    64: (2_127, 162, 1_695, 7, 14),
}


def main() -> None:
    raw = RESULT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256
    rows = json.loads(raw)["results"]
    source = {
        row["order"]: set(row["single_edge_relevant_primes"])
        for row in json.loads(INPUT.read_text())["results"]
    }
    assert [row["order"] for row in rows] == [32, 64]
    for row in rows:
        aligned = row["aligned_ideal_star_primes"]
        observed = (
            row["input_relevant_primes"],
            len(aligned),
            row["aligned_fiber_count"],
            row["maximum_small_fiber"],
            row["maximum_ordered_product_fiber"],
        )
        assert observed == EXPECTED[row["order"]]
        assert aligned == sorted(set(aligned))
        assert set(aligned) < source[row["order"]]
        assert row["complete"] is True
        assert row["rich_rows"] == []
        assert row["positive_x18_rows"] == []
        assert row["c36_violations"] == []
    print(
        "H3_LOW_DISTANCE_IDEAL_STAR_ALIGNMENT_PILOT_CHECK_PASS "
        f"n32=103/18 n64=2127/162 sha256={EXPECTED_SHA256}"
    )


if __name__ == "__main__":
    main()
