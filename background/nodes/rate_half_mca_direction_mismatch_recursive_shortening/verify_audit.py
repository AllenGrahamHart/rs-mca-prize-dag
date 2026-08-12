#!/usr/bin/env python3
"""Independent dimension-major audit of recursive shortening."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "d0354c1a0127c3527b405c3f57159e88624e4443439f29bce9e8ebec1a84514e"


class Reject(ValueError):
    pass


def audit_row(row: dict[str, object]) -> dict[str, object]:
    R, d, budget, base, base_bound = (
        int(row[key]) for key in ("R", "d", "budget", "base_s", "base_bound")
    )
    values = []
    for j in range(d):
        n = R + base
        denominator = d * d - (R - 2 * d) * base - n * j
        direct = n * (d - j) // denominator if denominator > 0 else None
        values.append(min(base_bound, direct) if direct is not None else base_bound)
    last = [base] * d
    s = base
    transitions = 0
    while values:
        s += 1
        next_values = []
        for j, value in enumerate(values):
            recursive = (R - j) * value // (d - j)
            n = R + s
            denominator = d * d - (R - 2 * d) * s - n * j
            direct = n * (d - j) // denominator if denominator > 0 else None
            candidate = min(recursive, direct) if direct is not None else recursive
            transitions += 1
            if candidate > budget:
                break
            next_values.append(candidate)
            last[j] = s
        values = next_values
    checkpoints = []
    for dimension, _ in row.get("checkpoints", []):
        frontier = next((j - 1 for j, endpoint in enumerate(last) if endpoint < dimension), d - 1)
        checkpoints.append([dimension, frontier])
    if checkpoints != row.get("checkpoints"):
        raise Reject("checkpoints")
    if last[0] != row.get("rank_regular_last_s"):
        raise Reject("rank regular")
    if sum(endpoint > base for endpoint in last) != row.get("extended_defects"):
        raise Reject("extended defects")
    return {"transitions": transitions, "last": last}


def audit(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict):
        raise Reject("contract")
    transitions = 0
    for row in contract.get("rows", ()):
        result = audit_row(row)
        transitions += int(result["transitions"])
    return {"transitions": transitions}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    contract = json.loads(CONTRACT.read_text())
    result = audit(contract)
    controls = []
    for index in (0, 1):
        changed = copy.deepcopy(contract)
        changed["rows"][index]["checkpoints"][-1][1] += 1
        try:
            audit(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    changed = copy.deepcopy(contract)
    changed["rows"][0]["extended_defects"] -= 1
    try:
        audit(changed)
    except Reject:
        controls.append(True)
    else:
        controls.append(False)
    if not all(controls):
        raise AssertionError("audit controls")
    print(
        "RATE_HALF_MCA_DIRECTION_MISMATCH_RECURSIVE_SHORTENING_AUDIT_PASS "
        f"transitions={result['transitions']} controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
