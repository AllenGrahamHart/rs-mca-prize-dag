#!/usr/bin/env python3
"""Independent small-field audit of the quotient-line ingredients."""

from __future__ import annotations

import hashlib
import itertools
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "2007208c46a197c7d526ea185b9fe9034c860279f02c6d7d815cc0816eb90c82"


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
        inverse = pow(work[rank][col], -1, prime)
        work[rank] = [(value * inverse) % prime for value in work[rank]]
        for row in range(rows):
            if row == rank:
                continue
            factor = work[row][col] % prime
            if factor:
                work[row] = [
                    (left - factor * right) % prime
                    for left, right in zip(work[row], work[rank])
                ]
        rank += 1
    return rank


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    p = json.loads(CONTRACT.read_text())["parameters"]

    prime = 17
    vandermonde = 0
    for size in range(1, 13):
        for subset in itertools.combinations(range(13), size):
            matrix = [
                [pow(point, degree, prime) for degree in range(12)]
                for point in subset
            ]
            assert rank_mod(matrix, prime) == size
            vandermonde += 1

    # Independently check every e,g branch and the projective root budget.
    branch_checks = 0
    m = p["official_support_size"]
    total = 2 * comb(m - 1, 10)
    for support in range(2, 6):
        candidates = [support + 1]
        for degree in range(1, support + 1):
            for fixed in range(support):
                assert fixed < support
                candidates.append(
                    support + (degree * (m - fixed)) // (support - fixed)
                )
                branch_checks += 1
        cap = max(candidates)
        assert cap == p["support_label_caps"][str(support)]
        total += cap * comb(m - support, 11 - support)
    assert total == p["per_record_sparse_incidence_cap"]

    print(
        "PASS codimension-two quotient-line sparse circuit audit: "
        f"{vandermonde} Vandermonde subsets, {branch_checks} fiber branches"
    )


if __name__ == "__main__":
    main()
