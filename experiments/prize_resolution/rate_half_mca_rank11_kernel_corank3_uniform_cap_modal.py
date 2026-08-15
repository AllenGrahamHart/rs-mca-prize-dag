#!/usr/bin/env python3
"""Audit the rank-four matroid floor and uniform corank-three cap on Modal."""

from __future__ import annotations

import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
RESULT = HERE / "rate_half_mca_rank11_kernel_corank3_uniform_cap_result.json"

app = modal.App("rate-half-mca-rank11-kernel-corank3-uniform-cap")
image = modal.Image.debian_slim()

R = 1048576
W = 67472
RANK_GAP = W + 2
T_MAX = R - 10
TARGET_CAP = 983902549


def sum_integers(lo: int, hi: int) -> int:
    if lo > hi:
        return 0
    return (lo + hi) * (hi - lo + 1) // 2


def square_prefix(value: int) -> int:
    return value * (value + 1) * (2 * value + 1) // 6


def sum_squares(lo: int, hi: int) -> int:
    if lo > hi:
        return 0
    return square_prefix(hi) - square_prefix(lo - 1)


def progression_sums(lo: int, hi: int, residue: int) -> tuple[int, int, int]:
    first = lo + ((residue - lo) % 4)
    if first > hi:
        return 0, 0, 0
    count = (hi - first) // 4 + 1
    last = first + 4 * (count - 1)
    index_sum = count * (count - 1) // 2
    index_square_sum = count * (count - 1) * (2 * count - 1) // 6
    value_sum = count * (first + last) // 2
    value_square_sum = (
        count * first * first
        + 8 * first * index_sum
        + 16 * index_square_sum
    )
    return count, value_sum, value_square_sum


def sum_h_weight(a: int, lo: int, hi: int) -> int:
    """Sum h_a(x)(x-2), splitting the floor by residues modulo four."""
    if lo > hi:
        return 0
    half = (a + 1) // 2
    constant_start = 4 * half - a
    floor_end = min(hi, constant_start - 1)
    total = 0
    if lo <= floor_end:
        numerator = 0
        for residue in range(4):
            count, value_sum, value_square_sum = progression_sums(
                lo, floor_end, residue
            )
            remainder = (a + residue) % 4
            shifted_a = a - remainder
            numerator += (
                value_square_sum
                + (shifted_a - 2) * value_sum
                - 2 * shifted_a * count
            )
        if numerator % 4:
            raise ArithmeticError("nonintegral residue-class floor sum")
        total += numerator // 4
    constant_lo = max(lo, constant_start)
    if constant_lo <= hi:
        count = hi - constant_lo + 1
        total += half * (sum_integers(constant_lo, hi) - 2 * count)
    return total


def sum_increment6(a: int, lo: int, hi: int) -> int:
    """Sum six times the contraction increments on an integer interval."""
    if lo > hi:
        return 0
    count = hi - lo + 1
    value_sum = sum_integers(lo, hi)
    value_square_sum = sum_squares(lo, hi)
    unfloored = (
        (a - 1) * (value_sum - 2 * count)
        + value_square_sum
        - 2 * value_sum
    )
    return 3 * (unfloored - sum_h_weight(a, lo, hi))


