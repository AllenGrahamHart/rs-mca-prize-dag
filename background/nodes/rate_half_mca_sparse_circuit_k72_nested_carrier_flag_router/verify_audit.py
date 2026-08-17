#!/usr/bin/env python3
"""Independent fixed-union arithmetic audit for the K'=72 flag."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


P = json.loads(Path(__file__).with_name("source_contract.json").read_text())["parameters"]
CAPS = tuple(P["active_caps"])
DEFICITS = (36, 28, 21, 15, 10, 6, 3, 1)


def count(K: int, m: int, u: int, g: int, d: int) -> int:
    r = g + 1 - d
    if r <= 0:
        return 10**500
    outside_budget = K - r - u
    return comb(u, d) + sum(
        comb(u, d - j)
        * comb(m - u, j - 1)
        * max(0, outside_budget - j + 1)
        // j
        for j in range(1, d + 1)
    )


def charge(caps: tuple[int, ...], u: int, g: int) -> tuple[int, ...]:
    answer = list(caps)
    for d in range(2, 10):
        answer[d - 2] = min(answer[d - 2], count(72, 67544, u, g, d) * comb(67544 - d, 11 - d))
    return tuple(answer)


def value(caps: tuple[int, ...]) -> int:
    return sum(weight * cap for weight, cap in zip(DEFICITS, caps))


cases = P["cases"]
assert value(charge(CAPS, 36, 6)) == cases["overlap_one_nested"]["premium"]
assert value(charge(CAPS, 37, 5)) == cases["overlap_zero_transverse"]["premium"]
assert value(charge(CAPS, 37, 6)) == cases["overlap_zero_nested"]["premium"]
flag = charge(charge(CAPS, 33, 8), 36, 5)
assert value(flag) == cases["overlap_one_flag"]["premium"]
print(json.dumps({"independent_cases": 4, "status": "PASS"}, sort_keys=True))
