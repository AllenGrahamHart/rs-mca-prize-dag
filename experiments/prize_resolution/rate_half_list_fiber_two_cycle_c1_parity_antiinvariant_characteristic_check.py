#!/usr/bin/env python3
"""Check the c=1 parity anti-invariant characteristic result packet."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT = (
    HERE
    / "rate_half_list_fiber_two_cycle_c1_parity_antiinvariant_characteristic_result.json"
)
SOURCE = (
    HERE
    / "rate_half_list_fiber_two_cycle_c1_parity_antiinvariant_characteristic_modal.py"
)
ORDER = 1 << 40
LOW_SQUARE = 3 * (1 << 128)
HIGH = 1 << 65
SHARDS = 16


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expected_interval() -> tuple[int, int, int, int, int]:
    lower = math.isqrt(LOW_SQUARE)
    if lower * lower < LOW_SQUARE:
        lower += 1
    start = (lower - 1 + ORDER - 1) // ORDER
    stop = (HIGH - 2) // ORDER + 1
    first_odd = start if start % 2 else start + 1
    odd_count = (stop - first_odd + 1) // 2
    return lower, start, stop, first_odd, odd_count


def trace_terminal(value: int, levels: int, modulus: int) -> int:
    for _ in range(levels):
        value = (value * value - 2) % modulus
    return value


def status_code(index: int, first_odd: int) -> int:
    k_value = first_odd + 2 * index
    modulus = 1 + k_value * ORDER
    if modulus % 5 == 0:
        return 4
    r_hit = trace_terminal(-8 % modulus, 40, modulus) == 2
    p_start = 6 * pow(5, -1, modulus) % modulus
    p_hit = trace_terminal(p_start, 40, modulus) == 2
    return int(r_hit) + 2 * int(p_hit)


def no_hit_digest(index_start: int, index_stop: int, first_odd: int) -> str:
    digest = hashlib.sha256()
    for index in range(index_start, index_stop):
        k_value = first_odd + 2 * index
        modulus = 1 + k_value * ORDER
        code = 4 if modulus % 5 == 0 else 0
        digest.update(k_value.to_bytes(4, "little"))
        digest.update(bytes((code,)))
    return digest.hexdigest()


def main() -> None:
    packet = json.loads(RESULT.read_text())
    lower, start, stop, first_odd, odd_count = expected_interval()
    width = (odd_count + SHARDS - 1) // SHARDS
    expected = [
        (index * width, min(odd_count, (index + 1) * width))
        for index in range(SHARDS)
        if index * width < odd_count
    ]

    assert packet["all_complete"] and packet["coverage_exact"]
    assert packet["hits"] == []
    assert packet["order"] == ORDER
    assert packet["lower_characteristic"] == lower
    assert packet["upper_characteristic_exclusive"] == HIGH
    assert packet["k_start"] == start and packet["k_stop"] == stop
    assert packet["odd_candidates"] == packet["processed"] == odd_count
    assert packet["source_sha256"] == sha256(SOURCE)
    assert packet["cost_ceiling_usd"] == 0.25

    rows = packet["shards"]
    assert [(row[0], row[1]) for row in rows] == expected
    assert sum(row[3] for row in rows) == odd_count
    assert sum(row[4] for row in rows) == packet["skipped_factor_five"]

    for index_start, index_stop, digest, processed, skipped, seconds in rows:
        assert processed == index_stop - index_start
        assert 0 < seconds < 60
        assert skipped == sum(
            (1 + (first_odd + 2 * index) * ORDER) % 5 == 0
            for index in range(index_start, index_stop)
        )
        assert digest == no_hit_digest(index_start, index_stop, first_odd)
        samples = {
            index_start,
            (index_start + index_stop) // 2,
            index_stop - 1,
        }
        assert all(status_code(index, first_odd) in (0, 4) for index in samples)

    print(
        "RATE_HALF_FIBER_TWO_CYCLE_C1_PARITY_ANTIINVARIANT_PASS "
        f"candidates={odd_count} shards={len(rows)} hits=0 traces=2"
    )


if __name__ == "__main__":
    main()

