#!/usr/bin/env python3
"""Independent audit of the terminal-deficit affine-line payment."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "b0a15b8c1b86ce9729fcc0e67ec9a1a95ab7b67f2b10973972d5eb051a7d8d76"
PINS = {
    "statement.md": "20787ec794b193f57a053f975c167c8e955e73e354cdac06f9697b6ed93f4960",
    "proof.md": "8fcd61a18f2855f8178e91e51be85b7eb6ed408c8de8d6b262989d0ed17733c5",
}


class Reject(ValueError):
    pass


def rational_raw_cap(R: int, d: int, K: int, e: int, h: int) -> int | None:
    n = R + K - e
    A = d + K - h
    c = K - 1
    den = A * A - n * c
    if den > 0:
        q = Fraction(n * (A - c), den)
    else:
        g = -den
        T = (n - A) ** 2 - (n - 1) * g
        if g < 0 or 2 * A * A < n * c or T <= 0:
            return None
        q = Fraction((n - 1) * n * n * (A - c), A * T)
    return q.numerator // q.denominator


def independent_profile(R: int, d: int, K: int, e: int) -> tuple[int, int, int] | None:
    raw = []
    for h in range(1, e):
        cap = rational_raw_cap(R, d, K, e, h)
        if cap is None:
            return None
        raw.append(cap)
    running = None
    suffix = [0] * (e - 1)
    for index in range(e - 2, -1, -1):
        running = raw[index] if running is None else min(running, raw[index])
        suffix[index] = running
    previous = 0
    prefix = 0
    for h, cap in enumerate(suffix, 1):
        prefix += (cap - previous) * (e // h)
        previous = cap
    n = R + K - e
    A = d + K - e
    c = K - 1
    line = Fraction(n - c, A - c)
    terminal = line.numerator // line.denominator
    return prefix, terminal, prefix + terminal


def finite_line_control() -> int:
    # Three affine-line agreement sets with a one-coordinate common core.
    blocks = [{0, 1, 2}, {0, 3, 4}, {0, 5, 6}]
    n, A, c = 7, 3, 1
    core = set.intersection(*blocks)
    if len(core) != c:
        raise Reject("core")
    stripped = [block - core for block in blocks]
    if any(left & right for i, left in enumerate(stripped) for right in stripped[i + 1:]):
        raise Reject("outside packing")
    cap = Fraction(n - c, A - c)
    if len(blocks) > cap.numerator // cap.denominator:
        raise Reject("line cap")
    return len(blocks) * len(stripped)


def validate(payload: dict) -> int:
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
        e = row["paid_e"]
        if e < K or row["equivalent_defect_floor"] != R - e:
            raise Reject("coordinates")
        profile = independent_profile(R, d, K, e)
        if profile is None:
            raise Reject("profile")
        prefix, terminal, total = profile
        if (row["prefix_profile"], row["terminal_cap"], row["total_profile"]) != profile:
            raise Reject("paid values")
        if total > budget:
            raise Reject("budget")
        adjacent = independent_profile(R, d, K, row["adjacent_e"])
        if row["adjacent_stop"] == "prefix-cap-unavailable":
            if adjacent is not None or row["adjacent_profile"] is not None:
                raise Reject("unavailable stop")
        elif adjacent is None or adjacent[2] != row["adjacent_profile"] or adjacent[2] <= budget:
            raise Reject("budget stop")
        checks += 6
    if checks != 12:
        raise Reject("row count")
    return checks


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for name, digest in PINS.items():
        if hashlib.sha256((HERE / name).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin: {name}")
    payload = json.loads(CONTRACT.read_text())
    checks = validate(payload) + finite_line_control()
    changed = copy.deepcopy(payload)
    changed["rows"][1]["terminal_cap"] += 1
    try:
        validate(changed)
    except Reject:
        mutation = 1
    else:
        mutation = 0
    if mutation != 1:
        raise AssertionError("mutation control")
    print(
        "RATE_HALF_MCA_SPARSE_DIRECTION_TERMINAL_DEFICIT_LINE_PAYMENT_AUDIT_PASS "
        f"checks={checks} mutations={mutation}/1"
    )


if __name__ == "__main__":
    main()
