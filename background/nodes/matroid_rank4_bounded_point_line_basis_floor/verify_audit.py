#!/usr/bin/env python3
"""Independent audit of the rank-four point/line recurrence."""

from __future__ import annotations

import hashlib
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "1e81b6891afdd1d54f65891b2f29128bb3fd47ff53526fa83e769446bc041f97"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def h_value(a: int, r: int) -> int:
    return min((a + 1) // 2, (a + r) // 4)


def coloop6(a: int, r: int) -> int:
    return (a + r - 1) * (r - 1) * (r - 2)


def increment6(a: int, r: int) -> int:
    return 3 * (a + r - h_value(a, r) - 1) * (r - 2)


def dynamic(a: int, r: int) -> int:
    value = 6
    for current in range(4, r + 1):
        value = min(coloop6(a, current), value + increment6(a, current))
    return value


def candidate_minimum(a: int, r: int) -> tuple[int, int]:
    candidates = [(6 + sum(increment6(a, x) for x in range(4, r + 1)), 3)]
    for reset in range(4, r + 1):
        candidates.append(
            (
                coloop6(a, reset)
                + sum(increment6(a, x) for x in range(reset + 1, r + 1)),
                reset,
            )
        )
    return min(candidates)


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    checks = 0
    sign_checks = 0
    for a in range(1, 51):
        for r in range(3, 91):
            value, reset = candidate_minimum(a, r)
            require(value == dynamic(a, r), "unfolded recurrence")
            if 4 <= reset < r:
                left_sign = 3 * h_value(a, reset) - a - 2
                right_sign = 3 * h_value(a, reset + 1) - a - 2
                require(left_sign <= right_sign, "one-sign ordering")
                sign_checks += 1
            checks += 1
    print(
        "MATROID_RANK4_BOUNDED_POINT_LINE_BASIS_FLOOR_AUDIT_PASS "
        f"recurrence_checks={checks} sign_checks={sign_checks}"
    )


if __name__ == "__main__":
    main()
