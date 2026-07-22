#!/usr/bin/env python3
"""Replay support-local transversality and the six rank thresholds."""

import json
from itertools import product
from math import comb
from pathlib import Path

P = 3
N = 4

# A [4,2] MDS parity check over F_3: its columns are all projective points.
H = ((1, 0, 1, 1), (0, 1, 1, 2))


def syndrome(word):
    return tuple(sum(row[i] * word[i] for i in range(N)) % P for row in H)


vectors = list(product(range(P), repeat=N))
zero = (0, 0)
code = [word for word in vectors if syndrome(word) == zero]
images = {}
for mask in range(1 << N):
    support = {i for i in range(N) if mask & (1 << i)}
    images[mask] = {
        syndrome(word)
        for word in vectors
        if all(word[i] == 0 for i in range(N) if i not in support)
    }
checks = 0

for u in vectors:
    hu = syndrome(u)
    for v in vectors:
        hv = syndrome(v)
        for mask, image in images.items():
            support = {i for i in range(N) if mask & (1 << i)}
            zeros = set(range(N)) - support
            u_explained = any(all(c[i] == u[i] for i in zeros) for c in code)
            v_explained = any(all(c[i] == v[i] for i in zeros) for c in code)
            explained = u_explained and v_explained
            assert explained == (hu in image and hv in image)
            checks += 1

rows = (
    ("rowc-r1_4", 1024, 261, True),
    ("rowc-r1_8", 1024, 133, False),
    ("rowc-r1_16", 1024, 67, False),
    ("prize-r1_4", 2**41, 558345748481, False),
    ("prize-r1_8", 2**41, 283467841537, False),
    ("prize-r1_16", 2**41, 141733920769, False),
)

for _, n, agreement, rank_four_paid in rows:
    radius = n - agreement
    assert comb(radius + 3, 3) <= 8 * n**3
    assert (comb(radius + 4, 4) <= 16 * n**3) == rank_four_paid

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
node_id = "xr_supportwise_transverse_lineray_rank_charge"
assert nodes[node_id]["status"] == "PROVED"
edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
assert ("xr_all_lineray_affine_core_bound", node_id, "req") in edges
assert (node_id, "xr_tangent_support_mismatch_bridge", "ev") in edges
assert (node_id, "xr_highcore_collision_count", "ev") in edges
assert (node_id, "xr_lowcore_spread_heart", "ev") in edges

print("XR_SUPPORTWISE_TRANSVERSE_LINERAY_RANK_CHARGE_PASS", checks)
