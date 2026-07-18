#!/usr/bin/env python3
"""Check the pinned H3 low-distance norm-template pilot result."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


RESULT = Path(__file__).with_name("h3_low_distance_norm_template_pilot_result.json")
EXPECTED_SHA256 = "ec1c79b660a15cad985423b6536e39acf9408e3b349113c5e065d40f43a026bf"


def main() -> None:
    raw = RESULT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256
    rows = json.loads(raw)["results"]
    assert [row["order"] for row in rows] == [32, 64]
    small, scaling = rows

    assert small["complete_norm_census"] is True
    assert small["raw_low_edges"] == 77_656
    assert sum(map(int, small["distance_histogram"].values())) == 77_656
    assert small["galois_exchange_orbits"] == small["norms_computed"] == 5_216
    assert small["distinct_absolute_norms"] == 227
    assert len(small["relevant_primes"]) == 103
    assert small["relevant_primes"] == sorted(set(small["relevant_primes"]))
    assert all(prime >= 32**2 and prime % 32 == 1 for prime in small["relevant_primes"])

    assert scaling["complete_norm_census"] is False
    assert scaling["raw_low_edges"] == 1_580_720
    assert sum(map(int, scaling["distance_histogram"].values())) == 1_580_720
    assert scaling["galois_exchange_orbits"] == 52_494
    assert scaling["norms_computed"] == 5_000
    assert scaling["distinct_absolute_norms"] == 2_567

    toy_compression = Fraction(5_216, 227)
    scaling_compression = Fraction(5_000, 2_567)
    assert toy_compression > 22
    assert scaling_compression < 2
    print(
        "H3_LOW_DISTANCE_NORM_TEMPLATE_PILOT_CHECK_PASS "
        "n32=5216/227 relevant_primes=103 n64_sample=5000/2567 "
        f"sha256={EXPECTED_SHA256}"
    )


if __name__ == "__main__":
    main()
