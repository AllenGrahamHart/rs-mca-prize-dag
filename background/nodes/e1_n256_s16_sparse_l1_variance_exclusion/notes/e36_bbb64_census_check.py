#!/usr/bin/env python3
"""Independently check the complete E=36 inner-layer Schur census."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e36_bbb64_census.cpp"
RESULT = HERE / "e36_bbb64_census_result.json"
SHARDS = 16


def schur_count(representatives: list[int]) -> int:
    layer = set(representatives) | {(-value) % 64 for value in representatives}
    assert len(layer) == 16 and 0 not in layer and 32 not in layer
    return sum(
        (-left - right) % 64 in layer
        for left in layer
        for right in layer
    )


def expected_shard_count(shard: int) -> int:
    return sum(
        math.comb(31 - first, 7)
        for first in range(1 + shard, 25, SHARDS)
    )


def main() -> None:
    packet = json.loads(RESULT.read_text())
    assert packet["schema"] == "e1-e36-bbb64-census-v1"
    assert packet["complete"] is True and packet["errors"] == []
    assert packet["source_sha256"] == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    results = packet["results"]
    assert len(results) == SHARDS
    assert {int(result["shard"]) for result in results} == set(range(SHARDS))
    for result in results:
        assert result["complete"] is True and result["shards"] == SHARDS
        assert result["processed"] == expected_shard_count(int(result["shard"]))
        representatives = [int(value) for value in result["representatives"]]
        assert representatives == sorted(representatives)
        assert schur_count(representatives) == result["best"]
    assert packet["processed"] == sum(
        expected_shard_count(shard) for shard in range(SHARDS)
    ) == math.comb(31, 8)
    assert packet["best"] in results
    assert packet["best"]["best"] == max(int(result["best"]) for result in results)
    print(
        "E1_E36_BBB64_CENSUS_CHECK_PASS "
        f"sets={packet['processed']} maximum={packet['best']['best']}"
    )


if __name__ == "__main__":
    main()
