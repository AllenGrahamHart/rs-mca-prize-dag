#!/usr/bin/env python3
"""Exact finite-field replay of the two-dimensional barycentric kernel."""

import json
from pathlib import Path


P = 101


def inv(value):
    return pow(value % P, P - 2, P)


for m in range(3, 7):
    points = tuple(range(2, 2 + m))
    derivatives = {}
    for x in points:
        value = 1
        for y in points:
            if y != x:
                value = value * (x - y) % P
        derivatives[x] = value

    basis = (
        tuple(inv(derivatives[x]) for x in points),
        tuple(x * inv(derivatives[x]) % P for x in points),
    )
    for vector in basis:
        for degree in range(m - 2):
            assert sum(vector[i] * pow(x, degree, P) for i, x in enumerate(points)) % P == 0

    # Any affine numerator a+bx gives a null vector, and two independent
    # choices give rank two on distinct points.
    rows = []
    for x in points:
        scale = inv(derivatives[x])
        rows.append((scale, x * scale % P))
    determinant = (rows[0][0] * rows[1][1] - rows[0][1] * rows[1][0]) % P
    assert determinant


def root_budget(e, r):
    m = r + 3
    numerator = r * e - 3
    lower = max(1, -(-numerator // (r + 2)))
    assert lower + m * (e - lower) <= 3 * e + 3
    if lower > 1:
        assert (lower - 1) + m * (e - lower + 1) > 3 * e + 3
    return lower


assert root_budget(183251937963, 0) == 1
assert root_budget(183251937963, 1) == 61083979320
assert root_budget(183251937963, 2) == 91625968981

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
node_id = (
    "rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_"
    "minimum_pair_rank_two_barycentric_normal_form"
)
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes[node_id]["status"] == "PROVED"

print("RATE_HALF_QUADRATIC_MINIMUM_PAIR_RANK_TWO_NORMAL_FORM_PASS")
