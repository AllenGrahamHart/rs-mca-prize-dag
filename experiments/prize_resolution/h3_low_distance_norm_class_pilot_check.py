#!/usr/bin/env python3
"""Check the pinned H3 low-distance norm-class pilot result."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


RESULT = Path(__file__).with_name("h3_low_distance_norm_class_pilot_result.json")
EXPECTED_SHA256 = "61f30dd669202102d8360ceb2b013d6fa8106a38e3a7647e8bdbc23b209e69ca"
EXPECTED = {
    32: {
        "2": (1_736, 154, 3, 0, 0),
        "4": (25_067, 1_701, 34, 17, 4),
        "6": (46_046, 2_967, 210, 120, 103),
    },
    64: {
        "2": (8_280, 393, 4, 0, 0),
        "4": (272_595, 9_619, 163, 102, 67),
        "6": (1_278_030, 41_527, 3_735, 2_212, 2_127),
    },
}


def main() -> None:
    raw = RESULT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256
    rows = json.loads(raw)["results"]
    assert [row["order"] for row in rows] == [32, 64]
    for row in rows:
        assert row["complete"] is True
        for square, expected in EXPECTED[row["order"]].items():
            data = row["classes"][square]
            observed = (
                data["raw_edges"],
                data["galois_exchange_orbits"],
                data["distinct_normalized_norms"],
                data["odd_prime_factors"],
                data["relevant_prime_factors"],
            )
            assert observed == expected
        assert row["classes"]["2"]["first_odd_witness"] is None
        assert row["classes"]["4"]["first_odd_witness"] is not None
        assert row["classes"]["6"]["first_odd_witness"] is not None
    print(
        "H3_LOW_DISTANCE_NORM_CLASS_PILOT_CHECK_PASS "
        f"d2=0/0 d4=4/67 d6=103/2127 sha256={EXPECTED_SHA256}"
    )


if __name__ == "__main__":
    main()
