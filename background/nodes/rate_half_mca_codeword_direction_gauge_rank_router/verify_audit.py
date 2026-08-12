#!/usr/bin/env python3
"""Independent ratio-and-binary-search audit of gauge rank walls."""

from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "eb086905c8b2f89769a5407875a8019f4cf7d9d04062aaf7e299efe22a9581a6"


class Reject(ValueError):
    pass


def value(R: int, d: int, K: int, rank: int) -> int:
    numerator = math.prod(R + K - index for index in range(rank + 1))
    denominator = (d + K) * math.prod(d + index for index in range(rank))
    first = numerator // denominator
    second = (
        math.prod(R + rank - index for index in range(rank + 1))
        // math.prod(d + index for index in range(rank + 1))
    )
    return max(first, second)


def audit(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict):
        raise Reject("contract")
    evaluations = 0
    for row in contract.get("rows", ()):
        R, d, budget, cap = (
            row.get("R"), row.get("d"), row.get("budget"), row.get("ambient_cap")
        )
        for wall in row.get("rank_walls", ()):
            rank = wall.get("rank")
            turn_numerator = R - (rank + 1) * d - rank
            turn = max(rank, turn_numerator // rank)
            candidates = {rank, min(cap, turn), min(cap, turn + 1)}
            for K in candidates:
                value(R, d, K, rank)
                evaluations += 1
            if value(R, d, rank, rank) > budget:
                observed_last = None
            elif value(R, d, cap, rank) <= budget:
                observed_last = cap
            else:
                low, high = max(rank, turn), cap
                while low < high:
                    middle = (low + high + 1) // 2
                    evaluations += 1
                    if value(R, d, middle, rank) <= budget:
                        low = middle
                    else:
                        high = middle - 1
                observed_last = low
            if observed_last != wall.get("last_paid_K"):
                raise Reject("last")
            if observed_last is None:
                first = rank
            elif observed_last == cap:
                first = None
            else:
                first = observed_last + 1
            if first != wall.get("first_unpaid_K"):
                raise Reject("first")
            if observed_last is not None and value(R, d, observed_last, rank) != wall.get("bound_last"):
                raise Reject("last value")
            if first is not None and value(R, d, first, rank) != wall.get("bound_first_unpaid"):
                raise Reject("first value")
    return {"evaluations": evaluations}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    contract = json.loads(CONTRACT.read_text())
    result = audit(contract)
    controls = []
    for row_index, wall_index, key in (
        (0, 0, "bound_last"), (0, 1, "first_unpaid_K"),
        (1, 1, "last_paid_K"),
    ):
        changed = copy.deepcopy(contract)
        changed["rows"][row_index]["rank_walls"][wall_index][key] += 1
        try:
            audit(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("audit controls")
    print(
        "RATE_HALF_MCA_CODEWORD_DIRECTION_GAUGE_RANK_ROUTER_AUDIT_PASS "
        f"evaluations={result['evaluations']} controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
