#!/usr/bin/env python3
"""Exact h=5 certificate scaling audit for the current MITM design."""

from __future__ import annotations

import json
import math
from pathlib import Path


NOTES = Path(__file__).resolve().parent
BYTES_PER_RECORD = 32

EXPECTED_ROWS = {
    64: {
        "left": 595_665,
        "right": 7_028_847,
        "left_gib": "0.017752",
        "right_shards": 1,
    },
    96: {
        "left": 3_183_545,
        "right": 57_940_519,
        "left_gib": "0.094877",
        "right_shards": 8,
    },
    128: {
        "left": 10_334_625,
        "right": 254_231_775,
        "left_gib": "0.307996",
        "right_shards": 32,
    },
    256: {
        "left": 172_061_505,
        "right": 8_637_487_551,
        "left_gib": "5.127832",
        "right_shards": 1088,
    },
    512: {
        "left": 2_807_768_705,
        "right": 284_707_746_687,
        "left_gib": "83.678028",
        "right_shards": 35_836,
    },
}


def load_json(name: str):
    return json.loads((NOTES / name).read_text())


def row_stats(n: int, n128_probes_per_shard: float) -> dict[str, object]:
    left = math.comb(n - 1, 4)
    right = math.comb(n - 1, 5)
    left_gib = left * BYTES_PER_RECORD / (1024**3)
    right_shards = math.ceil(right / n128_probes_per_shard)
    return {
        "left": left,
        "right": right,
        "left_gib": f"{left_gib:.6f}",
        "right_shards": right_shards,
    }


def main() -> None:
    n128 = load_json("f3_h5_n128_boundary_certificate.json")
    if n128["n"] != 128 or n128["h"] != 5:
        raise AssertionError(n128)
    if n128["shards"] != 32 or n128["shards_completed"] != 32:
        raise AssertionError(n128)
    if n128["hashed_per_shard"] != math.comb(127, 4):
        raise AssertionError((n128["hashed_per_shard"], math.comb(127, 4)))
    if n128["probed"] != math.comb(127, 5):
        raise AssertionError((n128["probed"], math.comb(127, 5)))

    probes_per_shard = n128["probed"] / n128["shards"]
    actual = {n: row_stats(n, probes_per_shard) for n in EXPECTED_ROWS}
    if actual != EXPECTED_ROWS:
        raise AssertionError((actual, EXPECTED_ROWS))

    print("h=5 certificate scaling frontier")
    print(" n     left_records       right_records     left_GiB  right_shards")
    for n, row in actual.items():
        print(
            f"{n:3d} {row['left']:16d} {row['right']:19d} "
            f"{row['left_gib']:>12} {row['right_shards']:13d}"
        )
    print("current n=128 design rebuilds the full left table in each shard")
    print("blind n=512 extension exceeds the 2000-shard right-probe policy")
    print("H5_CERTIFICATE_SCALING_FRONTIER_PASS")


if __name__ == "__main__":
    main()
