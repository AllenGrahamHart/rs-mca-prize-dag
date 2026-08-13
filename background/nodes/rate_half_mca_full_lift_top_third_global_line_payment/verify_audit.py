#!/usr/bin/env python3
"""Independent audit of the full-lift global-line payment."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "e769fbff60173dc27ab951c03627eb627c4835ad5cb057bb80c66f3ec677be79"
PINS = {
    "statement.md": "8d103c4c092961387fa02ee18ff851a084c0f7774c0b4b238d1e7fba42dbe02d",
    "proof.md": "5abca3dd268f99b38c483fb12b22c9c7d91e0908b5a4ef389195b648651e3cb2",
}


class Reject(ValueError):
    pass


def finite_cross_layer_control() -> int:
    E = set(range(11))
    missed = [{0, 1, 2}, {3, 4}, {5, 6, 7}]
    r = [len(current) for current in missed]
    shared = set.intersection(*(E - current for current in missed))
    if len(shared) != len(E) - sum(r) or len(shared) < 3:
        raise Reject("cross-layer overlap")
    blocks = [
        {0, 1, 2}, {0, 1, 3}, {0, 1, 4}, {0, 1, 5}, {0, 1, 6},
    ]
    core = set.intersection(*blocks)
    stripped = [block - core for block in blocks]
    if len(core) != 2 or any(
        left & right for i, left in enumerate(stripped) for right in stripped[i + 1:]
    ):
        raise Reject("total-core packing")
    return len(shared) + len(blocks)


def independent_endpoint(R: int, d: int, K: int, e: int) -> tuple[int, ...] | None:
    N, m, c = R + K, d + K, K - 1
    n = N - e
    s = (e - K) // 3
    H = e - s - 1
    u = e // 2
    values = []
    for h in (u, H):
        A = m - h
        D = A * A - n * c
        if D <= 0:
            return None
        values.append(n * (A - c) // D)
    prefix = (e - 1) * values[0] + values[1]
    return s, H, u, values[0], values[1], prefix, prefix + N - m + 1


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
        got = independent_endpoint(R, d, K, row["last_paid_e"])
        expected = tuple(row[key] for key in (
            "last_s", "last_H", "last_u", "last_J_u", "last_J_H",
            "last_prefix", "last_total",
        ))
        if got != expected or got[-1] > budget:
            raise Reject("last endpoint")
        if row["global_line_cap"] != R - d + 1:
            raise Reject("global line")
        e = row["adjacent_e"]
        if independent_endpoint(R, d, K, e) is not None:
            raise Reject("adjacent")
        H = e - (e - K) // 3 - 1
        A = d + K - H
        D = A * A - (R + K - e) * (K - 1)
        if (H, D) != (row["adjacent_H"], row["adjacent_H_denominator"]):
            raise Reject("adjacent record")
        checks += 8
    if checks != 16:
        raise Reject("row count")
    return checks


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for name, digest in PINS.items():
        if hashlib.sha256((HERE / name).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin: {name}")
    payload = json.loads(CONTRACT.read_text())
    checks = validate(payload) + finite_cross_layer_control()
    changed = copy.deepcopy(payload)
    changed["rows"][1]["global_line_cap"] += 1
    try:
        validate(changed)
    except Reject:
        mutation = 1
    else:
        mutation = 0
    if mutation != 1:
        raise AssertionError("mutation control")
    print(
        "RATE_HALF_MCA_FULL_LIFT_TOP_THIRD_GLOBAL_LINE_PAYMENT_AUDIT_PASS "
        f"checks={checks} mutations={mutation}/1"
    )


if __name__ == "__main__":
    main()
