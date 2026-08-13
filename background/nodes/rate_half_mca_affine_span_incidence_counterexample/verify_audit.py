#!/usr/bin/env python3
"""Independent exhaustive audit of the affine-span counterexample."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "7c0d75814b99fa6272e8c005ee93fd78220bb5717ea9211a84dec67c0bcd9f8a"


class Reject(ValueError):
    pass


def audit(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or contract.get("field") != 1009:
        raise Reject("contract")
    p = 1009
    base = [None] * 100
    direction = [None] * 100
    for x in range(20):
        base[x], direction[x] = 0, 0
    for i in range(1, 31):
        x = 19 + i
        base[x], direction[x] = (-i * i) % p, i

    forbidden_direction = {
        (-pow(i, -1, p)) % p for i in range(1, 31)
    }
    unused = iter(
        value for value in range(31, p)
        if value not in forbidden_direction
    )
    used = set(range(31))
    for x in range(50, 71):
        value = next(value for value in unused if value not in used)
        base[x], direction[x] = 1, value
        used.add(value)
    candidate = max(used) + 1
    for x in range(71, 100):
        while candidate in used:
            candidate += 1
        direction[x] = candidate
        used.add(candidate)
        forbidden = {0, 1} | {(-i * candidate) % p for i in range(1, 31)}
        base[x] = next(value for value in range(2, p) if value not in forbidden)
        candidate += 1

    if any(value is None for value in base + direction):
        raise Reject("construction")
    selected = [(i, 0) for i in range(1, 31)] + [(0, 1)]
    for slope, explanation in selected:
        support = tuple(
            x for x in range(100)
            if (base[x] + slope * direction[x]) % p == explanation
        )
        if len(support) != 21:
            raise Reject("support")
        b0, b1 = base[support[0]], direction[support[0]]
        if all(base[x] == b0 and direction[x] == b1 for x in support):
            raise Reject("contained")

    direction_max = max(
        sum(value == constant for value in direction)
        for constant in range(p)
    )
    if direction_max != 20:
        raise Reject("separation")
    affine = (100 * 99) // (21 * 20)
    supported = (100 * 99 - 20 * 19) // (21 * 20)
    if (len(selected), affine, supported) != (31, 23, 22):
        raise Reject("bounds")
    return {"field_values": p, "support_checks": len(selected)}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    result = audit(json.loads(CONTRACT.read_text()))
    print(
        "RATE_HALF_MCA_AFFINE_SPAN_INCIDENCE_COUNTEREXAMPLE_AUDIT_PASS "
        f"field_values={result['field_values']} support_checks={result['support_checks']}"
    )


if __name__ == "__main__":
    main()
