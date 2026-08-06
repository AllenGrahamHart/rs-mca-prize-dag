#!/usr/bin/env python3
"""Normalized ratio system for h=3 repeat-boundary loose triangles."""

from __future__ import annotations

from itertools import combinations

from f3_h3_pair_count_from_charts_compiler import root_table
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_loose_pair_membership_compiler import membership_pair_map
from f3_h3_repeat_loose_reciprocal_closure_compiler import coordinate_from_reciprocal
from f3_h3_repeat_loose_six_point_system import sorted_pair
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


def inv(x: int, p: int) -> int:
    if x % p == 0:
        raise AssertionError((p, "zero denominator"))
    return pow(x % p, -1, p)


def normalized_reciprocal_multipliers(a: int, b: int, p: int) -> tuple[int, ...]:
    return (
        1,
        a % p,
        b % p,
        (-(1 + a)) % p,
        (-(1 + b)) % p,
        (-(a + b)) % p,
    )


def normalized_coordinate_values(x: int, a: int, b: int, p: int) -> tuple[int, ...]:
    values = []
    for q in normalized_reciprocal_multipliers(a, b, p):
        values.append((1 + x * inv(q, p)) % p)
    return tuple(values)


def normalized_lambda_values(x: int, a: int, b: int, p: int) -> tuple[int, int, int]:
    return (
        (1 + x * (1 + inv(a, p) - inv((1 + a) % p, p))) % p,
        (1 + x * (1 + inv(b, p) - inv((1 + b) % p, p))) % p,
        (1 + x * (inv(a, p) + inv(b, p) - inv((a + b) % p, p))) % p,
    )


def normalized_system_from_core(r: int, s: int, t: int, p: int) -> tuple[int, int, int]:
    x = inv(r, p)
    a = s * x % p
    b = t * x % p
    return x, a, b


def verify_normalized_system(p: int, hset: set[int], core: tuple[int, int, int]) -> None:
    r, s, t = core
    x, a, b = normalized_system_from_core(r, s, t, p)
    q_values = normalized_reciprocal_multipliers(a, b, p)
    if len(set(q_values)) != 6:
        raise AssertionError((p, core, x, a, b, q_values, "multipliers not distinct"))
    if (1 + a + b) % p == 0:
        raise AssertionError((p, core, x, a, b, "contained, not loose"))

    rec_points = {r * q % p for q in q_values}
    expected = {r, s, t, (-(r + s)) % p, (-(r + t)) % p, (-(s + t)) % p}
    if rec_points != expected:
        raise AssertionError((p, core, x, a, b, rec_points, expected))

    coords = normalized_coordinate_values(x, a, b, p)
    lambdas = normalized_lambda_values(x, a, b, p)
    if any(value not in hset for value in coords):
        raise AssertionError((p, core, x, a, b, coords, "coordinate not in H"))
    if any(value not in hset for value in lambdas):
        raise AssertionError((p, core, x, a, b, lambdas, "lambda not in H"))


def verify_row(p: int, n: int) -> dict[str, int]:
    hset = set(root_table(p, n))
    pairs, _ = membership_pair_map(p, n)
    vertices = sorted({point for pair in pairs for point in pair})
    loose = 0
    normalized_orbits: set[tuple[int, int, int]] = set()
    ordered_normalizations = 0
    for r, s, t in combinations(vertices, 3):
        pair_keys = (sorted_pair(r, s), sorted_pair(r, t), sorted_pair(s, t))
        if not all(pair in pairs for pair in pair_keys):
            continue
        if (r + s + t) % p == 0:
            continue
        loose += 1
        for core in ((r, s, t), (r, t, s), (s, r, t), (s, t, r), (t, r, s), (t, s, r)):
            verify_normalized_system(p, hset, core)
            normalized_orbits.add(normalized_system_from_core(*core, p))
            ordered_normalizations += 1
    if ordered_normalizations != 6 * loose:
        raise AssertionError((p, n, ordered_normalizations, loose))
    return {
        "active_pairs": len(pairs),
        "loose_systems": loose,
        "ordered_normalizations": ordered_normalizations,
        "normalized_orbits": len(normalized_orbits),
    }


def main() -> None:
    print("h=3 repeat loose normalized system")
    print("normalize by s=a*r, t=b*r, X=1/r")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} active_pairs={row['active_pairs']} "
            f"loose_systems={row['loose_systems']} "
            f"ordered_normalizations={row['ordered_normalizations']} "
            f"normalized_orbits={row['normalized_orbits']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["loose_systems"] == 0:
            raise AssertionError((p, n, "contrast row should have loose normalized systems"))
        print(
            f"contrast p={p} n={n} active_pairs={row['active_pairs']} "
            f"loose_systems={row['loose_systems']} "
            f"ordered_normalizations={row['ordered_normalizations']} "
            f"normalized_orbits={row['normalized_orbits']}"
        )
    print("H3-NO-LOOSE-TRIANGLE is absence of normalized loose ratio systems")
    print("H3_REPEAT_LOOSE_NORMALIZED_SYSTEM_PASS")


if __name__ == "__main__":
    main()
