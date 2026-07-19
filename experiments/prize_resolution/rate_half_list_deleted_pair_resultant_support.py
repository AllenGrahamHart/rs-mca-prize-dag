#!/usr/bin/env python3
"""Tiny exact route diagnostic for the deleted-pair univariate gate.

This checks only M=1,...,5 and has no theorem or transport claim.
"""

from __future__ import annotations

import math

import sympy as sym


T = sym.symbols("t")
EXPECTED = {
    1: set(),
    2: {5, 7},
    3: {3, 5, 11},
    4: {3, 5, 11, 13},
    5: {3, 13, 17, 19},
}


def resultant_support(m_value: int) -> set[int]:
    coefficients = [sym.Integer(1)]
    for degree in range(1, 3 * m_value + 2):
        previous_two = coefficients[degree - 2] if degree >= 2 else 0
        coefficients.append(
            sym.cancel(
                (
                    (4 * degree - 3) * (1 + T) * coefficients[degree - 1]
                    - (4 * degree - 6) * T * previous_two
                )
                / (4 * degree)
            )
        )

    primary = sym.Poly(coefficients[2 * m_value], T, domain=sym.QQ)
    low = coefficients[: m_value + 1]
    tail = coefficients[2 * m_value + 1 : 3 * m_value + 2]
    square = [
        sum(low[index] * tail[degree - index] for index in range(degree + 1))
        / coefficients[2 * m_value + 1]
        for degree in range(m_value + 1)
    ]
    root = [sym.Integer(1)]
    for degree in range(1, m_value + 1):
        cross = sum(root[index] * root[degree - index] for index in range(1, degree))
        root.append(sym.cancel((square[degree] - cross) / 2))
    secondary_numerator = sym.cancel(root[m_value]).as_numer_denom()[0]

    torsion_resultant = sym.cancel(
        sym.resultant(primary.as_expr(), T ** (8 * m_value) - 1, T)
    ).as_numer_denom()[0]
    secondary_resultant = sym.cancel(
        sym.resultant(primary.as_expr(), secondary_numerator, T)
    ).as_numer_denom()[0]
    common = abs(math.gcd(int(torsion_resultant), int(secondary_resultant)))
    return set(sym.factorint(common))


def main() -> None:
    observed = {m_value: resultant_support(m_value) for m_value in EXPECTED}
    assert observed == EXPECTED
    assert all(
        all(prime <= 4 * m_value - 1 for prime in support)
        for m_value, support in observed.items()
    )
    compact = ";".join(
        f"M={m_value}:{','.join(map(str, sorted(support))) or '-'}"
        for m_value, support in observed.items()
    )
    print(f"RATE_HALF_DELETED_PAIR_RESULTANT_SUPPORT_PASS {compact}")


if __name__ == "__main__":
    main()
