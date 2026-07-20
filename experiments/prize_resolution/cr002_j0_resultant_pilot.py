#!/usr/bin/env python3
"""Small exact normalization controls for deferred compute request CR-002-J0."""

from __future__ import annotations

import json

import sympy as sp


EXPECTED = {
    1: {
        "minus": {23: 1},
        "plus": {},
    },
    2: {
        "minus": {3: 4, 47: 1, 39023: 1},
        "plus": {3: 3, 17: 1, 47: 1},
    },
    4: {
        "minus": {
            5: 8,
            7: 8,
            97: 1,
            641: 1,
            33247: 1,
            402078190242382847: 1,
        },
        "plus": {
            3: 1,
            5: 7,
            7: 9,
            13: 1,
            97: 1,
            182711: 1,
            258045217: 1,
        },
    },
}

SIZE_EXPECTED = {
    8: {"minus": 574, "plus": 500},
    16: {"minus": 2411, "plus": 2244},
    24: {"minus": 5475, "plus": 5248},
    32: {"minus": 9910, "plus": 9541},
}

OFFICIAL_M = 1 << 35


def primitive_resultant_numerator(primary: sp.Expr, torsion: sp.Expr, x: sp.Symbol) -> int:
    resultant = sp.cancel(sp.resultant(primary, torsion, x))
    numerator, denominator = sp.fraction(resultant)
    assert denominator > 0
    assert denominator & (denominator - 1) == 0
    return int(numerator)


def main() -> None:
    x = sp.symbols("x")
    rows = []
    for order, expected in EXPECTED.items():
        primary = sp.jacobi(order, sp.Rational(-1, 4), sp.Rational(-1, 2), x)
        torsion = {
            "minus": sp.chebyshevt(2 * order, x),
            "plus": sp.chebyshevu(2 * order - 1, x),
        }
        row: dict[str, object] = {"M": order}
        for sign, polynomial in torsion.items():
            numerator = primitive_resultant_numerator(primary, polynomial, x)
            factors = {int(p): int(v) for p, v in sp.factorint(abs(numerator)).items()}
            assert factors == expected[sign]
            row[sign] = {"numerator": numerator, "factors": factors}
        rows.append(row)

    size_rows = []
    for order, expected in SIZE_EXPECTED.items():
        primary = sp.jacobi(order, sp.Rational(-1, 4), sp.Rational(-1, 2), x)
        torsion = {
            "minus": sp.chebyshevt(2 * order, x),
            "plus": sp.chebyshevu(2 * order - 1, x),
        }
        bit_lengths = {
            sign: abs(
                primitive_resultant_numerator(primary, polynomial, x)
            ).bit_length()
            for sign, polynomial in torsion.items()
        }
        assert bit_lengths == expected
        size_rows.append({"M": order, "numerator_bits": bit_lengths})

    # This is an empirical size extrapolation, not a theorem about the
    # official resultant. It only route-fences explicit materialization.
    projected_bits = {
        sign: (SIZE_EXPECTED[32][sign] * OFFICIAL_M * OFFICIAL_M) // (32 * 32)
        for sign in ("minus", "plus")
    }

    print(json.dumps({
        "request": "CR-002-J0",
        "factor_rows": rows,
        "size_rows": size_rows,
        "quadratic_extrapolation_bits": projected_bits,
    }, sort_keys=True))
    print("CR002_J0_RESULTANT_PILOT_PASS factor_rows=3 size_rows=4 signs=2")


if __name__ == "__main__":
    main()
