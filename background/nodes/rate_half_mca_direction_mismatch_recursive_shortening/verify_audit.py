#!/usr/bin/env python3
"""Independent checkpoint audit for repaired recursive shortening."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "610813bd58e34e4c0e5892eb51011eab23b566c8859e5a58065744734f7e0c15"


class Reject(ValueError):
    pass


def direct(R: int, d: int, s: int, j: int) -> int | None:
    denominator = d * d - (R - 2 * d) * s - (R + s) * j
    return None if denominator <= 0 else (R + s) * (d - j) // denominator


def value_at(R: int, d: int, budget: int, j: int, target: int) -> int | None:
    value = direct(R, d, 1, j)
    if value is None or value > budget:
        return None
    for s in range(2, target + 1):
        recursive = (R - j) * value // (d - j)
        direct_value = direct(R, d, s, j)
        value = min(recursive, direct_value) if direct_value is not None else recursive
    return value


def audit(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or contract.get("schema") != "rate-half-mca-direction-mismatch-recursive-shortening-v2":
        raise Reject("contract")
    checks = 0
    for row in contract["rows"]:
        R, d, budget, base_max = (row[key] for key in ("R", "d", "budget", "base_max_j"))
        for s, frontier in row["checkpoints"]:
            if frontier >= 0:
                value = value_at(R, d, budget, frontier, s)
                if value is None or value > budget:
                    raise Reject("paid checkpoint")
                checks += 1
            adjacent = frontier + 1
            if adjacent <= base_max:
                value = value_at(R, d, budget, adjacent, s)
                if value is not None and value <= budget:
                    raise Reject("adjacent checkpoint")
                checks += 1
            elif frontier != base_max and s == 1:
                raise Reject("base frontier")
    return {"checks": checks}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    contract = json.loads(CONTRACT.read_text())
    result = audit(contract)
    changed = copy.deepcopy(contract)
    changed["rows"][0]["checkpoints"][3][1] += 1
    try:
        audit(changed)
    except Reject:
        mutation = 1
    else:
        raise AssertionError("mutation control")
    print(
        "RATE_HALF_MCA_DIRECTION_MISMATCH_RECURSIVE_SHORTENING_AUDIT_PASS "
        f"checks={result['checks']} mutations={mutation}/1"
    )


if __name__ == "__main__":
    main()
