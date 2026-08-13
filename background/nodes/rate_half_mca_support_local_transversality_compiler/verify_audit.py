#!/usr/bin/env python3
"""Independent audit of support-local transversality constants."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import prod
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "26c07a80357e75e2241c11aa85a06e6de70ad986120740d5fe92c12da8415f1c"


class Reject(ValueError):
    pass


def independent_cap(n: int, K: int, m: int, s: int, theta: int) -> int:
    w = m - K
    first = Fraction(
        prod(range(n - s, n + 1)),
        m * theta * prod(range(w + 1, w + s)),
    )
    second = Fraction(
        prod(range(n - K, n - K + s + 1)),
        theta * prod(range(w + 1, w + s + 1)),
    )
    chosen = first if first >= second else second
    return chosen.numerator // chosen.denominator


def finite_margin_control() -> int:
    support = {0, 1, 2, 3, 4}
    fibers = {
        "b0": {0, 1, 2, 3},
        "b1": {0, 1},
        "b2": set(),
    }
    theta0 = min(len(support - equal) for equal in fibers.values())
    if theta0 != 1 or min(theta0, 3) != 1:
        raise Reject("finite theta")
    return len(fibers)


def validate(payload: dict) -> int:
    row = payload.get("koalabear_shortened", {})
    R, d, budget = row.get("R"), row.get("d"), row.get("budget")
    if (R, d, budget) != (1048576, 67472, 274980728111395087):
        raise Reject("row")
    checks = finite_margin_control()
    expected_caps = {8: 3566101912297072, 9: 55413538236037195,
                     10: 861057176799343503}
    for s, expected in expected_caps.items():
        if independent_cap(R + s, s, d + s, s, 1) != expected:
            raise Reject("cap")
        checks += 1
    for s, threshold in {10: 4, 11: 49, 12: 757, 13: 11748}.items():
        paid = independent_cap(R + s, s, d + s, s, threshold)
        prior = independent_cap(R + s, s, d + s, s, threshold - 1)
        if not paid <= budget < prior:
            raise Reject("threshold")
        if row["least_paying_theta"].get(str(s)) != threshold:
            raise Reject("record")
        checks += 2
    return checks


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    payload = json.loads(CONTRACT.read_text())
    checks = validate(payload)
    changed = copy.deepcopy(payload)
    changed["koalabear_shortened"]["least_paying_theta"]["12"] += 1
    try:
        validate(changed)
    except Reject:
        mutation = 1
    else:
        mutation = 0
    if mutation != 1:
        raise AssertionError("mutation control")
    print(
        "RATE_HALF_MCA_SUPPORT_LOCAL_TRANSVERSALITY_COMPILER_AUDIT_PASS "
        f"checks={checks} mutations={mutation}/1"
    )


if __name__ == "__main__":
    main()
