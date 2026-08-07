#!/usr/bin/env python3
"""Trivial count bound for the h=3 lambda=1 scale branch."""

from __future__ import annotations

from math import comb

from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_lambda_one_scale_compiler import lambda_one_scale_edges, primitive_cube_roots
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


def scale_orbit_bound(n: int) -> int:
    # A nonzero scale orbit has size three: x, omega*x, omega^2*x.
    # The condition 1+x in H injects representatives into H \ {1}.
    return max(0, (n - 1) // 3)


def scale_collision_pair_bound(n: int) -> int:
    return comb(scale_orbit_bound(n), 2)


def verify_row(p: int, n: int) -> dict[str, int]:
    scale_edges = lambda_one_scale_edges(p, n)
    actual_orbits = len(set(scale_edges.values()))
    orbit_bound = scale_orbit_bound(n) if primitive_cube_roots(p) else 0
    if actual_orbits > orbit_bound:
        raise AssertionError((p, n, actual_orbits, orbit_bound))
    actual_pairs = comb(actual_orbits, 2)
    pair_bound = scale_collision_pair_bound(n) if primitive_cube_roots(p) else 0
    if actual_pairs > pair_bound:
        raise AssertionError((p, n, actual_pairs, pair_bound))
    return {
        "has_cube_roots": int(bool(primitive_cube_roots(p))),
        "actual_orbits": actual_orbits,
        "orbit_bound": orbit_bound,
        "actual_pairs": actual_pairs,
        "pair_bound": pair_bound,
    }


def main() -> None:
    print("h=3 repeat same-lambda scale count compiler")
    print("lambda=1 scale orbits K_1 <= floor((n-1)/3)")
    print("scale same-lambda collision pairs <= binom(floor((n-1)/3),2)")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} has_cube_roots={row['has_cube_roots']} "
            f"actual_orbits={row['actual_orbits']} orbit_bound={row['orbit_bound']} "
            f"actual_pairs={row['actual_pairs']} pair_bound={row['pair_bound']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["actual_orbits"] == 0:
            raise AssertionError((p, n, "contrast row should exercise scale branch"))
        print(
            f"contrast p={p} n={n} has_cube_roots={row['has_cube_roots']} "
            f"actual_orbits={row['actual_orbits']} orbit_bound={row['orbit_bound']} "
            f"actual_pairs={row['actual_pairs']} pair_bound={row['pair_bound']}"
        )
    official_ns = [2**s for s in range(13, 42)]
    bad = [n for n in official_ns if scale_collision_pair_bound(n) >= n * n]
    if bad:
        raise AssertionError(("scale collision bound unexpectedly quadratic-large", bad[:5]))
    print(
        "scale collision-pair bound is below n^2 for official n=2^13..2^41; "
        f"first_pair_bound={scale_collision_pair_bound(2**13)}"
    )
    print("H3_REPEAT_SAME_LAMBDA_SCALE_COUNT_PASS")


if __name__ == "__main__":
    main()
