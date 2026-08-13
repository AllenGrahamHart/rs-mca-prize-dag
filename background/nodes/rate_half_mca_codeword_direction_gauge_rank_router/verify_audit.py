#!/usr/bin/env python3
"""Independent affine-rank audit for the gauge equivalence."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "bbb7f5db9f5765ea4917d67595a431f55aa2135026820517168c016536365777"


class Reject(ValueError):
    pass


def rank_mod(rows: list[list[int]], p: int) -> int:
    matrix = [row[:] for row in rows]
    rank = 0
    for column in range(len(matrix[0]) if matrix else 0):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][column] % p), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inv = pow(matrix[rank][column], -1, p)
        matrix[rank] = [(inv * x) % p for x in matrix[rank]]
        for i in range(len(matrix)):
            if i != rank:
                factor = matrix[i][column]
                matrix[i] = [(x - factor * y) % p for x, y in zip(matrix[i], matrix[rank])]
        rank += 1
    return rank


def affine_rank(words: list[list[int]], p: int) -> int:
    anchor = words[0]
    return rank_mod([[(x - y) % p for x, y in zip(word, anchor)] for word in words[1:]], p)


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    contract = json.loads(CONTRACT.read_text())
    if contract.get("schema") != "rate-half-mca-codeword-direction-gauge-equivalence-v2":
        raise Reject("schema")
    p = 11
    slopes = list(range(8))
    words = [[(slope * slope + slope * x + x * x) % p for x in range(6)] for slope in slopes]
    for b in ([1] * 6, list(range(6)), [x * x % p for x in range(6)]):
        gauged = [[(value - slope * bx) % p for value, bx in zip(word, b)] for slope, word in zip(slopes, words)]
        if abs(affine_rank(words, p) - affine_rank(gauged, p)) > 1:
            raise Reject("rank shift")
    print("RATE_HALF_MCA_CODEWORD_DIRECTION_GAUGE_EQUIVALENCE_AUDIT_PASS gauges=3")


if __name__ == "__main__":
    main()
