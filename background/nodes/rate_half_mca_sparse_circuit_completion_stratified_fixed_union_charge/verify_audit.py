#!/usr/bin/env python3
"""Independent arithmetic audit of the stratified fixed-union formula."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


DATA = json.loads(Path(__file__).with_name("source_contract.json").read_text())
EXPECTED = ((1500, 1455), (1051, 981))


def c(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def replay(row: dict[str, int], structured: bool) -> int:
    def slots(size: int) -> int:
        if not structured:
            return c(row["u"], size)
        ordinary = row["u"] - row["b"]
        return c(ordinary, size) + row["b"] * c(ordinary, size - 1)

    answer = slots(row["d"])
    for j in range(1, row["d"] + 1):
        cap = row["M"]
        if j <= row["g"]:
            cap = min(cap, row["K"] - row["g"] - row["u"])
        answer += slots(row["d"] - j) * c(row["m"] - row["u"], j - 1) * cap // j
    return answer


rows = []
for source, expected in zip(DATA["toy_rows"], EXPECTED):
    pair = (replay(source, False), replay(source, True))
    assert pair == expected
    rows.append(pair)
print(json.dumps({"independent_rows": rows, "status": "PASS"}, sort_keys=True))
