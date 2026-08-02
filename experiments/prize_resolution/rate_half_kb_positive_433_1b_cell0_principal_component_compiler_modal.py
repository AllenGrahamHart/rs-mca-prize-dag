#!/usr/bin/env python3
"""Compile cell-0 principal component kernels for positive 433-1b."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell0_principal_component_compiler_result.json"
PRIME = 2130706433
IOTA = 16711679

app = modal.App("rs-mca-positive-433-1b-cell0-principal-components")
image = modal.Image.debian_slim(python_version="3.12").pip_install("sympy==1.14.0")


@app.function(image=image, cpu=1.0, memory=2048, timeout=180, max_containers=4)
def compile_component(case):
    import sympy as sp

    component, source_sign = case
    b, t = sp.symbols("b t")
    inverse_two = pow(2, -1, PRIME)
    alpha = (source_sign*IOTA + 1) * inverse_two % PRIME
    if component == "A":
        c = sp.Rational(source_sign*IOTA, 1) * b
        r = 1 / b
        relation = sp.expand(
            t*t*b*(1 + alpha*b) + alpha + source_sign*IOTA*b
        )
    elif component == "B":
        c = -sp.Rational(source_sign*IOTA, 1) * b
        r = b
        relation = sp.expand(
            t*t*(b + alpha) + b*(alpha*b + source_sign*IOTA)
        )
    else:
        raise ValueError(component)

    roots = (t, 1, source_sign*IOTA, r, source_sign*IOTA*r)
    labels = tuple(sp.cancel(root*root) for root in roots)
    products = (-1, b, c, b*c, -b*c)
    sums = (0, 1+b, 1+c, b+c, b-c)
    product_rows = [
        [-product, -product*label, -product*label**2,
         1, label, label**2, 0, 0]
        for product, label in zip(products, labels)
    ]
    sum_rows = [
        [q, q*label, q*label**2, 0, 0, 0, label, label**2]
        for root, label, edge_sum in zip(roots, labels, sums)
        for q in [sp.cancel(root*edge_sum)]
    ]

    def clear_row(row):
        denominators = [sp.fraction(sp.cancel(value))[1] for value in row]
        denominator = sp.lcm(denominators)
        return [sp.expand(sp.cancel(denominator*value)) for value in row]

    all_rows = [clear_row(row) for row in [*product_rows, *sum_rows]]
    pivot_rows = all_rows[:5] + [all_rows[5], all_rows[6]]
    matrix = sp.Matrix(pivot_rows)
    kernel = [
        (-1)**column
        * matrix[:, [index for index in range(8) if index != column]].det(
            method="domain-ge"
        )
        for column in range(8)
    ]

    def reduce_relation(expression):
        numerator, denominator = sp.fraction(sp.cancel(expression))
        field = sp.GF(PRIME).frac_field(b)
        reduced = sp.Poly(numerator, t, domain=field).rem(
            sp.Poly(relation, t, domain=field)
        ).as_expr()
        reduced = sp.cancel(reduced / denominator)
        numerator, denominator = sp.fraction(reduced)
        return sp.expand(numerator), sp.expand(denominator)

    rational_kernel = [reduce_relation(value) for value in kernel]
    common_denominator = sp.lcm([denominator for _, denominator in rational_kernel])
    reduced_kernel = [
        sp.Poly(
            sp.cancel(common_denominator*numerator/denominator),
            t, b, modulus=PRIME,
        ).as_expr()
        for numerator, denominator in rational_kernel
    ]
    first = next(sp.Poly(value, t, b, modulus=PRIME)
                 for value in reduced_kernel if value != 0)
    shared_inverse = pow(int(first.LC()) % PRIME, -1, PRIME)
    reduced_kernel = [
        sp.Poly(shared_inverse*value, t, b, modulus=PRIME).as_expr()
        for value in reduced_kernel
    ]
    kernel_gcd = next(
        sp.Poly(value, t, b, modulus=PRIME)
        for value in reduced_kernel if value != 0
    )
    for value in reduced_kernel:
        if value != 0:
            kernel_gcd = sp.gcd(
                kernel_gcd, sp.Poly(value, t, b, modulus=PRIME)
            )
    reduced_kernel = [
        sp.div(sp.Poly(value, t, b, modulus=PRIME), kernel_gcd)[0].as_expr()
        for value in reduced_kernel
    ]

    row_checks = []
    for row in all_rows:
        value = sum(left*right for left, right in zip(row, reduced_kernel))
        reduced, denominator = reduce_relation(value)
        row_checks.append({
            "zero": sp.Poly(reduced, t, b, modulus=PRIME).is_zero,
            "denominator": str(sp.Poly(denominator, t, b, modulus=PRIME).as_expr()),
        })

    def summary(value):
        polynomial = sp.Poly(value, t, b, modulus=PRIME)
        text = str(polynomial.as_expr())
        return {
            "degree": polynomial.total_degree(),
            "terms": len(polynomial.terms()),
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
            "expression": text,
        }

    return {
        "component": component,
        "source_sign": source_sign,
        "field": PRIME,
        "relation": summary(relation),
        "kernel": [summary(value) for value in reduced_kernel],
        "kernel_common_denominator": str(
            sp.Poly(common_denominator, t, b, modulus=PRIME).as_expr()
        ),
        "kernel_removed_gcd": summary(kernel_gcd.as_expr()),
        "row_checks": row_checks,
        "all_rows_zero": all(row["zero"] for row in row_checks),
    }


@app.local_entrypoint()
def main():
    cases = tuple(
        (component, source_sign)
        for component in ("A", "B") for source_sign in (-1, 1)
    )
    rows = list(compile_component.map(cases, order_outputs=True))
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell0-principal-components-v2",
        "app": "rs-mca-positive-433-1b-cell0-principal-components",
        "scope": "Exact division-free kernels for both equal-sign component families.",
        "field": PRIME,
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {"component": row["component"], "source_sign": row["source_sign"],
             "all_rows_zero": row["all_rows_zero"],
             "relation": [row["relation"]["degree"], row["relation"]["terms"]],
             "kernel": [[item["degree"], item["terms"]] for item in row["kernel"]]}
            for row in rows
        ],
    }, sort_keys=True))
