#!/usr/bin/env python3
"""Independent audit of the Mersenne boundary-anchor endpoint."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "f3b0dec86cd2d5fe518793ce10e42f7493e5b8b66d5dd5641704b7e1440af3cd"
PINS = {
    "statement.md": "8376a7b148ec4d7f8ee99bc0dbb41e5961a404184a8bced1eeff1c54c8822d8d",
    "proof.md": "6fefba234c0ef750ac2e85c19559d9ca9c2de3a748772fd79e226af7c465c977",
}


class Reject(ValueError):
    pass


def cap(n: int, m: int, c: int, h: int) -> int:
    agreement = m - h
    denominator = agreement * agreement - n * c
    if denominator > 0:
        return n * (agreement - c) // denominator
    gap = -denominator
    terminal = (n - agreement) ** 2 - (n - 1) * gap
    if 2 * agreement * agreement < n * c or terminal <= 0:
        raise Reject("undefined")
    return ((n - 1) * n * n * (agreement - c)) // (agreement * terminal)


def abel(R: int, d: int, K: int, e: int, endpoint: int) -> tuple[int, int, int]:
    n, m, c = R + K - e, d + K, K - 1
    raw = [cap(n, m, c, h) for h in range(1, endpoint + 1)]
    suffix = [0] * endpoint
    running = raw[-1]
    for index in range(endpoint - 1, -1, -1):
        if raw[index] < running:
            running = raw[index]
        suffix[index] = running
    total = 0
    previous = 0
    changes = 0
    for h, value in enumerate(suffix, start=1):
        if value != previous:
            total += (value - previous) * (e // h)
            previous = value
            changes += 1
    return total, changes, suffix[-1]


def endpoint(row: dict, e: int) -> tuple[int, ...]:
    s, q = divmod(e - row["K"], 3)
    H = e - s - 1
    full = abel(row["R"], row["d"], row["K"], e, H)
    previous = abel(row["R"], row["d"], row["K"], e, H - 1)
    line = row["R"] + row["K"] - (row["d"] + row["K"]) + 1
    small = full[0] + 1
    anchored = previous[0] + line
    return (s, q, H, line, *full, *previous, small, anchored,
            max(small, anchored))


def validate(payload: dict) -> int:
    if payload.get("schema") != "rate-half-mca-m31-boundary-anchor-case-split-v1":
        raise Reject("schema")
    row = payload["row"]
    expected = (
        row["s"], row["q"], row["H"], row["line_cap"],
        row["P_H"], row["P_H_breaks"], row["B_H"],
        row["P_previous"], row["P_previous_breaks"], row["B_previous"],
        row["small_tail_case"], row["two_anchor_case"], row["bound"],
    )
    if endpoint(row, row["e"]) != expected:
        raise Reject("endpoint")
    adjacent = endpoint(row, row["adjacent_e"])
    if (adjacent[1], adjacent[4], adjacent[7], adjacent[10], adjacent[11],
        adjacent[12]) != (
        row["adjacent_q"], row["adjacent_P_H"],
        row["adjacent_P_previous"], row["adjacent_small_tail_case"],
        row["adjacent_two_anchor_case"], row["adjacent_bound"]
    ):
        raise Reject("adjacent")
    if row["budget"] - row["bound"] != row["slack"]:
        raise Reject("slack")
    if row["adjacent_bound"] - row["budget"] != row["adjacent_excess"]:
        raise Reject("excess")
    return 18


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for name, digest in PINS.items():
        if hashlib.sha256((HERE / name).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin {name}")
    payload = json.loads(CONTRACT.read_text())
    checks = validate(payload)
    changed = copy.deepcopy(payload)
    changed["row"]["adjacent_excess"] += 1
    try:
        validate(changed)
    except Reject:
        mutation = 1
    else:
        mutation = 0
    if mutation != 1:
        raise AssertionError("mutation control")
    print(
        "RATE_HALF_MCA_M31_BOUNDARY_ANCHOR_CASE_SPLIT_AUDIT_PASS "
        f"checks={checks} mutations={mutation}/1"
    )


if __name__ == "__main__":
    main()
