#!/usr/bin/env python3
"""Signed seven-edge Vieta atlas for positive three-loop packets."""

import itertools

import sympy as sp


PLACEMENT_COLORED_ENDPOINTS = {
    "442_root_low": ("c", "c"),
    "442_root_high": ("b", "b"),
    "433_root_low": ("b", "c"),
    "433_root_high": ("1", "b"),
}


def sign_orbits():
    """Gauge flips of the two colored outside representatives."""
    unseen = set(itertools.product((1, -1), repeat=3))
    orbits = []
    while unseen:
        representative = min(unseen)
        orbit = {
            (representative[0] * flip_e,
             representative[1] * flip_f,
             representative[2] * flip_e * flip_f)
            for flip_e, flip_f in itertools.product((1, -1), repeat=2)
        }
        unseen -= orbit
        orbits.append(tuple(sorted(orbit)))
    return tuple(sorted(orbits))


def signed_edges(placement, cycle_sign):
    if placement not in PLACEMENT_COLORED_ENDPOINTS:
        raise ValueError(placement)
    if cycle_sign not in (-1, 1):
        raise ValueError(cycle_sign)
    endpoint_left, endpoint_right = PLACEMENT_COLORED_ENDPOINTS[placement]
    return (
        (endpoint_left, "e", 1, "colored-left"),
        (endpoint_right, "f", 1, "colored-right"),
        ("d", "e", 1, "internal-de-plus"),
        ("d", "e", -1, "internal-de-minus"),
        ("d", "f", 1, "internal-df-plus"),
        ("d", "f", -1, "internal-df-minus"),
        ("e", "f", cycle_sign, "internal-ef-cycle"),
    )


def target_record(left, right, edge_sign):
    product = edge_sign * left * right
    squared_sum = left**2 + right**2 + 2 * product
    return product, squared_sum


def coefficient_polynomials(a0, ai, a1, d0, d1, d2, beta, product,
                            squared_sum, w):
    denominator = d0 + d1 * w + d2 * w**2
    middle = (
        (a0**2 - a1**2) * d0
        - a1**2 * d1
        + (ai**2 - a1**2) * d2
    )
    numerator = -a0**2 * d0 + middle * w - ai**2 * d2 * w**2
    product_polynomial = sp.expand(numerator - product * denominator)
    sum_polynomial = sp.expand(
        beta**2 * w * (w - 1)**2 - squared_sum * denominator**2
    )
    return denominator, product_polynomial, sum_polynomial


def verify_edge_equivalence():
    a0, ai, a1, d0, d1, d2, beta = sp.symbols(
        "a0 ai a1 d0 d1 d2 beta"
    )
    p, s, z, w = sp.symbols("p s z w")
    denominator, product_polynomial, sum_polynomial = coefficient_polynomials(
        a0, ai, a1, d0, d1, d2, beta, p, s**2, w
    )
    direct_sum = z * beta * (z**2 - 1) + s * denominator.subs(w, z**2)
    conjugate_sum = -z * beta * (z**2 - 1) + s * denominator.subs(w, z**2)
    if sp.expand(
        direct_sum * conjugate_sum + sum_polynomial.subs(w, z**2)
    ) != 0:
        raise RuntimeError("squared sum equivalence")
    if sp.degree(product_polynomial, w) > 2:
        raise RuntimeError("product degree")
    if sp.degree(sum_polynomial, w) > 4:
        raise RuntimeError("sum degree")


def verify():
    orbits = sign_orbits()
    invariants = sorted(
        representative[0] * representative[1] * representative[2]
        for representative, *_ in orbits
    )
    if len(orbits) != 2 or invariants != [-1, 1]:
        raise RuntimeError(f"sign orbits {len(orbits)} {invariants}")

    lanes = {}
    symbols = {name: sp.Symbol(name) for name in ("b", "c", "d", "e", "f")}
    symbols["1"] = sp.Integer(1)
    for placement in PLACEMENT_COLORED_ENDPOINTS:
        for cycle_sign in (-1, 1):
            records = []
            for left, right, edge_sign, label in signed_edges(placement, cycle_sign):
                product, squared_sum = target_record(
                    symbols[left], symbols[right], edge_sign
                )
                records.append((label, sp.expand(product), sp.expand(squared_sum)))
            if len(records) != 7 or len({record[0] for record in records}) != 7:
                raise RuntimeError(f"edge coverage {placement} {cycle_sign}")
            lanes[(placement, cycle_sign)] = tuple(records)
    if len(lanes) != 8:
        raise RuntimeError("lane count")
    verify_edge_equivalence()
    return orbits, lanes


def main():
    orbits, lanes = verify()
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_SIGNED_OUTSIDE_VIETA_PASS "
        f"raw_signs={sum(len(orbit) for orbit in orbits)} "
        f"sign_orbits={len(orbits)} placements={len(PLACEMENT_COLORED_ENDPOINTS)} "
        f"lanes={len(lanes)} edges_per_lane=7"
    )


if __name__ == "__main__":
    main()
