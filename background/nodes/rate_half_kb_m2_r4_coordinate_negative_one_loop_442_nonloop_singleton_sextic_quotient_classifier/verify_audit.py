#!/usr/bin/env python3
"""Audit the other sextic sign rows and the retained finite witness."""

import importlib.util
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("primary", NODE / "verify.py")
PRIMARY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PRIMARY)


def main():
    b, c, r, t = sp.symbols("b c r t")
    sextic = b**6-2*b**5+7*b**4-8*b**3+7*b**2-2*b+1
    expected_leaders = {
        "t**0*r**1*b**2", "t**0*r**0*b**3", "t**2*r**0*b**0",
        "t**1*r**1*b**0", "t**0*r**2*b**0", "t**1*r**0*b**1",
    }
    monomials = (1, b, b**2, r, r*b, t)
    exponents = ((0, 0, 0), (0, 0, 1), (0, 0, 2),
                 (0, 1, 0), (0, 1, 1), (1, 0, 0))

    for epsilon_1, epsilon_2 in ((1, -1), (-1, 1), (-1, -1)):
        cubic, product, weld, denominator = PRIMARY.common_generators(
            epsilon_1, epsilon_2, b, c, r, t
        )
        basis = PRIMARY.quotient_basis(
            (cubic, sextic, product, weld), (t, r, b)
        )
        if len(basis.polys) != 6 or not basis.is_zero_dimensional:
            raise RuntimeError("sextic sign basis")
        if {str(poly.LM(order=basis.order)) for poly in basis.polys} != expected_leaders:
            raise RuntimeError("sextic sign leaders")

        def vector(expression):
            remainder = sp.Poly(basis.reduce(expression)[1], t, r, b,
                                modulus=PRIMARY.PRIME)
            terms = {power: int(value) % PRIMARY.PRIME
                     for power, value in remainder.terms()}
            return [terms.get(power, 0) for power in exponents]

        matrix = sp.Matrix.hstack(*(
            sp.Matrix(vector(denominator*monomial))
            for monomial in monomials
        ))
        if int(matrix.det()) % PRIMARY.PRIME != 2**19:
            raise RuntimeError("sextic sign denominator")

    # The F_41 witness retained by the parent lies on the sextic.
    if (10**6-2*10**5+7*10**4-8*10**3+7*10**2-2*10+1) % 41:
        raise RuntimeError("retained sextic witness")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_SEXTIC_AUDIT_PASS "
        "other_sign_rows=3 rank=6 denominator_norm=2^19 witness_field=41"
    )


if __name__ == "__main__":
    main()
