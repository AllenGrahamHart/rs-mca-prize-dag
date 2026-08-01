#!/usr/bin/env python3
"""Exact finite classifier for one-loop 433 common cells 3 and 6."""

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
B_POLYNOMIAL = (1, 278278958, 1)
B_ROOTS = (1375161449, 477266026)
R_ROWS = {
    (1, 1): 669515297,
    (1, -1): 1125500162,
    (-1, 1): 1461191136,
    (-1, -1): 1005206271,
}
T_ROWS = {
    (1, 1): 639982870,
    (1, -1): 1732861855,
    (-1, 1): 1490723563,
    (-1, -1): 397844578,
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def primitive(expression, variables):
    numerator = sp.cancel(expression).as_numer_denom()[0]
    return sp.Poly(numerator, *variables, modulus=P).monic().as_expr()


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


def h_polynomial(b, r, epsilon_1, epsilon_2):
    return (
        2*b**2*r**4+2*epsilon_2*IOTA*b**2*r**2+b*r**6
        +(-epsilon_1*epsilon_2+epsilon_1*IOTA)*b*r**5
        +3*epsilon_2*IOTA*b*r**4+3*b*r**2
        +(epsilon_1*epsilon_2-epsilon_1*IOTA)*b*r
        +epsilon_2*IOTA*b+2*r**4+2*epsilon_2*IOTA*r**2
    )


def k_polynomial(b, r, epsilon_1):
    return (
        4*b**4*r**4+2*b**3*r**6+4*epsilon_1*IOTA*b**3*r**5
        +4*b**3*r**4-4*epsilon_1*IOTA*b**3*r**3+2*b**3*r**2
        +b**2*r**8+2*epsilon_1*IOTA*b**2*r**7
        +2*epsilon_1*IOTA*b**2*r**5+6*b**2*r**4
        -2*epsilon_1*IOTA*b**2*r**3-2*epsilon_1*IOTA*b**2*r
        +b**2+2*b*r**6+4*epsilon_1*IOTA*b*r**5+4*b*r**4
        -4*epsilon_1*IOTA*b*r**3+2*b*r**2+4*r**4
    )


def root_polynomials(r, epsilon_1, epsilon_2):
    cubic = (
        r**3+(-epsilon_1*epsilon_2+2*epsilon_1*IOTA)*r**2
        +(1+2*epsilon_2*IOTA)*r-epsilon_1*epsilon_2
    )
    quartic = (
        r**4+(-epsilon_1*epsilon_2+epsilon_1*IOTA)*r**3-2*r**2
        +(-epsilon_1*epsilon_2-epsilon_1*IOTA)*r+1
    )
    return cubic, quartic


def reconstruct_c(b_value, r_value):
    capital_r = r_value*r_value % P
    numerator = (b_value*(capital_r*capital_r+1)+2*capital_r) % P
    denominator = (
        b_value*(capital_r*capital_r+1+2*capital_r*b_value)
    ) % P
    require(denominator != 0, "c denominator")
    return -numerator*pow(denominator, -1, P) % P


def compile_sign_row(epsilon_1, epsilon_2):
    variables, equations, metadata = ATLAS.compile_cell(
        3, epsilon_1, epsilon_2
    )
    t, r, c, b = variables
    x = sp.symbols("x")
    product_x = tuple(
        even_t_to_x(value, t, x, (r, c, b)) for value in equations[:2]
    )
    product_resultant = sp.resultant(product_x[0], product_x[1], x)
    product_guard_factors = (b, c, b-1, b+1, c-1, c+1, b-c, b+c)
    product_compatibility = ATLAS.BASE.strip_factors(
        product_resultant, product_guard_factors, (r, c, b)
    )
    expected_product = (
        b*(c+1)*(r**4+1)+2*r**2*(b**2*c+1)
    )
    require(
        sp.Poly(product_compatibility, r, c, b, modulus=P).monic()
        == sp.Poly(expected_product, r, c, b, modulus=P).monic(),
        "product compatibility",
    )

    capital_r = r**2
    denominator_core = capital_r**2+1+2*capital_r*b
    c_numerator = b*(capital_r**2+1)+2*capital_r
    require(
        sp.expand(
            c_numerator-b*denominator_core-2*capital_r*(1-b**2)
        ) == 0,
        "c denominator branch",
    )
    c_value = -c_numerator/(b*denominator_core)

    q_guard_factors = (
        t-epsilon_1*IOTA, t+epsilon_1*IOTA,
        r, b, c, b-1, b+1, c-1, c+1, r-1, r+1,
    )
    q_values = tuple(
        ATLAS.BASE.strip_factors(value, q_guard_factors, variables)
        for value in equations[2:]
    )
    routed_q = []
    for index, value in enumerate(q_values):
        numerator = sp.cancel(value.subs(c, c_value)).as_numer_denom()[0]
        routed_q.append(sp.cancel(numerator/(b-1 if index == 0 else b+1)))
    compatibility = primitive(
        sp.resultant(routed_q[0], routed_q[1], t), (r, b)
    )
    expected_h = h_polynomial(b, r, epsilon_1, epsilon_2)
    compatibility = ATLAS.BASE.strip_factors(
        compatibility,
        (b, r, r-1, r+1, r-IOTA, r+IOTA),
        (r, b),
    )
    require(
        sp.Poly(compatibility, r, b, modulus=P).monic()
        == sp.Poly(expected_h, r, b, modulus=P).monic(),
        "q compatibility",
    )
    q_coefficient = sp.diff(routed_q[0], t)
    q_constant = routed_q[0].subs(t, 0)
    coefficient_resultant = sp.Poly(
        sp.resultant(q_coefficient, q_constant, b), r, modulus=P
    )
    expected_coefficient = r**6*(r**2-1)**4*(r**2+1)**2
    require(
        coefficient_resultant.monic()
        == sp.Poly(expected_coefficient, r, modulus=P).monic(),
        "q coefficient branch",
    )

    product_coefficient_core = (
        2*b**2*r**2+b*r**6+3*b*r**4-b*r**2+b+2*r**2
    )
    product_constant_core = (
        2*b**2*r**4+b*r**6-b*r**4+3*b*r**2+b+2*r**4
    )
    product_degree_resultant = sp.Poly(
        sp.resultant(
            product_coefficient_core, product_constant_core, b
        ), r, modulus=P,
    )
    expected_degree = 4*r**4*(r**2-1)**2*(r**2+1)**6
    require(
        product_degree_resultant.monic()
        == sp.Poly(expected_degree, r, modulus=P).monic(),
        "product degree branch",
    )

    # The product row is linear in X=t^2 and gives
    # X=-r^2*product_constant_core/product_coefficient_core.
    square_equation = (
        q_constant**2*product_coefficient_core
        +r**2*product_constant_core*q_coefficient**2
    )
    expected_k = k_polynomial(b, r, epsilon_1)
    expected_square = (
        r**2*(b+r**2)*(r**2-1)*(r**2+1)*(b*r**2+1)*expected_k
    )
    require(
        sp.Poly(square_equation, r, b, modulus=P).monic()
        == sp.Poly(expected_square, r, b, modulus=P).monic(),
        "square equation",
    )
    for branch_value in (-r**2, -1/r**2):
        branch = sp.cancel(expected_h.subs(b, branch_value)).as_numer_denom()[0]
        branch_residual = ATLAS.BASE.strip_factors(
            branch, (r, r-1, r+1, r-IOTA, r+IOTA), (r,)
        )
        require(
            sp.Poly(branch_residual, r, modulus=P).degree() == 0,
            "linear square branch",
        )

    main_resultant = sp.Poly(
        sp.resultant(expected_h, expected_k, b), r, modulus=P
    )
    cubic, quartic = root_polynomials(r, epsilon_1, epsilon_2)
    # The exponents of r+/-1 vary by sign, but the guarded residual is fixed.
    main_residual = ATLAS.BASE.strip_factors(
        main_resultant.as_expr(),
        (r, r-1, r+1, r-IOTA, r+IOTA),
        (r,),
    )
    require(
        sp.Poly(main_residual, r, modulus=P).monic()
        == sp.Poly(cubic**2*quartic**2, r, modulus=P).monic(),
        "main root resultant",
    )
    cubic_factors = sp.factor_list(cubic, modulus=P)[1]
    quartic_factors = sp.factor_list(quartic, modulus=P)[1]
    require(
        len(cubic_factors) == 1
        and sp.Poly(cubic_factors[0][0], r, modulus=P).degree() == 3,
        "cubic base-field root",
    )
    linear = [factor for factor, _ in quartic_factors
              if sp.Poly(factor, r, modulus=P).degree() == 1]
    require(len(linear) == 1, "quartic root count")
    coefficients = sp.Poly(linear[0], r, modulus=P).all_coeffs()
    r_value = (
        -int(coefficients[1])
        *pow(int(coefficients[0]) % P, -1, P)
    ) % P
    require(r_value == R_ROWS[(epsilon_1, epsilon_2)], "deployed r row")

    b_gcd = sp.gcd(
        sp.Poly(expected_h.subs(r, r_value), b, modulus=P),
        sp.Poly(expected_k.subs(r, r_value), b, modulus=P),
    ).monic()
    require(
        b_gcd == sp.Poly(
            b**2+B_POLYNOMIAL[1]*b+1, b, modulus=P
        ).monic(),
        "deployed b row",
    )
    factor_roots = []
    for factor, _ in sp.factor_list(b_gcd.as_expr(), modulus=P)[1]:
        coefficients = sp.Poly(factor, b, modulus=P).all_coeffs()
        factor_roots.append(
            -int(coefficients[1])
            *pow(int(coefficients[0]) % P, -1, P) % P
        )
    require(set(factor_roots) == set(B_ROOTS), "deployed b roots")

    packets = []
    for b_value in B_ROOTS:
        c_packet = reconstruct_c(b_value, r_value)
        substitutions = {r: r_value, b: b_value}
        q_a = int(q_coefficient.subs(substitutions)) % P
        q_b = int(q_constant.subs(substitutions)) % P
        require(q_a != 0, "packet q coefficient")
        t_value = -q_b*pow(q_a, -1, P) % P
        require(t_value == T_ROWS[(epsilon_1, epsilon_2)], "deployed t row")
        packet = {t: t_value, r: r_value, c: c_packet, b: b_value}
        require(
            all(int(value.subs(packet)) % P == 0 for value in equations),
            "packet converse",
        )
        _, _, _, labels, products, _ = metadata
        label_values = [int(value.subs(packet)) % P for value in labels]
        product_values = [
            int(sp.sympify(value).subs(packet)) % P for value in products
        ]
        require(0 not in label_values and len(set(label_values)) == 5,
                "packet labels")
        require(0 not in product_values and len(set(product_values)) == 5,
                "packet products")
        packets.append((b_value, c_packet, r_value, t_value))
    return packets


def verify():
    warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)
    cell3 = {}
    for epsilon_1, epsilon_2 in itertools.product((1, -1), repeat=2):
        cell3[(epsilon_1, epsilon_2)] = compile_sign_row(epsilon_1, epsilon_2)
    cell6 = []
    for (epsilon_1, epsilon_2), packets in cell3.items():
        variables, equations, metadata = ATLAS.compile_cell(
            6, epsilon_1, -epsilon_2
        )
        t, r, c, b = variables
        for b_value, c_value, r_value, t_value in packets:
            packet = {t: t_value, r: r_value, b: c_value, c: b_value}
            require(
                all(int(value.subs(packet)) % P == 0 for value in equations),
                "cell 6 transport",
            )
            _, _, _, labels, products, _ = metadata
            require(len({int(value.subs(packet)) % P for value in labels}) == 5,
                    "cell 6 labels")
            require(len({int(sp.sympify(value).subs(packet)) % P
                         for value in products}) == 5,
                    "cell 6 products")
            cell6.append((epsilon_1, -epsilon_2, c_value, b_value,
                          r_value, t_value))
    return cell3, cell6


def main():
    cell3, cell6 = verify()
    print(
        "RATE_HALF_KB_ONE_LOOP_433_CELL36_FINITE_PASS "
        f"cell3_packets={sum(map(len,cell3.values()))} "
        f"cell6_packets={len(cell6)} total=16"
    )


if __name__ == "__main__":
    main()
