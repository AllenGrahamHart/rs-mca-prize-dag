#!/usr/bin/env python3
"""Verify the mismatch descent potential and six official depth caps."""

import json
from functools import lru_cache
from pathlib import Path


@lru_cache(maxsize=None)
def longest_chain(n, k, h):
    agreement = k + h
    assert n >= agreement and k >= 1 and h >= 1
    best = 0
    for d in range(k):
        next_k = k - d
        next_agreement = next_k + h
        max_next_n = n - agreement
        for next_n in range(next_agreement, max_next_n + 1):
            best = max(best, 1 + longest_chain(next_n, next_k, h))
    return best


checks = 0
for n in range(2, 31):
    for h in range(1, n):
        for k in range(1, n - h + 1):
            if k + h > n:
                continue
            depth = longest_chain(n, k, h)
            cap = n // (h + 1) - 1
            assert 0 <= depth <= cap
            checks += 1

rows = (
    (1024, 256, 261, 256, 169),
    (1024, 128, 133, 256, 169),
    (1024, 64, 67, 512, 255),
    (2**41, 2**39, 558345748481, 256, 254),
    (2**41, 2**38, 283467841537, 256, 254),
    (2**41, 2**37, 141733920769, 512, 510),
)
for n, k, agreement, scale, expected_cap in rows:
    h = agreement - k
    cap = n // (h + 1) - 1
    assert cap == expected_cap
    assert cap < scale

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes["xr_mismatch_nongeneric_invariant_excess_descent"]["status"] == "PROVED"
assert {
    (edge["from"], edge["to"], edge["kind"])
    for edge in dag["edges"]
} >= {
    (
        "xr_mismatch_nongeneric_invariant_excess_descent",
        "xr_tangent_support_mismatch_bridge",
        "ev",
    ),
}

print("XR_MISMATCH_NONGENERIC_DESCENT_PASS", checks, [row[-1] for row in rows])
