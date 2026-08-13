#!/usr/bin/env python3
"""Independent audit of the top-third affine-line payment."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "9132d3a2639804030b00e3f6d4c547ffd56430c0822b67cb318467c72e260b18"
PINS = {
    "statement.md": "d076028804ae5734d589e824fa35f6b5c4db3dceed5e85db112d3d1228c50683",
    "proof.md": "36615b434d592f9c68034de004fcb6f2199bb62efc9e1ec708edf3ba9f31f1e4",
}


class Reject(ValueError):
    pass


def grouped_floor_sum(numerator: int, first: int, last: int) -> int:
    total = 0
    x = first
    while x <= last:
        quotient = numerator // x
        if quotient == 0:
            break
        end = min(last, numerator // quotient)
        total += quotient * (end - x + 1)
        x = end + 1
    return total


def finite_triple_control() -> int:
    E = set(range(8))
    missed = [{0, 1}, {2, 3}, {4, 5}]
    sets = [E - current for current in missed]
    triple = set.intersection(*sets)
    e, r, K = 8, 2, 2
    if len(triple) != e - 3 * r or len(triple) < K:
        raise Reject("triple overlap")
    blocks = [{0, 1, 2}, {0, 3, 4}, {0, 5, 6}]
    core = set.intersection(*blocks)
    stripped = [block - core for block in blocks]
    if any(left & right for i, left in enumerate(stripped) for right in stripped[i + 1:]):
        raise Reject("outside packing")
    return len(triple) + sum(map(len, stripped))


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
        N, m, c = R + K, d + K, K - 1
        e = d - 1
        s = (e - K) // 3
        H = e - s - 1
        u = e // 2
        if (row["endpoint_e"], row["s"], row["H"], row["u"]) != (e, s, H, u):
            raise Reject("indices")
        for h, cap, prefix in (
            (u, 31, "J_u"),
            (H, 47, "J_H"),
        ):
            A = m - h
            numerator = N * (A - c)
            denominator = A * A - N * c
            value = Fraction(numerator, denominator)
            if value.numerator // value.denominator > cap:
                raise Reject(prefix)
            if row[f"{prefix}_numerator"] != numerator:
                raise Reject(f"{prefix} numerator")
            if row[f"{prefix}_denominator"] != denominator:
                raise Reject(f"{prefix} denominator")
            checks += 3
        n = N - e
        A = m - e
        line = grouped_floor_sum(n - c, A - c, A + s - c)
        if row["line_sum"] != line:
            raise Reject("grouped line sum")
        total = (d - 2) * 31 + 47 + line
        if row["uniform_total"] != total or total > budget:
            raise Reject("total")
        checks += 3
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
    checks = validate(payload) + finite_triple_control()
    changed = copy.deepcopy(payload)
    changed["rows"][0]["line_sum"] += 1
    try:
        validate(changed)
    except Reject:
        mutation = 1
    else:
        mutation = 0
    if mutation != 1:
        raise AssertionError("mutation control")
    print(
        "RATE_HALF_MCA_SPARSE_DIRECTION_TOP_THIRD_AFFINE_LINE_PAYMENT_AUDIT_PASS "
        f"checks={checks} mutations={mutation}/1"
    )


if __name__ == "__main__":
    main()
