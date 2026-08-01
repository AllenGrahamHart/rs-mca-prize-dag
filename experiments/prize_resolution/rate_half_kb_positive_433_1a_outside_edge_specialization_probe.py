#!/usr/bin/env python3
"""Bounded symbolic specialization of one positive 433-1a edge cut."""

import argparse
import functools
import json

import sympy as sp

from rate_half_kb_positive_433_1a_product_base_rank_compiler import (
    PRIME,
    cells,
    compile_cell,
)


IOTA = 16711679


def polynomial_summary(expression, variables):
    polynomial = sp.Poly(expression, *variables, modulus=PRIME)
    return {
        "degree": polynomial.total_degree(),
        "terms": len(polynomial.terms()),
    }


def primitive_product_kernel(cell):
    b, c, r, t = sp.symbols("b c r t")
    variables = (t, r, c, b)
    payload = compile_cell(cell, dump=True)
    cofactors = [
        sp.Poly(sp.sympify(value), *variables, modulus=PRIME)
        for value in payload["kernel_cofactor_expressions"]
    ]
    common_gcd = functools.reduce(sp.gcd, cofactors)
    primitive = []
    for cofactor in cofactors:
        quotient, remainder = sp.div(cofactor, common_gcd)
        if not remainder.is_zero:
            raise RuntimeError("nonexact common cofactor gcd")
        primitive.append(quotient.as_expr())
    return primitive, common_gcd.as_expr(), variables


def common_kernel(cell, epsilon_1, epsilon_2):
    primitive, common_gcd, common_variables = primitive_product_kernel(cell)
    b, c, r, t = sp.symbols("b c r t")
    singleton, matching = cells()[cell]
    roots = [None] * 5
    roots[matching[0][0]] = sp.Integer(1)
    roots[matching[0][1]] = epsilon_1 * IOTA
    roots[matching[1][0]] = r
    roots[matching[1][1]] = epsilon_2 * IOTA * r
    roots[singleton] = t
    labels = [sp.expand(root**2) for root in roots]

    a2 = primitive[:3]
    a0 = primitive[3:]
    loop_label = labels[0]
    nonloop_label = labels[1]
    q_nonloop = roots[1] * (1 + b)
    delta = sp.expand(nonloop_label * (nonloop_label - loop_label))
    a2_value = sp.expand(sum(a2[index] * nonloop_label**index
                             for index in range(3)))
    scaled_a2 = [sp.expand(delta * value) for value in a2]
    scaled_a0 = [sp.expand(delta * value) for value in a0]
    beta_scale = sp.expand(-q_nonloop * a2_value)
    b1 = [sp.expand(-beta_scale * loop_label), beta_scale]
    return scaled_a2, scaled_a0, b1, common_gcd, common_variables


def target_record(edge, cycle_sign):
    b, c, d, e, f = sp.symbols("b c d e f")
    records = {
        "de": (d * e, (d + e) ** 2),
        "nde": (-d * e, (d - e) ** 2),
        "df": (d * f, (d + f) ** 2),
        "ndf": (-d * f, (d - f) ** 2),
        "ef": (cycle_sign * e * f, (e + cycle_sign * f) ** 2),
        "be": (b * e, (b + e) ** 2),
        "cf": (c * f, (c + f) ** 2),
    }
    return records[edge]


def compile_case(cell, epsilon_1, epsilon_2, cycle_sign, edge):
    b, c, r, t, d, e, f = sp.symbols("b c r t d e f")
    variables = (f, e, d, t, r, c, b)
    a2, a0, b1, common_gcd, common_variables = common_kernel(
        cell, epsilon_1, epsilon_2
    )
    product, sum_squared = target_record(edge, cycle_sign)
    A = sp.expand(a0[2] - product * a2[2])
    B = sp.expand(a0[1] - product * a2[1])
    C = sp.expand(a0[0] - product * a2[0])
    q0 = sp.expand(-sum_squared * a2[0] ** 2)
    q1 = sp.expand(b1[0] ** 2 - 2 * sum_squared * a2[0] * a2[1])
    q2 = sp.expand(
        2 * b1[0] * b1[1]
        - sum_squared * (a2[1] ** 2 + 2 * a2[0] * a2[2])
    )
    q3 = sp.expand(b1[1] ** 2 - 2 * sum_squared * a2[1] * a2[2])
    q4 = sp.expand(-sum_squared * a2[2] ** 2)
    coefficients = (q0, q1, q2, q3, q4)

    header = {
        "cell": cell,
        "epsilon": [epsilon_1, epsilon_2],
        "cycle_sign": cycle_sign,
        "edge": edge,
        "common_gcd": polynomial_summary(common_gcd, common_variables),
        "primitive_a2": [polynomial_summary(value, common_variables)
                         for value in a2],
        "primitive_a0": [polynomial_summary(value, common_variables)
                         for value in a0],
        "b1": [polynomial_summary(value, common_variables) for value in b1],
        "product_coefficients": [polynomial_summary(value, variables)
                                 for value in (A, B, C)],
        "sum_coefficients": [polynomial_summary(value, variables)
                             for value in coefficients],
    }
    print(json.dumps({"status": "HEADER", **header}, sort_keys=True), flush=True)

    q0, q1, q2, q3, q4 = map(
        lambda value: sp.Poly(value, *variables, modulus=PRIME), coefficients
    )
    A, B, C = [sp.Poly(value, *variables, modulus=PRIME)
               for value in (A, B, C)]
    r1 = (
        q4 * (-B**3 + 2 * A * B * C)
        + q3 * A * (B**2 - A * C)
        - q2 * A**2 * B + q1 * A**3
    )
    r0 = (
        q4 * (-B**2 * C + A * C**2)
        + q3 * A * B * C - q2 * A**2 * C + q0 * A**3
    )
    compact = A * r0**2 - B * r0 * r1 + C * r1**2
    output = {
        **header,
        "status": "COMPLETE",
        "r0": {"degree": r0.total_degree(), "terms": len(r0.terms())},
        "r1": {"degree": r1.total_degree(), "terms": len(r1.terms())},
        "compact": {
            "degree": compact.total_degree(),
            "terms": len(compact.terms()),
        },
    }
    print(json.dumps(output, sort_keys=True), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cell", type=int, required=True)
    parser.add_argument("--epsilon-1", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--epsilon-2", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--cycle-sign", type=int, choices=(-1, 1), required=True)
    parser.add_argument(
        "--edge", choices=("de", "nde", "df", "ndf", "ef", "be", "cf"),
        required=True,
    )
    arguments = parser.parse_args()
    compile_case(
        arguments.cell, arguments.epsilon_1, arguments.epsilon_2,
        arguments.cycle_sign, arguments.edge,
    )


if __name__ == "__main__":
    main()
