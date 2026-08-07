#!/usr/bin/env python3
"""Quadratic-rho compiler for lambda-distinct active edge pairs."""

from __future__ import annotations

from itertools import combinations

from f3_h3_repeat_edge_cubic_gcd_form import edge_cubic_data
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


def rho_value(data_a: tuple[int, int], data_b: tuple[int, int], p: int) -> int:
    lam_a, prod_a = data_a
    lam_b, prod_b = data_b
    delta_lam = (lam_a - lam_b) % p
    if delta_lam == 0:
        raise AssertionError("rho is only defined for lambda-distinct pairs")
    delta_prod = (prod_a - prod_b) % p
    return delta_prod * pow(delta_lam, -1, p) % p


def rho_roots(edge: frozenset[int], rho: int, p: int) -> set[int]:
    return {t for t in edge if (t * ((2 - t) % p) - rho) % p == 0}


def verify_row(p: int, n: int) -> dict[str, int]:
    data = edge_cubic_data(p, n)
    lambda_distinct_pairs = 0
    rho_hit = 0
    rho_miss = 0
    rho_values: set[int] = set()
    for edge_a, edge_b in combinations(list(data), 2):
        lam_a, _ = data[edge_a]
        lam_b, _ = data[edge_b]
        if lam_a == lam_b:
            continue
        lambda_distinct_pairs += 1
        rho = rho_value(data[edge_a], data[edge_b], p)
        rho_values.add(rho)
        predicted = rho_roots(edge_a, rho, p)
        actual = set(edge_a) & set(edge_b)
        if predicted != actual:
            raise AssertionError((p, n, edge_a, edge_b, rho, predicted, actual))
        if actual:
            rho_hit += 1
        else:
            rho_miss += 1
    if lambda_distinct_pairs != rho_hit + rho_miss:
        raise AssertionError((p, n, lambda_distinct_pairs, rho_hit, rho_miss))
    return {
        "active_edges": len(data),
        "lambda_distinct_pairs": lambda_distinct_pairs,
        "rho_hit": rho_hit,
        "rho_miss": rho_miss,
        "rho_values": len(rho_values),
    }


def main() -> None:
    print("h=3 repeat quadratic-rho compiler")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} active_edges={row['active_edges']} "
            f"lambda_distinct_pairs={row['lambda_distinct_pairs']} "
            f"rho_hit={row['rho_hit']} rho_miss={row['rho_miss']} "
            f"rho_values={row['rho_values']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["rho_miss"] == 0:
            raise AssertionError((p, n, "contrast row should have rho misses"))
        print(
            f"contrast p={p} n={n} active_edges={row['active_edges']} "
            f"lambda_distinct_pairs={row['lambda_distinct_pairs']} "
            f"rho_hit={row['rho_hit']} rho_miss={row['rho_miss']} "
            f"rho_values={row['rho_values']}"
        )
    print("lambda-distinct intersections are exactly roots of T(2-T)=rho")
    print("H3_REPEAT_QUADRATIC_RHO_COMPILER_PASS")


if __name__ == "__main__":
    main()
