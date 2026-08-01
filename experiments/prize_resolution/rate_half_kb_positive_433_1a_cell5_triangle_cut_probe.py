#!/usr/bin/env python3
"""Compile target-free triangle sum cuts for positive 433-1a cell 5."""

import argparse
import json

import sympy as sp

from rate_half_kb_positive_433_1a_cell5_sparse_edge_probe import (
    PRIME,
    sparse_product_kernel,
)


def summary(expression, variables):
    polynomial = sp.Poly(expression, *variables, modulus=PRIME)
    return {
        "degree": polynomial.total_degree(),
        "terms": len(polynomial.terms()),
    }


def compile_cut(template):
    b, c, r, t, u = sp.symbols("b c r t u")
    variables = (u, t, r, c, b)
    a2, a0, _, _, _ = sparse_product_kernel()
    delta = t**2 * (t**2 - 1)
    q_nonloop = t * (1 + b)
    a2_at_t2 = sp.expand(sum(a2[index] * t ** (2 * index)
                              for index in range(3)))
    beta = sp.expand(-q_nonloop * a2_at_t2)
    denominator = [sp.expand(delta * value) for value in a2]
    numerator = [sp.expand(delta * value) for value in a0]

    def evaluate(coefficients, value):
        return sp.expand(sum(coefficients[index] * value**index
                             for index in range(3)))

    dw = evaluate(denominator, u)
    nw = evaluate(numerator, u)
    dm = evaluate(denominator, -u)
    nm = evaluate(numerator, -u)
    xi = -t**2
    dx = evaluate(denominator, xi)
    nx = evaluate(numerator, xi)
    bw = sp.expand(beta * (u - 1))
    components = {
        "dw": dw, "nw": nw, "dm": dm, "nm": nm,
        "dx": dx, "nx": nx, "bw": bw,
    }
    header = {
        "template": template,
        "variables": [str(value) for value in variables],
        "components": {
            name: summary(value, variables)
            for name, value in components.items()
        },
    }
    print(json.dumps({"status": "HEADER", **header}, sort_keys=True),
          flush=True)

    if template == "A":
        cross = nm * dx - nx * dm
        expression = (
            u * bw**2 * nx * nm * dx * dm
            + nw * dw * cross**2
        )
    else:
        inside = nw * nm**2 * dx**2 + c**2 * nx**2 * dw * dm**2
        expression = (
            u * bw**2 * c**2 * nx**2 * nm**2 * dm**2 * dx**2
            - inside**2
        )
    polynomial = sp.Poly(expression, *variables, modulus=PRIME)
    output = {
        **header,
        "status": "EXPANDED",
        "cut": {
            "degree": polynomial.total_degree(),
            "terms": len(polynomial.terms()),
        },
    }
    print(json.dumps(output, sort_keys=True), flush=True)

    coefficient, factors = sp.factor_list(polynomial)
    output["status"] = "COMPLETE"
    output["factor_count"] = len(factors)
    output["factors"] = [
        {
            "multiplicity": multiplicity,
            "degree": factor.total_degree(),
            "terms": len(factor.terms()),
            "expression": str(factor.as_expr()),
        }
        for factor, multiplicity in factors
    ]
    print(json.dumps(output, sort_keys=True), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", choices=("A", "B"), required=True)
    arguments = parser.parse_args()
    compile_cut(arguments.template)


if __name__ == "__main__":
    main()
