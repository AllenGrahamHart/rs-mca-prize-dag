#!/usr/bin/env python3
"""Verify the h=6 n=64 extra-prime Modal sweep."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
OUT = (
    ROOT
    / "critical/nodes/u1_x4_direct_column_budget/notes"
    / "f3_h6_n64_extra_primes_certificate.json"
)

EXPECTED_P4993_WITNESSES = [
    {
        "left": [0, 5, 13, 32, 37, 45],
        "right": [16, 18, 26, 48, 50, 58],
        "left_last": 269,
        "right_last": 4061,
        "shard": 0,
    },
    {
        "left": [0, 2, 10, 32, 34, 42],
        "right": [16, 21, 29, 48, 53, 61],
        "left_last": 932,
        "right_last": 4724,
        "shard": 0,
    },
    {
        "left": [0, 19, 24, 32, 51, 56],
        "right": [3, 5, 13, 35, 37, 45],
        "left_last": 3611,
        "right_last": 4881,
        "shard": 3,
    },
    {
        "left": [0, 22, 24, 32, 54, 56],
        "right": [6, 11, 19, 38, 43, 51],
        "left_last": 1058,
        "right_last": 2534,
        "shard": 6,
    },
    {
        "left": [0, 8, 27, 32, 40, 59],
        "right": [11, 13, 21, 43, 45, 53],
        "left_last": 3657,
        "right_last": 2717,
        "shard": 11,
    },
    {
        "left": [0, 8, 30, 32, 40, 62],
        "right": [14, 19, 27, 46, 51, 59],
        "left_last": 2598,
        "right_last": 4061,
        "shard": 14,
    },
]


def decode_mask(mask: int) -> list[int]:
    return [i for i in range(64) if (mask >> i) & 1]


def normalized_witnesses(witnesses: list[dict]) -> list[dict]:
    normalized = []
    for item in witnesses:
        normalized.append(
            {
                "left": decode_mask(item["left_mask"]),
                "right": decode_mask(item["right_mask"]),
                "left_last": item["left_last"],
                "right_last": item["right_last"],
                "shard": item["shard"],
            }
        )
    return normalized


def main() -> None:
    rows = json.loads(OUT.read_text())
    expected_primes = [4481, 4673, 4801, 4993, 5441, 5569]
    expected_nontoral = {
        4481: 0,
        4673: 0,
        4801: 0,
        4993: 6,
        5441: 0,
        5569: 0,
    }
    if [row.get("p") for row in rows] != expected_primes:
        raise AssertionError(rows)
    for row in rows:
        p = row["p"]
        expected = {
            "name": f"boundary_n64_h6_p{p}_SHARDED_CPP",
            "n": 64,
            "h": 6,
            "W": 64,
            "shards": 16,
            "shards_completed": 16,
            "hashed_per_shard": 7028847,
            "probed": 67945521,
            "anchored_toral_trades": 0,
            "anchored_nontoral_trades": expected_nontoral[p],
            "direct_n3_budget": 262144,
            "direct_n3_exceeded": False,
            "partial": False,
            "complete": True,
        }
        for key, value in expected.items():
            if row.get(key) != value:
                raise AssertionError((p, key, row.get(key), value, row))
        if len(row.get("rows", [])) != 16:
            raise AssertionError((p, "shards", row.get("rows")))
        if sum(shard.get("probed", 0) for shard in row["rows"]) != row["probed"]:
            raise AssertionError((p, "probed", row))
        witnesses = row.get("witnesses", [])
        if p == 4993:
            if normalized_witnesses(witnesses) != EXPECTED_P4993_WITNESSES:
                raise AssertionError((p, normalized_witnesses(witnesses)))
        elif witnesses:
            raise AssertionError((p, witnesses))
    print("h=6 n64 extra primes verified:", expected_primes)
    print("h=6 n64 p4993 nontoral witnesses:", expected_nontoral[4993])
    print("H6_N64_EXTRA_PRIMES_SWEEP_VERIFY_PASS")


if __name__ == "__main__":
    main()
