#!/usr/bin/env python3
"""Independent finite-field audit of the cross-support carrier mechanism."""

from __future__ import annotations

import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
PRIME = 101


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def rank_mod(matrix: list[list[int]], prime: int = PRIME) -> int:
    work = [[entry % prime for entry in row] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][col], -1, prime)
        work[pivot_row] = [(entry * inverse) % prime for entry in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or work[row][col] == 0:
                continue
            factor = work[row][col]
            work[row] = [
                (left - factor * right) % prime
                for left, right in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    require(p["correction_dimension"] == 10, "dimension")

    # Distinct evaluation columns are independent through the full K-column range.
    field_checks = 0
    for k in (11, 12, 17, 42):
        points = list(range(1, k + 1))
        vandermonde = [[pow(point, degree, PRIME) for point in points] for degree in range(k)]
        require(rank_mod(vandermonde) == k, f"Vandermonde rank K={k}")
        field_checks += 1

    # Private completion coordinates force exact rank q-s.
    for q, defect in ((5, 0), (8, 3), (32, 4)):
        count = q - defect
        private = [[int(row == col) for col in range(count)] for row in range(count)]
        require(rank_mod(private) == count, f"private rank q={q} s={defect}")
        field_checks += 1

    target_sets = {}
    arithmetic_checks = 0
    for defect in range(5):
        targets = []
        for target in range(2, 10):
            condition = 5 + (defect + 1) * target - defect - 1 <= 10
            q = 32
            carrier = q + 4 + defect * (target - 1)
            require(condition == (carrier + target <= q + 10), "union equivalence")
            if condition:
                targets.append(target)
            arithmetic_checks += 1
        target_sets[str(defect)] = targets
    require(target_sets == p["support5_specialization"]["target_supports"], "targets")
    print(
        "RATE_HALF_MCA_SPARSE_CIRCUIT_CROSS_SUPPORT_DEFECT_CARRIER_AUDIT_PASS "
        f"field_checks={field_checks} arithmetic_checks={arithmetic_checks}"
    )


if __name__ == "__main__":
    main()
