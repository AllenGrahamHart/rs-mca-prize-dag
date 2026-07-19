#!/usr/bin/env python3
"""Verify the full exceptional-only reciprocal complement."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_full_reciprocal_complement"
DEPENDENCY = "rate_half_ca_hankel_a1_core_one_exceptional_only_reciprocal_bezout_normalization"
CONSUMER = "rate_half_band_closure"


def add(left: list[int], right: list[int], p: int) -> list[int]:
    size = max(len(left), len(right))
    out = [0] * size
    for index in range(size):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % p
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def scale(poly: list[int], scalar: int, p: int) -> list[int]:
    return [scalar * value % p for value in poly]


def multiply(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            out[i + j] = (out[i + j] + left_value * right_value) % p
    return out


def determinant(matrix: list[list[int]], p: int) -> int:
    work = [row[:] for row in matrix]
    value = 1
    for column in range(len(work)):
        pivot = next(row for row in range(column, len(work)) if work[row][column] % p)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            value = -value
        pivot_value = work[column][column] % p
        value = value * pivot_value % p
        inverse = pow(pivot_value, -1, p)
        for row in range(column + 1, len(work)):
            factor = work[row][column] * inverse % p
            for entry in range(column, len(work)):
                work[row][entry] = (work[row][entry] - factor * work[column][entry]) % p
    return value % p


def resultant(left: list[int], right: list[int], p: int) -> int:
    m, n = len(left) - 1, len(right) - 1
    left_descending = list(reversed(left))
    right_descending = list(reversed(right))
    matrix: list[list[int]] = []
    for shift in range(n):
        matrix.append([0] * shift + left_descending + [0] * (n - shift - 1))
    for shift in range(m):
        matrix.append([0] * shift + right_descending + [0] * (m - shift - 1))
    return determinant(matrix, p)


def degree_check() -> None:
    profiles = 0
    for e in range(3, 256):
        r = 2 * e + 1
        d_0 = 8 * e + 7
        s = d_0 - r
        n_x = d_0 - 1
        assert r + (s - 1) == n_x
        assert n_x + 1 == d_0
        profiles += 1
    assert profiles == 253


def polynomial_fixture() -> None:
    p = 101
    exceptional, p_cl, j_inf, q_bar = 3, 5, 7, 2
    f = [exceptional * q_bar, 2, 1]
    g = [-j_inf * q_bar % p, 4, 3, 1]
    c = add(scale(f, j_inf, p), scale(g, exceptional, p), p)
    assert c[0] == 0
    ell = c[1:]

    u = [29, 9]
    a_vee = [p_cl * j_inf % p] + u
    r_x = add(multiply(f, u, p), scale(ell, p_cl, p), p)
    left_reversed = add(multiply(f, a_vee, p), scale(g, p_cl * exceptional, p), p)
    assert left_reversed == [0] + r_x
    assert r_x[0] == 1

    res_fl = resultant(f, ell, p)
    res_fr = resultant(f, r_x, p)
    assert res_fr == pow(p_cl, len(f) - 1, p) * res_fl % p

    mutated_u = u[:]
    mutated_u[0] += 1
    assert add(multiply(f, mutated_u, p), scale(ell, p_cl, p), p) != r_x


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    proof = (here / "proof.md").read_text()
    for marker in (
        "F U+P_cl L=R_X",
        "P_cl | (R_X-FU)",
        "E | (YL-j_infF)",
        "not a converse reconstruction theorem",
    ):
        assert marker in statement
    for marker in (
        "Reverse `(1)` at degree `D_0`",
        "=Y(P_clL+FU)",
        "recovers `(RBN2)`",
        "Res_Y(F,P_clL)",
    ):
        assert marker in proof


def main() -> None:
    degree_check()
    polynomial_fixture()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_FULL_RECIPROCAL_COMPLEMENT_PASS "
        "profiles=253 fixture=1 resultant=1 mutation=1"
    )


if __name__ == "__main__":
    main()
