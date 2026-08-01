#!/usr/bin/env python3
"""Sparse exact cell-5 specialization of one positive 433-1a edge cut."""

import argparse
import functools
import json

import sympy as sp


PRIME = 2130706433


def summary(expression, variables):
    polynomial = sp.Poly(expression, *variables, modulus=PRIME)
    return {
        "degree": polynomial.total_degree(),
        "terms": len(polynomial.terms()),
    }


def sparse_product_kernel():
    b, c, r, t = sp.symbols("b c r t")
    variables = (t, r, c, b)
    x = r**2
    y = t**2
    matrix = sp.Matrix([
        [2 * b, -2 * b * x, 2 * b * x**2, 2 * x * (x + y)],
        [b + c**2, b + c**2, b + c**2, (1 - x) * (1 - y)],
        [b - c, -(b - c), b - c, (1 + x) * (1 + y)],
    ])
    cofactors = [
        sp.expand((-1) ** omitted * matrix[:, [
            column for column in range(4) if column != omitted
        ]].det(method="domain-ge"))
        for omitted in range(4)
    ]
    polynomials = [sp.Poly(value, *variables, modulus=PRIME)
                   for value in cofactors]
    common_gcd = functools.reduce(sp.gcd, polynomials)
    primitive = []
    for polynomial in polynomials:
        quotient, remainder = sp.div(polynomial, common_gcd)
        if not remainder.is_zero:
            raise RuntimeError("nonexact sparse-kernel gcd")
        primitive.append(quotient.as_expr())

    a2 = primitive[:3]
    alpha = primitive[3]
    g = (x * y, -(x + y), sp.Integer(1))
    a0 = [sp.expand(b * a2[index] + alpha * g[index])
          for index in range(3)]
    kernel = sp.Matrix([*a2, alpha])
    if any(not sp.Poly(value, *variables, modulus=PRIME).is_zero
           for value in matrix * kernel):
        raise RuntimeError("sparse product-kernel identity failed")
    return a2, a0, alpha, common_gcd.as_expr(), variables


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


def compile_case(cycle_sign, edge):
    b, c, r, t, d, e, f = sp.symbols("b c r t d e f")
    variables = (f, e, d, t, r, c, b)
    common_variables = (t, r, c, b)
    a2, a0, alpha, common_gcd, _ = sparse_product_kernel()

    # Cell 5 has loop label 1 and singleton AB+1 label t^2.
    delta = t**2 * (t**2 - 1)
    q_nonloop = t * (1 + b)
    a2_at_t2 = sp.expand(sum(a2[index] * t ** (2 * index)
                              for index in range(3)))
    beta = sp.expand(-q_nonloop * a2_at_t2)
    b1 = (-beta, beta)

    product, sum_squared = target_record(edge, cycle_sign)
    # Delta is supported, so use the unscaled product quadratic.  The sum
    # equation is cleared by Delta^2 and remains polynomial.
    A = sp.expand(a0[2] - product * a2[2])
    B = sp.expand(a0[1] - product * a2[1])
    C = sp.expand(a0[0] - product * a2[0])
    delta_squared = sp.expand(delta**2)
    q0 = sp.expand(-sum_squared * delta_squared * a2[0] ** 2)
    q1 = sp.expand(b1[0] ** 2
                   - 2 * sum_squared * delta_squared * a2[0] * a2[1])
    q2 = sp.expand(
        2 * b1[0] * b1[1]
        - sum_squared * delta_squared
        * (a2[1] ** 2 + 2 * a2[0] * a2[2])
    )
    q3 = sp.expand(b1[1] ** 2
                   - 2 * sum_squared * delta_squared * a2[1] * a2[2])
    q4 = sp.expand(-sum_squared * delta_squared * a2[2] ** 2)
    coefficients = (q0, q1, q2, q3, q4)

    header = {
        "cell": 5,
        "cycle_sign": cycle_sign,
        "edge": edge,
        "normalization": "A0-b*A2=alpha*(W-r^2)*(W-t^2)",
        "common_gcd": summary(common_gcd, common_variables),
        "a2": [summary(value, common_variables) for value in a2],
        "a0": [summary(value, common_variables) for value in a0],
        "alpha": summary(alpha, common_variables),
        "b1_numerator": [summary(value, common_variables) for value in b1],
        "product_coefficients": [summary(value, variables)
                                 for value in (A, B, C)],
        "sum_coefficients": [summary(value, variables)
                             for value in coefficients],
    }
    print(json.dumps({"status": "HEADER", **header}, sort_keys=True),
          flush=True)

    q0, q1, q2, q3, q4 = [
        sp.Poly(value, *variables, modulus=PRIME) for value in coefficients
    ]
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
    print(json.dumps({
        "status": "REMAINDER",
        **header,
        "r0": {"degree": r0.total_degree(), "terms": len(r0.terms())},
        "r1": {"degree": r1.total_degree(), "terms": len(r1.terms())},
    }, sort_keys=True), flush=True)
    compact = A * r0**2 - B * r0 * r1 + C * r1**2
    print(json.dumps({
        "status": "COMPLETE",
        **header,
        "r0": {"degree": r0.total_degree(), "terms": len(r0.terms())},
        "r1": {"degree": r1.total_degree(), "terms": len(r1.terms())},
        "compact": {
            "degree": compact.total_degree(),
            "terms": len(compact.terms()),
        },
    }, sort_keys=True), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cycle-sign", type=int, choices=(-1, 1), required=True)
    parser.add_argument(
        "--edge", choices=("de", "nde", "df", "ndf", "ef", "be", "cf"),
        required=True,
    )
    arguments = parser.parse_args()
    compile_case(arguments.cycle_sign, arguments.edge)


if __name__ == "__main__":
    main()
