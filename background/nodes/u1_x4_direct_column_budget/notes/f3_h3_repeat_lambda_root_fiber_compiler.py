#!/usr/bin/env python3
"""Lambda-root fiber compiler for h=3 repeat-boundary active edges."""

from __future__ import annotations

from collections import defaultdict
from math import comb

from f3_h3_pair_count_from_charts_compiler import root_table
from f3_h3_repeat_edge_cubic_gcd_form import edge_cubic_data
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_loose_reciprocal_closure_compiler import (
    coordinate_from_reciprocal,
    reciprocal_image,
)
from f3_h3_repeat_reciprocal_product_compiler import (
    reciprocal_edge,
    reciprocal_product,
)
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


def phi_lambda(lam: int, r: int, p: int) -> int | None:
    denom = (1 - ((lam - 1) % p) * r) % p
    if denom == 0:
        return None
    return pow(r, 3, p) * pow(denom, -1, p) % p


def phi_size3_fibers(p: int, n: int) -> dict[frozenset[int], tuple[int, int]]:
    recs = sorted(reciprocal_image(p, n))
    fibers: dict[tuple[int, int], list[int]] = defaultdict(list)
    for lam in root_table(p, n):
        for r in recs:
            value = phi_lambda(lam, r, p)
            if value is not None:
                fibers[(lam, value)].append(r)

    out: dict[frozenset[int], tuple[int, int]] = {}
    for (lam, rprod), fiber in fibers.items():
        if len(fiber) > 3:
            raise AssertionError((p, n, lam, rprod, fiber))
        if len(fiber) != 3:
            continue
        if sum(fiber) % p != 0:
            raise AssertionError((p, n, lam, rprod, fiber, "size-3 fiber is not zero-sum"))
        edge = frozenset(coordinate_from_reciprocal(r, p) for r in fiber)
        if len(edge) != 3:
            raise AssertionError((p, n, lam, rprod, fiber, edge))
        if edge in out:
            raise AssertionError((p, n, edge, out[edge], (lam, rprod)))
        out[edge] = (lam, rprod)
    return out


def active_edges_as_phi_fibers(p: int, n: int) -> dict[frozenset[int], tuple[int, int]]:
    out: dict[frozenset[int], tuple[int, int]] = {}
    for edge, (lam, _) in edge_cubic_data(p, n).items():
        rec_edge = reciprocal_edge(edge, p)
        rprod = reciprocal_product(rec_edge, p)
        for r in rec_edge:
            value = phi_lambda(lam, r, p)
            if value != rprod:
                raise AssertionError((p, n, edge, rec_edge, lam, rprod, r, value))
        out[edge] = (lam, rprod)
    return out


def verify_row(p: int, n: int) -> dict[str, int]:
    phi_edges = phi_size3_fibers(p, n)
    active_edges = active_edges_as_phi_fibers(p, n)
    if phi_edges != active_edges:
        raise AssertionError((p, n, len(phi_edges), len(active_edges)))

    fibers_by_lambda: dict[int, list[int]] = defaultdict(list)
    for lam, rprod in phi_edges.values():
        fibers_by_lambda[lam].append(rprod)
    same_lambda_pairs = sum(comb(len(values), 2) for values in fibers_by_lambda.values())
    repeated_lambdas = sum(1 for values in fibers_by_lambda.values() if len(values) > 1)
    max_lambda_fibers = max((len(values) for values in fibers_by_lambda.values()), default=0)
    return {
        "active_edges": len(active_edges),
        "lambda_values": len(fibers_by_lambda),
        "max_lambda_fibers": max_lambda_fibers,
        "repeated_lambdas": repeated_lambdas,
        "same_lambda_pairs": same_lambda_pairs,
    }


def main() -> None:
    print("h=3 repeat lambda-root fiber compiler")
    print("Phi_lambda(r)=r^3/(1-(lambda-1)r)")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} active_edges={row['active_edges']} "
            f"lambda_values={row['lambda_values']} max_lambda_fibers={row['max_lambda_fibers']} "
            f"repeated_lambdas={row['repeated_lambdas']} "
            f"same_lambda_pairs={row['same_lambda_pairs']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["same_lambda_pairs"] == 0:
            raise AssertionError((p, n, "contrast row should have repeated lambda fibers"))
        print(
            f"contrast p={p} n={n} active_edges={row['active_edges']} "
            f"lambda_values={row['lambda_values']} "
            f"max_lambda_fibers={row['max_lambda_fibers']} "
            f"repeated_lambdas={row['repeated_lambdas']} "
            f"same_lambda_pairs={row['same_lambda_pairs']}"
        )
    print("active edges are exactly size-3 fibers of Phi_lambda on the reciprocal image")
    print("H3_REPEAT_LAMBDA_ROOT_FIBER_COMPILER_PASS")


if __name__ == "__main__":
    main()
