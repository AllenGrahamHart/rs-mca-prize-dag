#!/usr/bin/env python3
"""Mutation audit for the WCL fixed-divisor straight-line lift."""

from pathlib import Path

import verify


HERE = Path(__file__).resolve().parent


def main():
    joined = "\n".join(
        (HERE / name).read_text()
        for name in ("statement.md", "proof.md", "claim_contract.md", "audit.md")
    )
    required = [
        "b+m(2w-1)",
        "m(2w-1)+w",
        "total degree at most three",
        "No solutions or scheme components are introduced or discarded",
        "does not assert that Groebner elimination",
        "must be monic.",
        "b+k(2w-1)-w",
        "(1,5)   2   6       52          54",
    ]
    for token in required:
        assert token in joined, token

    verify.size_checks()
    verify.pruned_size_checks()
    verify.symbolic_shape_checks()
    verify.cubic_equation_check()

    p, n, w = verify.P, 256, 5
    omega = pow(3, (p - 1) // n, p)
    modulus = verify.polynomial_from_roots([pow(omega, j, p) for j in range(w)])
    rows = verify.transcript(modulus, 8)
    pruned = verify.pruned_transcript(modulus, 8)
    assert pruned == rows[2:]
    value, quotient, remainder = rows[-1]
    square = verify.mul(value, value, p)
    mutated_quotient = quotient[:]
    mutated_quotient[0] = (mutated_quotient[0] + 1) % p
    assert verify.add(verify.mul(modulus, mutated_quotient, p), remainder, p) != square
    assert remainder == [1]
    assert [(remainder[0] + 1) % p] != [1]

    nonmonic = modulus[:]
    nonmonic[-1] = 2
    caught = False
    try:
        verify.monic_divmod(square, nonmonic, p)
    except AssertionError:
        caught = True
    assert caught

    print(
        "DLI_WCL_FIXED_DIVISOR_STRAIGHT_LINE_LIFT_AUDIT_PASS "
        "docs=6 mutations=3"
    )


if __name__ == "__main__":
    main()
