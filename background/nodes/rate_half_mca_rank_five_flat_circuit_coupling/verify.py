#!/usr/bin/env python3
"""Verify the rank-five flat-circuit coupling contract and sharp controls."""

from __future__ import annotations

import copy
import hashlib
import itertools
import json
import sys
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "9d93ab795e311ec5789fe77494d9fd26ed8b17d5f5cf88bbbc1e04de112317e5"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def rank(rows: list[tuple[int, ...]], prime: int) -> int:
    matrix = [list(row) for row in rows]
    if not matrix:
        return 0
    columns = len(matrix[0])
    pivot = 0
    for column in range(columns):
        found = next((i for i in range(pivot, len(matrix)) if matrix[i][column] % prime), None)
        if found is None:
            continue
        matrix[pivot], matrix[found] = matrix[found], matrix[pivot]
        inverse = pow(matrix[pivot][column] % prime, -1, prime)
        matrix[pivot] = [(value * inverse) % prime for value in matrix[pivot]]
        for i in range(len(matrix)):
            if i == pivot:
                continue
            factor = matrix[i][column] % prime
            if factor:
                matrix[i] = [
                    (left - factor * right) % prime
                    for left, right in zip(matrix[i], matrix[pivot])
                ]
        pivot += 1
        if pivot == len(matrix):
            break
    return pivot


def moment_columns(dimension: int, count: int, prime: int) -> list[tuple[int, ...]]:
    return [tuple(pow(x, power, prime) for power in range(dimension)) for x in range(count)]


def circuit_count(columns: list[tuple[int, ...]], size: int, prime: int) -> int:
    count = 0
    for indices in itertools.combinations(range(len(columns)), size):
        vectors = [columns[i] for i in indices]
        if rank(vectors, prime) != size - 1:
            continue
        if all(rank(vectors[:j] + vectors[j + 1 :], prime) == size - 1 for j in range(size)):
            count += 1
    return count


def check_row(row: dict[str, int], dimension: int) -> None:
    columns = moment_columns(dimension, row["N"], row["prime"])
    c4 = circuit_count(columns, 4, row["prime"])
    c5 = circuit_count(columns, 5, row["prime"])
    require((c4, c5) == (row["C4"], row["C5"]), "circuit census")
    left = 5 * c5
    right = (row["B"] - 3) * comb(row["N"], 4) - (row["N"] - row["B"]) * c4
    require(left <= right, "flat-circuit inequality")
    if dimension == 4:
        require(left == right, "uniform rank-four sharpness")


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract object")
    require(data["schema"] == "rate-half-mca-rank-five-flat-circuit-coupling-v1", "schema")
    require(data["formula"]["left"] == "5*C5", "left formula")
    require(data["formula"]["right"] == "(B-3)*C(N,4)-(N-B)*C4", "right formula")
    require(data["hypotheses"]["minimum_B"] == 3, "minimum B")
    require(data["hypotheses"]["rank3_flat_cap"] == "B", "rank-three cap")
    require(data["hypotheses"]["rank4_flat_cap"] == "B+1", "rank-four cap")
    for row in data["uniform_rank4_rows"]:
        check_row(row, 4)
    check_row(data["uniform_rank5_row"], 5)
    return {"controls": len(data["uniform_rank4_rows"]) + 1}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item["formula"].__setitem__("left", "4*C5"),
        lambda item: item["formula"].__setitem__("right", "(B-3)*C(N,4)"),
        lambda item: item["hypotheses"].__setitem__("rank4_flat_cap", "B+2"),
        lambda item: item["uniform_rank4_rows"][0].__setitem__("C5", 0),
    )
    rejected = 0
    for mutate in mutations:
        trial = copy.deepcopy(data)
        mutate(trial)
        try:
            validate(trial)
        except (Reject, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "tamper rejection")
    return rejected


def main() -> int:
    raw = CONTRACT.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(raw)
    result = validate(data)
    result["contract_sha256"] = CONTRACT_SHA256
    result["tamper_rejected"] = tamper_selftest(data)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Reject as exc:
        print(f"REJECT: {exc}", file=sys.stderr)
        raise SystemExit(1)
