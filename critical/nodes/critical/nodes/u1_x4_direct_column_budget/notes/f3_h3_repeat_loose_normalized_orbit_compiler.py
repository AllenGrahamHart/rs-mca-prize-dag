#!/usr/bin/env python3
"""S3 orbit compiler for normalized h=3 loose systems."""

from __future__ import annotations

from itertools import combinations

from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_loose_affine_slope_compiler import coordinate_slopes, lambda_slopes
from f3_h3_repeat_loose_normalized_system import inv, normalized_system_from_core
from f3_h3_repeat_loose_pair_membership_compiler import membership_pair_map
from f3_h3_repeat_loose_six_point_system import sorted_pair
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


def ratio_orbit(a: int, b: int, p: int) -> frozenset[tuple[int, int]]:
    if a == 0 or b == 0:
        raise AssertionError((p, a, b, "zero ratio"))
    return frozenset(
        (
            (a % p, b % p),
            (b % p, a % p),
            (inv(a, p), b * inv(a, p) % p),
            (b * inv(a, p) % p, inv(a, p)),
            (inv(b, p), a * inv(b, p) % p),
            (a * inv(b, p) % p, inv(b, p)),
        )
    )


def canonical_ratio_orbit(a: int, b: int, p: int) -> tuple[tuple[int, int], ...]:
    return tuple(sorted(ratio_orbit(a, b, p)))


def slope_set(a: int, b: int, p: int) -> tuple[int, ...]:
    return tuple(sorted(coordinate_slopes(a, b, p) + lambda_slopes(a, b, p)))


def verify_core_orbit(
    p: int, core: tuple[int, int, int]
) -> tuple[tuple[tuple[int, int], ...], frozenset[tuple[int, ...]]]:
    r, s, t = core
    _, a, b = normalized_system_from_core(r, s, t, p)
    orbit = ratio_orbit(a, b, p)
    ordered_pairs: set[tuple[int, int]] = set()
    slope_sets: set[tuple[int, ...]] = set()
    for permuted in ((r, s, t), (r, t, s), (s, r, t), (s, t, r), (t, r, s), (t, s, r)):
        _, aa, bb = normalized_system_from_core(*permuted, p)
        ordered_pairs.add((aa, bb))
        slope_sets.add(slope_set(aa, bb, p))
    if ordered_pairs != orbit:
        raise AssertionError((p, core, ordered_pairs, orbit))
    if len(slope_sets) not in (1, 2, 3, 6):
        raise AssertionError((p, core, slope_sets, orbit, "unexpected slope-set orbit size"))
    return canonical_ratio_orbit(a, b, p), frozenset(slope_sets)


def verify_row(p: int, n: int) -> dict[str, int]:
    pairs, _ = membership_pair_map(p, n)
    vertices = sorted({point for pair in pairs for point in pair})
    loose_systems = 0
    normalized_orbits: set[tuple[tuple[int, int], ...]] = set()
    slope_sets: set[tuple[int, ...]] = set()
    for r, s, t in combinations(vertices, 3):
        pair_keys = (sorted_pair(r, s), sorted_pair(r, t), sorted_pair(s, t))
        if not all(pair in pairs for pair in pair_keys):
            continue
        if (r + s + t) % p == 0:
            continue
        loose_systems += 1
        orbit, slopes = verify_core_orbit(p, (r, s, t))
        normalized_orbits.add(orbit)
        slope_sets.update(slopes)
    return {
        "active_pairs": len(pairs),
        "loose_systems": loose_systems,
        "normalized_orbits": len(normalized_orbits),
        "representative_slope_sets": len(slope_sets),
    }


def main() -> None:
    print("h=3 repeat loose normalized orbit compiler")
    print("S3 orbit: (a,b),(b,a),(1/a,b/a),(b/a,1/a),(1/b,a/b),(a/b,1/b)")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} active_pairs={row['active_pairs']} "
            f"loose_systems={row['loose_systems']} "
            f"normalized_orbits={row['normalized_orbits']} "
            f"representative_slope_sets={row['representative_slope_sets']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["normalized_orbits"] == 0:
            raise AssertionError((p, n, "contrast row should have normalized loose orbits"))
        print(
            f"contrast p={p} n={n} active_pairs={row['active_pairs']} "
            f"loose_systems={row['loose_systems']} "
            f"normalized_orbits={row['normalized_orbits']} "
            f"representative_slope_sets={row['representative_slope_sets']}"
        )
    print("H3-NO-LOOSE-TRIANGLE is absence of admissible normalized S3 orbits")
    print("H3_REPEAT_LOOSE_NORMALIZED_ORBIT_COMPILER_PASS")


if __name__ == "__main__":
    main()
