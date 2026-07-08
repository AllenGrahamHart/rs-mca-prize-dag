#!/usr/bin/env python3
"""Affine value-slope form for h=3 repeat-boundary active cubics."""

from __future__ import annotations

from itertools import combinations

from f3_h3_repeat_edge_cubic_gcd_form import edge_cubic_data
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_quadratic_rho_compiler import rho_value
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


def a_lambda(lam: int, t: int, p: int) -> int:
    return (t * ((t - 1) % p) * ((t - 1) % p) + lam * t * ((2 - t) % p)) % p


def slope_value(t: int, p: int) -> int:
    return t * ((2 - t) % p) % p


def verify_row(p: int, n: int) -> dict[str, int]:
    data = edge_cubic_data(p, n)
    for edge, (lam, prod) in data.items():
        for t in edge:
            if a_lambda(lam, t, p) != prod:
                raise AssertionError((p, n, edge, lam, prod, t, a_lambda(lam, t, p)))

    lambda_distinct_pairs = 0
    rho_hit = 0
    rho_miss = 0
    repeated_rho_values: set[int] = set()
    for edge_a, edge_b in combinations(list(data), 2):
        lam_a, _ = data[edge_a]
        lam_b, _ = data[edge_b]
        if lam_a == lam_b:
            continue
        lambda_distinct_pairs += 1
        rho = rho_value(data[edge_a], data[edge_b], p)
        hits = {t for t in edge_a if slope_value(t, p) == rho}
        if hits != (set(edge_a) & set(edge_b)):
            raise AssertionError((p, n, edge_a, edge_b, rho, hits))
        if hits:
            rho_hit += 1
            repeated_rho_values.add(rho)
        else:
            rho_miss += 1
    return {
        "active_edges": len(data),
        "lambda_distinct_pairs": lambda_distinct_pairs,
        "rho_hit": rho_hit,
        "rho_miss": rho_miss,
        "hit_rho_values": len(repeated_rho_values),
    }


def main() -> None:
    print("h=3 repeat affine value-slope compiler")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} active_edges={row['active_edges']} "
            f"lambda_distinct_pairs={row['lambda_distinct_pairs']} "
            f"rho_hit={row['rho_hit']} rho_miss={row['rho_miss']} "
            f"hit_rho_values={row['hit_rho_values']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["rho_miss"] == 0:
            raise AssertionError((p, n, "contrast row should have rho misses"))
        print(
            f"contrast p={p} n={n} active_edges={row['active_edges']} "
            f"lambda_distinct_pairs={row['lambda_distinct_pairs']} "
            f"rho_hit={row['rho_hit']} rho_miss={row['rho_miss']} "
            f"hit_rho_values={row['hit_rho_values']}"
        )
    print("A_lambda(T)=T(T-1)^2+lambda*T(2-T)")
    print("H3_REPEAT_AFFINE_VALUE_SLOPE_COMPILER_PASS")


if __name__ == "__main__":
    main()
