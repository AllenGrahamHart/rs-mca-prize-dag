#!/usr/bin/env python3
"""Independent product audit of rank-refined sparse-direction walls."""

from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "4067e90440ab4d8640074a9c1583a2fba162221956821e329d35dcfbc3e4315d"


class Reject(ValueError):
    pass


def product_bound(R: int, d: int, rank: int, e: int) -> int:
    numerators = [R - e + index for index in range(1, rank + 1)]
    denominators = [d - e + index for index in range(1, rank + 1)]
    for i in range(rank):
        for j in range(rank):
            common = math.gcd(numerators[i], denominators[j])
            numerators[i] //= common
            denominators[j] //= common
    return e * (math.prod(numerators) // math.prod(denominators))


def audit(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict):
        raise Reject("contract")
    checks = 0
    for row in contract.get("rows", ()):
        R, d, budget = row.get("R"), row.get("d"), row.get("budget")
        for wall in row.get("rank_support_walls", ()):
            rank = wall.get("rank")
            last = 0
            for e in range(1, d):
                checks += 1
                if product_bound(R, d, rank, e) <= budget:
                    last = e
            if last != wall.get("last_paid_e"):
                raise Reject("last")
            if last:
                if product_bound(R, d, rank, last) != wall.get("bound_last"):
                    raise Reject("last value")
            elif wall.get("bound_last") != 0:
                raise Reject("empty last")
            if product_bound(R, d, rank, last + 1) != wall.get("bound_first_unpaid"):
                raise Reject("next value")
    return {"checks": checks}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    contract = json.loads(CONTRACT.read_text())
    result = audit(contract)
    controls = []
    for row_index, wall_index, key in (
        (0, 2, "bound_last"), (1, 0, "last_paid_e"),
        (1, 3, "bound_first_unpaid"),
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
        "RATE_HALF_MCA_SPARSE_DIRECTION_AFFINE_RANK_PAYMENT_AUDIT_PASS "
        f"checks={result['checks']} controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
