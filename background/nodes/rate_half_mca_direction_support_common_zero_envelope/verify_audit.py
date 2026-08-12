#!/usr/bin/env python3
"""Independent recurrence audit of the common-zero envelope."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "2c0e5a87b672f095c87423f88f0914a9c8b72654369d996329d5f7f06aab0328"


class Reject(ValueError):
    pass


def product(values: range) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def fall_rec(x: int, length: int) -> int:
    return product(range(x - length + 1, x + 1))


def rise_rec(x: int, length: int) -> int:
    return product(range(x, x + length))


def recurrence_maximum(R: int, d: int, rank: int, e: int) -> tuple[int, int, int]:
    length = rank + 1
    first_x, last_x = R + rank, 2 * R
    upper = fall_rec(first_x, length)
    lower = fall_rec(first_x - e, length)
    tail = rise_rec(d, rank)
    best_numerator = -1
    best_denominator = 1
    best_x = -1
    checks = 0
    for x in range(first_x, last_x + 1):
        numerator = upper - lower
        denominator = (x - R + d) * tail
        checks += 1
        if best_x < 0 or numerator * best_denominator > best_numerator * denominator:
            best_numerator, best_denominator, best_x = numerator, denominator, x
        if x < last_x:
            upper = upper * (x + 1) // (x + 1 - length)
            lower = lower * (x - e + 1) // (x - e + 1 - length)
    return best_numerator // best_denominator, best_x, checks


def denominator_checks() -> int:
    checks = 0
    for m in range(8, 15):
        for d in range(2, 7):
            for rank in range(1, 5):
                z = min(3, m - rank - 1)
                values = [
                    (m - z + c) * rise_rec(d + c, rank)
                    for c in range(z + 1)
                ]
                if values != sorted(values) or len(set(values)) != len(values):
                    raise Reject("fixed-z denominator")
                checks += 1
    return checks


def audit_shape(contract: object) -> None:
    if not isinstance(contract, dict) or contract.get("schema") != "rate-half-mca-direction-support-common-zero-envelope-v1":
        raise Reject("contract")
    expected_names = ("KoalaBear MCA", "Mersenne-31 MCA")
    if tuple(row.get("name") for row in contract.get("rows", ())) != expected_names:
        raise Reject("rows")


def audit(contract: object) -> dict[str, int]:
    audit_shape(contract)
    scans = 0
    walls = 0
    for row in contract["rows"]:
        R, d, budget = row["R"], row["d"], row["budget"]
        for wall in row["rank_support_walls"]:
            rank, last = wall["rank"], wall["last_paid_e"]
            if last:
                value, argmax, checks = recurrence_maximum(R, d, rank, last)
                scans += checks
                if (value, argmax) != (wall["bound_last"], wall["argmax_last_x"]):
                    raise Reject("last")
                if value > budget:
                    raise Reject("last budget")
            elif (wall["bound_last"], wall["argmax_last_x"]) != (0, None):
                raise Reject("empty")
            first = wall["first_unpaid_e"]
            value, argmax, checks = recurrence_maximum(R, d, rank, first)
            scans += checks
            if (value, argmax) != (wall["bound_first_unpaid"], wall["argmax_first_x"]):
                raise Reject("first")
            if first != last + 1 or value <= budget:
                raise Reject("boundary")
            walls += 1
    return {"scans": scans, "walls": walls, "denominators": denominator_checks()}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    contract = json.loads(CONTRACT.read_text())
    result = audit(contract)
    controls = []
    for row_index, wall_index, key in (
        (0, 0, "bound_last"),
        (0, 0, "argmax_first_x"),
        (0, 0, "last_paid_e"),
    ):
        changed = copy.deepcopy(contract)
        changed["rows"][row_index]["rank_support_walls"][wall_index][key] += 1
        try:
            audit(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("audit controls")
    print(
        "RATE_HALF_MCA_DIRECTION_SUPPORT_COMMON_ZERO_ENVELOPE_AUDIT_PASS "
        f"scan_cells={result['scans']} walls={result['walls']} "
        f"denominators={result['denominators']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
