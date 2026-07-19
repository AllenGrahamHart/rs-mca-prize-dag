#!/usr/bin/env python3
"""Check the harmonic characteristic result packet and shard coverage."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RESULT = Path(__file__).with_name(
    "rate_half_list_deleted_pair_harmonic_characteristic_result.json"
)
SOURCE = Path(__file__).with_name(
    "rate_half_list_deleted_pair_harmonic_characteristic_modal.py"
)
ORDER = 1 << 40
LOW_SQUARE = 3 * (1 << 128)
HIGH = 1 << 65
SHARDS = 32


def digest_range(start: int, stop: int) -> str:
    digest = hashlib.sha256()
    for k_value in range(start, stop):
        digest.update(k_value.to_bytes(4, "little"))
        digest.update((-1).to_bytes(2, "little", signed=True))
    return digest.hexdigest()


def trace_hit(k_value: int) -> int:
    p_value = 1 + k_value * ORDER
    trace = 4
    for index in range(1, 39):
        trace = (trace * trace - 2) % p_value
        if trace == 0:
            return index
    return -1


def main() -> None:
    packet = json.loads(RESULT.read_text())
    lower = math.isqrt(LOW_SQUARE)
    if lower * lower < LOW_SQUARE:
        lower += 1
    start = (lower - 1 + ORDER - 1) // ORDER
    stop = (HIGH - 2) // ORDER + 1
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
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == packet["source_sha256"]
    assert [(row[0], row[1]) for row in packet["shards"]] == expected

    for row in packet["shards"]:
        shard_start, shard_stop, expected_digest = row
        assert digest_range(shard_start, shard_stop) == expected_digest
        samples = {shard_start, (shard_start + shard_stop) // 2, shard_stop - 1}
        assert all(trace_hit(k_value) == -1 for k_value in samples)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    harmonic = "rate_half_list_budget_three_antipodal_generic_deleted_pair_harmonic_exclusion"
    if harmonic in nodes:
        assert nodes[harmonic]["status"] == "PROVED"

    print(
        "RATE_HALF_DELETED_PAIR_HARMONIC_CHARACTERISTIC_PASS "
        f"candidates={stop-start} shards={len(expected)} hits=0"
    )


if __name__ == "__main__":
    main()
