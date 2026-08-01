#!/usr/bin/env python3
"""Exact deployed-field router for one-loop 433 common cell 0."""

import importlib.util
import itertools
from pathlib import Path
import warnings

import sympy as sp
from sympy.utilities.exceptions import SymPyDeprecationWarning


ROOT = Path(__file__).resolve().parents[2]
ATLAS_PATH = ROOT / (
    "experiments/prize_resolution/rate_half_kb_one_loop_433_common_atlas.py"
)
SPEC = importlib.util.spec_from_file_location("atlas", ATLAS_PATH)
ATLAS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ATLAS)
P = ATLAS.PRIME
IOTA = ATLAS.IOTA


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def monic(expression, variables):
    return sp.Poly(expression, *variables, modulus=P).monic()


def even_t_to_x(expression, t, x, other_variables):
    polynomial = sp.Poly(expression, t, *other_variables, modulus=P)
    output = 0
    for powers, coefficient in polynomial.terms():
        require(powers[0] % 2 == 0, "odd t power")
        output += int(coefficient)*x**(powers[0]//2)*sp.prod(
            variable**power
            for variable, power in zip(other_variables, powers[1:])
        )
    return output


def q_branch(epsilon_1, epsilon_2, sign):
    variables, equations, _ = ATLAS.compile_cell(0, epsilon_1, epsilon_2)
    t, r, c, b = variables
    q_values = []
    for equation in equations[2:]:
        polynomial = sp.Poly(equation, *variables, modulus=P)
        polynomial = polynomial.exquo(sp.Poly(b+1, *variables, modulus=P))
        polynomial = polynomial.exquo(sp.Poly(c+1, *variables, modulus=P))
        q_values.append(polynomial.as_expr())
    q_resultant = sp.resultant(q_values[0], q_values[1], r)
    expected_q = (b**2-1)*(c**2-1)*(b*c-IOTA)*(b*c+IOTA)
    require(
        monic(q_resultant, (b, c)) == monic(expected_q, (b, c)),
        "q resultant",
    )

    c_value = sign*IOTA/b
    routed_q = [
        sp.cancel(value.subs(c, c_value)).as_numer_denom()[0]
        for value in q_values
    ]
    q_gcd = sp.gcd(
        sp.Poly(routed_q[0], r, b, modulus=P),
        sp.Poly(routed_q[1], r, b, modulus=P),
    ).monic()
    r_values = {
        (1, 1, 1): b,
        (1, 1, -1): 1/b,
        (1, -1, 1): IOTA/b,
        (1, -1, -1): IOTA*b,
        (-1, 1, 1): -IOTA*b,
        (-1, 1, -1): -IOTA/b,
        (-1, -1, 1): 1/b,
        (-1, -1, -1): b,
    }
    r_value = r_values[(epsilon_1, epsilon_2, sign)]
    r_numerator = sp.cancel(r-r_value).as_numer_denom()[0]
    require(q_gcd == monic(r_numerator, (r, b)), "q branch root")

    x = sp.symbols("x")
    product_values = []
    for equation in equations[:2]:
        in_x = even_t_to_x(equation, t, x, (r, c, b))
        routed = sp.cancel(
            in_x.subs({c: c_value, r: r_value})
        ).as_numer_denom()[0]
        product_values.append(routed)
    resultant = sp.resultant(product_values[0], product_values[1], x)
    quartics = (
        b**4-(1+IOTA)*b**3+(1-IOTA)*b-1,
        b**4+(-1+IOTA)*b**3+(1+IOTA)*b-1,
        b**4+(1+IOTA)*b**3+(-1+IOTA)*b-1,
        b**4+(1-IOTA)*b**3+(-1-IOTA)*b-1,
    )
    quartic_index = {
        (1, 1, 1): 0,
        (1, 1, -1): 1,
        (1, -1, 1): 2,
        (1, -1, -1): 3,
        (-1, 1, 1): 2,
        (-1, 1, -1): 3,
        (-1, -1, 1): 0,
        (-1, -1, -1): 1,
    }[(epsilon_1, epsilon_2, sign)]
    residual = sp.Poly(resultant, b, modulus=P)
    for factor in (b-1, b+1, b-IOTA, b+IOTA):
        divisor = sp.Poly(factor, b, modulus=P)
        while True:
            quotient, remainder = sp.div(residual, divisor)
            if not remainder.is_zero:
                break
            residual = quotient
    require(
        residual.monic() == monic(quartics[quartic_index], (b,)),
        "product quartic",
    )
    factors = sp.factor_list(residual.as_expr(), modulus=P)[1]
    require(
        len(factors) == 2
        and all(sp.Poly(factor, b, modulus=P).degree() == 2
                and multiplicity == 1 for factor, multiplicity in factors),
        "quartic has a base-field root",
    )
    return quartic_index, tuple(
        tuple(int(value) % P for value in sp.Poly(factor, b, modulus=P).all_coeffs())
        for factor, _ in factors
    )


def verify():
    warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)
    rows = []
    for epsilon_1, epsilon_2, sign in itertools.product((1, -1), repeat=3):
        rows.append(q_branch(epsilon_1, epsilon_2, sign))
    require({index for index, _ in rows} == set(range(4)), "quartic coverage")
    return rows


def main():
    warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)
    rows = verify()
    print(
        "RATE_HALF_KB_ONE_LOOP_433_CELL0_PASS "
        f"branches={len(rows)} quartics=4 linear_factors=0"
    )


if __name__ == "__main__":
    main()
