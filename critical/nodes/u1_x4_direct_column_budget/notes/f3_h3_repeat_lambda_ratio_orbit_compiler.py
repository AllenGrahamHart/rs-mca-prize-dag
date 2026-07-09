#!/usr/bin/env python3
"""S3 ratio-orbit compiler for h=3 repeat-boundary lambda fibers."""

from __future__ import annotations

from itertools import permutations

from f3_h3_repeat_edge_cubic_gcd_form import edge_cubic_data
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_lambda_ratio_membership_compiler import generic_coordinate_functions
from f3_h3_repeat_reciprocal_product_compiler import reciprocal_edge
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


def ratio_transforms(z: int, p: int) -> frozenset[int]:
    if z == 0 or (1 + z) % p == 0:
        raise AssertionError((p, "ratio transform pole", z))
    return frozenset(
        (
            z,
            pow(z, -1, p),
            (-(1 + z)) % p,
            (-pow((1 + z) % p, -1, p)) % p,
            (-(1 + z) * pow(z, -1, p)) % p,
            (-z * pow((1 + z) % p, -1, p)) % p,
        )
    )


def ordered_ratios(rec_edge: frozenset[int], p: int) -> frozenset[int]:
    return frozenset(s * pow(r, -1, p) % p for r, s in permutations(sorted(rec_edge), 2))


def canonical_ratio_orbit(z: int, p: int) -> tuple[int, ...]:
    return tuple(sorted(ratio_transforms(z, p)))


def verify_edge_orbit(p: int, edge: frozenset[int], lam: int) -> tuple[int, tuple[int, ...]]:
    rec_edge = reciprocal_edge(edge, p)
    ratios = ordered_ratios(rec_edge, p)
    first = next(iter(ratios))
    orbit = ratio_transforms(first, p)
    if orbit != ratios:
        raise AssertionError((p, edge, lam, ratios, orbit))

    if lam == 1:
        if len(ratios) != 2:
            raise AssertionError((p, edge, lam, ratios, "lambda=1 should have two ratios"))
        for z in ratios:
            if (z * z + z + 1) % p != 0:
                raise AssertionError((p, edge, lam, z, "lambda=1 non-cube ratio"))
    else:
        if len(ratios) != 6:
            raise AssertionError((p, edge, lam, ratios, "generic ratio orbit should have size six"))
        for z in ratios:
            coords = generic_coordinate_functions(lam, z, p)
            if coords is None or set(coords) != set(edge):
                raise AssertionError((p, edge, lam, z, coords))
    return len(ratios), canonical_ratio_orbit(first, p)


def verify_row(p: int, n: int) -> dict[str, int]:
    data = edge_cubic_data(p, n)
    lambda_orbits: set[tuple[int, tuple[int, ...]]] = set()
    generic_edges = 0
    lambda_one_edges = 0
    generic_orbit_size_total = 0
    lambda_one_orbit_size_total = 0
    for edge, (lam, _) in data.items():
        orbit_size, orbit = verify_edge_orbit(p, edge, lam)
        lambda_orbits.add((lam, orbit))
        if lam == 1:
            lambda_one_edges += 1
            lambda_one_orbit_size_total += orbit_size
        else:
            generic_edges += 1
            generic_orbit_size_total += orbit_size
    if len(lambda_orbits) != len(data):
        raise AssertionError((p, n, "distinct active edges should give distinct lambda-orbits"))
    return {
        "active_edges": len(data),
        "generic_edges": generic_edges,
        "lambda_one_edges": lambda_one_edges,
        "generic_orbit_size_total": generic_orbit_size_total,
        "lambda_one_orbit_size_total": lambda_one_orbit_size_total,
        "lambda_ratio_orbits": len(lambda_orbits),
    }


def main() -> None:
    print("h=3 repeat lambda-ratio orbit compiler")
    print("ratio orbit: z,1/z,-(1+z),-1/(1+z),-(1+z)/z,-z/(1+z)")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} active_edges={row['active_edges']} "
            f"generic_edges={row['generic_edges']} lambda_one_edges={row['lambda_one_edges']} "
            f"generic_orbit_size_total={row['generic_orbit_size_total']} "
            f"lambda_one_orbit_size_total={row['lambda_one_orbit_size_total']} "
            f"lambda_ratio_orbits={row['lambda_ratio_orbits']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["lambda_one_edges"] == 0:
            raise AssertionError((p, n, "contrast row should exercise lambda=1 branch"))
        print(
            f"contrast p={p} n={n} active_edges={row['active_edges']} "
            f"generic_edges={row['generic_edges']} lambda_one_edges={row['lambda_one_edges']} "
            f"generic_orbit_size_total={row['generic_orbit_size_total']} "
            f"lambda_one_orbit_size_total={row['lambda_one_orbit_size_total']} "
            f"lambda_ratio_orbits={row['lambda_ratio_orbits']}"
        )
    print("Fixed-lambda uniqueness is uniqueness of admissible S3 ratio orbits")
    print("H3_REPEAT_LAMBDA_RATIO_ORBIT_COMPILER_PASS")


if __name__ == "__main__":
    main()
