#!/usr/bin/env python3
"""Exact common-K Vieta compiler for the positive 433-1a route."""

import argparse
import hashlib
import itertools
import json

import sympy as sp


PRIME = 2130706433
IOTA = 16711679
ROLES = ("LC", "AB+1", "AB+2", "AB-", "AC")


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
    return tuple(output)


def swap_duplicate_role(cell):
    swap = {1: 2, 2: 1}

    def image(value):
        return swap.get(value, value)

    singleton, matching = cell
    return (
        image(singleton),
        tuple(sorted(tuple(sorted(image(value) for value in pair))
                     for pair in matching)),
    )


def cell_orbits():
    atlas = cells()
    indices = {cell: index for index, cell in enumerate(atlas)}
    unseen = set(range(len(atlas)))
    orbits = []
    while unseen:
        index = min(unseen)
        partner = indices[swap_duplicate_role(atlas[index])]
        orbit = tuple(sorted({index, partner}))
        unseen -= set(orbit)
        orbits.append(orbit)
    return tuple(orbits)


def primitive(expression, variables, prime=PRIME):
    polynomial = sp.Poly(sp.expand(expression), *variables, modulus=prime)
    if polynomial.is_zero:
        return sp.Integer(0)
    return polynomial.monic().as_expr()


def strip_factors(expression, factors, variables, prime=PRIME):
    polynomial = sp.Poly(expression, *variables, modulus=prime)
    for factor in factors:
        divisor = sp.Poly(factor, *variables, modulus=prime)
        if divisor.total_degree() == 0:
            continue
        while True:
            quotient, remainder = sp.div(polynomial, divisor)
            if not remainder.is_zero:
                break
            polynomial = quotient
    if polynomial.is_zero:
        return sp.Integer(0)
    return polynomial.monic().as_expr()


def compile_cell(
    cell_index,
    epsilon_1,
    epsilon_2,
    strip_fast=False,
    prime=PRIME,
    iota=IOTA,
):
    b, c, r, t = sp.symbols("b c r t")
    variables = (t, r, c, b)
    singleton, matching = cells()[cell_index]
    roots = [None] * 5
    roots[matching[0][0]] = sp.Integer(1)
    roots[matching[0][1]] = epsilon_1 * iota
    roots[matching[1][0]] = r
    roots[matching[1][1]] = epsilon_2 * iota * r
    roots[singleton] = t
    labels = tuple(sp.expand(root**2) for root in roots)
    products = (-c**2, b, b, -b, c)
    sums = (0, 1 + b, 1 + b, 1 - b, 1 + c)
    q_values = tuple(
        sp.expand(root * edge_sum) for root, edge_sum in zip(roots, sums)
    )

    product_rows = [
        sp.Matrix([[-product, -product * label, -product * label**2,
                    1, label, label**2, 0, 0]])
        for product, label in zip(products, labels)
    ]
    sum_rows = [
        sp.Matrix([[q_value, q_value * label, q_value * label**2,
                    0, 0, 0, label, label**2]])
        for q_value, label in zip(q_values, labels)
    ]
    base = [*product_rows, sum_rows[0]]
    equations = []
    for left, right in itertools.combinations(range(1, 5), 2):
        matrix = sp.Matrix.vstack(*base, sum_rows[left], sum_rows[right])
        equations.append(primitive(
            matrix.det(method="domain-ge"), variables, prime=prime
        ))
    if strip_fast:
        source_guards = [
            labels[left] - labels[right]
            for left, right in itertools.combinations(range(5), 2)
        ]
        target_guards = [
            r, t, b, c, b - 1, b + 1, c - 1, c + 1, b - c, b + c,
        ]
        equations = [
            strip_factors(
                equation,
                [*target_guards, *source_guards],
                variables,
                prime=prime,
            )
            for equation in equations
        ]
    return variables, tuple(equations), {
        "singleton": singleton,
        "matching": matching,
        "roots": roots,
        "labels": labels,
        "products": products,
        "sums": sums,
        "q_values": q_values,
    }


def polynomial_summary(expression, variables):
    polynomial = sp.Poly(expression, *variables, modulus=PRIME)
    text = str(polynomial.as_expr())
    return {
        "total_degree": polynomial.total_degree(),
        "terms": len(polynomial.terms()),
        "sha256": hashlib.sha256(text.encode()).hexdigest(),
    }


def gcd_summary(equations, variables):
    polynomials = [sp.Poly(value, *variables, modulus=PRIME) for value in equations]
    common = polynomials[0]
    for polynomial in polynomials[1:]:
        common = common.gcd(polynomial)
    common = common.monic()
    text = str(common.as_expr())
    return {
        "total_degree": common.total_degree(),
        "terms": len(common.terms()),
        "sha256": hashlib.sha256(text.encode()).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cell", type=int, choices=range(15), required=True)
    parser.add_argument("--epsilon-1", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--epsilon-2", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--strip-fast", action="store_true")
    parser.add_argument("--gcd-summary", action="store_true")
    parser.add_argument("--dump", action="store_true")
    arguments = parser.parse_args()
    variables, equations, metadata = compile_cell(
        arguments.cell, arguments.epsilon_1, arguments.epsilon_2,
        strip_fast=arguments.strip_fast,
    )
    output = {
        "cell": arguments.cell,
        "epsilon": [arguments.epsilon_1, arguments.epsilon_2],
        "singleton": ROLES[metadata["singleton"]],
        "matching": [[ROLES[value] for value in pair]
                     for pair in metadata["matching"]],
        "cell_orbits": cell_orbits(),
        "matrix_shape": [10, 8],
        "base_rank_guard": 6,
        "minor_count": len(equations),
        "mode": "stripped" if arguments.strip_fast else "raw",
        "minor_summaries": [
            polynomial_summary(equation, variables) for equation in equations
        ],
        "joint_gcd_summary": gcd_summary(equations, variables)
        if arguments.strip_fast and arguments.gcd_summary else None,
    }
    print(json.dumps(output, sort_keys=True), flush=True)
    if arguments.dump:
        for index, equation in enumerate(equations):
            print(f"equation[{index}]={sp.factor(equation)}", flush=True)


if __name__ == "__main__":
    main()
