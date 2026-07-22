#!/usr/bin/env python3
"""Replay the support-wise high/low partition and DAG scope transfer."""

import json
from itertools import combinations
from pathlib import Path


def partition(family, cap):
    assert all(len(left & right) <= cap for left, right in combinations(family, 2))
    high = {
        i
        for i, support in enumerate(family)
        if any(i != j and len(support & other) == cap for j, other in enumerate(family))
    }
    low = set(range(len(family))) - high
    assert high.isdisjoint(low)
    assert high | low == set(range(len(family)))
    for i in low:
        assert all(i == j or len(family[i] & family[j]) <= cap - 1 for j in range(len(family)))
    return high, low


base = [frozenset(s) for s in combinations(range(5), 3)]
checks = 0
for mask in range(1, 1 << len(base)):
    family = [base[i] for i in range(len(base)) if mask & (1 << i)]
    for cap in (1, 2):
        if all(len(left & right) <= cap for left, right in combinations(family, 2)):
            partition(family, cap)
            checks += 1

# The exact supports from the nondeep F_17 regression fixture.
fixture = [
    frozenset((2, 6, 7)),
    frozenset((1, 6, 7)),
    frozenset((0, 6, 7)),
    frozenset((0, 1, 7)),
    frozenset((3, 6, 7)),
    frozenset((4, 6, 7)),
    frozenset((5, 6, 7)),
    frozenset((0, 1, 6)),
]
assert len(fixture) == 8
assert all(len(left & right) <= 2 for left, right in combinations(fixture, 2))

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
node_id = "xr_tangent_support_mismatch_bridge"
assert nodes[node_id]["status"] == "PROVED"
assert "P-A1" in nodes["xr_highcore_collision_count"]["statement"]
assert "P-A2" in nodes["xr_highcore_collision_count"]["statement"]
assert "globally generic" in nodes["xr_lowcore_spread_heart"]["statement"]

edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
assert {
    ("xr_true_tangent_coordinate_injection", node_id, "req"),
    ("xr_supportwise_transverse_lineray_rank_charge", node_id, "ev"),
    ("xr_strip_classification_rungs", node_id, "req"),
    (node_id, "xr_smallcore_spread_count", "req"),
    (node_id, "xr_highcore_collision_count", "ev"),
    (node_id, "xr_lowcore_spread_heart", "ev"),
} <= edges
assert (node_id, "xr_clean_residual_any_gate", "req") not in edges

print("XR_TANGENT_SUPPORT_MISMATCH_BRIDGE_PASS", checks, len(fixture))
