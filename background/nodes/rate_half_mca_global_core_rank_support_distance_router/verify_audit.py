#!/usr/bin/env python3
"""Independent recurrence audit for the composite MCA router."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "0927849d22b4e72dcf5bd42bb96e8c5dcec183a5bba1f7d4ea403b5cb1d55a9f"


class Reject(ValueError):
    pass


def product(values: range) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def fall(x: int, length: int) -> int:
    return product(range(x - length + 1, x + 1))


def rise(x: int, length: int) -> int:
    return product(range(x, x + length))


def recurrence_support_maximum(R: int, d: int, last_s: int, rank: int, e: int) -> tuple[int, int, int]:
    length = rank + 1
    first_x, last_x = R + rank, R + last_s
    upper, lower = fall(first_x, length), fall(first_x - e, length)
    tail = rise(d, rank)
    best_num, best_den, best_x = -1, 1, -1
    checks = 0
    for x in range(first_x, last_x + 1):
        numerator = upper - lower
        denominator = (x - R + d) * tail
        if best_x < 0 or numerator * best_den > best_num * denominator:
            best_num, best_den, best_x = numerator, denominator, x
        checks += 1
        if x < last_x:
            upper = upper * (x + 1) // (x + 1 - length)
            lower_denominator = x - e + 1 - length
            if lower_denominator == 0:
                lower = fall(x - e + 1, length)
            else:
                lower = lower * (x - e + 1) // lower_denominator
    return best_num // best_den, best_x, checks


def direct_bound(R: int, d: int, s: int, j: int) -> int | None:
    denominator = d * d - (R - 2 * d) * s - (R + s) * j
    if denominator <= 0 or j >= d:
        return None
    return (R + s) * (d - j) // denominator


def paid(row: dict[str, object], j: int, target: int) -> bool:
    R, d, budget = (int(row[key]) for key in ("R", "d", "budget"))
    direction = row["direction"]
    s, value = int(direction["base_s"]), int(direction["base_bound"])
    direct = direct_bound(R, d, s, j)
    if direct is not None:
        value = min(value, direct)
    while s < target:
        s += 1
        value = (R - j) * value // (d - j)
        direct = direct_bound(R, d, s, j)
        if direct is not None:
            value = min(value, direct)
    return value <= budget


def monotonicity_checks() -> int:
    checks = 0
    for R in range(12, 20):
        for d in range(3, 7):
            for rank in range(1, 4):
                K = rank + 3
                values = [recurrence_support_maximum(R, d, K, rank, e)[0] for e in range(1, R + 1)]
                if values != sorted(values):
                    raise Reject("support monotonicity")
                checks += 1
    return checks


def audit(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or contract.get("schema") != "rate-half-mca-global-core-rank-support-distance-router-v1":
        raise Reject("contract")
    scans = frontiers = intervals = 0
    for row in contract["rows"]:
        R, d, budget = (int(row[key]) for key in ("R", "d", "budget"))
        last_s = int(row["last_s"])
        for wall in row["support_walls"]:
            for e_key, value_key, x_key in (
                ("last_paid_e", "bound_last", "argmax_last_x"),
                ("first_unpaid_e", "bound_first_unpaid", "argmax_first_x"),
            ):
                value, argmax, checks = recurrence_support_maximum(
                    R, d, last_s, int(wall["rank"]), int(wall[e_key])
                )
                scans += checks
                if (value, argmax) != (wall[value_key], wall[x_key]):
                    raise Reject("support wall")
            if wall["bound_last"] > budget or wall["bound_first_unpaid"] <= budget:
                raise Reject("support budget")
        for s, frontier in row["direction"]["checkpoints"]:
            if not paid(row, frontier, s) or paid(row, frontier + 1, s):
                raise Reject("direction frontier")
            frontiers += 1
        for wall, interval in zip(row["support_walls"], row["first_residual_intervals"]):
            rank = int(wall["rank"])
            frontier = -1
            for j in range(d):
                if paid(row, j, rank):
                    frontier = j
                else:
                    break
            expected = [
                rank, rank, wall["first_unpaid_e"],
                R - frontier - 1, frontier,
            ]
            if interval != expected:
                raise Reject("interval")
            intervals += 1
    return {"scans": scans, "frontiers": frontiers, "intervals": intervals, "monotonicity": monotonicity_checks()}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    contract = json.loads(CONTRACT.read_text())
    result = audit(contract)
    controls = []
    for row, wall, key in ((0, 1, "last_paid_e"), (0, 3, "bound_first_unpaid"), (1, 0, "argmax_last_x")):
        changed = copy.deepcopy(contract)
        changed["rows"][row]["support_walls"][wall][key] += 1
        try:
            audit(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("audit controls")
    print(
        "RATE_HALF_MCA_GLOBAL_CORE_RANK_SUPPORT_DISTANCE_ROUTER_AUDIT_PASS "
        f"scan_cells={result['scans']} frontiers={result['frontiers']} "
        f"intervals={result['intervals']} monotonicity={result['monotonicity']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
