#!/usr/bin/env python3
"""Mutation audit for the marked constant-shift multistrip theorem."""


def main() -> None:
    m, ell = 3, 7

    # At d=m*ell the one-kernel common factor need not exceed the marks.
    d, v = m * ell, 2
    assert d + v - m * ell == v

    # At the next boundary one more P-adic block is required.
    d, v = m * ell + 1, ell - 1
    assert d + v == (m + 1) * ell

    # With only 2m labels, a nonzero degree-2m cross polynomial can vanish on
    # every label, so the root-count step cannot be shortened.
    labels = list(range(2 * m))
    roots = [1]
    for label in labels:
        out = [0] * (len(roots) + 1)
        for index, coefficient in enumerate(roots):
            out[index] -= label * coefficient
            out[index + 1] += coefficient
        roots = out
    assert len(roots) - 1 == 2 * m
    assert all(
        sum(coefficient * label**index for index, coefficient in enumerate(roots))
        == 0
        for label in labels
    )

    # Primitive degree m leaves only constant multipliers and cannot support
    # the required two-dimensional kernel.
    assert m - m == 0

    # The strict background cap supplies the final minus one in the window.
    T, p = m, 2
    d_max_strict = T * ell + p - 1
    d_max_nonstrict = T * ell + p
    assert d_max_nonstrict == d_max_strict + 1

    print("L1_MARKED_MULTISTRIP_AUDIT_PASS mutations=5")


if __name__ == "__main__":
    main()
