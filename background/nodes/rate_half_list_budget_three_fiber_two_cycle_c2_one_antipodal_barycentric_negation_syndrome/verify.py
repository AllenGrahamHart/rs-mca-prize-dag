#!/usr/bin/env python3
"""Checks for the c2 barycentric negation syndrome."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_barycentric_negation_syndrome"
DEPENDENCY = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_canonical_cell_fourier_ladder"
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 101


def load_ladder_verify():
    path = ROOT / f"background/nodes/{DEPENDENCY}/verify.py"
    spec = importlib.util.spec_from_file_location("cell_ladder_verify", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def derivative_at_roots(roots: list[int], root: int) -> int:
    value = 1
    for other in roots:
        if other != root:
            value = value * (root - other) % PRIME
    return value


def main() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    incoming = {
        edge["from"]
        for edge in dag["edges"]
        if edge["to"] == NODE_ID and edge.get("kind") == "req"
    }
    outgoing = {
        edge["to"]
        for edge in dag["edges"]
        if edge["from"] == NODE_ID and edge.get("kind") == "ev"
    }
    assert nodes[NODE_ID]["status"] == "PROVED"
    assert incoming == {DEPENDENCY}
    assert CONSUMER in outgoing

    ladder = load_ladder_verify()
    h = 3
    ws = [1, 2, 3, -6 % PRIME]
    b = [1, 2, 3, 4]
    sums = []
    for w in ws:
        factor = b[:]
        factor[h] = (factor[h] + w) % PRIME
        sums.append(ladder.power_sums(factor, 3 * h + 1))

    lam = []
    for i, w in enumerate(ws):
        derivative = 1
        for j, other in enumerate(ws):
            if i != j:
                derivative = derivative * (w - other) % PRIME
        lam.append(pow(derivative, -1, PRIME))
    for exponent in range(3):
        assert sum(lam[i] * pow(ws[i], exponent, PRIME) for i in range(4)) % PRIME == 0
    assert sum(lam[i] * pow(ws[i], 3, PRIME) for i in range(4)) % PRIME == 1
    for j in range(3 * h):
        assert sum(lam[i] * sums[i][j] for i in range(4)) % PRIME == 0
    weighted_endpoint = sum(lam[i] * sums[i][3 * h] for i in range(4)) % PRIME
    assert weighted_endpoint == -h % PRIME
    assert 2 * weighted_endpoint % PRIME == -2 * h % PRIME

    # Equality-case measure on a negation-stable support of size 3H+1.
    roots = [value % PRIME for value in (1, -1, 2, -2, 3, -3, 4, -4, 5, -5)]
    assert len(roots) == 3 * h + 1 and len(set(roots)) == len(roots)
    weights = {
        root: (-2 * h) * pow(derivative_at_roots(roots, root), -1, PRIME) % PRIME
        for root in roots
    }
    for j in range(3 * h):
        assert sum(weights[root] * pow(root, j, PRIME) for root in roots) % PRIME == 0
    assert sum(weights[root] * pow(root, 3 * h, PRIME) for root in roots) % PRIME == -2 * h % PRIME
    for root in roots:
        assert weights[-root % PRIME] == -weights[root] % PRIME

    official_r = 2**37
    official_h = official_r + 1
    assert 3 * official_h + 1 == 3 * official_r + 4

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_BARYCENTRIC_SYNDROME_PASS "
        "toy_H=3 barycentric=4 zero_moments=9 endpoint=-6 equality_support=10 wiring=2"
    )


if __name__ == "__main__":
    main()
