#!/usr/bin/env python3
"""Build a deployed one-loop 442 forced-record cell in two variables."""

import argparse
import functools
import importlib.util
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
MATE_PATH = ROOT / (
    "background/nodes/"
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_"
    "nonloop_singleton_sextic_mate_coordinate_compiler/verify.py"
)
SPEC = importlib.util.spec_from_file_location("mate", MATE_PATH)
MATE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MATE)
SELECTOR_PATH = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_one_loop_442_sextic_row_selector.py"
)
SELECTOR_SPEC = importlib.util.spec_from_file_location("selector", SELECTOR_PATH)
SELECTOR = importlib.util.module_from_spec(SELECTOR_SPEC)
SELECTOR_SPEC.loader.exec_module(SELECTOR)
P = MATE.PARENT.PRIME
IOTA = MATE.PARENT.IOTA


@functools.lru_cache(maxsize=4)
def common_data(epsilon_1, epsilon_2):
    return MATE.quotient_data(epsilon_1, epsilon_2)


def poly_add(left, right):
    output = dict(left)
    for powers, coefficient in right.items():
        output[powers] = SELECTOR.add(output.get(powers, SELECTOR.ZERO),
                                     coefficient)
    return {powers: coefficient for powers, coefficient in output.items()
            if any(any(row) for row in coefficient)}


def poly_mul(left, right):
    output = {}
    for (d_left, s_left), first in left.items():
        for (d_right, s_right), second in right.items():
            powers = (d_left+d_right, s_left+s_right)
            term = SELECTOR.mul(first, second)
            output[powers] = SELECTOR.add(
                output.get(powers, SELECTOR.ZERO), term
            )
    return {powers: coefficient for powers, coefficient in output.items()
            if any(any(row) for row in coefficient)}


def poly_left_mul(value, polynomial):
    return {powers: SELECTOR.mul(value, coefficient)
            for powers, coefficient in polynomial.items()}


def binary_mul(left, right):
    output = [{} for _ in range(len(left)+len(right)-1)]
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            output[i+j] = poly_add(output[i+j], poly_mul(first, second))
    return output


