#!/usr/bin/env python3
"""Independent audit for the punctured Johnson profile."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "f485ce789dccf03b4767e63281bc404ba4529a750c8243e56b4946da484eeb08"
PINS = {
    "statement.md": "3cf121f53d306a72c6e624da54d7488a8036272e9013f54eceb87617923a2fdb",
    "proof.md": "109d04f93c9d4f0d506a5d5826f7a37241be174b96f8cb751dd3ca73e958092b",
}


class Reject(ValueError):
    pass


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def independent_cap(R: int, d: int, K: int, e: int, h: int) -> int:
    if h == 0:
        return 0
    length = R + K - e
    agreement = d + K - h
    den = agreement * agreement - length * (K - 1)
    if den <= 0:
        raise Reject("denominator")
    return floor_fraction(Fraction(length * (agreement - K + 1), den))


def record(R: int, d: int, K: int, budget: int) -> dict[str, int]:
    positive = []
    e = 1
    while e < d:
        den = (d + K - e) ** 2 - (R + K - e) * (K - 1)
        if den <= 0:
            break
        positive.append((e, den))
        e += 1
    if not positive:
        raise Reject("empty prefix")
    last, dlast = positive[-1]
    dnext = (d + K - last - 1) ** 2 - (R + K - last - 1) * (K - 1)

    best = (-1, -1)
    for support, _ in positive:
        half = support // 2
        value = (
            (support - 1) * independent_cap(R, d, K, support, half)
            + independent_cap(R, d, K, support, support)
        )
        if value > budget:
            raise Reject("budget")
        if value > best[1]:
            best = (support, value)

    half = last // 2
    return {
        "last_paid_e": last,
        "equivalent_defect_floor": R - last,
        "denominator_at_last": dlast,
        "denominator_at_next": dnext,
        "half_index": half,
        "johnson_at_half": independent_cap(R, d, K, last, half),
        "johnson_at_last": independent_cap(R, d, K, last, last),
        "coarse_bound_at_last": best[1],
        "coarse_maximizer": best[0],
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
            raise Reject("row name")
        R, d, K, budget = bases[name]
        if tuple(row.get(key) for key in ("R", "d", "K", "budget")) != bases[name]:
            raise Reject("base row")
        derived = record(R, d, K, budget)
        for key, value in derived.items():
            if row.get(key) != value:
                raise Reject(key)
            checks += 1
    if checks != 18:
        raise Reject("row count")
    return checks


def check_profile_coarsening() -> int:
    checks = 0
    for R, d, K in ((101, 20, 3), (211, 31, 5)):
        for e in range(1, min(d, 18)):
            den = (d + K - e) ** 2 - (R + K - e) * (K - 1)
            if den <= 0:
                continue
            previous = 0
            profile = 0
            for h in range(1, e + 1):
                current = independent_cap(R, d, K, e, h)
                if current < previous:
                    raise Reject("cumulative monotonicity")
                profile += (current - previous) * (e // h)
                previous = current
            coarse = (
                (e - 1) * independent_cap(R, d, K, e, e // 2)
                + independent_cap(R, d, K, e, e)
            )
            if profile > coarse:
                raise Reject("coarsening")
            checks += 1
    return checks


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for name, digest in PINS.items():
        if hashlib.sha256((HERE / name).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin: {name}")
    payload = json.loads(CONTRACT.read_text())
    checks = validate_rows(payload) + check_profile_coarsening()

    controls = []
    for row_index, key in ((0, "half_index"), (1, "coarse_bound_at_last")):
        changed = copy.deepcopy(payload)
        changed["rows"][row_index][key] += 1
        try:
            validate_rows(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_SPARSE_DIRECTION_PUNCTURED_JOHNSON_PROFILE_AUDIT_PASS "
        f"checks={checks} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
