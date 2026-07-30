#!/usr/bin/env python3
"""FLINT specialization generator for the positive q-slice.

This optional external-CAS helper emits necessary endpoint factors.  Pairwise
resultants and curve gcds are not a deletion certificate until every curve
and isolated specialization has been discharged independently.
"""

import argparse
import hashlib
import importlib.util
import itertools
from pathlib import Path

import sympy as sp
from flint import fmpq, fmpq_mpoly_ctx


HERE = Path(__file__).resolve().parent
SYMMETRIC = HERE / "kb_c2_112_positive_qslice_symmetric.py"


def load_symmetric():
    spec = importlib.util.spec_from_file_location("positive_symmetric", SYMMETRIC)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load symmetric helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def to_flint(poly, context):
    return context.from_dict({
        monomial: fmpq(str(coefficient))
        for monomial, coefficient in poly.as_dict().items()
    })


def coefficient_rows(primitive, b, w, p, t):
    rows = []
    for equation in primitive:
        as_b = sp.Poly(equation.as_expr(), b)
        if as_b.degree() > 2:
            raise RuntimeError("this generator currently expects b-quadratics")
        rows.append(tuple(
            sp.Poly(as_b.nth(index), b, w, p, t, domain=sp.QQ)
            for index in (2, 1, 0)
        ))
    return rows


def determinant(rows):
    first, second, third = rows
    return (
        first[0] * (second[1] * third[2] - second[2] * third[1])
        - first[1] * (second[0] * third[2] - second[2] * third[0])
        + first[2] * (second[0] * third[1] - second[1] * third[0])
    )


def cross(left, right):
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def factor_summary(label, polynomial):
    if polynomial.is_zero():
        print(f"{label}_zero=true", flush=True)
        return
    content, factors = polynomial.factor()
    print(f"{label}_content={content} {label}_factor_count={len(factors)}", flush=True)
    for index, (factor, exponent) in enumerate(factors):
        rendered = str(factor)
        digest = hashlib.sha256(rendered.encode("ascii")).hexdigest()
        terms = len(list(factor.terms()))
        detail = rendered if terms <= 50 else "OMITTED_LARGE"
        print(
            f"{label}_factor={index} exponent={exponent} "
            f"degrees={factor.degrees()} terms={terms} sha256={digest} "
            f"factor={detail}",
            flush=True,
        )


