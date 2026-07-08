#!/usr/bin/env python3
"""Ratio-form compiler for the h=3 repeat-boundary slope-hit target."""

from __future__ import annotations

from itertools import combinations, permutations

from f3_h3_repeat_edge_cubic_gcd_form import edge_cubic_data
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_lambda_one_scale_compiler import primitive_cube_roots
from f3_h3_repeat_lambda_ratio_membership_compiler import generic_coordinate_functions
from f3_h3_repeat_quadratic_rho_compiler import rho_value
from f3_h3_repeat_reciprocal_product_compiler import (
    reciprocal_edge,
    reciprocal_product,
    reciprocal_slope_value,
    rho_from_reciprocal_products,
)
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


def generic_inv_rprod(lam: int, z: int, p: int) -> int | None:
    if lam == 1 or z in (0, 1) or (1 + z) % p == 0:
        return None
    a = (lam - 1) % p
    n = (1 + z + z * z) % p
    if n == 0:
        return None
    numerator = (-pow(a, 3, p) * z * z * ((1 + z) % p) * ((1 + z) % p)) % p
    return numerator * pow(pow(n, 3, p), -1, p) % p


def generic_slope_values(lam: int, z: int, p: int) -> frozenset[int] | None:
    coords = generic_coordinate_functions(lam, z, p)
    if coords is None:
        return None
    return frozenset(t * ((2 - t) % p) % p for t in coords)


def lambda_one_inv_rprod_from_scale(x: int, p: int) -> int:
    return pow(x, 3, p)


def lambda_one_slope_values_from_scale(x: int, p: int) -> frozenset[int]:
    omegas = primitive_cube_roots(p)
    if not omegas:
        raise AssertionError((p, "lambda=1 branch needs primitive cube roots"))
    omega, omega2 = omegas
    return frozenset(
        (1 - y * y) % p for y in (x % p, omega * x % p, omega2 * x % p)
    )


def edge_ratio_data(edge: frozenset[int], lam: int, p: int) -> dict[str, int | frozenset[int]]:
    rec_edge = reciprocal_edge(edge, p)
    actual_inv_rprod = pow(reciprocal_product(rec_edge, p), -1, p)
    actual_slopes = frozenset(reciprocal_slope_value(r, p) for r in rec_edge)

    if lam == 1:
        x = pow(next(iter(rec_edge)), -1, p)
        inv_rprod = lambda_one_inv_rprod_from_scale(x, p)
        slopes = lambda_one_slope_values_from_scale(x, p)
        if inv_rprod != actual_inv_rprod or slopes != actual_slopes:
            raise AssertionError((p, edge, lam, inv_rprod, actual_inv_rprod, slopes, actual_slopes))
        return {
            "branch": 1,
            "inv_rprod": inv_rprod,
            "slope_values": slopes,
        }

    ratio_inv_values: set[int] = set()
    ratio_slope_sets: set[frozenset[int]] = set()
    for r, s in permutations(sorted(rec_edge), 2):
        z = s * pow(r, -1, p) % p
        inv_rprod = generic_inv_rprod(lam, z, p)
        slopes = generic_slope_values(lam, z, p)
        if inv_rprod is None or slopes is None:
            raise AssertionError((p, edge, lam, z, "generic ratio formula undefined"))
        ratio_inv_values.add(inv_rprod)
        ratio_slope_sets.add(slopes)
    if ratio_inv_values != {actual_inv_rprod} or ratio_slope_sets != {actual_slopes}:
        raise AssertionError(
            (p, edge, lam, ratio_inv_values, actual_inv_rprod, ratio_slope_sets, actual_slopes)
        )
    return {
        "branch": 0,
        "inv_rprod": actual_inv_rprod,
        "slope_values": actual_slopes,
    }


def ratio_rho(lam_a: int, inv_rprod_a: int, lam_b: int, inv_rprod_b: int, p: int) -> int:
    if lam_a == lam_b:
        raise AssertionError("ratio rho is only defined for lambda-distinct pairs")
    return (1 + (inv_rprod_a - inv_rprod_b) * pow((lam_a - lam_b) % p, -1, p)) % p


