#!/usr/bin/env python3
"""Independent arithmetic and Vandermonde audit of the K'=11 payment."""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "72c6d95b858551bceea1467d6832b9a0e1daf73edac9c9ae54dc9af3e11b692a"


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if work[i][col] % prime), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inv = pow(work[rank][col], -1, prime)
        work[rank] = [(value * inv) % prime for value in work[rank]]
        for i in range(rows):
            if i == rank:
                continue
            factor = work[i][col] % prime
            if factor:
                work[i] = [
                    (left - factor * right) % prime
                    for left, right in zip(work[i], work[rank])
                ]
        rank += 1
        if rank == rows:
            break
    return rank


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    assert p["K_prime"] == 11

    prime = 101
    points = list(range(13))
    vandermonde_checks = 0
    for size in range(1, 11):
        for subset in itertools.combinations(points, size):
            rows = [[pow(point, degree, prime) for degree in range(11)] for point in subset]
            assert rank_mod(rows, prime) == size
            vandermonde_checks += 1

    shadow_checks = 0
    for circuit_size in range(1, 12):
        rank8 = 0
        rank9 = 0
        for omitted in itertools.combinations(range(11), 2):
            if set(omitted).isdisjoint(range(circuit_size)):
                rank8 += 1
            else:
                rank9 += 1
        assert rank8 == comb(11 - circuit_size, 2)
        assert rank9 == 55 - rank8
        shadow_checks += 55
    assert min(55 - comb(11 - c, 2) for c in range(6, 12)) == 45

    n, m = 1048587, 67483
    records = 274980728111260126
    chart_cap = max(p["rank9_core_caps"])
    global_marks = comb(n, 9) * chart_cap
    high = global_marks // 45
    low_candidates = [records * comb(m - c, 11 - c) for c in range(1, 6)]
    assert low_candidates == sorted(low_candidates, reverse=True)
    low = low_candidates[0]
    required = Fraction(990810934 * records * comb(m, 11), 10**9)
    demand = (required.numerator + required.denominator - 1) // required.denominator
    capacity = high + low
    coefficient = Fraction(990810934 * comb(m, 11), 10**9) - comb(m - 1, 10)
    assert coefficient > 0
    assert chart_cap == 9275866238180030
    assert capacity == p["total_capacity_at_record_floor"]
    assert demand == p["required_incidence_at_record_floor"]
    assert demand - capacity == p["demand_capacity_gap"] > 0

    print(
        "PASS K11 circuit split-pencil payment audit: "
        f"{vandermonde_checks} Vandermonde subsets, "
        f"{shadow_checks} shadow omissions, "
        f"gap {demand-capacity}"
    )


if __name__ == "__main__":
    main()
