#!/usr/bin/env python3
"""Independent arithmetic audit of the K'=10 split-pencil payment."""

from __future__ import annotations

import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "029b609ad2401fa9c9e689bdff2496fff2b202f2d00acb6010b64eac67acf881"


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def modular_rank(matrix: list[list[int]], prime: int) -> int:
    rows = [row[:] for row in matrix]
    rank = 0
    for column in range(len(rows[0]) if rows else 0):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column] % prime), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, prime)
        rows[rank] = [(value * inverse) % prime for value in rows[rank]]
        for i in range(len(rows)):
            if i == rank:
                continue
            factor = rows[i][column] % prime
            if factor:
                rows[i] = [
                    (left - factor * right) % prime
                    for left, right in zip(rows[i], rows[rank])
                ]
        rank += 1
        if rank == len(rows):
            break
    return rank


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    n, m = 1048586, 67482
    density_num = 990810934
    density_den = 10**9
    records = 274980728111260126

    marked_num_a = density_num * records * 55 * comb(m, 11)
    marked_num_b = density_num * records * comb(m, 9) * comb(m - 9, 2)
    denominator_a = density_den * comb(n, 9)
    assert marked_num_a == marked_num_b
    demand = ceil_div(marked_num_a, denominator_a)

    a, total = m - 9, n - 9
    threshold = a // 2 + 1
    h = total // threshold
    terms = (
        (a - 2) * total * total // 8,
        total * (total - 1) // 2,
        h * (h - 1) // 2 * (a - 1) * (a - 2) // 2,
    )
    capacity = sum(terms)
    assert tuple(terms) == (
        p["clean_dominant_cap"],
        p["balanced_cap"],
        p["heavy_collision_cap"],
    )
    assert capacity == p["total_capacity"]
    assert demand == p["weighted_demand"]
    assert demand - capacity == p["demand_capacity_gap"] > 0

    rank_checks = 0
    for prime in (11, 13, 17, 19):
        points = list(range(10))
        for count in (9, 10):
            matrix = [[pow(x, degree, prime) for degree in range(10)] for x in points[:count]]
            assert modular_rank(matrix, prime) == count
            rank_checks += 1

    print(
        "PASS K10 split-pencil payment audit: "
        f"two marking formulas, three cap terms, {rank_checks} Vandermonde ranks"
    )


if __name__ == "__main__":
    main()
