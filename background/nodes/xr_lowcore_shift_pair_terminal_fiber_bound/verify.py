#!/usr/bin/env python3
"""Exact small-family and official-row checks for the terminal shift bound."""

from itertools import combinations
import json
from pathlib import Path


def terminal_bound(N, H, t):
    residual = N - 2 * t
    if residual > 4 * H:
        return None
    if residual == 4 * H:
        return 2 * residual
    return (4 * H) // (4 * H - residual)


checks = 0
for N in range(2, 6):
    universe = range(N)
    for a in range(1, N):
        supports = [frozenset(S) for S in combinations(universe, a)]
        for H in range(1, a + 1):
            cap = a - H
            K = cap + 1
            for mask in range(1 << len(supports)):
                family = [supports[i] for i in range(len(supports)) if mask >> i & 1]
                if any(len(S & T) > cap for S, T in combinations(family, 2)):
                    continue

                fibers = {}
                for S in family:
                    for T in family:
                        if S == T:
                            continue
                        X, Y, I = S - T, T - S, S & T
                        assert len(X) == len(Y)
                        assert H <= len(X) <= N - a
                        fibers.setdefault((X, Y), set()).add(I)

                terminal_energy = 0
                wide_energy = 0
                for (X, Y), residuals in fibers.items():
                    t = len(X)
                    for I, J in combinations(residuals, 2):
                        assert len(I ^ J) >= 2 * H
                    bound = terminal_bound(N, H, t)
                    if bound is not None:
                        assert len(residuals) <= bound
                        assert len(residuals) <= 8 * H
                        terminal_energy += len(residuals) ** 2
                    if t >= K:
                        assert len(residuals) <= 1
                        wide_energy += len(residuals) ** 2
                    checks += 1

                M = len(family)
                assert terminal_energy <= 8 * H * M * max(0, M - 1)
                assert wide_energy <= M * max(0, M - 1)


rows = [
    ("RowC 1/4", 2**10, 4, 256, 6, 256, 500, 763),
    ("RowC 1/8", 2**10, 8, 256, 6, 128, 500, 891),
    ("RowC 1/16", 2**10, 16, 512, 4, 64, 504, 957),
    ("prize 1/4", 2**41, 4, 256, 8589934594, 549755813888, 1082331758588, 1640677507071),
    ("prize 1/8", 2**41, 8, 256, 8589934594, 274877906944, 1082331758588, 1915555414015),
    ("prize 1/16", 2**41, 16, 512, 4294967298, 137438953472, 1090921693180, 2057289334783),
]
for _, n, rate_den, scale, expected_H, expected_K, expected_t0, expected_tmax in rows:
    K = n // rate_den
    h = n // scale + 1
    H = h + 1
    a = K + h
    t0 = max(H, (n - 4 * H + 1) // 2)
    assert (H, K, t0, n - a) == (expected_H, expected_K, expected_t0, expected_tmax)
    assert K < t0
    M = 8 * n**3 + 1
    assert 8 * H * M * (M - 1) * n**2 < M**3
    checks += 1


root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
node_id = "xr_lowcore_shift_pair_terminal_fiber_bound"
assert nodes[node_id]["status"] == "PROVED"
edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
assert ("xr_nongeneric_explanation_plotkin_width", node_id, "req") in edges
assert (node_id, "xr_lowcore_spread_heart", "ev") in edges

print("XR_LOWCORE_SHIFT_PAIR_TERMINAL_FIBER_BOUND_PASS", checks)
