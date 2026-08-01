#!/usr/bin/env python3
"""Bounded exact compiler for the negative zero-loop 433 common atlas."""

import argparse
import importlib.util
import itertools
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
ATLAS_442 = ROOT / (
    "critical/nodes/rate_half_band_closure/notes/"
    "kb_one_loop_442_common_atlas.py"
)
SPEC = importlib.util.spec_from_file_location("atlas_442", ATLAS_442)
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)
PRIME = BASE.PRIME
IOTA = BASE.ZETA
ROLES = ("AB+", "AB-", "AC+", "AC-", "BC+")


def primitive(expression, variables):
    numerator = sp.cancel(expression).as_numer_denom()[0]
    polynomial = sp.Poly(numerator, *variables, modulus=PRIME)
    if polynomial.is_zero:
        return sp.Integer(0)
    return polynomial.monic().as_expr()


def kernel_vector(matrix):
    """Return the signed-maximal-minor kernel of a rank-three 3 x 4 matrix."""
    return tuple(
        sp.expand((-1) ** column * matrix[:, [
            index for index in range(4) if index != column
        ]].det())
        for column in range(4)
    )


def compile_cell(cell_index, epsilon_1, epsilon_2, strip=False,
                 strip_fast=False):
    b, c, r, t = sp.symbols("b c r t")
    variables = (t, r, c, b)
    singleton, matching = BASE.cells()[cell_index]
    roots = [None] * 5
    roots[matching[0][0]] = sp.Integer(1)
    roots[matching[0][1]] = epsilon_1 * IOTA
    roots[matching[1][0]] = r
    roots[matching[1][1]] = epsilon_2 * IOTA * r
    roots[singleton] = t
    labels = tuple(sp.expand(root**2) for root in roots)
    products = (b, -b, c, -c, b*c)
    sums = (1+b, 1-b, 1+c, 1-c, b+c)
    q_values = tuple(
        sp.expand(root*edge_sum) for root, edge_sum in zip(roots, sums)
    )

    product_rows = [
        sp.Matrix([[-product, -product*label, 1, label]])
        for product, label in zip(products, labels)
    ]
    anchors = sp.Matrix.vstack(*product_rows[:3])
    d0, d1, _, _ = kernel_vector(anchors)
    product_equations = []
    for fourth in (3, 4):
        matrix = sp.Matrix.vstack(anchors, product_rows[fourth])
        product_equations.append(primitive(matrix.det(), variables))

    q_rows = []
    for label, q_value in zip(labels, q_values):
        denominator = sp.expand(d0+d1*label)
        q_rows.append(sp.Matrix([[1, label, label**2, q_value*denominator]]))
    q_anchors = sp.Matrix.vstack(*q_rows[:3])
    q_equations = []
    for fourth in (3, 4):
        matrix = sp.Matrix.vstack(q_anchors, q_rows[fourth])
        q_equations.append(primitive(matrix.det(), variables))

    label_guard = sp.prod(
        labels[left]-labels[right]
        for left, right in itertools.combinations(range(5), 2)
    )
    target_guard = b*c*(b**2-1)*(c**2-1)*(b**2-c**2)
    denominator_guard = sp.prod(d0+d1*label for label in labels)
    guard = primitive(
        label_guard*target_guard*denominator_guard*r*t, variables
    )
    equations = tuple(product_equations+q_equations)
    if strip:
        equations = tuple(
            BASE.strip_guard(equation, guard, variables)
            for equation in equations
        )
    elif strip_fast:
        guard_factors = [
            r, t, b, c, b-1, b+1, c-1, c+1, b-c, b+c,
        ]
        guard_factors.extend(
            labels[left]-labels[right]
            for left, right in itertools.combinations(range(5), 2)
        )
        guard_factors.extend(d0+d1*label for label in labels)
        equations = tuple(
            BASE.strip_factors(equation, guard_factors, variables)
            for equation in equations
        )
    return variables, equations, guard, (
        singleton, matching, roots, labels, products, q_values, (d0, d1),
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cell", type=int, choices=range(15), required=True)
    parser.add_argument("--epsilon-1", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--epsilon-2", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--strip", action="store_true")
    parser.add_argument("--strip-fast", action="store_true")
    parser.add_argument("--groebner", action="store_true")
    parser.add_argument("--order", choices=("lex", "grlex", "grevlex"),
                        default="grevlex")
    parser.add_argument("--dump", action="store_true")
    arguments = parser.parse_args()
    variables, equations, guard, metadata = compile_cell(
        arguments.cell, arguments.epsilon_1, arguments.epsilon_2,
        strip=arguments.strip, strip_fast=arguments.strip_fast,
    )
    singleton, matching, _, labels, _, _, denominator = metadata
    print(
        "KB_ZERO_LOOP_433_CELL "
        f"index={arguments.cell} singleton={ROLES[singleton]} "
        f"pairs={ROLES[matching[0][0]]}:{ROLES[matching[0][1]]},"
        f"{ROLES[matching[1][0]]}:{ROLES[matching[1][1]]} "
        f"eps={arguments.epsilon_1},{arguments.epsilon_2} labels={labels}",
        flush=True,
    )
    print(
        "equations=" + ",".join(
            f"{sp.Poly(value, *variables, modulus=PRIME).total_degree()}:"
            f"{len(sp.Poly(value, *variables, modulus=PRIME).terms())}"
            for value in equations
        ),
        flush=True,
    )
    if arguments.dump:
        print(f"denominator={denominator}", flush=True)
        print(f"guard={sp.factor(guard)}", flush=True)
        for index, equation in enumerate(equations):
            print(f"equation[{index}]={sp.factor(equation)}", flush=True)
    if arguments.groebner:
        basis = sp.groebner(
            equations, *variables, order=arguments.order, method="f5b",
            modulus=PRIME,
        )
        unit = len(basis.polys) == 1 and basis.polys[0].as_expr() == 1
        print(
            "KB_ZERO_LOOP_433_GROEBNER "
            f"unit={int(unit)} basis={len(basis.polys)} "
            f"zero_dimensional={int(basis.is_zero_dimensional)} "
            f"order={arguments.order}",
            flush=True,
        )
        if arguments.dump:
            for index, polynomial in enumerate(basis.polys):
                expression = polynomial.as_expr()
                print(
                    f"basis[{index}]="
                    f"degree:{sp.Poly(expression,*variables,modulus=PRIME).total_degree()} "
                    f"terms:{len(sp.Poly(expression,*variables,modulus=PRIME).terms())} "
                    f"expression:{expression}",
                    flush=True,
                )


if __name__ == "__main__":
    main()
