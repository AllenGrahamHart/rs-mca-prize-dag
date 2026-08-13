#!/usr/bin/env python3
"""Independent audit of the near-Johnson Gram-rank payment."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "52a8d0de1e089db1db91035f45b3affdd97039ce849f7340eb68f493ccda27a1"
PINS = {
    "statement.md": "5ef6875c80b2634397a0ab9963c0a868fa85210dc2c240ae2d4e8e1d543c85ba",
    "proof.md": "c67b8a386c2f2cfb9673f351dd1faaef2b1b83c3d348a64481a5c5f824150f7c",
}


class Reject(ValueError):
    pass


def rank(matrix: list[list[int]]) -> int:
    work = [[Fraction(value) for value in row] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((i for i in range(pivot_row, rows) if work[i][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for i in range(rows):
            if i == pivot_row or not work[i][col]:
                continue
            factor = work[i][col]
            work[i] = [x - factor * y for x, y in zip(work[i], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def gram_control() -> int:
    blocks = [
        {0, 1, 2}, {0, 3, 4}, {1, 3, 5}, {2, 4, 5},
        {0, 5, 6}, {1, 4, 6}, {2, 3, 6},
    ]
    n, A, c = 10, 3, 1
    if any(len(x & y) > c for x, y in combinations(blocks, 2)):
        raise Reject("control intersections")
    incidence = [[int(x in block) for x in range(n)] for block in blocks]
    ones = [1] * len(blocks)
    gram = [
        [sum(x * y for x, y in zip(left, right)) - c * u * v
         for right, v in zip(incidence, ones)]
        for left, u in zip(incidence, ones)
    ]
    if rank(gram) > rank(incidence) or rank(incidence) > n:
        raise Reject("rank placement")
    g = n * c - A * A
    G = (A - c) ** 2 - c * g
    cap = n * A * (A - c) // G
    if len(blocks) > cap:
        raise Reject("Gram cap")
    return len(blocks) * len(blocks)


def independent_record(R: int, d: int, K: int, e: int) -> dict[str, int | None]:
    n = R + K - e
    A = d + K - e
    c = K - 1
    g = n * c - A * A
    G = (A - c) ** 2 - c * g
    ordinary = None
    if G > 0:
        fraction = Fraction(n * A * (A - c), G)
        ordinary = fraction.numerator // fraction.denominator
    u = e // 2
    Au = d + K - u
    D = Au * Au - n * c
    half = Fraction(n * (Au - c), D)
    J = half.numerator // half.denominator
    return {
        "punctured_length_at_last": n,
        "agreement_at_last": A,
        "johnson_defect_at_last": g,
        "gram_denominator_at_last": G,
        "ordinary_cap_at_last": ordinary,
        "half_index_at_last": u,
        "johnson_cap_at_half": J,
        "bound_at_last": None if ordinary is None else (e - 1) * J + ordinary,
    }


def validate_rows(payload: dict) -> int:
    bases = {
        "KoalaBear MCA": (1048576, 67472, 14, 274980728111395087),
        "Mersenne-31 MCA": (1048576, 67448, 6, 16777215),
    }
    checks = 0
    for row in payload.get("rows", []):
        name = row.get("name")
        if name not in bases:
            raise Reject("name")
        R, d, K, budget = bases[name]
        if tuple(row.get(key) for key in ("R", "d", "K", "budget")) != bases[name]:
            raise Reject("base")
        endpoint = independent_record(R, d, K, row["last_paid_e"])
        for key, value in endpoint.items():
            if row.get(key) != value:
                raise Reject(key)
            checks += 1
        adjacent = independent_record(R, d, K, row["adjacent_e"])
        if row["adjacent_gram_denominator"] != adjacent["gram_denominator_at_last"]:
            raise Reject("adjacent denominator")
        if row["adjacent_bound"] != adjacent["bound_at_last"]:
            raise Reject("adjacent bound")
        if row["bound_at_last"] > budget:
            raise Reject("paid endpoint")
        if name == "Mersenne-31 MCA" and row["adjacent_bound"] <= budget:
            raise Reject("unpaid adjacent")
        checks += 3
    if checks != 22:
        raise Reject("row count")
    return checks


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for name, digest in PINS.items():
        if hashlib.sha256((HERE / name).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin: {name}")
    payload = json.loads(CONTRACT.read_text())
    checks = validate_rows(payload) + gram_control()

    changed = copy.deepcopy(payload)
    changed["rows"][1]["ordinary_cap_at_last"] += 1
    try:
        validate_rows(changed)
    except Reject:
        mutation = 1
    else:
        mutation = 0
    if mutation != 1:
        raise AssertionError("mutation control")
    print(
        "RATE_HALF_MCA_SPARSE_DIRECTION_NEAR_JOHNSON_GRAM_RANK_AUDIT_PASS "
        f"checks={checks} mutations={mutation}/1"
    )


if __name__ == "__main__":
    main()
