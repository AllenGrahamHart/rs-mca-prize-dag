#!/usr/bin/env python3
"""Bounded exact compiler for the negative one-loop 442 common-K atlas."""

import argparse
import itertools

import sympy as sp


PRIME = 2130706433
ZETA = 16711679
ROLES = ("L", "AB+", "AB-", "AC+", "AC-")


def pairings(values):
    values = tuple(values)
    first = values[0]
    for index in range(1, len(values)):
        second = values[index]
        rest = values[1:index] + values[index + 1:]
        yield ((first, second), (rest[0], rest[1]))


def cells():
    output = []
    for singleton in range(5):
        rest = tuple(index for index in range(5) if index != singleton)
        for matching in pairings(rest):
            output.append((singleton, matching))
    return output


def primitive(expression, variables):
    polynomial = sp.Poly(sp.expand(expression), *variables, modulus=PRIME)
    if polynomial.is_zero:
        return sp.Integer(0)
    return polynomial.monic().as_expr()


def reduced(expression, variables):
    return sp.Poly(sp.expand(expression), *variables, modulus=PRIME).as_expr()


def strip_guard(expression, guard, variables):
    polynomial = sp.Poly(expression, *variables, modulus=PRIME)
    guard_polynomial = sp.Poly(guard, *variables, modulus=PRIME)
    while True:
        common = sp.gcd(polynomial, guard_polynomial)
        if common.total_degree() == 0:
            return polynomial.monic().as_expr()
        polynomial = polynomial.exquo(common)


def strip_factors(expression, factors, variables):
    polynomial = sp.Poly(expression, *variables, modulus=PRIME)
    for factor in factors:
        factor_polynomial = sp.Poly(factor, *variables, modulus=PRIME)
        if factor_polynomial.total_degree() == 0:
            continue
        while True:
            quotient, remainder = sp.div(polynomial, factor_polynomial)
            if not remainder.is_zero:
                break
            polynomial = quotient
    return polynomial.monic().as_expr()


