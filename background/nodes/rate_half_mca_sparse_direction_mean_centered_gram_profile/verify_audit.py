#!/usr/bin/env python3
"""Independent audit of the mean-centered Gram profile."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "4e233dcdc3a51a92b2c8124ae8667e3cabdaa49c4bea9640903b467621c8f135"
PINS = {
    "statement.md": "3724b202ad5e1b50adb1c3ae17660e9cf09a70c588110ad46c79570196ca9f57",
    "proof.md": "b7e5a10b24b2ed60805d80be3e1ebcd4a47b8832800092f1c1f51123f41896bd",
}


class Reject(ValueError):
    pass


def independent_cap(n: int, A: int, c: int) -> int | None:
    g = n * c - A * A
    T = (n - A) ** 2 - (n - 1) * g
    if g < 0 or 2 * A * A < n * c or T <= 0:
        return None
    value = Fraction((n - 1) * n * n * (A - c), A * T)
    return value.numerator // value.denominator


def finite_block_control() -> int:
    blocks = [
        {0, 1, 2}, {0, 3, 4}, {1, 3, 5}, {2, 4, 5},
        {0, 5, 6}, {1, 4, 6}, {2, 3, 6},
    ]
    n, A, c = 10, 3, 1
    if any(len(left & right) > c for left, right in combinations(blocks, 2)):
        raise Reject("intersections")
    cap = independent_cap(n, A, c)
    if cap is None or len(blocks) > cap:
        raise Reject("finite cap")

    p = Fraction(A * A, n)
    C = p * (c - p)
    trace = len(blocks) * (A - p)
    entries = []
    for left in blocks:
        row = []
        for right in blocks:
            row.append(Fraction(len(left & right)) - p)
        entries.append(row)
    trace_square = sum(value * value for row in entries for value in row)
    upper = C * len(blocks) ** 2 + A * (A - c) * len(blocks)
    if trace_square > upper:
        raise Reject("trace-square chord")
    if trace * trace > (n - 1) * trace_square:
        raise Reject("rank trace")
    return len(blocks) ** 2


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
        e = row["last_paid_e"]
        n = R + K - e
        A = d + K - e
        c = K - 1
        g = n * c - A * A
        balance = 2 * A * A - n * c
        T = (n - A) ** 2 - (n - 1) * g
        cap = independent_cap(n, A, c)
        expected = {
            "equivalent_defect_floor": R - e,
            "punctured_length_at_last": n,
            "agreement_at_last": A,
            "johnson_defect_at_last": g,
            "chord_balance_at_last": balance,
            "mean_gram_denominator_at_last": T,
            "ordinary_cap_at_last": cap,
        }
        for key, value in expected.items():
            if row.get(key) != value:
                raise Reject(key)
            checks += 1
        adjacent = row["adjacent_e"]
        n2 = R + K - adjacent
        A2 = d + K - adjacent
        g2 = n2 * c - A2 * A2
        T2 = (n2 - A2) ** 2 - (n2 - 1) * g2
        if row["adjacent_mean_gram_denominator"] != T2:
            raise Reject("adjacent denominator")
        if row["profile_at_last"] > budget:
            raise Reject("endpoint budget")
        if name == "Mersenne-31 MCA" and row["adjacent_profile"] <= budget:
            raise Reject("adjacent budget")
        checks += 3
    if checks != 20:
        raise Reject("row count")
    return checks


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for name, digest in PINS.items():
        if hashlib.sha256((HERE / name).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin: {name}")
    payload = json.loads(CONTRACT.read_text())
    checks = validate_rows(payload) + finite_block_control()
    changed = copy.deepcopy(payload)
    changed["rows"][0]["ordinary_cap_at_last"] += 1
    try:
        validate_rows(changed)
    except Reject:
        mutation = 1
    else:
        mutation = 0
    if mutation != 1:
        raise AssertionError("mutation control")
    print(
        "RATE_HALF_MCA_SPARSE_DIRECTION_MEAN_CENTERED_GRAM_PROFILE_AUDIT_PASS "
        f"checks={checks} mutations={mutation}/1"
    )


if __name__ == "__main__":
    main()
