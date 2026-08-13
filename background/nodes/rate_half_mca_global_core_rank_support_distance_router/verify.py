#!/usr/bin/env python3
"""Verify the global-core rank/support/distance composition."""

from __future__ import annotations

import copy
import hashlib
import json
from math import prod
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "0927849d22b4e72dcf5bd42bb96e8c5dcec183a5bba1f7d4ea403b5cb1d55a9f"
PINNED = {
    "background/nodes/rate_half_mca_whole_line_global_core_router/statement.md": "fc7a61d44d6ee26e76db62973669930c65dc2acc6803046da33cdc8b633e90b9",
    "background/nodes/rate_half_mca_codeword_direction_gauge_rank_router/statement.md": "4e8bbe3ba4bda528d2dc88c071704379d6f3647928376df35c1927fbab30185e",
    "background/nodes/rate_half_mca_direction_support_common_zero_envelope/statement.md": "b9fedd832b68610c31013681848237a26f326fba975ed49009e4a80660981815",
    "background/nodes/rate_half_mca_direction_mismatch_recursive_shortening/statement.md": "c9e13d3ab56cbf5b35aa92775606f4a2f78466a584b6a67871cd1ce0adfb05c0",
    "background/nodes/rate_half_mca_direction_mismatch_recursive_shortening/source_contract.json": "d0354c1a0127c3527b405c3f57159e88624e4443439f29bce9e8ebec1a84514e",
}


class Reject(ValueError):
    pass


def falling(x: int, length: int) -> int:
    return prod(range(x - length + 1, x + 1))


def rising(x: int, length: int) -> int:
    return prod(range(x, x + length))


def support_maximum(R: int, d: int, last_s: int, rank: int, e: int) -> tuple[int, int, int]:
    tail = rising(d, rank)
    best_num, best_den, best_x = -1, 1, -1
    checks = 0
    for x in range(R + rank, R + last_s + 1):
        numerator = falling(x, rank + 1) - falling(x - e, rank + 1)
        denominator = (x - R + d) * tail
        checks += 1
        if best_x < 0 or numerator * best_den > best_num * denominator:
            best_num, best_den, best_x = numerator, denominator, x
    return best_num // best_den, best_x, checks


def affine_rank_bound(R: int, d: int, K: int, rank: int) -> int:
    first_num = falling(R + K, rank + 1)
    first_den = (d + K) * rising(d, rank)
    second_num = falling(R + rank, rank + 1)
    second_den = rising(d, rank + 1)
    if first_num * second_den >= second_num * first_den:
        return first_num // first_den
    return second_num // second_den


def direct_direction_bound(R: int, d: int, s: int, j: int) -> int | None:
    denominator = d * d - (R - 2 * d) * s - (R + s) * j
    if denominator <= 0 or j >= d:
        return None
    return (R + s) * (d - j) // denominator


def recursive_value(row: dict[str, object], j: int, target_s: int) -> int:
    R, d = int(row["R"]), int(row["d"])
    direction = row["direction"]
    base_s, value = int(direction["base_s"]), int(direction["base_bound"])
    direct = direct_direction_bound(R, d, base_s, j)
    if direct is not None:
        value = min(value, direct)
    for s in range(base_s + 1, target_s + 1):
        value = (R - j) * value // (d - j)
        direct = direct_direction_bound(R, d, s, j)
        if direct is not None:
            value = min(value, direct)
    return value


def validate_shape(contract: object) -> None:
    if not isinstance(contract, dict) or set(contract) != {"schema", "sources", "rows"}:
        raise Reject("shape")
    if contract["schema"] != "rate-half-mca-global-core-rank-support-distance-router-v1":
        raise Reject("schema")
    expected_sources = {
        "whole_line_router": "rate_half_mca_whole_line_global_core_router",
        "gauge_rank_router": "rate_half_mca_codeword_direction_gauge_rank_router",
        "support_envelope": "rate_half_mca_direction_support_common_zero_envelope",
        "direction_recursion": "rate_half_mca_direction_mismatch_recursive_shortening",
    }
    if contract["sources"] != expected_sources:
        raise Reject("sources")
    if [row.get("name") for row in contract["rows"]] != ["KoalaBear MCA", "Mersenne-31 MCA"]:
        raise Reject("rows")


def validate(contract: object) -> dict[str, int]:
    validate_shape(contract)
    support_checks = rank_checks = direction_checks = interval_checks = 0
    for row in contract["rows"]:
        R, d, budget = (int(row[key]) for key in ("R", "d", "budget"))
        first_s, last_s = int(row["first_s"]), int(row["last_s"])
        paid_rank = int(row["always_paid_rank"])
        for K in range(first_s, last_s + 1):
            if affine_rank_bound(R, d, K, paid_rank) > budget:
                raise Reject("rank prefix")
            rank_checks += 1

        for wall in row["support_walls"]:
            rank, last = int(wall["rank"]), int(wall["last_paid_e"])
            value, argmax, checks = support_maximum(R, d, last_s, rank, last)
            support_checks += checks
            if (value, argmax) != (wall["bound_last"], wall["argmax_last_x"]):
                raise Reject("support last")
            if value > budget:
                raise Reject("support last budget")
            first = int(wall["first_unpaid_e"])
            value, argmax, checks = support_maximum(R, d, last_s, rank, first)
            support_checks += checks
            if (value, argmax) != (wall["bound_first_unpaid"], wall["argmax_first_x"]):
                raise Reject("support first")
            if first != last + 1 or value <= budget:
                raise Reject("support boundary")

        direction = row["direction"]
        for s, frontier in direction["checkpoints"]:
            if recursive_value(row, frontier, s) > budget:
                raise Reject("direction paid")
            if frontier + 1 < d and recursive_value(row, frontier + 1, s) <= budget:
                raise Reject("direction adjacent")
            direction_checks += 2
        if int(direction["first_high_e"]) != R - int(direction["first_frontier_j"]):
            raise Reject("support/defect conversion")

        expected = []
        for wall in row["support_walls"]:
            rank = int(wall["rank"])
            if rank < first_s or rank > last_s:
                raise Reject("rank legality")
            frontier = -1
            for j in range(d):
                if recursive_value(row, j, rank) <= budget:
                    frontier = j
                else:
                    break
            expected.append([
                rank, rank, int(wall["first_unpaid_e"]),
                R - frontier - 1, frontier,
            ])
        if row["first_residual_intervals"] != expected:
            raise Reject("first intervals")
        interval_checks += len(expected)
    return {
        "support": support_checks,
        "rank": rank_checks,
        "direction": direction_checks,
        "intervals": interval_checks,
    }


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for relative, digest in PINNED.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != digest:
            raise Reject(f"source pin: {relative}")
    contract = json.loads(CONTRACT.read_text())
    result = validate(contract)
    controls = []
    mutations = (
        (0, "support_walls", 0, "bound_last"),
        (0, "direction", None, "first_high_e"),
        (1, "support_walls", 2, "argmax_first_x"),
        (1, "first_residual_intervals", 0, 2),
    )
    for row_index, section, item, key in mutations:
        changed = copy.deepcopy(contract)
        target = changed["rows"][row_index][section]
        if item is not None:
            target = target[item]
        target[key] += 1
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_GLOBAL_CORE_RANK_SUPPORT_DISTANCE_ROUTER_PASS "
        f"support_cells={result['support']} rank_cells={result['rank']} "
        f"direction_checks={result['direction']} intervals={result['intervals']} "
        f"mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
