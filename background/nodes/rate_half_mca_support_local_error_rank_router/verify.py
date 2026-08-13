#!/usr/bin/env python3
"""Verify the support-local error-rank router."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "93216139e5bdc23e79fbe652ea320be6b1a7effd9447656456cf2760575eb18f"
PINS = {
    "statement.md": "7565b677c23ab8636966bc8a82e46ebb3db392c51953d63b9b56a34d997c27e1",
    "proof.md": "8b706360068566100cf2378d2b029ec00938aa4bca1178c36564c2af4c9c460c",
}


class Reject(ValueError):
    pass


def product(values) -> int:
    out = 1
    for value in values:
        out *= value
    return out


def cap(n: int, K: int, m: int, s: int, theta: int) -> int:
    w = m - K
    first = Fraction(
        product(n - i for i in range(s + 1)),
        m * theta * product(w + 1 + i for i in range(s - 1)),
    )
    second = Fraction(
        product(n - K + s - i for i in range(s + 1)),
        theta * product(w + 1 + i for i in range(s)),
    )
    value = max(first, second)
    return value.numerator // value.denominator


def validate(payload: object) -> int:
    if not isinstance(payload, dict) or payload.get("schema") != (
        "rate-half-mca-support-local-error-rank-router-v1"
    ):
        raise Reject("schema")
    if payload.get("source_head") != "af0e7c63b3d60873bf3fe2fc898edad85848deb5":
        raise Reject("source")
    row = payload["koalabear"]
    n, K, m = row["n"], row["K"], row["m"]
    if (m - K, row["w"], row["near_charge"]) != (67472, 67472, 134944):
        raise Reject("row")
    budget, near = row["budget"], row["near_charge"]
    checks = 0
    for rank_text, record in row["rank_caps"].items():
        s = int(rank_text)
        got = cap(n, K, m, s, record["theta"])
        if got != record["cap"] or got + near != record["total"]:
            raise Reject(f"rank {s}")
        if record["total"] > budget:
            raise Reject(f"pay {s}")
        checks += 3
    for rank_text, expected in row["adjacent_nonpaying_totals"].items():
        s = int(rank_text)
        theta = row["rank_caps"][rank_text]["theta"] - 1
        if cap(n, K, m, s, theta) + near != expected or expected <= budget:
            raise Reject(f"adjacent {s}")
        checks += 2
    if budget - row["rank_caps"]["8"]["total"] != 164589758939087047:
        raise Reject("slack")
    return checks + 1


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for name, digest in PINS.items():
        if hashlib.sha256((HERE / name).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin {name}")
    payload = json.loads(CONTRACT.read_text())
    checks = validate(payload)
    controls = []
    for rank, key, delta in (
        ("8", "cap", 1),
        ("9", "theta", -1),
        ("10", "total", 1),
        ("11", "theta", 1),
    ):
        changed = copy.deepcopy(payload)
        changed["koalabear"]["rank_caps"][rank][key] += delta
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_SUPPORT_LOCAL_ERROR_RANK_ROUTER_PASS "
        f"checks={checks} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
