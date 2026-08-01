#!/usr/bin/env python3
"""Exact common-stage exclusion router for one-loop 433 cell 11."""

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


def even_t_to_x(expression, t, x, other_variables):
    output = 0
    for powers, coefficient in sp.Poly(
        expression, t, *other_variables, modulus=P
    ).terms():
        require(powers[0] % 2 == 0, "odd product power")
        output += int(coefficient)*x**(powers[0]//2)*sp.prod(
            variable**power
            for variable, power in zip(other_variables, powers[1:])
        )
    return output


def strip(expression, factors, variables):
    return ATLAS.BASE.strip_factors(expression, factors, variables)


def routed_numerator(expression, variable, value):
    return sp.cancel(expression.subs(variable, value)).as_numer_denom()[0]


def linear_root(factor, variable):
    coefficients = sp.Poly(factor, variable, modulus=P).all_coeffs()
    return (
        -int(coefficients[1])
        *pow(int(coefficients[0]) % P, -1, P)
    ) % P


def only_b_guards(polynomial, b):
    residual = strip(polynomial.as_expr(), (b, b-1, b+1), (b,))
    return sp.Poly(residual, b, modulus=P).degree() == 0


def compile_sign_row(epsilon_1, epsilon_2):
    variables, equations, _ = ATLAS.compile_cell(11, epsilon_1, epsilon_2)
    t, r, c, b = variables
    x = sp.symbols("x")
    target_guards = (
        b, c, r, b-1, b+1, c-1, c+1, b-c, b+c,
        b*c-1, b*c+1, r-1, r+1, r-IOTA, r+IOTA,
    )
    all_guards = target_guards+(
        t, t-1, t+1, t-IOTA, t+IOTA,
        r-t, r+t, r-IOTA*t, r+IOTA*t,
    )
    r_guards = (r, r-1, r+1, r-IOTA, r+IOTA)
    br_guards = (b, b-1, b+1)+r_guards

    q_rows = tuple(
        strip(value, all_guards, variables) for value in equations[2:]
    )
    q_moving = next(value for value in q_rows if sp.degree(value, t) > 0)
    q_static = next(value for value in q_rows if sp.degree(value, t) == 0)
    require(sp.degree(q_moving, t) == 2, "moving q degree")
    require(sp.degree(q_static, c) == 1, "static q c degree")

    product_rows = tuple(
        strip(
            even_t_to_x(value, t, x, (r, c, b)),
            target_guards, (x, b, c, r),
        )
        for value in equations[:2]
    )
    product_moving = next(
        value for value in product_rows if sp.degree(value, x) == 1
    )
    product_static = next(
        value for value in product_rows if sp.degree(value, x) == 0
    )
    x_coefficient = sp.diff(product_moving, x)
    x_constant = product_moving.subs(x, 0)
    product_branch = sp.resultant(x_coefficient, x_constant, c)
    product_branch = strip(product_branch, br_guards, (b, r))
    require(
        sp.Poly(product_branch, b, r, modulus=P).total_degree() == 0,
        "product lost degree branch",
    )

    c_coefficient = sp.diff(q_static, c)
    c_constant = q_static.subs(c, 0)
    c_branch = sp.resultant(c_coefficient, c_constant, b)
    c_branch = strip(c_branch, r_guards, (r,))
    require(sp.Poly(c_branch, r, modulus=P).degree() == 0, "q c branch")
    c_value = -c_constant/c_coefficient

    product_q_compatibility = sp.resultant(
        product_static, q_static, c
    )
    product_q_compatibility = strip(
        product_q_compatibility, br_guards, (b, r)
    )
    require(
        sp.degree(product_q_compatibility, b) == 2
        and sp.degree(product_q_compatibility, r) == 4,
        "product-q compatibility",
    )

    q_polynomial = sp.Poly(q_moving, t)
    q2 = q_polynomial.coeff_monomial(t**2)
    q1 = q_polynomial.coeff_monomial(t)
    q0 = q_polynomial.coeff_monomial(1)
    t_coefficient = q1*x_coefficient
    t_constant = q0*x_coefficient-q2*x_constant
    routed_t_coefficient = routed_numerator(
        t_coefficient, c, c_value
    )
    routed_t_constant = routed_numerator(t_constant, c, c_value)

    q_branch_projections = []
    for branch_value in (routed_t_coefficient, routed_t_constant):
        projection = sp.resultant(
            product_q_compatibility, branch_value, b
        )
        projection = strip(projection, r_guards, (r,))
        q_branch_projections.append(sp.Poly(projection, r, modulus=P))
    q_branch = sp.gcd(*q_branch_projections)
    q_factors = sp.factor_list(q_branch.as_expr(), modulus=P)[1]
    require(
        len(q_factors) == 4
        and all(sp.Poly(factor, r, modulus=P).degree() == 1
                for factor, _ in q_factors),
        "q branch factors",
    )
    for factor, _ in q_factors:
        r_value = linear_root(factor, r)
        candidate = sp.gcd(
            sp.Poly(product_q_compatibility.subs(r, r_value), b, modulus=P),
            sp.Poly(routed_t_coefficient.subs(r, r_value), b, modulus=P),
        )
        candidate = sp.gcd(
            candidate,
            sp.Poly(routed_t_constant.subs(r, r_value), b, modulus=P),
        ).monic()
        require(only_b_guards(candidate, b), "q branch target guard")

    square_compatibility = strip(
        t_constant**2*x_coefficient
        +x_constant*t_coefficient**2,
        target_guards, (b, c, r),
    )
    routed_square = routed_numerator(square_compatibility, c, c_value)
    final_resultant = sp.resultant(
        product_q_compatibility, routed_square, b
    )
    final_resultant = strip(final_resultant, r_guards, (r,))
    final_factors = sp.factor_list(final_resultant, modulus=P)[1]
    degree_pattern = sorted(
        (sp.Poly(factor, r, modulus=P).degree(), multiplicity)
        for factor, multiplicity in final_factors
    )
    require(
        degree_pattern == [(1, 1), (1, 3), (1, 10), (1, 10),
                           (2, 2), (4, 2)],
        f"terminal factor pattern {degree_pattern}",
    )
    for factor, _ in final_factors:
        if sp.Poly(factor, r, modulus=P).degree() != 1:
            continue
        r_value = linear_root(factor, r)
        candidate = sp.gcd(
            sp.Poly(product_q_compatibility.subs(r, r_value), b, modulus=P),
            sp.Poly(routed_square.subs(r, r_value), b, modulus=P),
        ).monic()
        require(only_b_guards(candidate, b), "terminal target guard")

    nonlinear = tuple(
        sp.Poly(factor, r, modulus=P).monic().as_expr()
        for factor, _ in final_factors
        if sp.Poly(factor, r, modulus=P).degree() > 1
    )
    return nonlinear


def verify():
    warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)
    rows = {}
    for epsilon_1, epsilon_2 in itertools.product((1, -1), repeat=2):
        rows[(epsilon_1, epsilon_2)] = compile_sign_row(
            epsilon_1, epsilon_2
        )
    return rows


def main():
    rows = verify()
    print(
        "RATE_HALF_KB_ONE_LOOP_433_CELL11_ROUTER_PASS "
        f"sign_rows={len(rows)} guarded_linear_branches=16 "
        "irreducible_quadratics=4 irreducible_quartics=4"
    )


if __name__ == "__main__":
    main()
