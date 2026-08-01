#!/usr/bin/env python3
"""Exact common-fiber kernel for positive coordinate three-loop packets."""

import sympy as sp


def product_row(w, product, loop_zero, loop_infinity, loop_one):
    """Coefficients on (d0,d1,d2,beta) of A0(w)-product*A2(w)."""
    return (
        -loop_zero**2 + (loop_zero**2 - loop_one**2) * w - product,
        -(loop_one**2 + product) * w,
        (loop_infinity**2 - loop_one**2) * w
        - (loop_infinity**2 + product) * w**2,
        sp.Integer(0),
    )


def sum_row(source, target_sum):
    """Coefficients of source*B1(w)+target_sum*A2(w), w=source^2."""
    w = source**2
    return (
        target_sum,
        target_sum * w,
        target_sum * w**2,
        source * (w - 1),
    )


def common_matrix(loop_zero, loop_infinity, loop_one, records):
    rows = []
    for source, product, target_sum in records:
        rows.append(
            product_row(
                source**2,
                product,
                loop_zero,
                loop_infinity,
                loop_one,
            )
        )
        rows.append(sum_row(source, target_sum))
    return sp.Matrix(rows)


def loop_interpolant(loop_zero, loop_infinity, loop_one, d0, d1, d2, w):
    """The forced A0 after loops at quotient labels 0, infinity, and 1."""
    e1 = (
        (loop_zero**2 - loop_one**2) * d0
        - loop_one**2 * d1
        + (loop_infinity**2 - loop_one**2) * d2
    )
    return -loop_zero**2 * d0 + e1 * w - loop_infinity**2 * d2 * w**2


def verify_loop_interpolation():
    a0, ai, a1, d0, d1, d2, w = sp.symbols("a0 ai a1 d0 d1 d2 w")
    denominator = d0 + d1 * w + d2 * w**2
    numerator = loop_interpolant(a0, ai, a1, d0, d1, d2, w)
    checks = (
        numerator.subs(w, 0) + a0**2 * denominator.subs(w, 0),
        numerator.subs(w, 1) + a1**2 * denominator.subs(w, 1),
        sp.Poly(numerator, w).coeff_monomial(w**2) + ai**2 * d2,
    )
    if any(sp.expand(value) != 0 for value in checks):
        raise RuntimeError("loop interpolation")

    p, s, z = sp.symbols("p s z")
    h = sp.Matrix((d0, d1, d2, sp.symbols("beta")))
    product_identity = sp.expand(
        sp.Matrix([product_row(w, p, a0, ai, a1)]) * h
    )
    if product_identity != sp.Matrix([[sp.expand(numerator - p * denominator)]]):
        raise RuntimeError("product row")
    sum_identity = sp.expand(sp.Matrix([sum_row(z, s)]) * h)
    expected_sum = sp.Matrix(
        [[sp.expand(s * denominator.subs(w, z**2) + z * h[3] * (z**2 - 1))]]
    )
    if sum_identity != expected_sum:
        raise RuntimeError("sum row")


def representative_factorizations():
    x, y, b, c = sp.symbols("x y b c")

    matrix_442 = common_matrix(
        1,
        b,
        c,
        ((x, b, 1 + b), (y, -b, 1 - b)),
    )
    guards_442 = (
        -x
        * y
        * (b - 1)
        * (b + 1)
        * (x - 1)
        * (x + 1)
        * (x - y)
        * (x + y)
        * (y - 1)
        * (y + 1)
    )
    residual_442 = (
        (y - x) * (b**2 - c**2)
        + b * x * y * (x + y) * (c**2 - 1)
    )

    matrix_433 = common_matrix(
        1,
        b,
        c,
        ((x, b, 1 + b), (y, c, 1 + c)),
    )
    guards_433 = (
        x
        * y
        * (b + 1)
        * (c + 1)
        * (x - 1)
        * (x + 1)
        * (x - y)
        * (x + y)
        * (y - 1)
        * (y + 1)
    )
    residual_433 = (
        (y - x) * (b**2 - c**2)
        + (c - 1)
        * x
        * y
        * (b * (c + 1) * x - (b**2 + c) * y)
    )

    records = (
        ("442", matrix_442, guards_442, residual_442),
        ("433", matrix_433, guards_433, residual_433),
    )
    for name, matrix, guards, residual in records:
        if sp.expand(matrix.det() - guards * residual) != 0:
            raise RuntimeError(f"{name} determinant factorization")
    return records


def verify():
    verify_loop_interpolation()
    records = representative_factorizations()
    return {
        name: {
            "rows": matrix.rows,
            "columns": matrix.cols,
            "residual_total_degree": sp.total_degree(residual),
        }
        for name, matrix, _, residual in records
    }


def main():
    result = verify()
    dimensions = ",".join(
        f"{value['rows']}x{value['columns']}" for value in result.values()
    )
    degrees = ",".join(
        str(value["residual_total_degree"]) for value in result.values()
    )
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_COMMON_KERNEL_PASS "
        f"profiles={len(result)} matrices={dimensions} residual_degrees={degrees}"
    )


if __name__ == "__main__":
    main()
