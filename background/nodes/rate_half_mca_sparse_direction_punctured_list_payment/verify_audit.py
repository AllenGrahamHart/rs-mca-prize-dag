#!/usr/bin/env python3
"""Independent product audit of sparse-direction boundaries."""

from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "a5eb9a794e69df94bc4aa69f040854693c0f411e09c18d2986f982aae7da57c4"


class Reject(ValueError):
    pass


def product_bound(R: int, d: int, s: int, e: int) -> int:
    numerators = [R - e + index for index in range(1, s + 1)]
    denominators = [d - e + index for index in range(1, s + 1)]
    for index in range(s):
        for target in range(s):
            common = math.gcd(numerators[index], denominators[target])
            numerators[index] //= common
            denominators[target] //= common
    return e * (math.prod(numerators) // math.prod(denominators))


def audit(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict):
        raise Reject("contract")
    checks = 0
    for row in contract.get("rows", ()):
        R, d, budget, s = (
            row.get("R"), row.get("d"), row.get("budget"), row.get("first_unpaid_s")
        )
        last = 0
        for e in range(1, d):
            value = product_bound(R, d, s, e)
            checks += 1
            if value <= budget:
                last = e
        if last != row.get("last_paid_e"):
            raise Reject("last")
        if product_bound(R, d, s, last) != row.get("bound_last"):
            raise Reject("last value")
        if product_bound(R, d, s, last + 1) != row.get("bound_first_unpaid"):
            raise Reject("next value")
    return {"checks": checks}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    contract = json.loads(CONTRACT.read_text())
    result = audit(contract)
    controls = []
    for index, key in ((0, "last_paid_e"), (1, "bound_last")):
        changed = copy.deepcopy(contract)
        changed["rows"][index][key] += 1
        try:
            audit(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    changed = copy.deepcopy(contract)
    changed["rows"][0]["bound_first_unpaid"] -= 1
    try:
        audit(changed)
    except Reject:
        controls.append(True)
    else:
        controls.append(False)
    if not all(controls):
        raise AssertionError("audit controls")
    print(
        "RATE_HALF_MCA_SPARSE_DIRECTION_PUNCTURED_LIST_PAYMENT_AUDIT_PASS "
        f"checks={result['checks']} controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
