#!/usr/bin/env python3
"""
Exact checks for the DLI-CLOSE-4 fulfilment note.

This script verifies two things:

1. The printed orbit-decomposition upper bound
       E <= (q^L / 2^N) * (1 + K * 2N * 2^-(L+1))
   cannot be correct as a bound for E itself.  A valid R* row
   (q=65537, n'=512, L=1, N=256) has a weight-3 vanishing ternary
   orbit, but even the gross maximum possible number of weight-3
   signed reduced elements gives a right-hand side < 1, while E >= 1
   from the lambda=0 Fourier term.

2. The corrected conditional aggregate arithmetic for the 34-level
   production schedule L=1..34: if the effective shadow-closed generator
   multiplicity M_L is uniformly bounded by M, then
       sum_L log2(1 + M * 256L / 2^L)
   is <= 100 for M <= 13.2907840779..., and equals about 51.16997
   for M=1 and 79.70215 for M=5.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, gcd, log2


def pocklington_65537() -> None:
    q = 65537
    a = 3
    # q - 1 = 2^16; F = 2^16 > sqrt(q), and 2 is the only prime divisor of F.
    assert q - 1 == 2**16
    assert (2**16) ** 2 > q
    assert pow(a, q - 1, q) == 1
    assert gcd(pow(a, (q - 1) // 2, q) - 1, q) == 1


def smallest_primitive_root_prime_q(q: int) -> int:
    # q=65537, q-1 is a power of two, so g is primitive iff g^((q-1)/2)=-1.
    for g in range(2, q):
        if pow(g, (q - 1) // 2, q) == q - 1:
            return g
    raise RuntimeError("no primitive root found")


def check_literal_bound_failure() -> None:
    q = 65537
    nprime = 512
    N = nprime // 2
    L = 1
    assert q < 2**256
    assert (q - 1) % nprime == 0
    assert 2**N >= q**L

    pocklington_65537()
    g = smallest_primitive_root_prime_q(q)
    assert g == 3
    omega = pow(g, (q - 1) // nprime, q)
    assert omega == 15028
    assert pow(omega, nprime, q) == 1
    assert pow(omega, N, q) == q - 1
    assert (1 + pow(omega, 95, q) - pow(omega, 146, q)) % q == 0

    # Since L=1, this is a primitive weight-3 first-moment relation.
    # The number K of minimal weight-3 orbits is certainly no larger than
    # the number of signed reduced weight-3 ternary elements.
    K_upper = (2**3) * comb(N, 3)
    orbit_factor = Fraction(2 * N, 2 ** (L + 1))  # 2N * 2^-(L+1) = 128
    rhs_upper = Fraction(q**L, 2**N) * (1 + K_upper * orbit_factor)

    # But E is a Fourier mass with the lambda=0 term equal to 1.
    assert rhs_upper < 1
    print("literal-bound check")
    print(f"  q={q}, n'={nprime}, N={N}, L={L}, omega={omega}")
    print("  relation: 1 + omega^95 - omega^146 == 0 mod q")
    print(f"  gross K_upper={K_upper}")
    print(f"  RHS upper using gross K_upper = {rhs_upper}")
    print(f"  RHS upper as log2 = {log2(rhs_upper.numerator) - log2(rhs_upper.denominator):.6f}")
    print("  E >= 1 from the lambda=0 term, so the printed upper bound cannot bound E itself.")


def aggregate_sum(M: float) -> float:
    return sum(log2(1.0 + M * 256.0 * L / (2.0**L)) for L in range(1, 35))


def conditional_constants() -> None:
    lo, hi = 0.0, 100.0
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if aggregate_sum(mid) <= 100.0:
            lo = mid
        else:
            hi = mid
    print("\nconditional aggregate constants")
    for M in [1.0, 5.0, 10.0, 13.0, lo, 14.0]:
        print(f"  M={M:.12g}: sum={aggregate_sum(M):.12f} bits")
    print(f"  threshold M*={lo:.12f}")


if __name__ == "__main__":
    check_literal_bound_failure()
    conditional_constants()
