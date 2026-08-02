#!/usr/bin/env python3
"""Compile exact cell-14 kernels on the dense quadratic-cover chart."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
STRUCTURE = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_kernel_structure_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_curve_kernel_result.json"
REMOTE_STRUCTURE = "/root/structure.json"
PRIME = 2130706433
IOTA = 16711679

app = modal.App("rs-mca-positive-433-1b-cell14-curve-kernel")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(STRUCTURE, REMOTE_STRUCTURE)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=300, max_containers=4)
def compile_kernel(signs):
    import sympy as sp

    epsilon_1, epsilon_2 = signs
    payload = json.loads(Path(REMOTE_STRUCTURE).read_text())
    source = next(
        row for row in payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2] and row["chart"] == 3
    )
    t, r, c, b = sp.symbols("t r c b")
    relation_t = sp.sympify(source["relation_t"]["expression"])
    relation_c = sp.sympify(source["relation_c"]["expression"])
    relation_rb = sp.sympify(source["relation_rb"]["expression"])

    t_polynomial = sp.Poly(relation_t, t)
    t_denominator = t_polynomial.coeff_monomial(t)
    t_map = sp.cancel(-t_polynomial.coeff_monomial(1) / t_denominator)
    c_polynomial = sp.Poly(relation_c, c)
    c_denominator = c_polynomial.coeff_monomial(c)
    c_map = sp.cancel(-c_polynomial.coeff_monomial(1) / c_denominator)

    roots = (1, r, epsilon_2*IOTA*r, epsilon_1*IOTA, t_map)
    labels = tuple(sp.cancel(root*root) for root in roots)
    products = (-1, b, c_map, b*c_map, -b*c_map)
    sums = (0, 1+b, 1+c_map, b+c_map, b-c_map)
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

    def interpolate(points, values):
        matrix = sp.Matrix([[1, point, point**2] for point in points])
        return tuple(sp.cancel(value) for value in matrix.inv() * sp.Matrix(values))

    q_values = tuple(
        sp.cancel(root*edge_sum) for root, edge_sum in zip(roots, sums)
    )
    a_points = labels[1:4]
    a_values = tuple(
        sp.cancel(label*(1-label)/q_value)
        for label, q_value in zip(labels[1:4], q_values[1:4])
    )
    a_coefficients = interpolate(a_points, a_values)

    def evaluate(coefficients, value):
        return sp.cancel(
            coefficients[0] + coefficients[1]*value + coefficients[2]*value**2
        )

    b_points = labels[:3]
    b_values = tuple(
        sp.cancel(product*evaluate(a_coefficients, label))
        for product, label in zip(products[:3], labels[:3])
    )
    b_coefficients = interpolate(b_points, b_values)
    kernel = [*a_coefficients, *b_coefficients, sp.Integer(-1), sp.Integer(1)]

    field = sp.GF(PRIME).frac_field(r)
    relation_over_field = sp.Poly(relation_rb, b, domain=field)

    def reduce_relation(expression):
        numerator, denominator = sp.fraction(sp.cancel(expression))
        reduced = sp.Poly(numerator, b, domain=field).rem(
            relation_over_field
        ).as_expr()
        reduced = sp.cancel(reduced / denominator)
        return sp.fraction(reduced)

    rational_kernel = [reduce_relation(value) for value in kernel]
    common_denominator = sp.lcm(
        [denominator for _, denominator in rational_kernel]
    )
    reduced_kernel = [
        sp.Poly(
            sp.cancel(common_denominator*numerator/denominator),
            r, b, modulus=PRIME,
        ).as_expr()
        for numerator, denominator in rational_kernel
    ]
    first = next(
        sp.Poly(value, r, b, modulus=PRIME)
        for value in reduced_kernel if value != 0
    )
    shared_inverse = pow(int(first.LC()) % PRIME, -1, PRIME)
    reduced_kernel = [
        sp.Poly(shared_inverse*value, r, b, modulus=PRIME).as_expr()
        for value in reduced_kernel
    ]
    kernel_gcd = next(
        sp.Poly(value, r, b, modulus=PRIME)
        for value in reduced_kernel if value != 0
    )
    for value in reduced_kernel:
        if value != 0:
            kernel_gcd = sp.gcd(
                kernel_gcd, sp.Poly(value, r, b, modulus=PRIME)
            )
    reduced_kernel = [
        sp.div(sp.Poly(value, r, b, modulus=PRIME), kernel_gcd)[0].as_expr()
        for value in reduced_kernel
    ]

    row_checks = []
    for row in [*product_rows, *sum_rows]:
        value = sum(left*right for left, right in zip(row, reduced_kernel))
        numerator, denominator = reduce_relation(value)
        row_checks.append({
            "zero": sp.Poly(numerator, r, b, modulus=PRIME).is_zero,
            "denominator": str(
                sp.Poly(denominator, r, b, modulus=PRIME).as_expr()
            ),
        })

    def summary(value, variables=(r, b)):
        polynomial = sp.Poly(value, *variables, modulus=PRIME)
        text = str(polynomial.as_expr())
        return {
            "degree": polynomial.total_degree(),
            "terms": len(polynomial.terms()),
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
            "expression": text,
        }

    def rational_summary(value):
        numerator, denominator = sp.fraction(sp.cancel(value))
        return {
            "numerator": summary(numerator),
            "denominator": summary(denominator),
        }

    return {
        "epsilon": [epsilon_1, epsilon_2],
        "field": PRIME,
        "relation_rb": summary(relation_rb),
        "t_map": rational_summary(t_map),
        "c_map": rational_summary(c_map),
        "normalized_kernel": [
            rational_summary(sp.cancel(numerator/denominator))
            for numerator, denominator in rational_kernel
        ],
        "kernel": [summary(value) for value in reduced_kernel],
        "kernel_common_denominator": summary(common_denominator),
        "kernel_removed_gcd": summary(kernel_gcd.as_expr()),
        "row_checks": row_checks,
        "all_rows_zero": all(row["zero"] for row in row_checks),
    }


@app.local_entrypoint()
def main():
    cases = tuple((epsilon_1, epsilon_2)
                  for epsilon_1 in (-1, 1) for epsilon_2 in (-1, 1))
    rows = list(compile_kernel.map(cases, order_outputs=True, return_exceptions=True))
    normalized_rows = []
    for case, row in zip(cases, rows):
        if isinstance(row, BaseException):
            normalized_rows.append({
                "epsilon": list(case), "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            row["status"] = "COMPLETE"
            normalized_rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell14-curve-kernel-v1",
        "field": PRIME,
        "scope": (
            "Exact common-route kernels on the dense cell-14 chart where the "
            "linear c-relation coefficient is nonzero."
        ),
        "source_structure_sha256": hashlib.sha256(STRUCTURE.read_bytes()).hexdigest(),
        "rows": normalized_rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {
                "epsilon": row.get("epsilon"),
                "status": row.get("status"),
                "all_rows_zero": row.get("all_rows_zero"),
                "relation": (
                    [row["relation_rb"]["degree"], row["relation_rb"]["terms"]]
                    if row.get("relation_rb") else None
                ),
                "kernel": (
                    [[item["degree"], item["terms"]] for item in row["kernel"]]
                    if row.get("kernel") else None
                ),
                "error": row.get("error"),
            }
            for row in normalized_rows
        ],
    }, sort_keys=True))
