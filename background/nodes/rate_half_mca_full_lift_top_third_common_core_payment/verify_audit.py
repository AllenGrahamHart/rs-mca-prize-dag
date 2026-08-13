#!/usr/bin/env python3
"""Independent audit of the full-lift common-core payment."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "53abad99118d8c726d7d13edf5792d4e53c1bd22460623e2783a5e5a0795cc9a"
PINS = {
    "statement.md": "767b9a387abf3606d5ccb990846789b45afa92e3489a4c10169443a55a139edf",
    "proof.md": "677c8378f7bf2f87dfc10a5340e3a0861a1124a3cc68e460e61bd42dc9c32c1d",
}


class Reject(ValueError):
    pass


def direct_line_sum(R: int, d: int, K: int, e: int) -> int:
    N, m, c = R + K, d + K, K - 1
    n, t = N - e, N - m
    s = (e - K) // 3
    r0 = max(0, e - m)
    total = 0
    for r in range(r0, s + 1):
        A = m - e + r
        total += t + 1 if A <= c else (n - c) // (A - c)
    return total


def johnson_values(R: int, d: int, K: int, e: int) -> tuple[int, int, int]:
    N, m, c = R + K, d + K, K - 1
    n = N - e
    s = (e - K) // 3
    H = e - s - 1
    u = e // 2
    values = []
    for h in (u, H):
        A = m - h
        denominator = A * A - n * c
        if denominator <= 0:
            raise Reject("Johnson unavailable")
        values.append(n * (A - c) // denominator)
    return values[0], values[1], H


def finite_core_control() -> int:
    blocks = [
        {0, 1, 2}, {0, 1, 3}, {0, 1, 4}, {0, 1, 5}, {0, 1, 6},
    ]
    N, m = 7, 3
    core = set.intersection(*blocks)
    if len(core) != m - 1:
        raise Reject("common core")
    stripped = [block - core for block in blocks]
    if any(left & right for i, left in enumerate(stripped) for right in stripped[i + 1:]):
        raise Reject("off-core packing")
    if len(blocks) != N - m + 1:
        raise Reject("sharp total cap")
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
        last = row["last_paid_e"]
        J_u, J_H, H = johnson_values(R, d, K, last)
        line = direct_line_sum(R, d, K, last)
        prefix = (last - 1) * J_u + J_H
        if (J_u, J_H, H, line, prefix, prefix + line) != (
            row["last_J_u"], row["last_J_H"], row["last_H"],
            row["last_line_sum"], row["last_prefix"], row["last_total"],
        ):
            raise Reject("last endpoint")
        if prefix + line > budget:
            raise Reject("budget")

        if name == "KoalaBear MCA":
            max_u = max_H = 0
            for e in range(d, last + 1):
                current_u, current_H, _ = johnson_values(R, d, K, e)
                max_u = max(max_u, current_u)
                max_H = max(max_H, current_H)
            if (max_u, max_H) != (50, 557844):
                raise Reject("uniform Johnson maxima")
            at_m = direct_line_sum(R, d, K, d + K)
            if at_m != row["max_line_sum"] or row["max_line_sum_e"] != d + K:
                raise Reject("line maximum")
            uniform = (last - 1) * max_u + max_H + at_m
            if uniform > budget:
                raise Reject("uniform KoalaBear")
        else:
            for e in range(d, last + 1):
                current_u, current_H, _ = johnson_values(R, d, K, e)
                current = (e - 1) * current_u + current_H + direct_line_sum(R, d, K, e)
                if current > budget:
                    raise Reject("Mersenne strip")
            adjacent = row["adjacent_e"]
            current_u, current_H, adjacent_H = johnson_values(R, d, K, adjacent)
            current = (
                (adjacent - 1) * current_u
                + current_H
                + direct_line_sum(R, d, K, adjacent)
            )
            if (adjacent_H, current) != (row["adjacent_H"], row["adjacent_total"]):
                raise Reject("Mersenne adjacent")
        checks += 9
    if checks != 18:
        raise Reject("row count")
    return checks


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for name, digest in PINS.items():
        if hashlib.sha256((HERE / name).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin: {name}")
    payload = json.loads(CONTRACT.read_text())
    checks = validate(payload) + finite_core_control()
    changed = copy.deepcopy(payload)
    changed["rows"][1]["adjacent_total"] -= 1
    try:
        validate(changed)
    except Reject:
        mutation = 1
    else:
        mutation = 0
    if mutation != 1:
        raise AssertionError("mutation control")
    print(
        "RATE_HALF_MCA_FULL_LIFT_TOP_THIRD_COMMON_CORE_PAYMENT_AUDIT_PASS "
        f"checks={checks} mutations={mutation}/1"
    )


if __name__ == "__main__":
    main()
