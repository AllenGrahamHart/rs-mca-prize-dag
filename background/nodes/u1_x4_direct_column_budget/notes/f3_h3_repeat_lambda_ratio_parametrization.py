#!/usr/bin/env python3
"""Ratio parametrization for h=3 repeat-boundary lambda fibers."""

from __future__ import annotations

from itertools import permutations

from f3_h3_repeat_edge_cubic_gcd_form import edge_cubic_data
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_reciprocal_product_compiler import reciprocal_edge
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


def ratio_root(lam: int, z: int, p: int) -> int | None:
    if z == 0 or z == 1:
        return None
    a = (lam - 1) % p
    numerator = (1 + z + z * z) % p
    if a == 0:
        return None
    denom = a * z * ((1 + z) % p) % p
    if denom == 0:
        return None
    return numerator * pow(denom, -1, p) % p


def ratio_reciprocal_edge(lam: int, z: int, p: int) -> frozenset[int] | None:
    if z == 0 or z == 1:
        return None
    if lam == 1:
        if (z * z + z + 1) % p != 0:
            return None
        # The scale is not determined when lambda=1; callers must supply a root.
        return None
    r = ratio_root(lam, z, p)
    if r is None or r == 0:
        return None
    return frozenset((r, z * r % p, (-(1 + z) * r) % p))


def verify_ordered_pair(lam: int, r: int, s: int, rec_edge: frozenset[int], p: int) -> None:
    z = s * pow(r, -1, p) % p
    if lam == 1:
        if (z * z + z + 1) % p != 0:
            raise AssertionError((p, lam, rec_edge, r, s, z, "lambda=1 ratio"))
        reconstructed = frozenset((r, z * r % p, z * z * r % p))
    else:
        reconstructed = ratio_reciprocal_edge(lam, z, p)
        if reconstructed is None:
            raise AssertionError((p, lam, rec_edge, r, s, z, "generic ratio undefined"))
    if reconstructed != rec_edge:
        raise AssertionError((p, lam, rec_edge, r, s, z, reconstructed))


def verify_row(p: int, n: int) -> dict[str, int]:
    data = edge_cubic_data(p, n)
    oriented_ratio_checks = 0
    lambda_one_edges = 0
    unique_ratio_values: set[tuple[int, int]] = set()
    for edge, (lam, _) in data.items():
        rec_edge = reciprocal_edge(edge, p)
        if lam == 1:
            lambda_one_edges += 1
        for r, s in permutations(sorted(rec_edge), 2):
            verify_ordered_pair(lam, r, s, rec_edge, p)
            z = s * pow(r, -1, p) % p
            unique_ratio_values.add((lam, z))
            oriented_ratio_checks += 1
    return {
        "active_edges": len(data),
        "lambda_one_edges": lambda_one_edges,
        "oriented_ratio_checks": oriented_ratio_checks,
        "unique_lambda_ratios": len(unique_ratio_values),
    }


def main() -> None:
    print("h=3 repeat lambda-ratio parametrization")
    print("lambda!=1: r=(1+z+z^2)/((lambda-1)z(1+z))")
    print("lambda=1: z^2+z+1=0")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} active_edges={row['active_edges']} "
            f"lambda_one_edges={row['lambda_one_edges']} "
            f"oriented_ratio_checks={row['oriented_ratio_checks']} "
            f"unique_lambda_ratios={row['unique_lambda_ratios']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["lambda_one_edges"] == 0:
            raise AssertionError((p, n, "contrast row should exercise lambda=1 branch"))
        print(
            f"contrast p={p} n={n} active_edges={row['active_edges']} "
            f"lambda_one_edges={row['lambda_one_edges']} "
            f"oriented_ratio_checks={row['oriented_ratio_checks']} "
            f"unique_lambda_ratios={row['unique_lambda_ratios']}"
        )
    print("Three-point lambda fibers are parametrized by ordered root ratios")
    print("H3_REPEAT_LAMBDA_RATIO_PARAMETRIZATION_PASS")


if __name__ == "__main__":
    main()
