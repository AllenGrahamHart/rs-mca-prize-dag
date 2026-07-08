#!/usr/bin/env python3
"""Lambda-fiber ledger for h=3 repeat-boundary active edges."""

from __future__ import annotations

from collections import defaultdict
from math import comb

from f3_h3_repeat_edge_cubic_gcd_form import edge_cubic_data
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


def lambda_fibers(p: int, n: int) -> dict[int, list[frozenset[int]]]:
    fibers: dict[int, list[frozenset[int]]] = defaultdict(list)
    for edge, (lam, _) in edge_cubic_data(p, n).items():
        fibers[lam].append(edge)
    return dict(fibers)


def verify_row(p: int, n: int) -> dict[str, int]:
    fibers = lambda_fibers(p, n)
    same_lambda_pairs = sum(comb(len(edges), 2) for edges in fibers.values())
    direct_pairs = 0
    active_edges = [edge for edges in fibers.values() for edge in edges]
    for i, edge_a in enumerate(active_edges):
        for edge_b in active_edges[i + 1 :]:
            lam_a = next(lam for lam, edges in fibers.items() if edge_a in edges)
            lam_b = next(lam for lam, edges in fibers.items() if edge_b in edges)
            if lam_a == lam_b:
                if set(edge_a) & set(edge_b):
                    raise AssertionError((p, n, "same-lambda edges intersect", edge_a, edge_b))
                direct_pairs += 1
    if direct_pairs != same_lambda_pairs:
        raise AssertionError((p, n, direct_pairs, same_lambda_pairs))
    max_fiber = max((len(edges) for edges in fibers.values()), default=0)
    repeated_lambdas = sum(1 for edges in fibers.values() if len(edges) > 1)
    return {
        "active_edges": len(active_edges),
        "lambda_values": len(fibers),
        "max_lambda_fiber": max_fiber,
        "repeated_lambdas": repeated_lambdas,
        "same_lambda_pairs": same_lambda_pairs,
    }


def main() -> None:
    print("h=3 repeat lambda-fiber ledger")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} active_edges={row['active_edges']} "
            f"lambda_values={row['lambda_values']} max_K_lambda={row['max_lambda_fiber']} "
            f"repeated_lambdas={row['repeated_lambdas']} "
            f"same_lambda_pairs={row['same_lambda_pairs']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["same_lambda_pairs"] == 0:
            raise AssertionError((p, n, "contrast row should have same-lambda collision"))
        print(
            f"contrast p={p} n={n} active_edges={row['active_edges']} "
            f"lambda_values={row['lambda_values']} max_K_lambda={row['max_lambda_fiber']} "
            f"repeated_lambdas={row['repeated_lambdas']} "
            f"same_lambda_pairs={row['same_lambda_pairs']}"
        )
    print("same-lambda pairs = sum_lambda binom(K_lambda,2)")
    print("H3_REPEAT_LAMBDA_FIBER_LEDGER_PASS")


if __name__ == "__main__":
    main()
