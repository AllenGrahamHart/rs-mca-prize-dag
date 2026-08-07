#!/usr/bin/env python3
"""Slope-multiplicity compiler for normalized h=3 loose systems."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_loose_affine_slope_compiler import coordinate_slopes, lambda_slopes
from f3_h3_repeat_loose_normalized_system import normalized_system_from_core
from f3_h3_repeat_loose_pair_membership_compiler import membership_pair_map
from f3_h3_repeat_loose_six_point_system import sorted_pair
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


def slope_multiplicity(a: int, b: int, p: int) -> dict[str, int | tuple[int, ...]]:
    coords = coordinate_slopes(a, b, p)
    lambdas = lambda_slopes(a, b, p)
    if len(set(coords)) != 6:
        raise AssertionError((p, a, b, coords, "coordinate slopes should be distinct"))
    if len(set(lambdas)) != 3:
        raise AssertionError((p, a, b, lambdas, "lambda slopes should be distinct"))
    all_slopes = coords + lambdas
    multiplicities = sorted(Counter(all_slopes).values(), reverse=True)
    return {
        "coordinate_distinct": len(set(coords)),
        "lambda_distinct": len(set(lambdas)),
        "total_distinct": len(set(all_slopes)),
        "max_multiplicity": max(multiplicities),
        "multiplicities": tuple(multiplicities),
    }


def verify_row(p: int, n: int) -> dict[str, int | str]:
    pairs, _ = membership_pair_map(p, n)
    vertices = sorted({point for pair in pairs for point in pair})
    loose_systems = 0
    ordered_normalizations = 0
    min_total = 9
    max_total = 0
    max_multiplicity = 0
    patterns: Counter[tuple[int, ...]] = Counter()
    for r, s, t in combinations(vertices, 3):
        pair_keys = (sorted_pair(r, s), sorted_pair(r, t), sorted_pair(s, t))
        if not all(pair in pairs for pair in pair_keys):
            continue
        if (r + s + t) % p == 0:
            continue
        loose_systems += 1
        for core in ((r, s, t), (r, t, s), (s, r, t), (s, t, r), (t, r, s), (t, s, r)):
            _, a, b = normalized_system_from_core(*core, p)
            row = slope_multiplicity(a, b, p)
            total = int(row["total_distinct"])
            min_total = min(min_total, total)
            max_total = max(max_total, total)
            max_multiplicity = max(max_multiplicity, int(row["max_multiplicity"]))
            patterns[row["multiplicities"]] += 1  # type: ignore[index]
            ordered_normalizations += 1
    if loose_systems == 0:
        min_total = 0
    pattern_text = ";".join(f"{pattern}:{count}" for pattern, count in sorted(patterns.items()))
    return {
        "loose_systems": loose_systems,
        "ordered_normalizations": ordered_normalizations,
        "min_total_distinct": min_total,
        "max_total_distinct": max_total,
        "max_multiplicity": max_multiplicity,
        "patterns": pattern_text or "-",
    }


def main() -> None:
    print("h=3 repeat loose slope-multiplicity compiler")
    print("six coordinate slopes are distinct; lambda slopes may collide")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} loose_systems={row['loose_systems']} "
            f"ordered_normalizations={row['ordered_normalizations']} "
            f"distinct_range={row['min_total_distinct']}..{row['max_total_distinct']} "
            f"max_multiplicity={row['max_multiplicity']} patterns={row['patterns']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["loose_systems"] == 0:
            raise AssertionError((p, n, "contrast row should have loose slope patterns"))
        print(
            f"contrast p={p} n={n} loose_systems={row['loose_systems']} "
            f"ordered_normalizations={row['ordered_normalizations']} "
            f"distinct_range={row['min_total_distinct']}..{row['max_total_distinct']} "
            f"max_multiplicity={row['max_multiplicity']} patterns={row['patterns']}"
        )
    print("H3_REPEAT_LOOSE_SLOPE_MULTIPLICITY_PASS")


if __name__ == "__main__":
    main()
