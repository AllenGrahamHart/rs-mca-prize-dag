#!/usr/bin/env python3
"""Check the pinned order-64 primary-gap high-characteristic pilot."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


RESULT = Path(__file__).with_name("rate_half_list_order64_primary_gap_result.json")
EXPECTED_SHA256 = "26d48487a885ccd31a01a7b336e3b3c0c4574ed08c6957721ab4c394a078138e"
EXPECTED_COUNTS = {
    193: (3_328, 64),
    4_289: (64, 0),
    4_481: (64, 0),
    4_673: (128, 0),
    4_801: (64, 0),
    4_993: (192, 0),
    5_441: (0, 0),
    5_569: (0, 0),
    5_953: (128, 0),
}


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    for divisor in range(2, math.isqrt(value) + 1):
        if value % divisor == 0:
            return False
    return True


def main() -> None:
    raw = RESULT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256
    payload = json.loads(raw)
    assert payload["order"] == 64
    assert payload["app_id"] == "ap-wLXZpGxaBiBlZ1NZ3MP14e"
    rows = payload["results"]
    assert [row["prime"] for row in rows] == list(EXPECTED_COUNTS)
    for row in rows:
        prime = row["prime"]
        assert is_prime(prime)
        assert (prime - 1) % 64 == 0
        assert row["complete"] is True
        assert row["processed"] == math.comb(64, 4)
        assert pow(row["zeta"], 64, prime) == 1
        assert pow(row["zeta"], 32, prime) != 1
        assert (row["single"], row["double"]) == EXPECTED_COUNTS[prime]
        assert row["first"] == (
            [0, 1, 3, 62] if prime == 193 else [-1, -1, -1, -1]
        )
    high_characteristic = rows[1:]
    assert payload["threshold"] == "p>=64^2 and p=1 mod 64"
    assert all(row["prime"] >= 64**2 for row in high_characteristic)
    assert all(row["double"] == 0 for row in high_characteristic)
    print(
        "RATE_HALF_LIST_ORDER64_PRIMARY_GAP_CHECK_PASS "
        f"high_characteristic_primes={len(high_characteristic)} "
        f"falsifiers=0 sha256={EXPECTED_SHA256}"
    )


if __name__ == "__main__":
    main()
