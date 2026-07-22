#!/usr/bin/env python3
"""Check the c2 reciprocal affine torsion result packet."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT = HERE / "rate_half_list_c2_reciprocal_affine_torsion_result.json"
SOURCE = HERE / "rate_half_list_c2_reciprocal_affine_torsion_modal.py"
ORDER = 1 << 40
LOW_SQUARE = 3 * (1 << 128)
HIGH = 1 << 65
SHARDS = 16


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expected_interval() -> tuple[int, int, int]:
    lower = math.isqrt(LOW_SQUARE)
    if lower * lower < LOW_SQUARE:
        lower += 1
    start = (lower + 1 + ORDER - 1) // ORDER
    stop = HIGH // ORDER + 1
    return lower, start, stop


def trace_terminal(modulus: int, levels: int) -> int:
    value = -2 * pow(3, -1, modulus) % modulus
    for _ in range(levels):
        value = (value * value - 2) % modulus
    return value


def status_code(k_value: int) -> int:
    modulus = k_value * ORDER - 1
    if modulus % 3 == 0:
        return 2
    return int(trace_terminal(modulus, 40) == 2)


def no_hit_digest(start: int, stop: int) -> str:
    digest = hashlib.sha256()
    for k_value in range(start, stop):
        modulus = k_value * ORDER - 1
        code = 2 if modulus % 3 == 0 else 0
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
    assert packet["cost_ceiling_usd"] == 0.25

    rows = packet["shards"]
    assert [(row[0], row[1]) for row in rows] == expected
    assert sum(row[3] for row in rows) == stop - start
    assert sum(row[4] for row in rows) == packet["skipped_factor_three"]

    for start_value, stop_value, digest, processed, skipped, seconds in rows:
        assert processed == stop_value - start_value
        assert 0 < seconds < 60
        assert skipped == sum(
            (k_value * ORDER - 1) % 3 == 0
            for k_value in range(start_value, stop_value)
        )
        assert digest == no_hit_digest(start_value, stop_value)
        samples = {start_value, (start_value + stop_value) // 2, stop_value - 1}
        assert all(status_code(k_value) in (0, 2) for k_value in samples)

    assert trace_terminal(31, 5) == 2
    print(
        "RATE_HALF_LIST_C2_RECIPROCAL_AFFINE_TORSION_SCREEN_PASS "
        f"candidates={stop-start} shards={len(rows)} hits=0 traces=1"
    )


if __name__ == "__main__":
    main()
