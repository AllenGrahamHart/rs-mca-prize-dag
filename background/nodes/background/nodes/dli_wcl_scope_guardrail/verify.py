#!/usr/bin/env python3
"""Exact audit of the isolated-row counterexample and its scope separation."""

from __future__ import annotations

from fractions import Fraction
from math import gcd


Q = 65537
NP = 512
N = 256
ELL = 1


def shifted_vector(shift: int) -> tuple[int, ...]:
    coeffs = [0] * N
    for exponent, sign in ((0, 1), (95, 1), (146, -1)):
        reduced = (exponent + shift) % NP
        if reduced >= N:
            reduced -= N
            sign = -sign
        coeffs[reduced] += sign
    return tuple(coeffs)


def main() -> None:
    # Complete-factor Pocklington certificate and primitive-root pin.
    assert Q - 1 == 2**16
    assert pow(3, Q - 1, Q) == 1
    assert gcd(pow(3, (Q - 1) // 2, Q) - 1, Q) == 1
    assert pow(3, (Q - 1) // 2, Q) == Q - 1

    omega = pow(3, (Q - 1) // NP, Q)
    assert omega == 15028
    assert pow(omega, NP, Q) == 1
    assert pow(omega, N, Q) == Q - 1

    terms = (1, pow(omega, 95, Q), -pow(omega, 146, Q))
    assert sum(terms) % Q == 0
    assert all(term % Q for term in terms)
    assert all((terms[i] + terms[j]) % Q for i in range(3) for j in range(i + 1, 3))
    assert all(pow(omega, d, Q) not in (1, Q - 1) for d in range(1, N))

    orbit = {shifted_vector(shift) for shift in range(NP)}
    assert len(orbit) == 2 * N
    assert all(sum(value != 0 for value in vector) == 3 for vector in orbit)

    charge = Fraction(2 * N, 2**3)
    assert charge == 64 and charge > Fraction(1, 32)

    assert (Q - 1) % NP == 0
    assert 2**N >= Q**ELL
    assert N >= 16 * ELL
    assert (Q - 1) % 2**41 != 0
    assert (Q - 1 & -(Q - 1)).bit_length() - 1 == 16

    print(
        "DLI_WCL_SCOPE_GUARDRAIL_PASS "
        f"q={Q} order={NP} weight=3 orbit={len(orbit)} charge={charge} "
        "ambient_split=false"
    )


if __name__ == "__main__":
    main()
