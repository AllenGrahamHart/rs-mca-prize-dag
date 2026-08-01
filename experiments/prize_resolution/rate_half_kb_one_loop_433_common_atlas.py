#!/usr/bin/env python3
"""Bounded exact compiler for the negative one-loop 433 common atlas."""

import argparse
import importlib.util
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
ROLES = ("L", "AB", "AC", "BC+", "BC-")


def primitive(expression, variables):
    numerator = sp.cancel(expression).as_numer_denom()[0]
    polynomial = sp.Poly(numerator, *variables, modulus=PRIME)
    if polynomial.is_zero:
        return sp.Integer(0)
    return polynomial.monic().as_expr()


def compile_cell(cell_index, epsilon_1, epsilon_2):
    b, c, r, t = sp.symbols("b c r t")
    variables = (t, r, c, b)
    singleton, matching = BASE.cells()[cell_index]
    roots = [None]*5
    roots[matching[0][0]] = sp.Integer(1)
    roots[matching[0][1]] = epsilon_1*IOTA
    roots[matching[1][0]] = r
    roots[matching[1][1]] = epsilon_2*IOTA*r
    roots[singleton] = t
    labels = tuple(sp.expand(root**2) for root in roots)
    products = (-1, b, c, b*c, -b*c)
    sums = (0, 1+b, 1+c, b+c, b-c)
    q_values = tuple(
        sp.expand(root*edge_sum) for root, edge_sum in zip(roots, sums)
    )

    rows = [sp.Matrix([[-product, -product*label, 1, label]])
            for product, label in zip(products, labels)]
    product_equations = []
    for fourth in (3, 4):
        matrix = sp.Matrix.vstack(rows[0], rows[1], rows[2], rows[fourth])
        product_equations.append(primitive(matrix.det(), variables))

    weld_equations = []
    h_product = products[0]
    for third in (3, 4):
        left, right = 1, 2
        d_left = h_product-products[left]
        d_right = h_product-products[right]
        d_third = h_product-products[third]
        weld = (
            q_values[left]*d_right*d_third*(labels[third]-labels[right])
            +q_values[right]*d_left*d_third*(labels[left]-labels[third])
            +q_values[third]*d_left*d_right*(labels[right]-labels[left])
        )
        weld_equations.append(primitive(weld, variables))
    return variables, tuple(product_equations+weld_equations), (
        singleton, matching, roots, labels, products, q_values,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cell", type=int, choices=range(15), required=True)
    parser.add_argument("--epsilon-1", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--epsilon-2", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--dump", action="store_true")
    arguments = parser.parse_args()
    variables, equations, metadata = compile_cell(
        arguments.cell, arguments.epsilon_1, arguments.epsilon_2
    )
    singleton, matching, _, labels, _, _ = metadata
    print(
        "KB_ONE_LOOP_433_CELL "
        f"index={arguments.cell} singleton={ROLES[singleton]} "
        f"pairs={ROLES[matching[0][0]]}:{ROLES[matching[0][1]]},"
        f"{ROLES[matching[1][0]]}:{ROLES[matching[1][1]]} "
        f"eps={arguments.epsilon_1},{arguments.epsilon_2} labels={labels}",
        flush=True,
    )
    print(
        "equations="+",".join(
            f"{sp.Poly(value,*variables,modulus=PRIME).total_degree()}:"
            f"{len(sp.Poly(value,*variables,modulus=PRIME).terms())}"
            for value in equations
        ),
        flush=True,
    )
    if arguments.dump:
        for index, equation in enumerate(equations):
            print(f"equation[{index}]={sp.factor(equation)}", flush=True)


if __name__ == "__main__":
    main()
