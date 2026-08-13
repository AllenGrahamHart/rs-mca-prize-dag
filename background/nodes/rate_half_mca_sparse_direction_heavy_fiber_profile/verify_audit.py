#!/usr/bin/env python3
"""Independent product and allocation audit of the heavy-fiber profile."""

from __future__ import annotations

import copy
import hashlib
import itertools
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "11c2587813b0f6973198fc3c0c772c0193e43c7b4c099c05e1b5c79b9ef1d636"


class Reject(ValueError):
    pass


def product_quotient(numerators: list[int], denominators: list[int]) -> int:
    for i in range(len(numerators)):
        for j in range(len(denominators)):
            common = math.gcd(numerators[i], denominators[j])
            numerators[i] //= common
            denominators[j] //= common
    return math.prod(numerators) // math.prod(denominators)


def cumulative_cap(R: int, d: int, rank: int, e: int, h: int) -> int:
    return product_quotient(
        [R - e + i for i in range(1, rank + 1)],
        [d - h + i for i in range(1, rank + 1)],
    )


def product_profile(R: int, d: int, rank: int, e: int) -> int:
    previous = 0
    total = 0
    for h in range(1, e + 1):
        current = cumulative_cap(R, d, rank, e, h)
        total += (current - previous) * (e // h)
        previous = current
    return total


def brute_allocation(e: int, caps: tuple[int, ...]) -> int:
    best = 0
    ranges = [range(caps[-1] + 1) for _ in range(e)]
    for allocation in itertools.product(*ranges):
        if all(sum(allocation[:h]) <= caps[h - 1] for h in range(1, e + 1)):
            best = max(best, sum(allocation[h - 1] * (e // h) for h in range(1, e + 1)))
    return best


def telescoping_allocation(e: int, caps: tuple[int, ...]) -> int:
    previous = 0
    total = 0
    for h, cap in enumerate(caps, start=1):
        total += (cap - previous) * (e // h)
        previous = cap
    return total


def audit(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict):
        raise Reject("contract")
    checks = 0
    for row in contract.get("rows", ()):
        R, d, budget = row.get("R"), row.get("d"), row.get("budget")
        for wall in row.get("rank_support_prefixes", ()):
            rank = wall.get("rank")
            end = wall.get("paid_prefix_end")
            first = wall.get("adjacent_first_unpaid")
            if first != end + 1:
                raise Reject("adjacency")
            if end:
                end_value = product_profile(R, d, rank, end)
                checks += 1
                if end_value != wall.get("bound_at_end"):
                    raise Reject("end")
            elif wall.get("bound_at_end") != 0:
                raise Reject("empty end")
            else:
                end_value = 0
            first_value = product_profile(R, d, rank, first)
            checks += 1
            if first_value != wall.get("bound_at_first_unpaid"):
                raise Reject("first")
            if not end_value <= budget < first_value:
                raise Reject("budget")
    allocation_checks = 0
    for e in range(1, 6):
        for caps in itertools.combinations_with_replacement(range(4), e):
            if brute_allocation(e, caps) != telescoping_allocation(e, caps):
                raise Reject("allocation formula")
            allocation_checks += 1
    return {"checks": checks, "allocation_checks": allocation_checks}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    contract = json.loads(CONTRACT.read_text())
    result = audit(contract)
    controls = []
    for row_index, wall_index, key in (
        (0, 2, "bound_at_end"),
        (1, 0, "paid_prefix_end"),
        (1, 3, "bound_at_first_unpaid"),
    ):
        changed = copy.deepcopy(contract)
        changed["rows"][row_index]["rank_support_prefixes"][wall_index][key] += 1
        try:
            audit(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("audit controls")
    print(
        "RATE_HALF_MCA_SPARSE_DIRECTION_HEAVY_FIBER_PROFILE_AUDIT_PASS "
        f"checks={result['checks']} allocations={result['allocation_checks']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
