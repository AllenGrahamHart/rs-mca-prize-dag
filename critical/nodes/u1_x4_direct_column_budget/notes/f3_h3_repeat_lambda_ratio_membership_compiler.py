#!/usr/bin/env python3
"""Ratio membership functions for h=3 repeat-boundary lambda fibers."""

from __future__ import annotations

from itertools import permutations

from f3_h3_pair_count_from_charts_compiler import root_table
from f3_h3_repeat_edge_cubic_gcd_form import edge_cubic_data
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_reciprocal_product_compiler import reciprocal_edge
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


def generic_coordinate_functions(lam: int, z: int, p: int) -> tuple[int, int, int] | None:
    if lam == 1 or z in (0, 1) or (1 + z) % p == 0:
        return None
    a = (lam - 1) % p
    n = (1 + z + z * z) % p
    if n == 0:
        return None
    inv_n = pow(n, -1, p)
    u = (1 + a * z * ((1 + z) % p) * inv_n) % p
    v = (1 + a * ((1 + z) % p) * inv_n) % p
    w = (1 - a * z * inv_n) % p
    return (u, v, w)


def verify_generic_pair(
    p: int, hset: set[int], edge: frozenset[int], lam: int, r: int, s: int
) -> None:
    z = s * pow(r, -1, p) % p
    coords = generic_coordinate_functions(lam, z, p)
    if coords is None:
        raise AssertionError((p, edge, lam, r, s, z, "generic functions undefined"))
    if set(coords) != set(edge):
        raise AssertionError((p, edge, lam, r, s, z, coords))
    if any(coord not in hset for coord in coords):
        raise AssertionError((p, edge, lam, z, coords, "coordinate not in H"))


def verify_lambda_one_pair(p: int, hset: set[int], edge: frozenset[int], r: int, s: int) -> None:
    z = s * pow(r, -1, p) % p
    if (z * z + z + 1) % p != 0:
        raise AssertionError((p, edge, r, s, z, "lambda=1 ratio"))
    rec_edge = frozenset((r, z * r % p, z * z * r % p))
    coords = {(1 + pow(x, -1, p)) % p for x in rec_edge}
    if coords != set(edge):
        raise AssertionError((p, edge, r, s, z, coords))
    if any(coord not in hset for coord in coords):
        raise AssertionError((p, edge, z, coords, "coordinate not in H"))


def verify_row(p: int, n: int) -> dict[str, int]:
    hset = set(root_table(p, n))
    data = edge_cubic_data(p, n)
    generic_checks = 0
    lambda_one_checks = 0
    for edge, (lam, _) in data.items():
        rec_edge = reciprocal_edge(edge, p)
        for r, s in permutations(sorted(rec_edge), 2):
            if lam == 1:
                verify_lambda_one_pair(p, hset, edge, r, s)
                lambda_one_checks += 1
            else:
                verify_generic_pair(p, hset, edge, lam, r, s)
                generic_checks += 1
    return {
        "active_edges": len(data),
        "generic_checks": generic_checks,
        "lambda_one_checks": lambda_one_checks,
    }


def main() -> None:
    print("h=3 repeat lambda-ratio membership compiler")
    print("generic coordinates are rational functions of lambda and z")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} active_edges={row['active_edges']} "
            f"generic_checks={row['generic_checks']} "
            f"lambda_one_checks={row['lambda_one_checks']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["lambda_one_checks"] == 0:
            raise AssertionError((p, n, "contrast row should exercise lambda=1 branch"))
        print(
            f"contrast p={p} n={n} active_edges={row['active_edges']} "
            f"generic_checks={row['generic_checks']} "
            f"lambda_one_checks={row['lambda_one_checks']}"
        )
    print("H3_REPEAT_LAMBDA_RATIO_MEMBERSHIP_COMPILER_PASS")


if __name__ == "__main__":
    main()
