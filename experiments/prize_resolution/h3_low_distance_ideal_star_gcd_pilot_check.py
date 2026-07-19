#!/usr/bin/env python3
"""Check the pinned H3 ideal-star gcd pilot result."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


RESULT = Path(__file__).with_name("h3_low_distance_ideal_star_gcd_pilot_result.json")
EXPECTED_SHA256 = "17f47ce015e1d70327fb78a126c3f8afe0366074af6d83367866f57b0e353ab8"
EXPECTED = {
    32: (435, 40, 72_849, 4_822, 24_407_583, 227, 103, 1_168, 64),
    64: (1_891, 87, 1_558_905, 51_539, 2_569_691_591, 3_836, 2_127, 22_523, 144),
}


def main() -> None:
    raw = RESULT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256
    rows = json.loads(raw)["results"]
    assert [row["order"] for row in rows] == [32, 64]
    for row in rows:
        expected = EXPECTED[row["order"]]
        observed = (
            row["small_vector_pairs"],
            row["galois_center_orbits"],
            row["raw_low_edges"],
            row["galois_exchange_edge_orbits"],
            row["raw_rooted_stars"],
            row["distinct_normalized_principal_norms"],
            len(row["single_edge_relevant_primes"]),
            row["center_prime_rows"],
            row["maximum_prime_incidence"],
        )
        assert observed == expected
        assert row["complete"] is True
        assert row["single_edge_relevant_primes"] == row["two_incident_edge_relevant_primes"]
        assert row["single_edge_relevant_primes"] == sorted(set(row["single_edge_relevant_primes"]))
        assert all(
            prime >= row["order"] ** 2 and prime % row["order"] == 1
            for prime in row["single_edge_relevant_primes"]
        )
    print(
        "H3_LOW_DISTANCE_IDEAL_STAR_GCD_PILOT_CHECK_PASS "
        f"n32=103/103 n64=2127/2127 sha256={EXPECTED_SHA256}"
    )


if __name__ == "__main__":
    main()
