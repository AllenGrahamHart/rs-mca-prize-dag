#!/usr/bin/env python3
"""Pair-intersection compiler for h=3 repeat-boundary edge cubics."""

from __future__ import annotations

from itertools import combinations

from f3_h3_repeat_edge_cubic_gcd_form import edge_cubic_data
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


def quadratic_difference_roots(
    edge_a: frozenset[int],
    data_a: tuple[int, int],
    data_b: tuple[int, int],
    p: int,
) -> set[int]:
    lam_a, prod_a = data_a
    lam_b, prod_b = data_b
    if lam_a == lam_b:
        return set(edge_a) if prod_a == prod_b else set()
    delta_lam = (lam_a - lam_b) % p
    delta_prod = (prod_a - prod_b) % p
    roots: set[int] = set()
    for t in edge_a:
        q = (-delta_lam * t * t + 2 * delta_lam * t - delta_prod) % p
        if q == 0:
            roots.add(t)
    return roots


def verify_row(p: int, n: int) -> dict[str, int]:
    data = edge_cubic_data(p, n)
    edges = list(data)
    total_pairs = 0
    intersecting_pairs = 0
    disjoint_pairs = 0
    same_lambda_distinct = 0
    quadratic_miss = 0
    for edge_a, edge_b in combinations(edges, 2):
        total_pairs += 1
        actual = set(edge_a) & set(edge_b)
        lam_a, prod_a = data[edge_a]
        lam_b, prod_b = data[edge_b]
        predicted = quadratic_difference_roots(edge_a, data[edge_a], data[edge_b], p)
        if predicted != actual:
            raise AssertionError((p, n, edge_a, edge_b, actual, predicted))

        if actual:
            intersecting_pairs += 1
        else:
            disjoint_pairs += 1
            if lam_a == lam_b:
                if prod_a == prod_b:
                    raise AssertionError((p, n, "same cubic but distinct edge", edge_a, edge_b))
                same_lambda_distinct += 1
            else:
                quadratic_miss += 1
    if disjoint_pairs != same_lambda_distinct + quadratic_miss:
        raise AssertionError((p, n, disjoint_pairs, same_lambda_distinct, quadratic_miss))
    return {
        "active_edges": len(edges),
        "total_pairs": total_pairs,
        "intersecting_pairs": intersecting_pairs,
        "disjoint_pairs": disjoint_pairs,
        "same_lambda_distinct": same_lambda_distinct,
        "quadratic_miss": quadratic_miss,
    }


def main() -> None:
    print("h=3 repeat pair-intersection compiler")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} active_edges={row['active_edges']} "
            f"pairs={row['total_pairs']} intersecting={row['intersecting_pairs']} "
            f"disjoint={row['disjoint_pairs']} same_lambda={row['same_lambda_distinct']} "
            f"quadratic_miss={row['quadratic_miss']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["disjoint_pairs"] == 0:
            raise AssertionError((p, n, "contrast row should have disjoint pairs"))
        print(
            f"contrast p={p} n={n} active_edges={row['active_edges']} "
            f"pairs={row['total_pairs']} intersecting={row['intersecting_pairs']} "
            f"disjoint={row['disjoint_pairs']} same_lambda={row['same_lambda_distinct']} "
            f"quadratic_miss={row['quadratic_miss']}"
        )
    print("Disjoint active-edge pairs split into same-lambda and quadratic-miss cases")
    print("H3_REPEAT_PAIR_INTERSECTION_COMPILER_PASS")


if __name__ == "__main__":
    main()
