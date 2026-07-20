#!/usr/bin/env python3
"""Check the c=1 parity harmonic characteristic result packet."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT = (
    HERE
    / "rate_half_list_fiber_two_cycle_c1_parity_harmonic_characteristic_result.json"
)
SOURCE = (
    HERE
    / "rate_half_list_fiber_two_cycle_c1_parity_harmonic_characteristic_modal.py"
)
ORDER = 1 << 40
LOW_SQUARE = 3 * (1 << 128)
HIGH = 1 << 65
SHARDS = 32


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expected_interval() -> tuple[int, int, int]:
    lower = math.isqrt(LOW_SQUARE)
    if lower * lower < LOW_SQUARE:
        lower += 1
    start = (lower - 1 + ORDER - 1) // ORDER
    stop = (HIGH - 2) // ORDER + 1
    return lower, start, stop


def trace_terminal(value: int, levels: int, modulus: int) -> int:
    for _ in range(levels):
        value = (value * value - 2) % modulus
    return value


def status_code(k_value: int) -> int:
    modulus = 1 + k_value * ORDER
    if modulus % 5 == 0:
        return 4
    h_r_hit = trace_terminal(16, 40, modulus) == 2
    h_p_start = 8 * pow(5, -1, modulus) % modulus
    h_p_hit = trace_terminal(h_p_start, 41, modulus) == 2
    return int(h_r_hit) + 2 * int(h_p_hit)


def no_hit_digest(start: int, stop: int) -> str:
    digest = hashlib.sha256()
    for k_value in range(start, stop):
        modulus = 1 + k_value * ORDER
        code = 4 if modulus % 5 == 0 else 0
        digest.update(k_value.to_bytes(4, "little"))
        digest.update(bytes((code,)))
    return digest.hexdigest()


def main() -> None:
    packet = json.loads(RESULT.read_text())
    lower, start, stop = expected_interval()
    width = (stop - start + SHARDS - 1) // SHARDS
    expected = [
        (start + index * width, min(stop, start + (index + 1) * width))
        for index in range(SHARDS)
        if start + index * width < stop
    ]

    assert packet["all_complete"] and packet["coverage_exact"]
    assert packet["hits"] == []
    assert packet["order"] == ORDER
    assert packet["lower_characteristic"] == lower
    assert packet["upper_characteristic_exclusive"] == HIGH
    assert packet["k_start"] == start and packet["k_stop"] == stop
    assert packet["expected_candidates"] == packet["processed"] == stop - start
    assert packet["source_sha256"] == sha256(SOURCE)
    assert packet["cost_ceiling_usd"] == 0.50

    rows = packet["shards"]
    assert [(row[0], row[1]) for row in rows] == expected
    assert sum(row[3] for row in rows) == stop - start
    assert sum(row[4] for row in rows) == packet["skipped_factor_five"]

    for start_value, stop_value, digest, processed, skipped, seconds in rows:
        assert processed == stop_value - start_value
        assert 0 < seconds < 60
        assert skipped == sum(
            (1 + k_value * ORDER) % 5 == 0
            for k_value in range(start_value, stop_value)
        )
        assert digest == no_hit_digest(start_value, stop_value)
        samples = {
            start_value,
            (start_value + stop_value) // 2,
            stop_value - 1,
        }
        assert all(status_code(k_value) in (0, 4) for k_value in samples)

    print(
        "RATE_HALF_FIBER_TWO_CYCLE_C1_PARITY_HARMONIC_CHARACTERISTIC_PASS "
        f"candidates={stop-start} shards={len(rows)} hits=0 traces=2"
    )


if __name__ == "__main__":
    main()
