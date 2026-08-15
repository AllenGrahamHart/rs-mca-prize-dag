#!/usr/bin/env python3
"""Verify the uniform corank-three projective-basis cap."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "598eb55c00ce2778fa57b185360f80208b5ae34b418a001bd5293b55d6669a7d"
R = 1048576
W = 67472
RANK_GAP = 67474
T_MAX = R - 10
TARGET = 983902549


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


def basis_floor6(a: int, r: int = RANK_GAP) -> int:
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


def row(t: int) -> dict[str, int]:
    floor6 = basis_floor6(t + 1)
    n = R + t + 3
    resource = n * (n - 1) * (n - 2) * (n - 3)
    ordered = 4 * floor6
    cap, remainder = divmod(resource, ordered)
    return {
        "t": t,
        "basis_floor_times_6": floor6,
        "ordered_basis_floor": ordered,
        "record_cap": cap,
        "division_remainder": remainder,
        "next_integer_gap": (TARGET + 1) * ordered - resource,
    }


def validate_contract(data: object) -> None:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-kernel-corank3-uniform-projective-basis-cap-v1", "schema")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["R"], p["w"], p["dimension"], p["rank_gap"]) == (R, W, 3, RANK_GAP), "constants")
    require((p["t_minimum"], p["t_maximum"]) == (0, T_MAX), "range")
    require(p["parallel_class_ceiling"] == "a", "point ceiling")
    require(p["rank2_flat_ceiling"] == "a+1", "line ceiling")
    require(p["uniform_record_cap"] == TARGET, "target")
    require(p["complete_row"] == row(0), "complete row")
    require(p["adjacent_row"] == row(1), "adjacent row")
    require(p["official_endpoint"] == row(T_MAX), "official endpoint")
    evidence = data.get("evidence")
    require(isinstance(evidence, dict), "evidence")
    require(evidence["checked_rows"] == T_MAX + 1, "checked rows")
    require(evidence["maximum_record_cap"] == TARGET and evidence["first_maximizer"] == 0, "maximum")
    require(evidence["first_excess"] is None, "no excess")
    require((evidence["worker_timeout_seconds"], evidence["worker_memory_mb"], evidence["max_containers"]) == (60, 512, 1), "worker bounds")
    for key in ("script", "result"):
        path = ROOT / evidence[key]
        require(path.is_file(), f"{key} path")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == evidence[f"{key}_sha256"], f"{key} hash")
    result = json.loads((ROOT / evidence["result"]).read_text())
    require(result["complete"] is True and result["schema"] == evidence["result_schema"], "result schema")
    require(result["scan"]["checked_rows"] == T_MAX + 1, "result rows")
    require(result["scan"]["maximum_record_cap"] == TARGET, "result maximum")
    require(result["scan"]["first_excess"] is None, "result excess")
    require("does not select" in str(data.get("nonclaim")), "nonclaim")


def scan_rows() -> tuple[int, int, int]:
    maximum = (-1, -1)
    first_excess = -1
    for t in range(T_MAX + 1):
        current = row(t)
        require(current["next_integer_gap"] > 0, "row next-integer gap")
        candidate = (current["record_cap"], -t)
        if candidate > maximum:
            maximum = candidate
        if current["record_cap"] > TARGET and first_excess < 0:
            first_excess = t
    return maximum[0], -maximum[1], first_excess


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    validate_contract(data)
    recurrence_checks = 0
    for a in range(1, 31):
        for r in range(3, 81):
            require(basis_floor6(a, r) == recurrence(a, r), "small recurrence")
            recurrence_checks += 1
    maximum, first_maximizer, first_excess = scan_rows()
    require((maximum, first_maximizer, first_excess) == (TARGET, 0, -1), "all-row result")

    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item["parameters"].__setitem__("rank_gap", RANK_GAP - 1),
        lambda item: item["parameters"].__setitem__("rank2_flat_ceiling", "a+2"),
        lambda item: item["parameters"].__setitem__("uniform_record_cap", TARGET + 1),
        lambda item: item["evidence"].__setitem__("checked_rows", T_MAX),
        lambda item: item["evidence"].__setitem__("first_excess", {"t": 1}),
    )
    caught = 0
    for mutation in mutations:
        altered = copy.deepcopy(data)
        mutation(altered)
        try:
            validate_contract(altered)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_CORANK3_UNIFORM_PROJECTIVE_BASIS_CAP_PASS "
        f"rows={T_MAX + 1} cap={maximum} recurrence_checks={recurrence_checks} "
        f"controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