def verify_row(p: int, n: int) -> dict[str, int]:
    data = edge_cubic_data(p, n)
    ratio_data = {
        edge: edge_ratio_data(edge, lam, p) for edge, (lam, _) in data.items()
    }
    lambda_distinct_pairs = 0
    generic_generic_pairs = 0
    lambda_one_pairs = 0
    rho_hit = 0
    rho_miss = 0
    for edge_a, edge_b in combinations(list(data), 2):
        lam_a, prod_a = data[edge_a]
        lam_b, prod_b = data[edge_b]
        if lam_a == lam_b:
            continue
        lambda_distinct_pairs += 1
        branch_a = int(ratio_data[edge_a]["branch"])
        branch_b = int(ratio_data[edge_b]["branch"])
        if branch_a == 0 and branch_b == 0:
            generic_generic_pairs += 1
        if branch_a == 1 or branch_b == 1:
            lambda_one_pairs += 1
        rho = rho_value((lam_a, prod_a), (lam_b, prod_b), p)
        rec_rho = rho_from_reciprocal_products(
            lam_a,
            pow(int(ratio_data[edge_a]["inv_rprod"]), -1, p),
            lam_b,
            pow(int(ratio_data[edge_b]["inv_rprod"]), -1, p),
            p,
        )
        explicit_rho = ratio_rho(
            lam_a,
            int(ratio_data[edge_a]["inv_rprod"]),
            lam_b,
            int(ratio_data[edge_b]["inv_rprod"]),
            p,
        )
        if rho != rec_rho or rho != explicit_rho:
            raise AssertionError((p, n, edge_a, edge_b, rho, rec_rho, explicit_rho))
        source_slopes = ratio_data[edge_a]["slope_values"]
        if not isinstance(source_slopes, frozenset):
            raise AssertionError((p, n, edge_a, "bad slope set"))
        if rho in source_slopes:
            rho_hit += 1
            if not (set(edge_a) & set(edge_b)):
                raise AssertionError((p, n, edge_a, edge_b, rho, source_slopes))
        else:
            rho_miss += 1
            if set(edge_a) & set(edge_b):
                raise AssertionError((p, n, edge_a, edge_b, rho, source_slopes))
    return {
        "active_edges": len(data),
        "lambda_distinct_pairs": lambda_distinct_pairs,
        "generic_generic_pairs": generic_generic_pairs,
        "lambda_one_pairs": lambda_one_pairs,
        "rho_hit": rho_hit,
        "rho_miss": rho_miss,
    }


def main() -> None:
    print("h=3 repeat slope-ratio compiler")
    print("generic R^-1=-(lambda-1)^3 z^2(1+z)^2/(1+z+z^2)^3")
    print("rho=1+(R^-1-S^-1)/(lambda-mu)")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} active_edges={row['active_edges']} "
            f"lambda_distinct_pairs={row['lambda_distinct_pairs']} "
            f"generic_generic_pairs={row['generic_generic_pairs']} "
            f"lambda_one_pairs={row['lambda_one_pairs']} "
            f"rho_hit={row['rho_hit']} rho_miss={row['rho_miss']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["rho_miss"] == 0 or row["lambda_one_pairs"] == 0:
            raise AssertionError((p, n, "contrast row should exercise misses and lambda=1 pairs"))
        print(
            f"contrast p={p} n={n} active_edges={row['active_edges']} "
            f"lambda_distinct_pairs={row['lambda_distinct_pairs']} "
            f"generic_generic_pairs={row['generic_generic_pairs']} "
            f"lambda_one_pairs={row['lambda_one_pairs']} "
            f"rho_hit={row['rho_hit']} rho_miss={row['rho_miss']}"
        )
    print("H3-SLOPE-HIT is a ratio-rho membership in the source slope set")
    print("H3_REPEAT_SLOPE_RATIO_COMPILER_PASS")


if __name__ == "__main__":
    main()
