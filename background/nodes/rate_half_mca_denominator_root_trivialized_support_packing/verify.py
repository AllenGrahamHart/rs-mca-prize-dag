#!/usr/bin/env python3
import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
node = json.loads((HERE / "node.json").read_text())

assert node["node"]["status"] == "PROVED"
assert node["requires"] == [
    {"from": "rate_half_mca_denominator_root_cancellation_dichotomy"}
]

for n in range(7, 16):
    for m in range(4, n):
        for k in range(2, m):
            for t in range(m - k + 1):
                N, M = n - t, m - t
                ratio = comb(N, k) / comb(M, k)
                assert ratio >= (N / M) ** k
                assert N / M >= n / m

rows = (
    (1116048, 274980728111395087),
    (1116024, 16777215),
)
n = 2097152
k = 1048576
assert 3 ** 100 > 2 ** 158
for m, budget in rows:
    assert 2 * n > 3 * m
    assert k > 100
    assert budget < 2 ** 58

print("PASS trivialized-support shadow packing small_grid_and_exact_budget_fence")
