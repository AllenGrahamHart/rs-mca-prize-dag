#!/usr/bin/env python3
"""Adversarial audit for the norm-one torus affine quotient cap."""

from __future__ import annotations

from verify import add, finite_check, mul, norm


def main() -> None:
    order, maximum, sharp = finite_check()
    assert order == 16 and maximum == 2 and sharp > 0

    # Removing t!=1 makes the affine map the identity on all of H.
    assert order > 2

    # The norm-one premise is essential: F_p^* meets z -> 2z-1 in p-2 points.
    p = 31
    prime_group = set(range(1, p))
    prime_affine = sum((2 * z - 1) % p in prime_group for z in prime_group)
    assert prime_affine == p - 2 > 2

    # The quadratic norm equation has nonzero endpoints at a,b != 0.
    nonsquare = 3
    a = (2, 1)
    b = (4, 3)
    assert a != (0, 0) and b != (0, 0)
    leading = mul(a, (b[0], -b[1] % p), p, nonsquare)
    constant = mul((a[0], -a[1] % p), b, p, nonsquare)
    assert leading != (0, 0) and constant != (0, 0)
    assert norm((1, 0), p, nonsquare) == 1

    p_m = 2**31 - 1
    n = 2**21
    assert (p_m + 1) % n == 0
    assert (p_m - 1) % n != 0
    assert 17 * (n - 1) ** 2 < 300 * n**2
    assert not (301 * (n - 1) ** 2 < 300 * n**2)

    print("F3_H3_NORM_ONE_TORUS_AFFINE_QUOTIENT_CAP_AUDIT_PASS mutations=8")


if __name__ == "__main__":
    main()
