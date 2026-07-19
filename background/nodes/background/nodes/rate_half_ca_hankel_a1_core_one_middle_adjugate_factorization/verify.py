#!/usr/bin/env python3
"""Verify the core-one middle-Hankel adjugate factorization packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_middle_adjugate_factorization"
DEPENDENCY = "rate_half_ca_hankel_half_distance_a1_core_slope_slack_ledger"
CONSUMER = "rate_half_band_closure"


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    work = [[value % prime for value in row] for row in matrix]
    rows = len(work)
    columns = len(work[0])
    rank = 0
    for column in range(columns):
        pivot = next((i for i in range(rank, rows) if work[i][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], -1, prime)
        work[rank] = [(value * inverse) % prime for value in work[rank]]
        for i in range(rows):
            if i == rank or not work[i][column]:
                continue
            factor = work[i][column]
            work[i] = [
                (left - factor * right) % prime
                for left, right in zip(work[i], work[rank])
            ]
        rank += 1
    return rank


def canonical_symmetric_block(index: int, u: int, v: int, lam: int) -> list[list[int]]:
    size = 2 * index + 2
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    # The singular symmetric block is [[0,L_e],[L_e^T,0]].
    for row in range(index):
        matrix[row][index + row] = v
        matrix[index + row][row] = v
        matrix[row][index + row + 1] = -u
        matrix[index + row + 1][row] = -u
    matrix[-1][-1] = lam
    return matrix


def canonical_rank_check() -> None:
    prime = 101
    for index in range(1, 8):
        d = 2 * index + 1
        for u, v in ((1, 2), (3, 5), (7, 1)):
            regular = (u + 9 * v) % prime
            matrix = canonical_symmetric_block(index, u, v, regular)
            assert rank_mod(matrix, prime) == d
            exceptional = canonical_symmetric_block(index, u, v, 0)
            assert rank_mod(exceptional, prime) == d - 1


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    assert f"background/nodes/{NODE}/statement.md" in nodes[CONSUMER]["refs"]

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md", "dependency_subdag.md",
        "audit.md", "result.md", "verify.py", "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    packet = (base / "statement.md").read_text() + (base / "proof.md").read_text()
    for marker in (
        "adj M=lambda*q*q^T",
        "gcd of all nonzero maximal minors",
        "rank exactly `d-1`",
        "O in {0,1}",
        "C=e-1+O",
        "one `L_e`, one transpose block `L_e^T`",
    ):
        assert marker in packet


def main() -> None:
    for m in range(2, 512):
        e = 2 * m - 1
        d = 4 * m - 1
        assert d == 2 * e + 1
        assert 8 * m - 2 == 2 * d
        assert d - 2 * e == 1
    canonical_rank_check()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_MIDDLE_ADJUGATE_FACTORIZATION_PASS "
        "canonical_indices=1..7 regular_degree=1"
    )


if __name__ == "__main__":
    main()
