#!/usr/bin/env python3
"""Verify the smooth nondeep tangent support-mismatch counterexample."""

import json
from itertools import combinations
from pathlib import Path

P = 17
D = (1, 2, 4, 8, 16, 15, 13, 9)
K = 2
A = 3
U = (0, 0, 0, 0, 0, 0, 1, 1)
V = (0, 0, 0, 0, 0, 0, 1, 2)


def solve_linear(word, support):
    i, j = support[:2]
    slope = (word[j] - word[i]) * pow((D[j] - D[i]) % P, P - 2, P) % P
    constant = (word[i] - slope * D[i]) % P
    if all((constant + slope * D[index]) % P == word[index] for index in support):
        return constant, slope
    return None


def extends_jointly(support):
    return solve_linear(U, support) is not None and solve_linear(V, support) is not None


def stabilizer(support):
    support = set(support)
    return [
        shift
        for shift in range(len(D))
        if {(index + shift) % len(D) for index in support} == support
    ]


assert len(set(D)) == len(D)
assert all(pow(x, 8, P) == 1 for x in D)
assert 3 * (len(D) - A) > len(D) - K
assert extends_jointly((0, 1, 2, 3, 4, 5))

bad_by_slope = {}
for z in range(P):
    word = tuple((u + z * v) % P for u, v in zip(U, V))
    bad = [
        support
        for support in combinations(range(len(D)), A)
        if solve_linear(word, support) is not None and not extends_jointly(support)
    ]
    if bad:
        bad_by_slope[z] = bad

expected_slopes = (1, 2, 4, 8, 9, 13, 15, 16)
expected_supports = (
    (2, 6, 7),
    (1, 6, 7),
    (0, 6, 7),
    (0, 1, 7),
    (3, 6, 7),
    (4, 6, 7),
    (5, 6, 7),
    (0, 1, 6),
)
assert tuple(bad_by_slope) == expected_slopes
chosen = tuple(bad_by_slope[z][0] for z in expected_slopes)
assert chosen == expected_supports
assert len(chosen) == 8 > len(D) - A + 1 == 6
assert len(set(chosen)) == len(chosen)
assert max(len(set(left) & set(right)) for left, right in combinations(chosen, 2)) <= K
assert all(stabilizer(support) == [0] for support in chosen)

# A pullback through x -> x^2 would be constant on index pairs separated by 4.
assert any(U[index] != U[index + 4] or V[index] != V[index + 4] for index in range(4))

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes["xr_nondeep_tangent_supportwise_payment"]["status"] == "REFUTED"
assert nodes["xr_tangent_support_mismatch_bridge"]["status"] in ("TARGET", "PROVED")  # bridge closed 2026-07-22 at the re-posed scope (wave-20, maintainer-ratified)

print("XR_NONDEEP_TANGENT_PAYMENT_REFUTED", list(expected_slopes))
