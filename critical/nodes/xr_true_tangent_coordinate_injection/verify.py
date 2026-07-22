#!/usr/bin/env python3
"""Exhaust the true-tangent coordinate injection over a finite toy model."""

import json
from itertools import product
from pathlib import Path

P = 3
N = 4
checks = 0

for e0 in product(range(P), repeat=N):
    for e1 in product(range(P), repeat=N):
        support = {
            index
            for index, pair in enumerate(zip(e0, e1))
            if pair != (0, 0)
        }
        charge = {}
        for z in range(P):
            roots = [
                index
                for index in support
                if (e0[index] + z * e1[index]) % P == 0
            ]
            if not roots:
                continue
            index = roots[0]
            assert index not in charge
            charge[index] = z
        assert len(charge) <= len(support)
        checks += 1

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes["xr_true_tangent_coordinate_injection"]["status"] == "PROVED"
assert nodes["xr_tangent_support_mismatch_bridge"]["status"] in ("TARGET", "PROVED")  # bridge closed 2026-07-22 at the re-posed scope (wave-20, maintainer-ratified)
assert {
    (edge["from"], edge["to"], edge["kind"])
    for edge in dag["edges"]
} >= {
    # ev -> req at the wave-20 bridge closure (true_tangent is a req parent of
    # the re-posed proved bridge; maintainer-ratified 2026-07-22)
    ("xr_true_tangent_coordinate_injection", "xr_tangent_support_mismatch_bridge", "req"),
    ("xr_true_tangent_coordinate_injection", "xr_clean_residual_any_gate", "req"),
}

print("XR_TRUE_TANGENT_COORDINATE_INJECTION_PASS", checks)
