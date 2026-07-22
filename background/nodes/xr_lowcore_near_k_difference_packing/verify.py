#!/usr/bin/env python3
"""Verify the near-K subset-packing formula and official exact arithmetic."""

from itertools import combinations
from math import comb
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_lowcore_near_k_difference_packing"
checks = 0


# Exhaust the local ownership implication on small residual universes.
for v in range(4, 9):
    ground = range(v)
    for c in range(1, 4):
        for w in range(c, min(v, c + 3) + 1):
            residuals = [frozenset(x) for x in combinations(ground, w)]
            for i, left in enumerate(residuals):
                left_owned = set(combinations(sorted(left), c))
                for right in residuals[i + 1 :]:
                    if len(left & right) <= c - 1:
                        right_owned = set(combinations(sorted(right), c))
                        assert left_owned.isdisjoint(right_owned)
                        checks += 1


rows = (
    (2**10, 4, 256, 2, 6_327, 411_273),
    (2**10, 8, 256, 1, 128, 14_171),
    (2**10, 16, 512, 1, 224, 40_455),
    (2**41, 4, 256, 6, 4_398_046_497_508, 562_949_951_166_976),
    (2**41, 8, 256, 5, 260_919_262_630, 50_096_498_384_811),
    (2**41, 16, 512, 4, 40_282_095_485, 18_046_378_752_308),
)

for n, rate_den, scale, c0, expected_last, expected_next in rows:
    K = n // rate_den
    h = n // scale + 1
    H = h + 1

    values = []
    previous_num = 0
    previous_den = 1
    for c in range(1, c0 + 2):
        numerator = comb(n - 2 * K + 2 * c, c)
        denominator = comb(H + c - 1, c)
        value = numerator // denominator
        values.append(value)
        assert numerator * previous_den >= previous_num * denominator
        previous_num, previous_den = numerator, denominator
        checks += 1

    assert values[c0 - 1] == expected_last
    assert values[c0] == expected_next
    assert expected_last <= 8 * n < expected_next
    assert n - 2 * K + 1 > H
    checks += 4


dag = json.loads((ROOT / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes[NODE]["status"] == "PROVED"
edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
assert ("xr_lowcore_shift_pair_terminal_fiber_bound", NODE, "req") in edges
assert (NODE, "xr_lowcore_spread_heart", "ev") in edges

statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
for needle in (
    "two distinct residuals intersect in at most `c-1`",
    "E_C<=max_(c in C) R_c M(M-1)",
    "`2,1,1,6,5,4`",
    "no P-B",
):
    assert needle in statement
    checks += 1

print("XR_LOWCORE_NEAR_K_DIFFERENCE_PACKING_PASS", checks)
