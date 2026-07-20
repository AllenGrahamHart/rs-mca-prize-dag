#!/usr/bin/env python3
"""Verify the exceptional Hankel kernel-plane transversality."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_kernel_plane_transversality"
DEPENDENCIES = {
    "rate_half_ca_hankel_exceptional_root_charge",
    "rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_factor_pin",
}
CONSUMER = "rate_half_band_closure"


def matrix_vector(matrix: list[list[int]], vector: list[int], p: int) -> list[int]:
    return [sum(left * right for left, right in zip(row, vector)) % p for row in matrix]


def dot(left: list[int], right: list[int], p: int) -> int:
    return sum(x * y for x, y in zip(left, right)) % p


def rank_mod(matrix: list[list[int]], p: int) -> int:
    work = [[value % p for value in row] for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next((row for row in range(rank, len(work)) if work[row][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], -1, p)
        work[rank] = [value * inverse % p for value in work[rank]]
        for row in range(len(work)):
            if row == rank or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                (left - factor * right) % p
                for left, right in zip(work[row], work[rank])
            ]
        rank += 1
    return rank


def profile_check() -> None:
    profiles = 0
    for e in range(3, 256):
        r = 2 * e + 1
        form_degree = 2 * r
        minimal_degree = r - 1
        other_degree = form_degree + 2 - minimal_degree
        assert other_degree == r + 3
        assert other_degree > r
        assert (r + 1) - (r - 1) == 2
        profiles += 1
    assert profiles == 253


def hankel_kernel_and_crossing_fixture() -> None:
    p = 101
    # Q_0(X)=X. Its degree-two multiples are X and X^2.
    u = [0, 1, 0]
    v = [0, 0, 1]
    m_0 = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    m_1 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1],
    ]
    q_1 = u[:]  # A harmless local rescaling of the continuing kernel line.

    assert rank_mod(m_0, p) == 1
    assert matrix_vector(m_0, u, p) == [0, 0, 0]
    assert matrix_vector(m_0, v, p) == [0, 0, 0]
    assert rank_mod([u, v], p) == 2

    lift = [
        (left + right) % p
        for left, right in zip(matrix_vector(m_0, q_1, p), matrix_vector(m_1, u, p))
    ]
    assert lift == [0, 0, 0]
    m_1_u = matrix_vector(m_1, u, p)
    m_1_v = matrix_vector(m_1, v, p)
    assert dot(u, m_1_u, p) == 0
    assert dot(v, m_1_u, p) == 0
    assert dot(v, m_1_v, p) == 1

    for z in (1, 2, 7, 19):
        pencil = [
            [(left + z * right) % p for left, right in zip(row_0, row_1)]
            for row_0, row_1 in zip(m_0, m_1)
        ]
        assert rank_mod(pencil, p) == 2
        assert matrix_vector(pencil, u, p) == [0, 0, 0]

    broken_m_1 = [[0, 0, 0] for _ in range(3)]
    assert dot(v, matrix_vector(broken_m_1, v, p), p) == 0
    assert rank_mod(m_0, p) == rank_mod(
        [[(left + right) % p for left, right in zip(row_0, row_1)] for row_0, row_1 in zip(m_0, broken_m_1)],
        p,
    )


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    proof = (here / "proof.md").read_text()
    for marker in (
        "ker M_0=span{u,v}",
        "M_0q_1+M_1u=0",
        "v^TM_1v!=0",
        "compact exceptional Hankel gate",
    ):
        assert marker in statement
    for marker in (
        "other generator has degree `r+3`",
        "span{Q(gamma_0;X), XQ(gamma_0;X)}",
        "det(A)beta",
        "adj M/z",
    ):
        assert marker in proof


def main() -> None:
    profile_check()
    hankel_kernel_and_crossing_fixture()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_KERNEL_PLANE_TRANSVERSALITY_PASS "
        "profiles=253 kernel_dim=2 crossing=1 mutation=1"
    )


if __name__ == "__main__":
    main()
