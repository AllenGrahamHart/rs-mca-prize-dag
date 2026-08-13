#!/usr/bin/env python3
"""Verify the support-local transversality compiler calibration."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "26c07a80357e75e2241c11aa85a06e6de70ad986120740d5fe92c12da8415f1c"
PINS = {
    "statement.md": "ce4d0421e9c6e52969c9066863e7038a57681caad026c4b0e6071f8d4dd172e1",
    "proof.md": "76f14ccd4e72be5db14080c1290adabffd34cc4ed5004c8794c0a9042f613c21",
}


class Reject(ValueError):
    pass


def falling(value: int, length: int) -> int:
    out = 1
    for offset in range(length):
        out *= value - offset
    return out


def rising(value: int, length: int) -> int:
    out = 1
    for offset in range(length):
        out *= value + offset
    return out


def cap(n: int, K: int, m: int, s: int, theta: int) -> int:
    w = m - K
    first = Fraction(
        falling(n, s + 1),
        m * theta * rising(w + 1, s - 1),
    )
    second = Fraction(
        falling(n - K + s, s + 1),
        theta * rising(w + 1, s),
    )
    value = max(first, second)
    return value.numerator // value.denominator


def validate(contract: object) -> int:
    if not isinstance(contract, dict) or set(contract) != {
        "schema", "source", "theorem", "koalabear_shortened"
    }:
        raise Reject("schema")
    if contract["schema"] != "rate-half-mca-support-local-transversality-compiler-v1":
        raise Reject("version")
    source = contract["source"]
    if source.get("pr") != 1166 or source.get("head") != (
        "af0e7c63b3d60873bf3fe2fc898edad85848deb5"
    ):
        raise Reject("source")
    theorem = contract["theorem"]
    if theorem.get("lower_bound") != 1 or set(theorem) != {
        "margin", "lower_bound", "first_endpoint", "second_endpoint"
    }:
        raise Reject("theorem")

    row = contract["koalabear_shortened"]
    R, d, budget = row["R"], row["d"], row["budget"]
    checks = 0
    for rank_text, expected in row["theta_one_caps"].items():
        s = int(rank_text)
        got = cap(R + s, s, d + s, s, 1)
        if got != expected:
            raise Reject(f"theta-one cap s={s}")
        checks += 1
    if row["theta_one_caps"]["9"] > budget or row["theta_one_caps"]["10"] <= budget:
        raise Reject("automatic wall")

    for rank_text, expected_theta in row["least_paying_theta"].items():
        s = int(rank_text)
        n, K, m = R + s, s, d + s
        got = next((theta for theta in range(1, expected_theta + 1)
                    if cap(n, K, m, s, theta) <= budget), None)
        if got != expected_theta:
            raise Reject(f"least theta s={s}")
        if expected_theta > 1 and cap(n, K, m, s, expected_theta - 1) <= budget:
            raise Reject(f"adjacent theta s={s}")
        checks += 2
    return checks


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for name, digest in PINS.items():
        if hashlib.sha256((HERE / name).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin {name}")
    contract = json.loads(CONTRACT.read_text())
    checks = validate(contract)
    controls = []
    for path, delta in (
        (("theta_one_caps", "9"), 1),
        (("theta_one_caps", "10"), -1),
        (("least_paying_theta", "10"), 1),
        (("least_paying_theta", "13"), -1),
    ):
        changed = copy.deepcopy(contract)
        changed["koalabear_shortened"][path[0]][path[1]] += delta
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_SUPPORT_LOCAL_TRANSVERSALITY_COMPILER_PASS "
        f"checks={checks} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
