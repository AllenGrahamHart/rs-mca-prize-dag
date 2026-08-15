#!/usr/bin/env python3
"""Verify the rank-four bounded point/line basis-floor contract."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "1e81b6891afdd1d54f65891b2f29128bb3fd47ff53526fa83e769446bc041f97"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def sum_integers(lo: int, hi: int) -> int:
    return 0 if lo > hi else (lo + hi) * (hi - lo + 1) // 2


def square_prefix(value: int) -> int:
    return value * (value + 1) * (2 * value + 1) // 6


def sum_squares(lo: int, hi: int) -> int:
    return 0 if lo > hi else square_prefix(hi) - square_prefix(lo - 1)


def progression_sums(lo: int, hi: int, residue: int) -> tuple[int, int, int]:
    first = lo + ((residue - lo) % 4)
    if first > hi:
        return 0, 0, 0
    count = (hi - first) // 4 + 1
    last = first + 4 * (count - 1)
    index_sum = count * (count - 1) // 2
    index_square_sum = count * (count - 1) * (2 * count - 1) // 6
    return (
        count,
        count * (first + last) // 2,
        count * first * first + 8 * first * index_sum + 16 * index_square_sum,
    )


def sum_h_weight(a: int, lo: int, hi: int) -> int:
    if lo > hi:
        return 0
    half = (a + 1) // 2
    constant_start = 4 * half - a
    floor_end = min(hi, constant_start - 1)
    total = 0
    if lo <= floor_end:
        numerator = 0
        for residue in range(4):
            count, value_sum, square_sum = progression_sums(lo, floor_end, residue)
            remainder = (a + residue) % 4
            shifted_a = a - remainder
            numerator += square_sum + (shifted_a - 2) * value_sum - 2 * shifted_a * count
        require(numerator % 4 == 0, "residue divisibility")
        total += numerator // 4
    constant_lo = max(lo, constant_start)
    if constant_lo <= hi:
        count = hi - constant_lo + 1
        total += half * (sum_integers(constant_lo, hi) - 2 * count)
    return total


def sum_increment6(a: int, lo: int, hi: int) -> int:
    if lo > hi:
        return 0
    count = hi - lo + 1
    value_sum = sum_integers(lo, hi)
    unfloored = (
        (a - 1) * (value_sum - 2 * count)
        + sum_squares(lo, hi)
        - 2 * value_sum
    )
    return 3 * (unfloored - sum_h_weight(a, lo, hi))


def h_value(a: int, r: int) -> int:
    return min((a + 1) // 2, (a + r) // 4)


def coloop6(a: int, r: int) -> int:
    return (a + r - 1) * (r - 1) * (r - 2)


def increment6(a: int, r: int) -> int:
    return 3 * (a + r - h_value(a, r) - 1) * (r - 2)


def recurrence(a: int, r: int) -> int:
    value = 6
    for current in range(4, r + 1):
        value = min(coloop6(a, current), value + increment6(a, current))
    return value


def closed(a: int, r: int) -> int:
    base = 6 + sum_increment6(a, 4, r)
    half = (a + 1) // 2
    threshold = (a + 4) // 3
    if threshold > half:
        reset = r
    else:
        first_nondecreasing = max(5, 4 * threshold - a)
        reset = r if first_nondecreasing > r else first_nondecreasing - 1
    reset_value = coloop6(a, reset) + sum_increment6(a, reset + 1, r)
    return min(base, reset_value)


def validate(data: object) -> int:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "matroid-rank4-bounded-point-line-basis-floor-v1", "schema")
    require(data.get("dependencies") == ["matroid_rank3_bounded_parallel_basis_floor"], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["rank"], p["minimum_a"], p["minimum_r"]) == (4, 1, 3), "range")
    require(p["loopless"] is True, "loopless")
    require(p["parallel_class_ceiling"] == "a", "point ceiling")
    require(p["rank2_flat_ceiling"] == "a+1", "line ceiling")
    require(p["basis_floor"] == "6*b(M)>=Q_a(r)", "basis floor")
    require(p["reset_difference_sign"] == "3*h_a(x)-a-2", "reset sign")
    require((p["audited_a_maximum"], p["audited_r_maximum"]) == (80, 120), "audit grid")

    checks = 0
    for a in range(1, 81):
        previous = 6
        for r in range(3, 121):
            value = recurrence(a, r)
            require(value == closed(a, r), "closed evaluator")
            require(value >= 6, "positive floor")
            if r >= 4:
                h = h_value(a, r)
                require(h <= (a + 1) // 2 and h <= (a + r) // 4, "smallest-class ceiling")
                for c in range(1, h + 1):
                    contraction6 = 3 * (a + r - c - 1) * (r - 2)
                    require(contraction6 >= increment6(a, r), "contraction monotonicity")
                    checks += 1
                require(value == min(coloop6(a, r), previous + increment6(a, r)), "recurrence step")
            previous = value
            checks += 3
    require("does not establish" in str(data.get("nonclaim")), "nonclaim")
    return checks


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    checks = validate(data)
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item["parameters"].__setitem__("rank", 3),
        lambda item: item["parameters"].__setitem__("loopless", False),
        lambda item: item["parameters"].__setitem__("rank2_flat_ceiling", "a+2"),
        lambda item: item["parameters"].__setitem__("basis_floor", "b(M)>=Q_a(r)"),
        lambda item: item["parameters"].__setitem__("reset_difference_sign", "3*h_a(x)-a-1"),
    )
    caught = 0
    for mutation in mutations:
        altered = copy.deepcopy(data)
        mutation(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    print(
        "MATROID_RANK4_BOUNDED_POINT_LINE_BASIS_FLOOR_PASS "
        f"checks={checks} grid=80x118 controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