def h_value(a: int, r: int) -> int:
    return min((a + 1) // 2, (a + r) // 4)


def coloop6(a: int, r: int) -> int:
    return (a + r - 1) * (r - 1) * (r - 2)


def increment6(a: int, r: int) -> int:
    return 3 * (a + r - h_value(a, r) - 1) * (r - 2)


def reset_index(a: int, r: int) -> int:
    """Locate the minimum coloop-reset candidate by its one-sign difference."""
    half = (a + 1) // 2
    threshold = (a + 4) // 3
    if threshold > half:
        return r
    first_nondecreasing = max(5, 4 * threshold - a)
    if first_nondecreasing > r:
        return r
    return first_nondecreasing - 1


def basis_floor6(a: int, r: int = RANK_GAP) -> tuple[int, str, int]:
    base_candidate = 6 + sum_increment6(a, 4, r)
    reset = reset_index(a, r)
    reset_candidate = coloop6(a, reset) + sum_increment6(a, reset + 1, r)
    if base_candidate <= reset_candidate:
        return base_candidate, "base", reset
    return reset_candidate, "reset", reset


def recurrence_floor6(a: int, r: int) -> int:
    value = 6
    for current in range(4, r + 1):
        value = min(coloop6(a, current), value + increment6(a, current))
    return value


def row(t: int) -> dict[str, int | str]:
    a = t + 1
    floor6, branch, reset = basis_floor6(a)
    n = R + t + 3
    resource = n * (n - 1) * (n - 2) * (n - 3)
    ordered_basis_floor = 4 * floor6
    cap, remainder = divmod(resource, ordered_basis_floor)
    return {
        "t": t,
        "a": a,
        "resource": resource,
        "basis_floor_times_6": floor6,
        "ordered_basis_floor": ordered_basis_floor,
        "record_cap": cap,
        "division_remainder": remainder,
        "next_integer_gap": (TARGET_CAP + 1) * ordered_basis_floor - resource,
        "active_branch": branch,
        "reset_index": reset,
    }


@app.function(image=image, cpu=1.0, memory=512, timeout=60, max_containers=1)
def audit() -> dict[str, object]:
    recurrence_checks = 0
    residue_checks = 0
    for a in range(1, 81):
        for r in range(3, 121):
            closed, _, _ = basis_floor6(a, r)
            if closed != recurrence_floor6(a, r):
                raise ArithmeticError(f"closed recurrence mismatch at {(a, r)}")
            recurrence_checks += 1
        for lo in range(4, 32):
            hi = min(48, lo + 9)
            direct = sum(increment6(a, x) for x in range(lo, hi + 1))
            if direct != sum_increment6(a, lo, hi):
                raise ArithmeticError(f"residue sum mismatch at {(a, lo, hi)}")
            residue_checks += 1

    maximum = (-1, -1)
    minimum = (10**30, -1)
    first_excess: dict[str, int | str] | None = None
    branch_counts = {"base": 0, "reset": 0}
    for t in range(T_MAX + 1):
        current = row(t)
        cap = int(current["record_cap"])
        branch_counts[str(current["active_branch"])] += 1
        if (cap, -t) > maximum:
            maximum = (cap, -t)
        if (cap, t) < minimum:
            minimum = (cap, t)
        if cap > TARGET_CAP and first_excess is None:
            first_excess = current

    return {
        "schema": "rate-half-mca-rank11-kernel-corank3-uniform-cap-v1",
        "complete": True,
        "parameters": {
            "R": R,
            "w": W,
            "rank_gap": RANK_GAP,
            "t_minimum": 0,
            "t_maximum": T_MAX,
            "target_cap": TARGET_CAP,
        },
        "rows": {
            "complete": row(0),
            "adjacent": row(1),
            "first_nontrivial": row(2),
            "middle": row(T_MAX // 2),
            "official_endpoint": row(T_MAX),
        },
        "scan": {
            "checked_rows": T_MAX + 1,
            "maximum_record_cap": maximum[0],
            "first_maximizer": -maximum[1],
            "minimum_record_cap": minimum[0],
            "first_minimizer": minimum[1],
            "first_excess": first_excess,
            "branch_counts": branch_counts,
            "recurrence_checks": recurrence_checks,
            "residue_checks": residue_checks,
        },
    }


@app.local_entrypoint()
def main() -> None:
    RESULT.write_text(json.dumps({"complete": False}, indent=2) + "\n")
    try:
        payload = audit.remote()
    except BaseException as error:
        RESULT.write_text(
            json.dumps(
                {"complete": False, "error": f"{type(error).__name__}: {error}"},
                indent=2,
            )
            + "\n"
        )
        raise
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))
    print(f"RESULT {RESULT}")


if __name__ == "__main__":
    main()
