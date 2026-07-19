#!/usr/bin/env python3
"""Affine-slope compiler for normalized h=3 loose systems."""

from __future__ import annotations

from itertools import combinations

from f3_h3_pair_count_from_charts_compiler import root_table
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_loose_normalized_system import (
    inv,
    normalized_coordinate_values,
    normalized_lambda_values,
    normalized_system_from_core,
)
from f3_h3_repeat_loose_pair_membership_compiler import membership_pair_map
from f3_h3_repeat_loose_six_point_system import sorted_pair
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


def coordinate_slopes(a: int, b: int, p: int) -> tuple[int, ...]:
    return (
        1,
        inv(a, p),
        inv(b, p),
        -inv((1 + a) % p, p) % p,
        -inv((1 + b) % p, p) % p,
        -inv((a + b) % p, p) % p,
    )


def lambda_slopes(a: int, b: int, p: int) -> tuple[int, int, int]:
    return (
        (1 + inv(a, p) - inv((1 + a) % p, p)) % p,
        (1 + inv(b, p) - inv((1 + b) % p, p)) % p,
        (inv(a, p) + inv(b, p) - inv((a + b) % p, p)) % p,
    )


def affine_values(x: int, slopes: tuple[int, ...], p: int) -> tuple[int, ...]:
    return tuple((1 + x * slope) % p for slope in slopes)


def verify_affine_system(p: int, hset: set[int], core: tuple[int, int, int]) -> None:
    x, a, b = normalized_system_from_core(*core, p)
    c_slopes = coordinate_slopes(a, b, p)
    l_slopes = lambda_slopes(a, b, p)
    if affine_values(x, c_slopes, p) != normalized_coordinate_values(x, a, b, p):
        raise AssertionError((p, core, x, a, b, c_slopes))
    if affine_values(x, l_slopes, p) != normalized_lambda_values(x, a, b, p):
        raise AssertionError((p, core, x, a, b, l_slopes))
    all_slopes = c_slopes + l_slopes
    if any((1 + x * slope) % p not in hset for slope in all_slopes):
        raise AssertionError((p, core, x, a, b, all_slopes, "affine value not in H"))
    if len(set(c_slopes)) != 6:
        raise AssertionError((p, core, x, a, b, c_slopes, "coordinate slopes collide"))


def verify_row(p: int, n: int) -> dict[str, int]:
    hset = set(root_table(p, n))
    pairs, _ = membership_pair_map(p, n)
    vertices = sorted({point for pair in pairs for point in pair})
    loose = 0
    ordered_normalizations = 0
    repeated_full_slope_sets = 0
    slope_sets: set[tuple[int, ...]] = set()
    for r, s, t in combinations(vertices, 3):
        pair_keys = (sorted_pair(r, s), sorted_pair(r, t), sorted_pair(s, t))
        if not all(pair in pairs for pair in pair_keys):
            continue
        if (r + s + t) % p == 0:
            continue
        loose += 1
        for core in ((r, s, t), (r, t, s), (s, r, t), (s, t, r), (t, r, s), (t, s, r)):
            verify_affine_system(p, hset, core)
            x, a, b = normalized_system_from_core(*core, p)
            slopes = coordinate_slopes(a, b, p) + lambda_slopes(a, b, p)
            key = tuple(sorted(slopes))
            if key in slope_sets:
                repeated_full_slope_sets += 1
            slope_sets.add(key)
            ordered_normalizations += 1
    return {
        "active_pairs": len(pairs),
        "loose_systems": loose,
        "ordered_normalizations": ordered_normalizations,
        "affine_slope_sets": len(slope_sets),
        "repeated_full_slope_sets": repeated_full_slope_sets,
    }


def main() -> None:
    print("h=3 repeat loose affine-slope compiler")
    print("normalized loose system = nine affine values 1+c_i X in H")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} active_pairs={row['active_pairs']} "
            f"loose_systems={row['loose_systems']} "
            f"ordered_normalizations={row['ordered_normalizations']} "
            f"affine_slope_sets={row['affine_slope_sets']} "
            f"repeated_full_slope_sets={row['repeated_full_slope_sets']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["loose_systems"] == 0:
            raise AssertionError((p, n, "contrast row should have loose affine systems"))
        print(
            f"contrast p={p} n={n} active_pairs={row['active_pairs']} "
            f"loose_systems={row['loose_systems']} "
            f"ordered_normalizations={row['ordered_normalizations']} "
            f"affine_slope_sets={row['affine_slope_sets']} "
            f"repeated_full_slope_sets={row['repeated_full_slope_sets']}"
        )
    print("H3-NO-LOOSE-TRIANGLE is absence of nine-slope affine H-lines")
    print("H3_REPEAT_LOOSE_AFFINE_SLOPE_COMPILER_PASS")


if __name__ == "__main__":
    main()
