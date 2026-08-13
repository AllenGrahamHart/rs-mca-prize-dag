#!/usr/bin/env python3
"""Independent endpoint audit of the full-lift Gram/global-line profile."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "12b70130eee9f99192a07d730de15006455229ff192f60f46788464ff1846c73"
PINS = {
    "statement.md": "b1fa6c8ce0dfe3eca422dec52348346dae7d342a77c71ad685bcb88ef23f4632",
    "proof.md": "523c35fc8eefa4d8ea9612b2bc6ecd48373af2e9d09e5791eacc441309f2308b",
}


class Reject(ValueError):
    pass


def cumulative_cap(n: int, m: int, c: int, h: int) -> tuple[int | None, tuple[int, ...]]:
    A = m - h
    johnson = A * A - n * c
    if johnson > 0:
        return n * (A - c) // johnson, (A, -johnson, 2 * A * A - n * c, 0)
    g = -johnson
    balance = 2 * A * A - n * c
    T = (n - A) ** 2 - (n - 1) * g
    if balance < 0 or T <= 0:
        return None, (A, g, balance, T)
    return (n - 1) * n * n * (A - c) // (A * T), (A, g, balance, T)


def grouped_profile(R: int, d: int, K: int, e: int) -> tuple[int | None, dict[str, int]]:
    N, m, c, n = R + K, d + K, K - 1, R + K - e
    H = e - (e - K) // 3 - 1
    if m - H <= c:
        raise Reject("prefix agreement guard")
    raw = []
    for h in range(1, H + 1):
        value, record = cumulative_cap(n, m, c, h)
        if value is None:
            return None, {
                "H": H, "failure_h": h, "A": record[0], "g": record[1],
                "balance": record[2], "T": record[3],
            }
        raw.append(value)
    suffix = [0] * H
    running = raw[-1]
    for index in range(H - 1, -1, -1):
        running = min(running, raw[index])
        suffix[index] = running
    prefix = 0
    previous = 0
    breaks = 0
    for h, value in enumerate(suffix, start=1):
        if value != previous:
            prefix += (value - previous) * (e // h)
            previous = value
            breaks += 1
    return prefix + N - m + 1, {
        "H": H, "prefix": prefix, "B_H": suffix[-1], "breaks": breaks,
    }


def validate(payload: dict) -> int:
    if payload.get("schema") != "rate-half-mca-full-lift-mean-centered-global-line-profile-v1":
        raise Reject("schema")
    checks = 0
    for row in payload.get("rows", []):
        R, d, K = row["R"], row["d"], row["K"]
        total, detail = grouped_profile(R, d, K, row["last_paid_e"])
        if (total, detail["H"], detail["prefix"], detail["B_H"],
            detail["breaks"]) != (
            row["last_total"], row["last_H"], row["last_prefix"],
            row["last_B_H"], row["last_breaks"]
        ):
            raise Reject("last endpoint")
        adjacent, next_detail = grouped_profile(R, d, K, row["adjacent_e"])
        if adjacent != row["adjacent_total"]:
            raise Reject("adjacent total")
        if row["adjacent_failure_h"] is not None:
            if (next_detail["failure_h"], next_detail["A"], next_detail["g"],
                next_detail["balance"], next_detail["T"]) != (
                row["adjacent_failure_h"], row["adjacent_A"],
                row["adjacent_g"], row["adjacent_balance"], row["adjacent_T"]
            ):
                raise Reject("theorem wall")
        else:
            value, record = cumulative_cap(
                R + K - row["adjacent_e"], d + K, K - 1, next_detail["H"]
            )
            if (record[0], record[1], record[2], record[3]) != (
                row["adjacent_A"], row["adjacent_g"],
                row["adjacent_balance"], row["adjacent_T"]
            ) or value is None or adjacent <= row["budget"]:
                raise Reject("budget wall")
        checks += 10
    if checks != 20:
        raise Reject("row count")
    return checks


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for name, digest in PINS.items():
        if hashlib.sha256((HERE / name).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin {name}")
    payload = json.loads(CONTRACT.read_text())
    checks = validate(payload)
    changed = copy.deepcopy(payload)
    changed["rows"][1]["last_breaks"] += 1
    try:
        validate(changed)
    except Reject:
        mutation = 1
    else:
        mutation = 0
    if mutation != 1:
        raise AssertionError("mutation control")
    print(
        "RATE_HALF_MCA_FULL_LIFT_MEAN_CENTERED_GLOBAL_LINE_PROFILE_AUDIT_PASS "
        f"checks={checks} mutations={mutation}/1"
    )


if __name__ == "__main__":
    main()
