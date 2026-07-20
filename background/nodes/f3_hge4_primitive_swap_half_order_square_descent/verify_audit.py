#!/usr/bin/env python3
"""Mutation audit for the HGE4 half-order square descent."""

from __future__ import annotations

import verify


def main() -> None:
    valid = frozenset((0, 1, 2, 4, 6))
    mutated = frozenset((0, 1, 2, 4, 7))
    assert verify.square_test(valid, 16, 97) is not None
    assert verify.square_test(mutated, 16, 97) is None

    square = (1, 7, 11)
    polynomial = verify.multiply(square, square, 97)
    assert verify.monic_square_root(polynomial, 97) == square
    broken = (*polynomial[:-1], (polynomial[-1] + 1) % 97)
    assert verify.monic_square_root(broken, 97) is None

    valid_root = verify.square_test(valid, 16, 97)
    assert valid_root is not None
    valid_values = tuple(pow(pow(verify.primitive_root(97), 6, 97), exponent, 97) for exponent in sorted(valid))
    valid_product = 1
    for value in valid_values:
        valid_product = valid_product * value % 97
    divisor = (*verify.multiply(valid_root, valid_root, 97), -valid_product % 97)
    cyclotomic = (1, *((0,) * 15), -1 % 97)
    assert verify.remainder(cyclotomic, divisor, 97) == ()
    bad_divisor = (*divisor[:-1], (divisor[-1] + 1) % 97)
    assert verify.remainder(cyclotomic, bad_divisor, 97) != ()

    periodic = frozenset((0, 2, 4, 6))
    assert verify.stabilizer(periodic, 8) != (0,)
    assert verify.stabilizer(valid, 16) == (0,)

    print(
        "F3_HGE4_PRIMITIVE_SWAP_HALF_ORDER_SQUARE_DESCENT_AUDIT_PASS "
        "square_mutation=1 coefficient_mutation=1 divisor_mutation=1 "
        "stabilizer_guard=1"
    )


if __name__ == "__main__":
    main()
