#!/usr/bin/env python3
"""Collision-system compiler for h=3 same-lambda active edges."""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations

from f3_h3_pair_count_from_charts_compiler import root_table
from f3_h3_repeat_edge_cubic_gcd_form import edge_cubic_data
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_lambda_one_scale_compiler import lambda_one_scale_edges
from f3_h3_repeat_lambda_ratio_membership_compiler import generic_coordinate_functions
from f3_h3_repeat_lambda_ratio_orbit_compiler import verify_edge_orbit
from f3_h3_repeat_reciprocal_product_compiler import reciprocal_edge, reciprocal_product
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


def generic_ratio_orbit_data(p: int, n: int) -> dict[int, list[tuple[frozenset[int], tuple[int, ...], int]]]:
    hset = set(root_table(p, n))
    out: dict[int, list[tuple[frozenset[int], tuple[int, ...], int]]] = defaultdict(list)
    for edge, (lam, _) in edge_cubic_data(p, n).items():
        if lam == 1:
            continue
        _, orbit = verify_edge_orbit(p, edge, lam)
        z = orbit[0]
        coords = generic_coordinate_functions(lam, z, p)
        if coords is None or set(coords) != set(edge):
            raise AssertionError((p, n, edge, lam, z, coords))
        if any(coord not in hset for coord in coords):
            raise AssertionError((p, n, edge, lam, z, coords, "not in H"))
        rprod = reciprocal_product(reciprocal_edge(edge, p), p)
        out[lam].append((edge, orbit, rprod))
    return dict(out)


def lambda_one_scale_data(p: int, n: int) -> list[tuple[frozenset[int], frozenset[int]]]:
    active = {edge for edge, (lam, _) in edge_cubic_data(p, n).items() if lam == 1}
    scale_edges = lambda_one_scale_edges(p, n)
    if set(scale_edges) != active:
        raise AssertionError((p, n, active, scale_edges))
    return sorted(scale_edges.items(), key=lambda item: tuple(sorted(item[0])))


def verify_row(p: int, n: int) -> dict[str, int]:
    generic_by_lambda = generic_ratio_orbit_data(p, n)
    scale_rows = lambda_one_scale_data(p, n)

    generic_collision_pairs = 0
    repeated_generic_lambdas = 0
    for lam, rows in generic_by_lambda.items():
        orbit_set = {orbit for _, orbit, _ in rows}
        rprod_set = {rprod for _, _, rprod in rows}
        if len(orbit_set) != len(rows) or len(rprod_set) != len(rows):
            raise AssertionError((p, n, lam, rows, "orbit/product collision"))
        if len(rows) > 1:
            repeated_generic_lambdas += 1
        for (edge_a, orbit_a, _), (edge_b, orbit_b, _) in combinations(rows, 2):
            if orbit_a == orbit_b:
                raise AssertionError((p, n, lam, edge_a, edge_b, "same orbit"))
            if set(edge_a) & set(edge_b):
                raise AssertionError((p, n, lam, edge_a, edge_b, "same-lambda edges intersect"))
            generic_collision_pairs += 1

    scale_orbits = {orbit for _, orbit in scale_rows}
    if len(scale_orbits) != len(scale_rows):
        raise AssertionError((p, n, "lambda=1 scale orbit collision", scale_rows))
    scale_collision_pairs = len(scale_rows) * (len(scale_rows) - 1) // 2

    same_lambda_pairs = generic_collision_pairs + scale_collision_pairs
    direct_same_lambda_pairs = 0
    data = edge_cubic_data(p, n)
    for edge_a, edge_b in combinations(list(data), 2):
        if data[edge_a][0] == data[edge_b][0]:
            direct_same_lambda_pairs += 1
    if same_lambda_pairs != direct_same_lambda_pairs:
        raise AssertionError((p, n, same_lambda_pairs, direct_same_lambda_pairs))

    return {
        "active_edges": len(data),
        "generic_lambdas": len(generic_by_lambda),
        "repeated_generic_lambdas": repeated_generic_lambdas,
        "generic_collision_pairs": generic_collision_pairs,
        "lambda_one_scale_orbits": len(scale_rows),
        "scale_collision_pairs": scale_collision_pairs,
        "same_lambda_pairs": same_lambda_pairs,
    }


def main() -> None:
    print("h=3 repeat same-lambda collision system")
    print("same-lambda failure = two generic ratio orbits or two lambda=1 scale orbits")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} active_edges={row['active_edges']} "
            f"generic_lambdas={row['generic_lambdas']} "
            f"repeated_generic_lambdas={row['repeated_generic_lambdas']} "
            f"generic_collision_pairs={row['generic_collision_pairs']} "
            f"lambda_one_scale_orbits={row['lambda_one_scale_orbits']} "
            f"scale_collision_pairs={row['scale_collision_pairs']} "
            f"same_lambda_pairs={row['same_lambda_pairs']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["same_lambda_pairs"] == 0:
            raise AssertionError((p, n, "contrast row should have same-lambda collision"))
        print(
            f"contrast p={p} n={n} active_edges={row['active_edges']} "
            f"generic_lambdas={row['generic_lambdas']} "
            f"repeated_generic_lambdas={row['repeated_generic_lambdas']} "
            f"generic_collision_pairs={row['generic_collision_pairs']} "
            f"lambda_one_scale_orbits={row['lambda_one_scale_orbits']} "
            f"scale_collision_pairs={row['scale_collision_pairs']} "
            f"same_lambda_pairs={row['same_lambda_pairs']}"
        )
    print("H3-VALUE-INJECTIVE is absence of same-lambda collision systems")
    print("H3_REPEAT_SAME_LAMBDA_COLLISION_SYSTEM_PASS")


if __name__ == "__main__":
    main()
