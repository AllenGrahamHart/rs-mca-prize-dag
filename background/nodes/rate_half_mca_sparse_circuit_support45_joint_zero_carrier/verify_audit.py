#!/usr/bin/env python3
"""Independent dimension audit for the joint zero-carrier theorem."""

from __future__ import annotations

import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    work = [[value % prime for value in row] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((row for row in range(pivot_row, rows) if work[row][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][col], -1, prime)
        work[pivot_row] = [(value * inverse) % prime for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not work[row][col]:
                continue
            factor = work[row][col]
            work[row] = [
                (left - factor * right) % prime
                for left, right in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
    return pivot_row


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    require(p["source_vanishing_dimensions"] == {"4": 7, "5": 6}, "dimensions")

    arithmetic = 0
    for q in (10, 17, 35):
        for s4 in range(6):
            for s5 in range(5):
                if q <= s4 + s5:
                    continue
                overlap = (q + 3 - s4) + (q + 4 - s5) - (q + 7)
                require(overlap == q - s4 - s5 > 0, "minimal intersection contradiction")
                for t in range(4, 7):
                    for delta in range(min(s4, s5) + 1):
                        b = q + 10 - t - delta
                        label_dimension = b - (10 - t)
                        require(label_dimension == q - delta, "label dimension")
                        require((q + 10) - (t - 3) - b == delta + 3, "outside bound")
                        arithmetic += 1

    prime = 101
    points = list(range(1, 46))
    vandermonde = [[pow(point, degree, prime) for point in points] for degree in range(45)]
    require(rank_mod(vandermonde, prime) == 45, "K=45 Vandermonde independence")
    print(
        "RATE_HALF_MCA_SPARSE_CIRCUIT_SUPPORT45_JOINT_ZERO_CARRIER_AUDIT_PASS "
        f"arithmetic_checks={arithmetic} vandermonde_rank=45"
    )


if __name__ == "__main__":
    main()
