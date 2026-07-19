#!/usr/bin/env python3
"""Verify the E1 250-bit exhibit field by Pocklington's theorem."""

from __future__ import annotations

from math import gcd

C = 562949953421383
F = 1 << 200
P = 904625697166646869347790708689937759412227977745095982970820953353127723009
A = 3

RHO_128 = 440266185830122294862552098878717819794821358702875176198798016633729926114
RHO_256 = 368095729527972287347366462180303065908636718991804826343652948937354262881


def exact_order_power_check(rho: int, order: int) -> None:
    assert pow(rho, order, P) == 1
    assert pow(rho, order // 2, P) != 1


def main() -> None:
    assert P == C * F + 1
    assert P.bit_length() == 250
    assert P < (1 << 256)
    assert P % 256 == 1
    assert F * F > P

    # Pocklington with known factor F=2^200 of P-1 and base 3.
    assert pow(A, P - 1, P) == 1
    assert gcd(pow(A, (P - 1) // 2, P) - 1, P) == 1

    assert RHO_128 == pow(A, (P - 1) // 128, P)
    assert RHO_256 == pow(A, (P - 1) // 256, P)
    exact_order_power_check(RHO_128, 128)
    exact_order_power_check(RHO_256, 256)

    print("PASS: E1 250-bit Pocklington exhibit field")


if __name__ == "__main__":
    main()
