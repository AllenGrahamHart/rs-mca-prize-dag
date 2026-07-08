#!/usr/bin/env python3
"""Non-diagonal h=3 bridge-budget lift for low official rows."""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt


C_RED = 13
H3_ACT_C = 16
B_MAX = 50_000


@dataclass(frozen=True)
class Row:
    s: int
    old_z: int
    z: int
    bound: int
    a: int
    b: int
    d: int
    next_bound: int
    next_a: int
    next_b: int
    next_d: int


EXPECTED_ROWS = (
    Row(13, 11, 16, 123_137, 195, 63, 396, 132_401, 214, 62, 385),
    Row(14, 14, 21, 259_244, 296, 83, 653, 274_061, 303, 84, 655),
    Row(15, 18, 26, 508_053, 527, 98, 976, 531_877, 477, 105, 1_038),
    Row(16, 23, 33, 1_026_191, 824, 125, 1_568, 1_063_869, 809, 128, 1_596),
    Row(17, 29, 42, 2_079_745, 1_251, 162, 2_557, 2_139_141, 1_265, 163, 2_561),
    Row(18, 36, 53, 4_170_160, 1_974, 205, 4_078, 4_264_529, 2_011, 205, 4_063),
    Row(19, 46, 67, 8_378_221, 3_179, 257, 6_440, 8_528_431, 3_226, 257, 6_421),
    Row(20, 58, 84, 16_665_312, 5_145, 320, 10_116, 16_903_661, 5_110, 323, 10_187),
    Row(21, 73, 106, 33_406_481, 8_032, 407, 16_210, 33_785_625, 8_029, 409, 16_259),
    Row(22, 92, 134, 67_102_386, 12_889, 511, 25_630, 67_704_006, 12_935, 512, 25_642),
    Row(23, 116, 168, 133_444_877, 20_294, 645, 40_807, 134_399_623, 20_477, 644, 40_695),
)


def witness_bound(n: int, z: int, a: int, b: int, d: int) -> tuple[int, int, int, int]:
    conditions = C_RED * d * (a + d) * z
    coeffs = a * b**3
    degree = (a - 1) + 6 * n * (b - 1)
    image_cap = z * (degree + 1)
    if not (conditions < coeffs and conditions < image_cap):
        raise AssertionError((n, z, a, b, d, conditions, coeffs, image_cap))
    bound = (z * degree + d - 1) // d
    return bound, conditions, coeffs, image_cap


def minimal_a(n: int, z: int, b: int, d: int) -> int | None:
    del n
    denominator = b**3 - C_RED * d * z
    if denominator <= 0:
        return None
    return (C_RED * d * d * z) // denominator + 1


def feasible_witness(n: int, z: int, b: int, d: int) -> tuple[int, int, int, int, int, int, int] | None:
    a = minimal_a(n, z, b, d)
    if a is None:
        return None
    conditions = C_RED * d * (a + d) * z
    coeffs = a * b**3
    degree = (a - 1) + 6 * n * (b - 1)
    image_cap = z * (degree + 1)
    if conditions < coeffs and conditions < image_cap:
        bound = (z * degree + d - 1) // d
        return bound, a, b, d, degree, conditions, image_cap
    return None


def best_nondiagonal_bound(n: int, z: int) -> tuple[int, int, int, int]:
    best: tuple[int, int, int, int] | None = None
    for b in range(2, B_MAX + 1):
        coeff_cap = (b**3 - 1) // (C_RED * z)
        image_cap = isqrt(max(0, (6 * n * (b - 1) - 1) // C_RED))
        hi = min(coeff_cap, image_cap)
        if hi < 1:
            continue

        lo = 0
        upper = hi + 1
        while lo + 1 < upper:
            mid = (lo + upper) // 2
            if feasible_witness(n, z, b, mid) is not None:
                lo = mid
            else:
                upper = mid

        for d in range(max(1, lo - 4), min(hi, lo + 4) + 1):
            witness = feasible_witness(n, z, b, d)
            if witness is None:
                continue
            bound, a, got_b, got_d, *_ = witness
            row = (bound, a, got_b, got_d)
            if best is None or row < best:
                best = row

    if best is None:
        raise AssertionError(("no admissible non-diagonal box", n, z))
    return best


def main() -> None:
    print("h=3 non-diagonal low-row bridge-budget lift")
    print(f"C_red={C_RED} H3_ACT_C={H3_ACT_C} B_max={B_MAX}")
    print(" s      n       old_Z   new_Z       bound          16n     next_bound    A     B      D")
    for row in EXPECTED_ROWS:
        n = 2**row.s
        target = H3_ACT_C * n
        got_bound, *_ = witness_bound(n, row.z, row.a, row.b, row.d)
        if got_bound != row.bound:
            raise AssertionError((row.s, got_bound, row.bound))
        if got_bound > target:
            raise AssertionError((row.s, "passing witness exceeds target", got_bound, target))

        next_bound, next_a, next_b, next_d = best_nondiagonal_bound(n, row.z + 1)
        got_next = (next_bound, next_a, next_b, next_d)
        expected_next = (row.next_bound, row.next_a, row.next_b, row.next_d)
        if got_next != expected_next:
            raise AssertionError((row.s, got_next, expected_next))
        if next_bound <= target:
            raise AssertionError((row.s, "next budget passes", next_bound, target))

        print(
            f"{row.s:2d} {n:8d} {row.old_z:10d} {row.z:7d}"
            f" {row.bound:11d} {target:12d} {row.next_bound:14d}"
            f" {row.a:5d} {row.b:5d} {row.d:6d}"
        )

    print("maximality check: new_Z passes and new_Z+1 fails for s=13..23")
    print("conditional conclusion: non-diagonal boxes enlarge the low-row H3-BRIDGE budgets")
    print("H3_NONDIAGONAL_LOWROW_BUDGET_PASS")


if __name__ == "__main__":
    main()
