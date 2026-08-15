#!/usr/bin/env python3
"""Independent audit of the bounded-parallel rank-three basis floor."""

from __future__ import annotations

import json
from functools import cache
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


@cache
def maximum_square_sum(total: int, ceiling: int, largest: int, classes: int) -> int:
    if total == 0:
        return 0 if classes >= 2 else -10**9
    best = -10**9
    for part in range(min(total, ceiling, largest), 0, -1):
        suffix = maximum_square_sum(total - part, ceiling, part, classes + 1)
        best = max(best, part * part + suffix)
    return best


def main() -> None:
    p = json.loads(CONTRACT.read_text())["parameters"]
    partition_checks = 0
    for a in p["audited_parallel_ceilings"][:8]:
        for total in range(2, 33):
            squares = maximum_square_sum(total, a, total, 0)
            independent_twice = total * total - squares
            require(independent_twice >= total * (total - a), "rank-two partition")
            partition_checks += 1

    contraction_checks = 0
    for c in range(1, 11):
        for total in range(2 * c, 31):
            cross_floor = c * (total - c)
            m = total + c
            if m >= 3 * c:
                require(cross_floor >= m - 2, "contraction partition")
                contraction_checks += 1

    print(
        "MATROID_RANK3_BOUNDED_PARALLEL_BASIS_FLOOR_AUDIT_PASS "
        f"partition_checks={partition_checks} contraction_checks={contraction_checks}"
    )


if __name__ == "__main__":
    main()