def build(alpha_sign=1, cell="forced-de", delta_sign=-1, ef_sign=1,
          epsilon_1=1, epsilon_2=1):
    if alpha_sign not in (-1, 1):
        raise ValueError("alpha_sign must be +/-1")
    if delta_sign not in (-1, 1):
        raise ValueError("delta_sign must be +/-1")
    if ef_sign not in (-1, 1):
        raise ValueError("ef_sign must be +/-1")
    if cell not in ("forced-de", "forced-ce", "forced-ef",
                    "s2-forced-colored", "s2-forced-df", "s2-forced-ef",
                    "s2-forced-loop"):
        raise ValueError("unsupported cell")
    if epsilon_1 not in (-1, 1) or epsilon_2 not in (-1, 1):
        raise ValueError("common signs must be +/-1")
    b, r, t, d_c, vector, polynomial, matrix = common_data(
        epsilon_1, epsilon_2
    )
    d, s = sp.symbols("d s")
    x = r**2
    a_poly = x**2-6*x+1
    b_poly = (x+1)**2
    c_numerator = b*(b*a_poly+b_poly)
    c_coordinates = matrix(d_c).inv_mod(P)*vector(c_numerator)
    c_value = polynomial(c_coordinates % P)

    d_m = b**3-b**2*c_value+3*b*c_value+c_value**2
    mate_numerator = -b*(b**3+3*b**2*c_value-b*c_value+c_value**2)
    mate_coordinates = matrix(d_m).inv_mod(P)*vector(mate_numerator)
    mate_value = polynomial(mate_coordinates % P)

    b_matrix = SELECTOR.as_lists(matrix(b))
    c_multiplication = matrix(c_value)
    c_matrix = SELECTOR.as_lists(c_multiplication)
    c_inverse = SELECTOR.as_lists(c_multiplication.inv_mod(P))
    mate_matrix = SELECTOR.as_lists(matrix(mate_value))
    b_squared = SELECTOR.mul(b_matrix, b_matrix)
    alpha = SELECTOR.neg(SELECTOR.mul(
        b_matrix, SELECTOR.add(c_matrix, b_squared)
    ))
    beta = SELECTOR.mul(
        b_squared,
        SELECTOR.sub(
            SELECTOR.sub(c_matrix, b_squared),
            SELECTOR.scale(2, SELECTOR.mul(b_matrix, c_matrix)),
        ),
    )
    gamma = SELECTOR.sub(
        SELECTOR.add(c_matrix, SELECTOR.scale(2, b_matrix)), b_squared
    )
    delta = SELECTOR.add(SELECTOR.mul(alpha, alpha),
                         SELECTOR.mul(beta, gamma))
    powers = {
        "a": [SELECTOR.power(alpha, exponent) for exponent in range(7)],
        "b": [SELECTOR.power(beta, exponent) for exponent in range(7)],
        "g": [SELECTOR.power(gamma, exponent) for exponent in range(7)],
    }
    action = [[SELECTOR.ZERO for _ in range(7)] for _ in range(3)]
    for ell in range(3):
        for j in range(7):
            value = SELECTOR.ZERO
            for q in range(max(0, ell-(6-j)), min(ell, j)+1):
                p = ell-q
                term = SELECTOR.mul(
                    SELECTOR.mul(powers["a"][6-j-p], powers["b"][p]),
                    SELECTOR.mul(powers["g"][j-q], powers["a"][q]),
                )
                scalar = math.comb(6-j, p)*math.comb(j, q)
                if q % 2:
                    scalar = -scalar
                value = SELECTOR.add(value, SELECTOR.scale(scalar, term))
            if ell == j:
                value = SELECTOR.sub(value, SELECTOR.power(delta, 3))
            action[ell][j] = value

    constant = lambda value: {(0, 0): value}
    monomial = lambda d_power, s_power, value=SELECTOR.IDENTITY: {
        (d_power, s_power): value
    }
    if cell == "forced-de":
        factors = (
            (monomial(1, 0), constant(SELECTOR.scale(
                alpha_sign, SELECTOR.mul(c_matrix, mate_matrix)
            ))),
            (constant(SELECTOR.IDENTITY), monomial(1, 1, c_matrix)),
            (constant(SELECTOR.IDENTITY), monomial(2, 0)),
            (constant(SELECTOR.IDENTITY), monomial(
                2, 1, SELECTOR.neg(SELECTOR.IDENTITY)
            )),
            (constant(SELECTOR.IDENTITY), {}, monomial(
                0, 2, SELECTOR.neg(SELECTOR.mul(mate_matrix, mate_matrix))
            )),
        )
    elif cell == "forced-ce":
        mate_over_c = SELECTOR.mul(mate_matrix, c_inverse)
        factors = (
            (constant(SELECTOR.IDENTITY), monomial(0, 1, c_matrix)),
            (constant(SELECTOR.IDENTITY), monomial(2, 0)),
            (constant(SELECTOR.IDENTITY), monomial(
                1, 0, SELECTOR.neg(mate_over_c)
            )),
            (constant(SELECTOR.IDENTITY), monomial(
                1, 1, SELECTOR.scale(-delta_sign, SELECTOR.IDENTITY)
            )),
            (constant(SELECTOR.IDENTITY), {}, monomial(
                0, 2, SELECTOR.neg(SELECTOR.mul(mate_over_c, mate_over_c))
            )),
        )
    elif cell == "forced-ef":
        factors = (
            (monomial(0, 1), constant(SELECTOR.scale(
                ef_sign, SELECTOR.mul(c_matrix, mate_matrix)
            ))),
            (monomial(0, 1), monomial(
                1, 0, SELECTOR.scale(-delta_sign*ef_sign, mate_matrix)
            )),
            (constant(SELECTOR.IDENTITY), monomial(0, 1, c_matrix)),
            (constant(SELECTOR.IDENTITY), monomial(2, 0)),
            (constant(SELECTOR.IDENTITY), monomial(1, 1)),
            (constant(SELECTOR.IDENTITY), constant(mate_matrix)),
        )
    elif cell == "s2-forced-colored":
        mate_over_c = SELECTOR.mul(mate_matrix, c_inverse)
        factors = (
            (constant(SELECTOR.IDENTITY), constant(mate_matrix)),
            (constant(SELECTOR.IDENTITY), monomial(2, 0)),
            (constant(SELECTOR.IDENTITY), {}, monomial(
                0, 2, SELECTOR.neg(SELECTOR.mul(
                    mate_over_c, mate_over_c
                ))
            )),
            (constant(SELECTOR.IDENTITY), {}, monomial(
                2, 2, SELECTOR.neg(SELECTOR.IDENTITY)
            )),
        )
    elif cell == "s2-forced-df":
        c_squared = SELECTOR.mul(c_matrix, c_matrix)
        mate_squared = SELECTOR.mul(mate_matrix, mate_matrix)
        factors = (
            (constant(SELECTOR.IDENTITY), {}, monomial(
                2, 0, SELECTOR.neg(c_squared)
            )),
            (constant(SELECTOR.IDENTITY), monomial(0, 2)),
            (constant(SELECTOR.IDENTITY), constant(mate_matrix)),
            (monomial(2, 0), {}, monomial(
                0, 2, SELECTOR.neg(mate_squared)
            )),
        )
    elif cell == "s2-forced-ef":
        c_squared = SELECTOR.mul(c_matrix, c_matrix)
        mate_squared = SELECTOR.mul(mate_matrix, mate_matrix)
        factors = (
            (constant(SELECTOR.IDENTITY), {}, monomial(
                2, 0, SELECTOR.neg(c_squared)
            )),
            (constant(SELECTOR.IDENTITY), monomial(0, 2)),
            (monomial(0, 2), {}, monomial(
                2, 0, SELECTOR.neg(mate_squared)
            )),
            (constant(SELECTOR.IDENTITY), constant(mate_matrix)),
        )
    else:
        c_squared = SELECTOR.mul(c_matrix, c_matrix)
        factors = (
            (constant(SELECTOR.IDENTITY), {}, monomial(
                2, 0, SELECTOR.neg(c_squared)
            )),
            (constant(SELECTOR.IDENTITY), {}, monomial(
                2, 2, SELECTOR.neg(SELECTOR.IDENTITY)
            )),
            (constant(SELECTOR.IDENTITY), {}, monomial(
                0, 2, mate_matrix
            )),
        )
    coefficients = [constant(SELECTOR.IDENTITY)]
    for factor in factors:
        coefficients = binary_mul(coefficients, factor)

    matrix_equations = []
    for ell in range(3):
        equation = {}
        for j in range(7):
            equation = poly_add(
                equation, poly_left_mul(action[ell][j], coefficients[j])
            )
        matrix_equations.append(equation)

    equations = []
    for equation in matrix_equations:
        expression = 0
        for (d_power, s_power), coefficient in equation.items():
            coordinates = sp.Matrix([coefficient[index][0]
                                     for index in range(SELECTOR.SIZE)])
            quotient_value = sp.Poly(polynomial(coordinates), t, r, b,
                                     modulus=P).as_expr()
            expression += quotient_value*d**d_power*s**s_power
        equations.append(sp.Poly(expression, d, s, t, r, b,
                                 modulus=P).as_expr())

    inverse_2 = pow(2, -1, P)
    common_basis = (
        b**2*r+b**2+(IOTA-1)*b*r-(IOTA+1)*b+r+1,
        b**3-(IOTA+1)*b**2+(IOTA-1)*b*r+(IOTA+2)*b
        +(IOTA+1)*inverse_2*(r+t)-IOTA,
        t**2-IOTA*r-(2*IOTA+1)*t-(2*IOTA-1),
        r*t+IOTA,
        r**2+(IOTA+2)*r+t-(2*IOTA+1),
        (IOTA-1)*b**2+b*(r+t)-(IOTA-1)*b+(IOTA-1),
    )
    common_basis = tuple(sp.Poly(value, d, s, t, r, b,
                                 modulus=P).as_expr()
                         for value in common_basis)
    return (d, s, t, r, b), common_basis, equations, matrix_equations


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--groebner", action="store_true")
    parser.add_argument("--alpha-sign", type=int, choices=(-1, 1), default=1)
    parser.add_argument("--cell", choices=("forced-de", "forced-ce", "forced-ef",
                                            "s2-forced-colored", "s2-forced-df",
                                            "s2-forced-ef", "s2-forced-loop"),
                        default="forced-de")
    parser.add_argument("--delta-sign", type=int, choices=(-1, 1), default=-1)
    parser.add_argument("--ef-sign", type=int, choices=(-1, 1), default=1)
    parser.add_argument("--epsilon-1", type=int, choices=(-1, 1), default=1)
    parser.add_argument("--epsilon-2", type=int, choices=(-1, 1), default=1)
    arguments = parser.parse_args()
    variables, common_basis, equations, _ = build(
        arguments.alpha_sign, arguments.cell, arguments.delta_sign,
        arguments.ef_sign, arguments.epsilon_1, arguments.epsilon_2,
    )
    d, s, t, r, b = variables
    profiles = []
    for equation in equations:
        full_poly = sp.Poly(equation, d, s, t, r, b, modulus=P)
        outside_support = {(powers[0], powers[1])
                           for powers, _ in full_poly.terms()}
        profiles.append((
            full_poly.total_degree(), len(full_poly.terms()),
            max(power[0] for power in outside_support),
            max(power[1] for power in outside_support),
            len(outside_support),
            min(power[0] for power in outside_support),
            min(power[1] for power in outside_support),
        ))
    profiles = tuple(profiles)
    print(
        f"S1_DEPLOYED_CELL_BUILT cell={arguments.cell} "
        f"alpha_sign={arguments.alpha_sign} delta_sign={arguments.delta_sign} "
        f"ef_sign={arguments.ef_sign} "
        f"common_signs={arguments.epsilon_1},{arguments.epsilon_2} "
        f"profiles={profiles}", flush=True
    )
    if not arguments.groebner:
        return

    basis = sp.groebner(
        common_basis+tuple(equations), *variables,
        order="grevlex", method="f5b", modulus=P,
    )
    print(
        "S1_DEPLOYED_CELL_GROEBNER "
        f"unit={basis == [1]} zero_dimensional={basis.is_zero_dimensional} "
        f"basis_length={len(basis.polys)}",
        flush=True,
    )


if __name__ == "__main__":
    main()
