#!/usr/bin/env python3
"""Independent arithmetic and tuple audit of affine-basis support payment."""

from __future__ import annotations

import copy
import hashlib
import itertools
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "876a14f1386caafd12c5227cbb88be352eb05fc7d9ca9d26c55b75eb68e7d6e0"


class Reject(ValueError):
    pass


def fall_rec(x: int, length: int) -> int:
    value = 1
    for offset in range(length):
        value *= x - offset
    return value


def rise_rec(x: int, length: int) -> int:
    value = 1
    for offset in range(length):
        value *= x + offset
    return value


def reduce_pair(numerator: int, denominator: int) -> tuple[int, int]:
    common = math.gcd(numerator, denominator)
    return numerator // common, denominator // common


def independent_bound(R: int, d: int, K: int, rank: int, e: int) -> int:
    a_num, a_den = reduce_pair(
        fall_rec(R + K, rank + 1),
        (d + K) * rise_rec(d, rank),
    )
    b_num, b_den = reduce_pair(
        fall_rec(R + rank, rank + 1),
        rise_rec(d, rank + 1),
    )
    if a_num * b_den >= b_num * a_den:
        envelope_num, envelope_den = a_num, a_den
    else:
        envelope_num, envelope_den = b_num, b_den
    base = fall_rec(R + rank, rank + 1)
    support_num = base - fall_rec(R + rank - e, rank + 1)
    numerator, denominator = reduce_pair(envelope_num * support_num, envelope_den * base)
    return numerator // denominator


def tuple_subtraction_checks() -> int:
    checks = 0
    for n in range(3, 9):
        universe = tuple(range(n))
        for rank in range(1, min(3, n - 1) + 1):
            length = rank + 1
            for e in range(1, n - rank + 1):
                support = set(range(e))
                outside = tuple(range(e, n))
                for z in range(0, min(len(outside), n - length) + 1):
                    zero = set(outside[:z])
                    active = tuple(x for x in universe if x not in zero)
                    observed = sum(
                        1 for item in itertools.permutations(active, length)
                        if any(x in support for x in item)
                    )
                    expected = fall_rec(n - z, length) - fall_rec(n - e - z, length)
                    if observed != expected:
                        raise Reject("tuple subtraction")
                    checks += 1
    return checks


def support_monotonicity_checks() -> int:
    checks = 0
    for R in range(3, 12):
        for rank in range(1, 4):
            if rank > R:
                continue
            base = fall_rec(R + rank, rank + 1)
            previous = -1
            for e in range(1, R + 1):
                numerator = base - fall_rec(R + rank - e, rank + 1)
                if numerator <= previous:
                    raise Reject("support monotonicity")
                previous = numerator
                checks += 1
    return checks


def audit(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict):
        raise Reject("contract")
    checks = 0
    for row in contract.get("rows", ()):
        R, d, budget, K = row.get("R"), row.get("d"), row.get("budget"), row.get("K_cap")
        for wall in row.get("rank_support_walls", ()):
            rank = wall.get("rank")
            last = wall.get("last_paid_e")
            end_value = 0 if last == 0 else independent_bound(R, d, K, rank, last)
            checks += 1
            if end_value != wall.get("bound_last") or end_value > budget:
                raise Reject("end")
            first = wall.get("first_unpaid_e")
            if first is None:
                if last != R or wall.get("bound_first_unpaid") is not None:
                    raise Reject("full")
            else:
                first_value = independent_bound(R, d, K, rank, first)
                checks += 1
                if first != last + 1 or first_value != wall.get("bound_first_unpaid"):
                    raise Reject("first")
                if first_value <= budget:
                    raise Reject("unpaid")
    return {
        "checks": checks,
        "tuple_checks": tuple_subtraction_checks(),
        "monotonicity_checks": support_monotonicity_checks(),
    }


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    contract = json.loads(CONTRACT.read_text())
    result = audit(contract)
    controls = []
    for row_index, wall_index, key in (
        (0, 2, "bound_last"),
        (1, 2, "last_paid_e"),
        (1, 5, "bound_first_unpaid"),
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
        "RATE_HALF_MCA_DIRECTION_SUPPORT_AFFINE_BASIS_PAYMENT_AUDIT_PASS "
        f"checks={result['checks']} tuples={result['tuple_checks']} "
        f"monotonicity={result['monotonicity_checks']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
