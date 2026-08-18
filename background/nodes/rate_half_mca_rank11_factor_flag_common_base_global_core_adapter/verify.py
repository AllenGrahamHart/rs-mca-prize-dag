#!/usr/bin/env python3
"""Finite exact control for the factor-base/global-core adapter."""

from __future__ import annotations

import argparse


Q = 101
X = 7


def ev(poly: tuple[int, ...], x: int) -> int:
    return sum(coef * pow(x, degree, Q) for degree, coef in enumerate(poly)) % Q


def mul(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % Q
    return tuple(out)


def build(tamper: bool = False) -> dict[str, object]:
    # Both pencil generators have the common factor X-7.
    common = ((-X) % Q, 1)
    pencil = (common, mul(common, (3, 1)))
    residual = ((1,), (2, 1), (5, 0, 1), (9, 4), (6, 3, 2))
    products = tuple(mul(g, b) for g in pencil for b in residual)
    pencil_b = ((1,), (4, 1))
    residual_b = tuple(mul(common, b) for b in residual)
    products_b = tuple(mul(g, b) for g in pencil_b for b in residual_b)
    if tamper:
        products = products + ((1,),)
    product_values = tuple(ev(poly, X) for poly in products)
    product_values_b = tuple(ev(poly, X) for poly in products_b)
    anchor = (23, 61)
    pair_coefficients = ((2, 0), (0, 3), (5, 8), (11, 4))
    pairs = tuple(
        (
            (anchor[0] + a * product_values[0] + b * product_values[3]) % Q,
            (anchor[1] + a * product_values[5] + b * product_values[8]) % Q,
        )
        for a, b in pair_coefficients
    )
    assert all(value == 0 for value in product_values)
    assert all(value == 0 for value in product_values_b)
    assert all(pair == anchor for pair in pairs)
    return {
        "product_values": product_values,
        "product_values_b": product_values_b,
        "pairs": pairs,
        "anchor": anchor,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        caught = 0
        try:
            build(tamper=True)
        except AssertionError:
            caught = 1
        assert caught == 1
        print("RANK11_FACTOR_BASE_GLOBAL_CORE_TAMPER_PASS mutations=1/1")
        return
    print(
        "RANK11_FACTOR_BASE_GLOBAL_CORE_PASS "
        f"p_base_products={len(result['product_values'])} "
        f"b_base_products={len(result['product_values_b'])} records={len(result['pairs'])}"
    )


if __name__ == "__main__":
    main()
