#!/usr/bin/env python3
"""Check the doubled-order harmonic top-characteristic result packet."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT = HERE / "rate_half_list_fiber_two_cycle_harmonic_top_characteristic_result.json"
SOURCE = HERE / "rate_half_list_fiber_two_cycle_harmonic_top_characteristic_modal.py"
PRIOR = HERE / "rate_half_list_deleted_pair_harmonic_characteristic_result.json"
ORDER = 1 << 40
SPLIT_ORDER = 1 << 41
LOW_SQUARE = 3 * (1 << 128)
HIGH = 1 << 65
SHARDS = 16


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expected_interval() -> tuple[int, int, int, int]:
    lower = math.isqrt(LOW_SQUARE)
    if lower * lower < LOW_SQUARE:
        lower += 1
    start = (lower - 1 + ORDER - 1) // ORDER
    stop = (HIGH - 2) // ORDER + 1
    first_even = start + (start & 1)
    count = (stop - first_even + 1) // 2
    return lower, start, stop, count


def digest_range(first_even: int, start: int, stop: int) -> str:
    digest = hashlib.sha256()
    for ordinal in range(start, stop):
        k_value = first_even + 2 * ordinal
        digest.update(k_value.to_bytes(4, "little"))
        digest.update(b"\x00")
    return digest.hexdigest()


def trace_39(k_value: int) -> int:
    modulus = 1 + k_value * ORDER
    trace = 4
    for _ in range(39):
        trace = (trace * trace - 2) % modulus
    return trace


def main() -> None:
    packet = json.loads(RESULT.read_text())
    prior = json.loads(PRIOR.read_text())
    lower, start, stop, count = expected_interval()
    first_even = start + (start & 1)
    width = (count + SHARDS - 1) // SHARDS
    expected = [
        (shard * width, min(count, (shard + 1) * width))
        for shard in range(SHARDS)
        if shard * width < count
    ]

    assert packet["all_complete"] and packet["coverage_exact"]
    assert packet["hits"] == []
    assert packet["order"] == ORDER and packet["split_order"] == SPLIT_ORDER
    assert packet["lower_characteristic"] == lower
    assert packet["upper_characteristic_exclusive"] == HIGH
    assert packet["k_start"] == start and packet["k_stop"] == stop
    assert packet["parity"] == "even"
    assert packet["expected_candidates"] == packet["processed"] == count
    assert packet["source_sha256"] == sha256(SOURCE)
    assert packet["prior_levels_result_sha256"] == sha256(PRIOR)
    assert prior["all_complete"] and prior["coverage_exact"] and prior["hits"] == []

    rows = packet["shards"]
    assert [(row[0], row[1]) for row in rows] == expected
    assert sum(row[3] for row in rows) == count
    for start_ordinal, stop_ordinal, digest, processed, seconds in rows:
        assert processed == stop_ordinal - start_ordinal
        assert 0 < seconds < 60
        assert digest == digest_range(first_even, start_ordinal, stop_ordinal)
        samples = {
            start_ordinal,
            (start_ordinal + stop_ordinal) // 2,
            stop_ordinal - 1,
        }
        assert all(trace_39(first_even + 2 * ordinal) != 0 for ordinal in samples)

    print(
        "RATE_HALF_FIBER_TWO_CYCLE_HARMONIC_TOP_CHARACTERISTIC_PASS "
        f"candidates={count} shards={len(rows)} hits=0 prior_levels=38"
    )


if __name__ == "__main__":
    main()
