#!/usr/bin/env python3
"""Audit the mate-denominator norm in the other sextic sign rows."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("primary", NODE / "verify.py")
PRIMARY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PRIMARY)


def main():
    for epsilon_1, epsilon_2 in ((1, -1), (-1, 1), (-1, -1)):
        b, r, t, d_c, vector, polynomial, matrix = PRIMARY.quotient_data(
            epsilon_1, epsilon_2
        )
        x = r**2
        a_poly = x**2-6*x+1
        b_poly = (x+1)**2
        c_numerator = b*(b*a_poly+b_poly)
        c_coordinates = (
            matrix(d_c).inv_mod(PRIMARY.PARENT.PRIME)*vector(c_numerator)
        ) % PRIMARY.PARENT.PRIME
        c_value = polynomial(c_coordinates)
        d_m = b**3-b**2*c_value+3*b*c_value+c_value**2
        if int(matrix(d_m).det()) % PRIMARY.PARENT.PRIME != 652:
            raise RuntimeError("mate denominator sign row")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_MATE_AUDIT_PASS "
        "other_sign_rows=3 mate_norm=652"
    )


if __name__ == "__main__":
    main()
