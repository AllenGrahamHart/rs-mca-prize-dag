#!/usr/bin/env python3
"""Reciprocal-product compiler for h=3 repeat-boundary active edges."""

from __future__ import annotations

from itertools import combinations

from f3_h3_pair_count_from_charts_compiler import root_table
from f3_h3_repeat_edge_cubic_gcd_form import edge_cubic_data
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_loose_reciprocal_closure_compiler import reciprocal_coordinate
from f3_h3_repeat_quadratic_rho_compiler import rho_value
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


def reciprocal_edge(edge: frozenset[int], p: int) -> frozenset[int]:
    return frozenset(reciprocal_coordinate(u, p) for u in edge)


def elementary_q(rec_edge: frozenset[int], p: int) -> int:
    total = 0
    for r, s in combinations(sorted(rec_edge), 2):
        total = (total + r * s) % p
    return total


def reciprocal_product(rec_edge: frozenset[int], p: int) -> int:
    out = 1
    for r in rec_edge:
        out = (out * r) % p
    if out == 0:
        raise AssertionError((p, "zero reciprocal product", rec_edge))
    return out


def lambda_from_reciprocal_edge(rec_edge: frozenset[int], p: int) -> int:
    rprod = reciprocal_product(rec_edge, p)
    return (1 + elementary_q(rec_edge, p) * pow(rprod, -1, p)) % p


def coordinate_product_from_reciprocal_edge(rec_edge: frozenset[int], p: int) -> int:
    lam = lambda_from_reciprocal_edge(rec_edge, p)
    rprod = reciprocal_product(rec_edge, p)
    return (lam + pow(rprod, -1, p)) % p


def rho_from_reciprocal_products(
    lam_a: int, rprod_a: int, lam_b: int, rprod_b: int, p: int
) -> int:
    delta_lam = (lam_a - lam_b) % p
    if delta_lam == 0:
        raise AssertionError("rho is only defined for lambda-distinct pairs")
    delta_inv_rprod = (pow(rprod_a, -1, p) - pow(rprod_b, -1, p)) % p
    return (1 + delta_inv_rprod * pow(delta_lam, -1, p)) % p


def reciprocal_slope_value(r: int, p: int) -> int:
    return (1 - pow(r, -2, p)) % p


def verify_row(p: int, n: int) -> dict[str, int]:
    hset = set(root_table(p, n))
    data = edge_cubic_data(p, n)
    rec_data: dict[frozenset[int], tuple[int, int, int]] = {}
    for edge, (lam, coord_prod) in data.items():
        rec_edge = reciprocal_edge(edge, p)
        if sum(rec_edge) % p != 0:
            raise AssertionError((p, n, edge, rec_edge, "not zero-sum"))
        rprod = reciprocal_product(rec_edge, p)
        if lambda_from_reciprocal_edge(rec_edge, p) != lam:
            raise AssertionError((p, n, edge, rec_edge, "lambda mismatch"))
        if coordinate_product_from_reciprocal_edge(rec_edge, p) != coord_prod:
            raise AssertionError((p, n, edge, rec_edge, "coordinate product mismatch"))
        expected_q = ((lam - 1) % p) * rprod % p
        if elementary_q(rec_edge, p) != expected_q:
            raise AssertionError((p, n, edge, rec_edge, "q mismatch"))
        roots_in_s = {
            r
            for r in (reciprocal_coordinate(u, p) for u in hset if u != 1)
            if (pow(r, 3, p) + ((lam - 1) % p) * rprod * r - rprod) % p == 0
        }
        if roots_in_s != rec_edge:
            raise AssertionError((p, n, edge, rec_edge, roots_in_s))
        rec_data[edge] = (lam, coord_prod, rprod)

    same_lambda_pairs = 0
    same_lambda_same_rprod = 0
    lambda_distinct_pairs = 0
    rho_hit = 0
    rho_miss = 0
    for edge_a, edge_b in combinations(list(data), 2):
        lam_a, coord_prod_a, rprod_a = rec_data[edge_a]
        lam_b, coord_prod_b, rprod_b = rec_data[edge_b]
        if lam_a == lam_b:
            same_lambda_pairs += 1
            if rprod_a == rprod_b:
                same_lambda_same_rprod += 1
            continue
        lambda_distinct_pairs += 1
        rho = rho_value((lam_a, coord_prod_a), (lam_b, coord_prod_b), p)
        rec_rho = rho_from_reciprocal_products(lam_a, rprod_a, lam_b, rprod_b, p)
        if rho != rec_rho:
            raise AssertionError((p, n, edge_a, edge_b, rho, rec_rho))
        rec_edge_a = reciprocal_edge(edge_a, p)
        rec_edge_b = reciprocal_edge(edge_b, p)
        hits = {r for r in rec_edge_a if reciprocal_slope_value(r, p) == rho}
        actual = rec_edge_a & rec_edge_b
        if hits != actual:
            raise AssertionError((p, n, edge_a, edge_b, rho, hits, actual))
        if hits:
            rho_hit += 1
        else:
            rho_miss += 1

    return {
        "active_edges": len(data),
        "same_lambda_pairs": same_lambda_pairs,
        "same_lambda_same_rprod": same_lambda_same_rprod,
        "lambda_distinct_pairs": lambda_distinct_pairs,
        "rho_hit": rho_hit,
        "rho_miss": rho_miss,
    }


def main() -> None:
    print("h=3 repeat reciprocal-product compiler")
    print("reciprocal edge polynomial: X^3 + (lambda-1)R X - R")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} active_edges={row['active_edges']} "
            f"same_lambda_pairs={row['same_lambda_pairs']} "
            f"same_lambda_same_R={row['same_lambda_same_rprod']} "
            f"lambda_distinct_pairs={row['lambda_distinct_pairs']} "
            f"rho_hit={row['rho_hit']} rho_miss={row['rho_miss']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["same_lambda_pairs"] == 0 or row["rho_miss"] == 0:
            raise AssertionError((p, n, "contrast row should hit both disjoint-edge failures"))
        print(
            f"contrast p={p} n={n} active_edges={row['active_edges']} "
            f"same_lambda_pairs={row['same_lambda_pairs']} "
            f"same_lambda_same_R={row['same_lambda_same_rprod']} "
            f"lambda_distinct_pairs={row['lambda_distinct_pairs']} "
            f"rho_hit={row['rho_hit']} rho_miss={row['rho_miss']}"
        )
    print("same-lambda injectivity is uniqueness of reciprocal product R")
    print("rho slope values are 1-r^-2 on reciprocal roots")
    print("H3_REPEAT_RECIPROCAL_PRODUCT_COMPILER_PASS")


if __name__ == "__main__":
    main()
