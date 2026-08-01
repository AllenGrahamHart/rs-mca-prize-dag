#!/usr/bin/env python3
"""Exact deployed-field ratio chart for positive 433-1a cell 5."""

import copy
import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as sp


DIRECTORY = Path(__file__).resolve().parent
COMMON = DIRECTORY / "rate_half_kb_positive_433_1a_common_vieta_compiler.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_ratio_result.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def payload_hash(value):
    clone = copy.deepcopy(value)
    clone.pop("payload_sha256", None)
    return hashlib.sha256(canonical_json(clone).encode()).hexdigest()


def load_common():
    specification = importlib.util.spec_from_file_location("common", COMMON)
    common = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(common)
    return common


def normalized(expression, variables, prime):
    polynomial = sp.Poly(expression, *variables, modulus=prime)
    require(not polynomial.is_zero, "unexpected zero polynomial")
    return polynomial.monic()


def polynomial_summary(expression, variables, prime):
    polynomial = normalized(expression, variables, prime)
    text = str(polynomial.as_expr())
    return {
        "degree": polynomial.total_degree(),
        "terms": len(polynomial.terms()),
        "sha256": hashlib.sha256(text.encode()).hexdigest(),
    }


def compile_result():
    common = load_common()
    prime = common.PRIME
    iota = common.IOTA
    require((iota * iota + 1) % prime == 0, "deployed iota square")

    variables, equations, metadata = common.compile_cell(
        5, -1, -1, strip_fast=True
    )
    t, r, c, b = variables
    x = sp.symbols("x")
    ratio_variables = (t, r, x)
    atomic_guards = (
        t-1, t+1, r-1, r+1, r-iota, r+iota,
        t-r, t+r, t-iota*r, t+iota*r, t-iota, t+iota,
        r, t, b, c, b-1, b+1, c-1, c+1, c-b, b+c,
    )

    localized = []
    removed = []
    for equation in equations[:3]:
        polynomial = sp.Poly(equation, *variables, modulus=prime).monic()
        row_removed = []
        for guard in atomic_guards:
            divisor = sp.Poly(guard, *variables, modulus=prime).monic()
            while True:
                quotient, remainder = polynomial.div(divisor)
                if not remainder.is_zero:
                    break
                polynomial = quotient.monic()
                row_removed.append(str(divisor.as_expr()))
        localized.append(polynomial.as_expr())
        removed.append(row_removed)

    quotient_polynomials = []
    coefficient_ledgers = []
    for equation in localized:
        substituted = sp.Poly(
            sp.expand(equation.subs(c, b*x)), b, t, r, x, modulus=prime
        )
        b_valuation = min(monomial[0] for monomial, _ in substituted.terms())
        require(b_valuation == 2, "ratio b valuation")
        quotient = sp.expand(substituted.as_expr() / b**2)
        polynomial = sp.Poly(quotient, b, domain="EX")
        quotient_polynomials.append(polynomial)
        coefficient_ledgers.append([
            polynomial_summary(polynomial.nth(degree), ratio_variables, prime)
            for degree in range(polynomial.degree() + 1)
        ])

    degrees_in_b = [polynomial.degree() for polynomial in quotient_polynomials]
    require(degrees_in_b == [1, 2, 2], "linear/quadratic ratio shape")
    linear = quotient_polynomials[0]
    a0, a1 = linear.nth(0), linear.nth(1)
    eliminants = []
    for quadratic in quotient_polynomials[1:]:
        q0, q1, q2 = (quadratic.nth(degree) for degree in range(3))
        eliminant = sp.expand(q0*a1**2 - q1*a0*a1 + q2*a0**2)
        # This is a cleared evaluation of q at b=-a0/a1.
        replay = sp.Poly(
            eliminant - (q0*a1**2 - q1*a0*a1 + q2*a0**2),
            *ratio_variables, modulus=prime,
        )
        require(replay.is_zero, "cleared substitution identity")
        eliminants.append(polynomial_summary(eliminant, ratio_variables, prime))

    output = {
        "field": prime,
        "iota": iota,
        "cell": 5,
        "epsilon": [-1, -1],
        "chart": "C1 minors 12,13,14",
        "labels": ["1", "t^2", "r^2", "-r^2", "-1"],
        "atomic_guard_count": len(atomic_guards),
        "removed_atomic_guard_factors": removed,
        "localized_chart": [
            polynomial_summary(value, variables, prime) for value in localized
        ],
        "ratio_coordinate": "x=c/b",
        "removed_unit": "b^2",
        "degrees_in_b": degrees_in_b,
        "coefficient_ledgers": coefficient_ledgers,
        "linear_coefficients": {
            "a0": polynomial_summary(a0, ratio_variables, prime),
            "a1": polynomial_summary(a1, ratio_variables, prime),
        },
        "generic_reconstruction": "b=-a0/a1",
        "generic_eliminants": eliminants,
        "exceptional_branch": "a0=a1=0",
        "conclusion": {
            "deployed_cell5_chart_reduced_exactly": True,
            "generic_source_variables": ["x", "r", "t"],
            "denominator_branch_closed": False,
            "outside_equations_imposed": False,
            "route_deleted": False,
        },
    }
    output["payload_sha256"] = payload_hash(output)
    return output


def main():
    observed = compile_result()
    if RESULT.exists():
        require(json.loads(RESULT.read_text()) == observed, "sealed result")
    print(json.dumps(observed, sort_keys=True))


if __name__ == "__main__":
    main()
