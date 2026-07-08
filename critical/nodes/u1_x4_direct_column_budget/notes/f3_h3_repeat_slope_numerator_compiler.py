#!/usr/bin/env python3
"""Denominator-cleared numerator compiler for h=3 slope-hit."""

from __future__ import annotations

from itertools import combinations, permutations

from f3_h3_repeat_edge_cubic_gcd_form import edge_cubic_data
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_quadratic_rho_compiler import rho_value
from f3_h3_repeat_reciprocal_product_compiler import reciprocal_edge
from f3_h3_repeat_slope_ratio_compiler import (
    edge_ratio_data,
    generic_inv_rprod,
    lambda_one_slope_values_from_scale,
    ratio_rho,
)
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


def first_ordered_ratio(edge: frozenset[int], p: int) -> int:
    rec_edge = sorted(reciprocal_edge(edge, p))
    for r, s in permutations(rec_edge, 2):
        z = s * pow(r, -1, p) % p
        if z not in (0, 1) and (1 + z) % p:
            return z
    raise AssertionError((p, edge, "no valid ordered ratio"))


def first_scale(edge: frozenset[int], p: int) -> int:
    rec_edge = reciprocal_edge(edge, p)
    return pow(next(iter(rec_edge)), -1, p)


def source_slope_numerators(lam: int, z: int, p: int) -> tuple[int, int, int]:
    a = (lam - 1) % p
    n = (1 + z + z * z) % p
    if n == 0:
        raise AssertionError((p, lam, z, "slope denominator pole"))
    n2 = n * n % p
    return (
        (n2 - a * a * z * z * ((1 + z) % p) * ((1 + z) % p)) % p,
        (n2 - a * a * ((1 + z) % p) * ((1 + z) % p)) % p,
        (n2 - a * a * z * z) % p,
    )


def generic_source_q_values(
    lam: int, z: int, mu: int, target_inv_rprod: int, p: int
) -> tuple[int, int, int]:
    if lam == 1 or lam == mu:
        raise AssertionError((p, lam, mu, "generic lambda-distinct source required"))
    a = (lam - 1) % p
    n = (1 + z + z * z) % p
    if n == 0:
        raise AssertionError((p, lam, z, "source pole"))
    b = pow(n, 3, p)
    source_a = (-pow(a, 3, p) * z * z * ((1 + z) % p) * ((1 + z) % p)) % p
    source_inv = source_a * pow(b, -1, p) % p
    if source_inv != generic_inv_rprod(lam, z, p):
        raise AssertionError((p, lam, z, source_inv, generic_inv_rprod(lam, z, p)))
    delta = (lam - mu) % p
    rho_num = (delta * b + source_a - target_inv_rprod * b) % p
    return tuple((rho_num - slope_num * delta * n) % p for slope_num in source_slope_numerators(lam, z, p))


def scale_source_q_values(
    x: int, lam: int, target_lam: int, target_inv_rprod: int, p: int
) -> tuple[int, int, int]:
    if lam != 1 or target_lam == 1:
        raise AssertionError((p, lam, target_lam, "scale source needs lambda=1 and target distinct"))
    rho = ratio_rho(lam, pow(x, 3, p), target_lam, target_inv_rprod, p)
    return tuple((rho - slope) % p for slope in lambda_one_slope_values_from_scale(x, p))


def verify_row(p: int, n: int) -> dict[str, int]:
    data = edge_cubic_data(p, n)
    ratio_data = {edge: edge_ratio_data(edge, lam, p) for edge, (lam, _) in data.items()}
    checked_pairs = 0
    generic_source_pairs = 0
    scale_source_pairs = 0
    numerator_zero = 0
    numerator_nonzero = 0
    for edge_a, edge_b in combinations(list(data), 2):
        lam_a, prod_a = data[edge_a]
        lam_b, prod_b = data[edge_b]
        if lam_a == lam_b:
            continue
        checked_pairs += 1
        rho = rho_value((lam_a, prod_a), (lam_b, prod_b), p)
        explicit_rho = ratio_rho(
            lam_a,
            int(ratio_data[edge_a]["inv_rprod"]),
            lam_b,
            int(ratio_data[edge_b]["inv_rprod"]),
            p,
        )
        if rho != explicit_rho:
            raise AssertionError((p, n, edge_a, edge_b, rho, explicit_rho))
        if lam_a == 1:
            scale_source_pairs += 1
            q_values = scale_source_q_values(
                first_scale(edge_a, p),
                lam_a,
                lam_b,
                int(ratio_data[edge_b]["inv_rprod"]),
                p,
            )
        else:
            generic_source_pairs += 1
            q_values = generic_source_q_values(
                lam_a,
                first_ordered_ratio(edge_a, p),
                lam_b,
                int(ratio_data[edge_b]["inv_rprod"]),
                p,
            )
        q_product = 1
        for q in q_values:
            q_product = q_product * q % p
        hit = bool(set(edge_a) & set(edge_b))
        if q_product == 0:
            numerator_zero += 1
        else:
            numerator_nonzero += 1
        if (q_product == 0) != hit:
            raise AssertionError((p, n, edge_a, edge_b, q_values, q_product, hit))
    return {
        "checked_pairs": checked_pairs,
        "generic_source_pairs": generic_source_pairs,
        "scale_source_pairs": scale_source_pairs,
        "numerator_zero": numerator_zero,
        "numerator_nonzero": numerator_nonzero,
    }


def main() -> None:
    print("h=3 repeat slope numerator compiler")
    print("slope-hit iff product_i Q_i=0 after denominator clearing")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} checked_pairs={row['checked_pairs']} "
            f"generic_source_pairs={row['generic_source_pairs']} "
            f"scale_source_pairs={row['scale_source_pairs']} "
            f"numerator_zero={row['numerator_zero']} "
            f"numerator_nonzero={row['numerator_nonzero']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["numerator_nonzero"] == 0:
            raise AssertionError((p, n, "contrast row should have nonzero slope numerators"))
        print(
            f"contrast p={p} n={n} checked_pairs={row['checked_pairs']} "
            f"generic_source_pairs={row['generic_source_pairs']} "
            f"scale_source_pairs={row['scale_source_pairs']} "
            f"numerator_zero={row['numerator_zero']} "
            f"numerator_nonzero={row['numerator_nonzero']}"
        )
    print("H3_REPEAT_SLOPE_NUMERATOR_COMPILER_PASS")


if __name__ == "__main__":
    main()