def compile_cell(cell_index, epsilon_1, epsilon_2, strip=False, strip_fast=False):
    b, c, r, t = sp.symbols("b c r t")
    variables = (t, r, c, b)
    singleton, matching = cells()[cell_index]
    roots = [None] * 5
    roots[matching[0][0]] = sp.Integer(1)
    roots[matching[0][1]] = epsilon_1*ZETA
    roots[matching[1][0]] = r
    roots[matching[1][1]] = epsilon_2*ZETA*r
    roots[singleton] = t
    labels = tuple(reduced(root**2, variables) for root in roots)
    products = (-b**2, b, -b, c, -c)
    sums = (0, 1+b, 1-b, 1+c, 1-c)
    q_values = tuple(sp.expand(root*edge_sum)
                     for root, edge_sum in zip(roots, sums))

    product_rows = [sp.Matrix([[-p, -p*s, 1, s]])
                    for p, s in zip(products, labels)]
    product_equations = []
    for fourth in (3, 4):
        matrix = sp.Matrix.vstack(
            product_rows[0], product_rows[1], product_rows[2],
            product_rows[fourth],
        )
        product_equations.append(primitive(matrix.det(), variables))

    nonloops = (1, 2, 3, 4)
    h_product = products[0]
    weld_equations = []
    for third in nonloops[2:]:
        i, j, k = nonloops[0], nonloops[1], third
        d_i = h_product-products[i]
        d_j = h_product-products[j]
        d_k = h_product-products[k]
        weld = (
            q_values[i]*d_j*d_k*(labels[k]-labels[j])
            + q_values[j]*d_i*d_k*(labels[i]-labels[k])
            + q_values[k]*d_i*d_j*(labels[j]-labels[i])
        )
        weld_equations.append(primitive(weld, variables))

    label_guard = sp.prod(
        labels[left]-labels[right]
        for left, right in itertools.combinations(range(5), 2)
    )
    product_guard = sp.prod(
        products[left]-products[right]
        for left, right in itertools.combinations(range(5), 2)
    )
    target_guard = b*c*(b**2-1)*(c**2-1)*(b**2-c**2)
    guard = primitive(label_guard*product_guard*target_guard*r*t, variables)
    equations = tuple(product_equations+weld_equations)
    if strip:
        equations = tuple(
            strip_guard(equation, guard, variables) for equation in equations
        )
    elif strip_fast:
        guard_factors = [r, t, b, c, b-1, b+1, c-1, c+1, b-c, b+c,
                         b**2-c, b**2+c]
        guard_factors.extend(
            labels[left]-labels[right]
            for left, right in itertools.combinations(range(5), 2)
        )
        equations = tuple(
            strip_factors(equation, guard_factors, variables)
            for equation in equations
        )
    return variables, equations, guard, (
        singleton, matching, labels, products, q_values,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cell", type=int, choices=range(15), required=True)
    parser.add_argument("--epsilon-1", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--epsilon-2", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--saturate", action="store_true")
    parser.add_argument("--dump", action="store_true")
    parser.add_argument("--cube-branch", action="store_true")
    parser.add_argument("--subbranch", choices=("br-c", "b+t2"))
    parser.add_argument("--invert-b", action="store_true")
    parser.add_argument("--strip", action="store_true")
    parser.add_argument("--strip-fast", action="store_true")
    parser.add_argument("--linear-c", action="store_true")
    arguments = parser.parse_args()
    variables, equations, guard, metadata = compile_cell(
        arguments.cell, arguments.epsilon_1, arguments.epsilon_2,
        strip=arguments.strip, strip_fast=arguments.strip_fast,
    )
    singleton, matching, labels, _, _ = metadata
    print(
        "KB_442_ONE_LOOP_CELL "
        f"index={arguments.cell} singleton={ROLES[singleton]} "
        f"pairs={ROLES[matching[0][0]]}:{ROLES[matching[0][1]]},"
        f"{ROLES[matching[1][0]]}:{ROLES[matching[1][1]]} "
        f"eps={arguments.epsilon_1},{arguments.epsilon_2}"
    , flush=True)
    print("labels=" + ",".join(map(str, labels)), flush=True)
    print("equations=" + ",".join(
        f"{sp.Poly(value, *variables, modulus=PRIME).total_degree()}:"
        f"{len(sp.Poly(value, *variables, modulus=PRIME).terms())}"
        for value in equations
    ), flush=True)
    if arguments.dump:
        for index, equation in enumerate(equations):
            print(f"equation[{index}]={sp.factor(equation)}", flush=True)
    generators = list(equations)
    groebner_variables = list(variables)
    if arguments.linear_c:
        t, r, c, b = variables
        p_left, p_right, q_left, q_right = equations
        a_left = sp.diff(p_left, c)
        a_right = sp.diff(p_right, c)
        b_left = p_left.subs(c, 0)
        b_right = p_right.subs(c, 0)
        require_linear = (
            sp.Poly(p_left, c).degree() <= 1 and
            sp.Poly(p_right, c).degree() <= 1
        )
        if not require_linear:
            raise RuntimeError("product equations are not linear in c")
        compatibility = primitive(
            a_left*b_right-a_right*b_left, (t, r, b)
        )
        q_numerators = []
        for equation in (q_left, q_right):
            numerator = sp.together(equation.subs(c, -b_left/a_left)).as_numer_denom()[0]
            q_numerators.append(primitive(numerator, (t, r, b)))
        generators = [compatibility, *q_numerators]
        groebner_variables = [t, r, b]
        print(
            "linear_c=" + ",".join(
                f"{sp.Poly(value, t, r, b, modulus=PRIME).total_degree()}:"
                f"{len(sp.Poly(value, t, r, b, modulus=PRIME).terms())}"
                for value in generators
            ), flush=True,
        )
        if arguments.dump:
            print(f"c_numerator={-b_left}", flush=True)
            print(f"c_denominator={a_left}", flush=True)
            for index, equation in enumerate(generators):
                print(f"linear_c_equation[{index}]={sp.factor(equation)}", flush=True)
    if arguments.cube_branch:
        t, r, c, b = variables
        generators.append(b**2+b*c+c**2)
    if arguments.subbranch == "br-c":
        t, r, c, b = variables
        generators.append(b*r-c)
    elif arguments.subbranch == "b+t2":
        t, r, c, b = variables
        generators.append(b+t**2)
    if arguments.invert_b:
        u_b = sp.symbols("u_b")
        generators.append(u_b*variables[-1]-1)
        groebner_variables.insert(0, u_b)
    if arguments.saturate:
        u = sp.symbols("u")
        generators.append(sp.expand(u*guard-1))
        groebner_variables.insert(0, u)
    basis = sp.groebner(
        generators, *groebner_variables, order="grevlex", method="f5b",
        modulus=PRIME,
    )
    unit = len(basis.polys) == 1 and basis.polys[0].as_expr() == 1
    print(
        "KB_442_ONE_LOOP_RESULT "
        f"unit={int(unit)} basis={len(basis.polys)} "
        f"zero_dimensional={int(basis.is_zero_dimensional)} "
        f"saturated={int(arguments.saturate)}"
    , flush=True)
    if arguments.dump:
        for index, polynomial in enumerate(basis.polys):
            print(f"basis[{index}]={polynomial.as_expr()}", flush=True)


if __name__ == "__main__":
    main()
