#!/usr/bin/env python3
"""Audit the saved N10 census packet's deterministic arithmetic.

This checks provenance and aggregation, not the remote exhaustive search.
"""

from __future__ import annotations

import hashlib
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "experiments/prize_resolution/l1_balanced_mixed_growth_census_modal.py"
EXPECTED_SHA256 = "08ff22fa18be71ff4bb8ef7f6322d0b0fdc7d79933b2ef802256c8aff1c96cc8"


def candidate_count(n: int) -> int:
    k = n // 2
    total = 0
    for core_count in range(4):
        for background in (0, 1):
            for omitted in (1, 2, 3):
                if core_count + background - omitted < 1:
                    continue
                omission_count = math.comb(k, omitted)
                if omitted == 2:
                    omission_count -= k // 2
                total += math.comb(k - 1, core_count) * omission_count
    return total


def main() -> None:
    digest = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    assert digest == EXPECTED_SHA256, (digest, EXPECTED_SHA256)

    assert [candidate_count(n) for n in (16, 32, 64, 128)] == [
        5_096,
        386_640,
        27_152_032,
        1_821_304_128,
    ]

    consecutive_partial = 99_105
    consecutive_retry = 10_286
    consecutive = consecutive_partial + consecutive_retry
    geometric = 108_600
    assert consecutive == 109_391
    assert 109_329 + 62 == consecutive
    assert 987 + 108_404 == consecutive
    assert 108_547 + 53 == geometric
    assert 6 + 1_001 + 107_593 == geometric

    consecutive_counts = (43, 2_879, consecutive)
    geometric_counts = (33, 2_857, geometric)
    consecutive_exponents = [
        math.log2(right / left)
        for left, right in zip(consecutive_counts, consecutive_counts[1:])
    ]
    geometric_exponents = [
        math.log2(right / left)
        for left, right in zip(geometric_counts, geometric_counts[1:])
    ]
    assert abs(consecutive_exponents[0] - 6.065087318861337) < 1e-12
    assert abs(consecutive_exponents[1] - 5.247782448057918) < 1e-12
    assert abs(geometric_exponents[0] - 6.435891201577919) < 1e-12
    assert abs(geometric_exponents[1] - 5.248379256642714) < 1e-12

    worker_seconds = 452.0566 + 48.335 + 497.6485
    published_rate = 0.0000131 + 0.00000222
    assert abs(worker_seconds - 998.0401) < 1e-9
    assert 0.015 < worker_seconds * published_rate < 0.016

    print("L1_N10_PACKET_AUDIT_PASS")


if __name__ == "__main__":
    main()
