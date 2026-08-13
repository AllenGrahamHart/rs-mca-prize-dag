#!/usr/bin/env python3
"""Independent audit of the support-local error-rank route."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import prod
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "93216139e5bdc23e79fbe652ea320be6b1a7effd9447656456cf2760575eb18f"


class Reject(ValueError):
    pass


def independent_cap(n: int, K: int, m: int, s: int, theta: int) -> int:
    w = m - K
    first = Fraction(prod(range(n - s, n + 1)),
                     m * theta * prod(range(w + 1, w + s)))
    second = Fraction(prod(range(n - K, n - K + s + 1)),
                      theta * prod(range(w + 1, w + s + 1)))
    value = first if first >= second else second
    return value.numerator // value.denominator


def rank(vectors: list[tuple[int, ...]], p: int) -> int:
    rows = [list(vector) for vector in vectors]
    out = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(out, len(rows)) if rows[i][column] % p), None)
        if pivot is None:
            continue
        rows[out], rows[pivot] = rows[pivot], rows[out]
        inverse = pow(rows[out][column], -1, p)
        rows[out] = [value * inverse % p for value in rows[out]]
        for i in range(len(rows)):
            if i != out and rows[i][column] % p:
                factor = rows[i][column]
                rows[i] = [(a - factor * b) % p for a, b in zip(rows[i], rows[out])]
        out += 1
    return out


def gauge_control() -> int:
    p = 17
    b, c, r1 = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    slopes = (0, 1, 2)
    explanations = ((0, 0, 0), b, tuple((2 * b[i] + c[i]) % p for i in range(3)))
    errors = [tuple((gamma * r1[i] - h[i]) % p for i in range(3))
              for gamma, h in zip(slopes, explanations)]
    transformed = [tuple((h[i] - gamma * b[i]) % p for i in range(3))
                   for gamma, h in zip(slopes, explanations)]
    if rank([tuple((errors[i][j] - errors[0][j]) % p for j in range(3))
             for i in (1, 2)], p) != 2:
        raise Reject("error rank")
    if rank([tuple((transformed[i][j] - transformed[0][j]) % p for j in range(3))
             for i in (1, 2)], p) != 1:
        raise Reject("gauge rank")
    for gamma, h, hp in zip(slopes, explanations, transformed):
        for i in range(3):
            if (gamma * r1[i] - h[i]) % p != (gamma * (r1[i] - b[i]) - hp[i]) % p:
                raise Reject("gauge identity")
    return len(slopes)


def validate(payload: dict) -> int:
    row = payload.get("koalabear", {})
    if (row.get("n"), row.get("K"), row.get("m"), row.get("near_charge")) != (
        2097152, 1048576, 1116048, 134944
    ):
        raise Reject("row")
    checks = gauge_control()
    thresholds = {8: 1, 9: 13, 10: 388, 11: 12050}
    for s, theta in thresholds.items():
        record = row["rank_caps"][str(s)]
        got = independent_cap(row["n"], row["K"], row["m"], s, theta)
        if (record["theta"], record["cap"], record["total"]) != (
            theta, got, got + row["near_charge"]
        ):
            raise Reject("record")
        if record["total"] > row["budget"]:
            raise Reject("budget")
        checks += 3
    return checks


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    payload = json.loads(CONTRACT.read_text())
    checks = validate(payload)
    changed = copy.deepcopy(payload)
    changed["koalabear"]["rank_caps"]["10"]["cap"] -= 1
    try:
        validate(changed)
    except Reject:
        mutation = 1
    else:
        mutation = 0
    if mutation != 1:
        raise AssertionError("mutation control")
    print(
        "RATE_HALF_MCA_SUPPORT_LOCAL_ERROR_RANK_ROUTER_AUDIT_PASS "
        f"checks={checks} mutations={mutation}/1"
    )


if __name__ == "__main__":
    main()
