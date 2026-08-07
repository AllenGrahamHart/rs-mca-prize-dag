#!/usr/bin/env python3
"""Six-point system compiler for h=3 repeat-boundary loose triangles."""

from __future__ import annotations

from itertools import combinations

from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_loose_pair_membership_compiler import membership_pair_map
from f3_h3_repeat_loose_reciprocal_closure_compiler import reciprocal_image
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


def sorted_pair(a: int, b: int) -> tuple[int, int]:
    return (a, b) if a < b else (b, a)


def triangle_systems(p: int, n: int) -> dict[str, int]:
    pairs, _ = membership_pair_map(p, n)
    image = set(reciprocal_image(p, n))
    vertices = sorted({point for pair in pairs for point in pair})
    contained = 0
    loose = 0
    six_point_systems = 0
    for r, s, t in combinations(vertices, 3):
        pair_keys = (sorted_pair(r, s), sorted_pair(r, t), sorted_pair(s, t))
        if not all(pair in pairs for pair in pair_keys):
            continue

        closures = {
            (-(r + s)) % p,
            (-(r + t)) % p,
            (-(s + t)) % p,
        }
        owner_thirds = {pairs[pair][0] for pair in pair_keys}
        if closures != owner_thirds:
            raise AssertionError((p, n, (r, s, t), closures, owner_thirds))
        if not closures <= image:
            raise AssertionError((p, n, (r, s, t), closures, "closures not in S"))

        q = (r + s + t) % p
        if q == 0:
            contained += 1
            if closures != {r, s, t}:
                raise AssertionError((p, n, (r, s, t), closures, "contained mismatch"))
            continue

        loose += 1
        six_points = {r, s, t, *closures}
        if len(six_points) != 6:
            raise AssertionError((p, n, (r, s, t), closures, six_points))

        edge_rs = {r, s, (-(r + s)) % p}
        edge_rt = {r, t, (-(r + t)) % p}
        edge_st = {s, t, (-(s + t)) % p}
        if edge_rs & edge_rt != {r}:
            raise AssertionError((p, n, edge_rs, edge_rt))
        if edge_rs & edge_st != {s}:
            raise AssertionError((p, n, edge_rs, edge_st))
        if edge_rt & edge_st != {t}:
            raise AssertionError((p, n, edge_rt, edge_st))
        if edge_rs & edge_rt & edge_st:
            raise AssertionError((p, n, edge_rs, edge_rt, edge_st))
        six_point_systems += 1
    return {
        "active_pairs": len(pairs),
        "contained_triangles": contained,
        "loose_triangles": loose,
        "six_point_systems": six_point_systems,
    }


def main() -> None:
    print("h=3 repeat loose six-point system")
    print("loose system: r,s,t,-r-s,-r-t,-s-t in S with three lambda tests and r+s+t!=0")
    for p, n in WITNESS_ROWS:
        row = triangle_systems(p, n)
        print(
            f"p={p} n={n} active_pairs={row['active_pairs']} "
            f"contained_triangles={row['contained_triangles']} "
            f"loose_triangles={row['loose_triangles']} "
            f"six_point_systems={row['six_point_systems']}"
        )
    for p, n in CONTRAST_ROWS:
        row = triangle_systems(p, n)
        if row["six_point_systems"] == 0:
            raise AssertionError((p, n, "contrast row should have loose six-point systems"))
        print(
            f"contrast p={p} n={n} active_pairs={row['active_pairs']} "
            f"contained_triangles={row['contained_triangles']} "
            f"loose_triangles={row['loose_triangles']} "
            f"six_point_systems={row['six_point_systems']}"
        )
    print("H3-NO-LOOSE-TRIANGLE is absence of loose six-point systems")
    print("H3_REPEAT_LOOSE_SIX_POINT_SYSTEM_PASS")


if __name__ == "__main__":
    main()
