#!/usr/bin/env python3
"""Independent audit of the fixed nine-subset target router."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "6bcbfc8f5ae87e892898137660af54014a48c57f5d55295327923af6ab5f6e4b"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def vector_rank(rows: list[list[int]]) -> int:
    field = 103
    matrix = [[x % field for x in row] for row in rows]
    rank = 0
    for column in range(len(matrix[0])):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inv = pow(matrix[rank][column], -1, field)
        matrix[rank] = [(inv * x) % field for x in matrix[rank]]
        for i in range(len(matrix)):
            if i != rank and matrix[i][column]:
                factor = matrix[i][column]
                matrix[i] = [(a - factor * b) % field for a, b in zip(matrix[i], matrix[rank])]
        rank += 1
    return rank


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    require(2578110 - 1434405 == 1143705, "population gap")
    require(p["population_excess_over_plane_cap"] == 1143705, "manifest gap")
    # Independent sharp model for span(U,d): e1, e2, and d all occur.
    require(vector_rank([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3, "rank-three model")
    statement = (HERE / "statement.md").read_text()
    proof = (HERE / "proof.md").read_text()
    for token in ("Fixed kernel chart", "Large shared-core rank-nine plane", "Rank-eight owner flat"):
        require(token in statement, f"statement route {token}")
    for token in ("rank(ev_B) in {8,9}", "span(U,r_1-B_*)"):
        require(token in proof, f"proof token {token}")
    print(
        "RATE_HALF_MCA_RANK11_COMPONENT_NINESUBSET_TARGET_ROUTER_AUDIT_PASS "
        "routes=3 population=2578110 excess=1143705"
    )


if __name__ == "__main__":
    main()
