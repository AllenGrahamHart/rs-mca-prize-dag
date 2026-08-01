#!/usr/bin/env python3
"""Exact common-stage exclusion router for one-loop 433 cell 4."""

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


def guard_residual(expression, factors, variables):
    residual = ATLAS.BASE.strip_factors(expression, factors, variables)
    return sp.Poly(residual, *variables, modulus=P)


def compile_sign_row(epsilon_1, epsilon_2):
    variables, equations, _ = ATLAS.compile_cell(4, epsilon_1, epsilon_2)
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

    q_rows = tuple(
        ATLAS.BASE.strip_factors(value, all_guards, variables)
        for value in equations[2:]
    )
    require(all(sp.degree(value, t) == 1 for value in q_rows), "linear q")
    q_coefficient = sp.diff(q_rows[0], t)
    q_constant = q_rows[0].subs(t, 0)
    q_compatibility = sp.resultant(q_rows[0], q_rows[1], t)
    for elimination_variable, remaining_variable in ((b, c), (c, b)):
        branch = sp.resultant(
            q_coefficient, q_constant, elimination_variable
        )
        residual = guard_residual(
            branch,
            (remaining_variable, remaining_variable-1,
             remaining_variable+1, r, r-1, r+1, r-IOTA, r+IOTA),
            (remaining_variable, r),
        )
        require(residual.total_degree() == 0, "q coefficient branch")

    product_rows = tuple(
        even_t_to_x(value, t, x, (r, c, b)) for value in equations[:2]
    )
    product_coefficient = sp.diff(product_rows[0], x)
    product_constant = product_rows[0].subs(x, 0)
    for elimination_variable, remaining in ((b, (c, r)), (c, (b, r))):
        remaining_target = remaining[0]
        branch = sp.resultant(
            product_coefficient, product_constant, elimination_variable
        )
        residual = guard_residual(
            branch,
            (remaining_target, remaining_target-1, remaining_target+1,
             r, r-1, r+1, r-IOTA, r+IOTA),
            remaining,
        )
        require(residual.total_degree() == 0, "product coefficient branch")

    product_compatibility = ATLAS.BASE.strip_factors(
        sp.resultant(product_rows[0], product_rows[1], x),
        target_guards, (b, c, r),
    )
    square_compatibility = ATLAS.BASE.strip_factors(
        q_constant**2*product_coefficient
        +product_constant*q_coefficient**2,
        target_guards, (b, c, r),
    )
    require(sp.degree(product_compatibility, c) == 1, "product c degree")
    require(sp.degree(square_compatibility, c) == 0, "square c degree")

    c_coefficient = sp.diff(product_compatibility, c)
    c_constant = product_compatibility.subs(c, 0)
    c_branch = sp.resultant(c_coefficient, c_constant, b)
    c_residual = guard_residual(
        c_branch, (r, r-1, r+1, r-IOTA, r+IOTA), (r,)
    )
    require(c_residual.degree() == 0, "product c branch")

    c_value = -c_constant/c_coefficient
    routed_q = sp.cancel(
        q_compatibility.subs(c, c_value)
    ).as_numer_denom()[0]
    final_resultant = sp.resultant(
        routed_q, square_compatibility, b
    )
    final_residual = guard_residual(
        final_resultant, (r, r-1, r+1, r-IOTA, r+IOTA), (r,)
    )
    factors = sp.factor_list(final_residual.as_expr(), modulus=P)[1]
    require(
        len(factors) == 1
        and sp.Poly(factors[0][0], r, modulus=P).degree() == 3
        and factors[0][1] == 2,
        "irreducible cubic square",
    )
    return sp.Poly(factors[0][0], r, modulus=P).monic().as_expr()


def verify():
    warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)
    cubics = {}
    for epsilon_1, epsilon_2 in itertools.product((1, -1), repeat=2):
        cubics[(epsilon_1, epsilon_2)] = compile_sign_row(
            epsilon_1, epsilon_2
        )
    require(len(set(map(str, cubics.values()))) == 4, "cubic sign rows")
    return cubics


def main():
    cubics = verify()
    print(
        "RATE_HALF_KB_ONE_LOOP_433_CELL4_ROUTER_PASS "
        f"sign_rows={len(cubics)} irreducible_cubics={len(cubics)}"
    )


if __name__ == "__main__":
    main()
