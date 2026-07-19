#!/usr/bin/env python3
"""Independent audit of the order-sixteen path route fence."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def multiply(left: tuple[int, ...], right: tuple[int, ...], p: int) -> tuple[int, ...]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % p
    return tuple(answer)


def locator(roots: tuple[int, ...], p: int) -> tuple[int, ...]:
    answer = (1,)
    for root in roots:
        answer = multiply(answer, (-root % p, 1), p)
    return answer


def evaluate(poly: tuple[int, ...], x: int, p: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % p
    return value


def collinear(a: tuple[int, ...], b: tuple[int, ...], c: tuple[int, ...], p: int) -> bool:
    left = tuple((y - x) % p for x, y in zip(a[:-1], b[:-1], strict=True))
    right = tuple((z - x) % p for x, z in zip(a[:-1], c[:-1], strict=True))
    pivot = next((i for i, value in enumerate(left) if value), None)
    if pivot is None:
        return False
    scalar = right[pivot] * pow(left[pivot], -1, p) % p
    return scalar not in (0, 1) and all(
        right[i] == scalar * left[i] % p for i in range(len(left))
    )


def main() -> None:
    p = 17
    domain = tuple(range(1, 17))
    polys = (
        (0,),
        (8, 5, 13, 2, 15, 3, 1, 8),
        (12, 16, 8, 3, 7, 12, 10, 4),
        (5, 13, 0, 14, 16, 2, 4, 1),
    )
    received = [4, 14, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 2]
    counts = tuple(
        sum(evaluate(poly, x, p) == value for x, value in zip(domain, received, strict=True))
        for poly in polys
    )
    assert counts == (11, 11, 11, 11)
    received[13] = (received[13] + 1) % p
    mutated_counts = tuple(
        sum(evaluate(poly, x, p) == value for x, value in zip(domain, received, strict=True))
        for poly in polys
    )
    assert mutated_counts != counts

    exponents = {
        "t0": (0, 14, 1),
        "t1": (12, 5, 13),
        "t2": (11, 10, 4, 6),
        "t3": (15, 3, 7),
        "r": (2,),
        "s": (8,),
    }
    p2 = 97
    generator = pow(5, 6, p2)
    sets = {key: tuple(pow(generator, exponent, p2) for exponent in values) for key, values in exponents.items()}
    a0, a1, a2, a3 = (locator(sets[key], p2) for key in ("t0", "t1", "t2", "t3"))
    p0 = locator(sets["t0"] + sets["s"], p2)
    p1 = locator(sets["t1"] + sets["r"], p2)
    assert not collinear(a0, a1, a3, p2)
    assert not collinear(p0, p1, a2, p2)
    search_result = json.loads(
        (
            ROOT
            / "background/nodes/rate_half_list_budget_three_path_power_two_witness"
            / "notes/order16_proper_search_result.json"
        ).read_text()
    )
    assert search_result["complete"] is True
    assert search_result["field_prime"] == 97
    assert search_result["second_pencils"] == 960
    assert search_result["path_assignments"] == 3_830_400
    assert search_result["witness_count"] == 0 and search_result["witnesses"] == []
    print(
        "AUDIT_RATE_HALF_LIST_BUDGET_THREE_PATH_POWER_TWO_WITNESS_PASS "
        f"agreements={counts} mutation={mutated_counts} "
        "proper_F97_assignments=3830400 witnesses=0"
    )


if __name__ == "__main__":
    main()