def generate(template, allocation, ramified, elimination, constraint_pair,
             linear_pair):
    symmetric = load_symmetric()
    variables, odd, coefficients, _ = symmetric.reconstruct_fraction_free(template)
    p, t, b, w = variables
    if ramified:
        _, primitive = symmetric.ramified_allocation_equations(
            template, allocation, variables, coefficients
        )
    else:
        f, g, m = odd
        x0, _, x2, x3, _ = coefficients
        leading = (sp.expand(x2 - p * x0), sp.expand(x3 - t * x0))
        constant = (sp.expand(x0 - p * x2), sp.expand(x3 - t * x2))
        gamma = (sp.expand(g - p * f), sp.expand(m - t * f))
        _, primitive = symmetric.allocation_equations(
            template, allocation, variables, leading, constant, gamma
        )

    rows = coefficient_rows(primitive, b, w, p, t)
    context = fmpq_mpoly_ctx.get(("b", "w", "p", "t"), "lex")
    flint_rows = [tuple(to_flint(value, context) for value in row) for row in rows]
    if linear_pair:
        left, right = (flint_rows[index] for index in linear_pair)
        linear_lead = right[0] * left[1] - left[0] * right[1]
        linear_constant = right[0] * left[2] - left[0] * right[2]
        factor_summary("linear_lead", linear_lead)
        factor_summary("linear_constant", linear_constant)
        substituted = []
        for row in flint_rows:
            value = (row[0] * linear_constant**2
                     - row[1] * linear_constant * linear_lead
                     + row[2] * linear_lead**2)
            if not value.is_zero():
                substituted.append(value)
        common_substituted = substituted[0]
        for value in substituted[1:]:
            common_substituted = common_substituted.gcd(value)
        print(
            f"linear_substituted_count={len(substituted)} "
            f"linear_substituted_common={common_substituted.factor()}",
            flush=True,
        )
        linear_quotients = [value / common_substituted for value in substituted]
        for index, quotient in enumerate(linear_quotients):
            print(
                f"linear_constraint={index} degrees={quotient.degrees()} "
                f"terms={len(list(quotient.terms()))}",
                flush=True,
            )
        if elimination:
            endpoint_polys = []
            for index in range(1, len(linear_quotients)):
                endpoint = linear_quotients[0].resultant(
                    linear_quotients[index], "w"
                )
                if endpoint.is_zero():
                    print(f"linear_endpoint={index} zero=true", flush=True)
                    continue
                endpoint_polys.append(endpoint)
                print(
                    f"linear_endpoint={index} degree={endpoint.total_degree()} "
                    f"terms={len(list(endpoint.terms()))}",
                    flush=True,
                )
            endpoint_common = endpoint_polys[0]
            for endpoint in endpoint_polys[1:]:
                endpoint_common = endpoint_common.gcd(endpoint)
            factor_summary("linear_endpoint_curve", endpoint_common)
        return
    minors = [
        determinant([flint_rows[index] for index in indices])
        for indices in itertools.combinations(range(4), 3)
    ]
    conics = []
    for left, right in itertools.combinations(range(4), 2):
        kernel = cross(flint_rows[left], flint_rows[right])
        conics.append(kernel[1]**2 - kernel[0] * kernel[2])
    nonzero = [value for value in (*minors, *conics) if not value.is_zero()]
    common = nonzero[0]
    for value in nonzero[1:]:
        common = common.gcd(value)
    quotients = [value / common for value in nonzero]
    print(
        f"template={template} allocation={allocation} ramified={ramified} "
        f"constraint_count={len(nonzero)} common_factorization={common.factor()}",
        flush=True,
    )
    for index, constraint in enumerate(nonzero):
        print(
            f"constraint={index} degrees={constraint.degrees()} "
            f"terms={len(list(constraint.terms()))}",
            flush=True,
        )
    if constraint_pair:
        left, right = constraint_pair
        pair_common = nonzero[left].gcd(nonzero[right])
        print(f"constraint_pair_common={pair_common.factor()}", flush=True)
        endpoint = (nonzero[left] / pair_common).resultant(
            nonzero[right] / pair_common, "w"
        )
        if endpoint.is_zero():
            print(f"constraint_pair={left},{right} endpoint_zero=true", flush=True)
            return
        print(
            f"constraint_pair={left},{right} "
            f"endpoint_total_degree={endpoint.total_degree()} "
            f"endpoint_terms={len(list(endpoint.terms()))}",
            flush=True,
        )
        factor_summary("constraint_endpoint", endpoint)
        return
    if elimination:
        combinations = []
        for power in range(3):
            value = context.constant(0)
            for index, constraint in enumerate(quotients):
                value += (index + 1)**power * constraint
            combinations.append(value)
        combination_gcd = combinations[0]
        for value in combinations[1:]:
            combination_gcd = combination_gcd.gcd(value)
        print(
            f"combination_gcd_factorization={combination_gcd.factor()}",
            flush=True,
        )
        combinations = [value / combination_gcd for value in combinations]
        endpoint_polys = []
        for left, right in itertools.combinations(range(3), 2):
            endpoint = combinations[left].resultant(combinations[right], "w")
            if endpoint.is_zero():
                print(f"combination_endpoint={left},{right} zero=true", flush=True)
                continue
            endpoint_polys.append(endpoint)
            print(
                f"combination_endpoint={left},{right} "
                f"total_degree={endpoint.total_degree()} "
                f"terms={len(list(endpoint.terms()))}",
                flush=True,
            )
        curve = endpoint_polys[0]
        for endpoint in endpoint_polys[1:]:
            curve = curve.gcd(endpoint)
        factor_summary("endpoint_curve", curve)
        residual = [endpoint / curve for endpoint in endpoint_polys]
        isolated = []
        for left, right in itertools.combinations(range(len(residual)), 2):
            value = residual[left].resultant(residual[right], "t")
            if value.is_zero():
                print(f"isolated_pair={left},{right} zero=true", flush=True)
                continue
            isolated.append(value)
            print(
                f"isolated_pair={left},{right} p_degree={value.degrees()[2]} "
                f"terms={len(list(value.terms()))}",
                flush=True,
            )
        if isolated:
            isolated_common = isolated[0]
            for value in isolated[1:]:
                isolated_common = isolated_common.gcd(value)
            factor_summary("isolated_p", isolated_common)
        return
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("template", choices=("fixed-moving", "moving-moving"))
    parser.add_argument("allocation", choices=("same", "swap", "mixed"))
    parser.add_argument("--ramified", action="store_true")
    parser.add_argument("--elimination", action="store_true")
    parser.add_argument("--constraint-pair")
    parser.add_argument("--linear-pair")
    args = parser.parse_args()
    constraint_pair = None
    if args.constraint_pair:
        constraint_pair = tuple(
            int(value) for value in args.constraint_pair.split(",")
        )
        if len(constraint_pair) != 2:
            parser.error("--constraint-pair must contain two indices")
    linear_pair = None
    if args.linear_pair:
        linear_pair = tuple(int(value) for value in args.linear_pair.split(","))
        if len(linear_pair) != 2:
            parser.error("--linear-pair must contain two indices")
    actions = sum((args.elimination, constraint_pair is not None,
                   linear_pair is not None))
    if actions > 1:
        parser.error("choose only one of --elimination, --constraint-pair, or "
                     "--linear-pair")
    if actions == 0:
        constraint_pair = (0, 1)
    generate(args.template, args.allocation, args.ramified, args.elimination,
             constraint_pair, linear_pair)


if __name__ == "__main__":
    main()
