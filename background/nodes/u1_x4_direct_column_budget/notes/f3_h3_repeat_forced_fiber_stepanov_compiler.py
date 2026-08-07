#!/usr/bin/env python3
"""Arithmetic checks for the forced-coordinate fiber Stepanov compiler."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp


C_RED = 5


@dataclass(frozen=True)
class Row:
    n: int
    forced: int
    a: int
    b: int
    d: int
    coeffs: int
    conditions: int
    degree: int
    bound: int
    ls_slack: int
    image_slack: int


def ceil_div(num: int, den: int) -> int:
    return -(-num // den)


def row(n: int, forced: int, a: int, b: int, d: int, c_red: int = C_RED) -> Row:
    if min(n, forced, a, b, d, c_red) < 1:
        raise ValueError((n, forced, a, b, d, c_red))
    coeffs = a * b**2
    conditions = c_red * d * (a + d) * forced
    degree = (a - 1) + 3 * n * (b - 1)
    image_cap = forced * (degree + 1)
    if conditions >= coeffs:
        raise AssertionError(("FF-LS fails", n, forced, a, b, d, coeffs, conditions))
    if conditions >= image_cap:
        raise AssertionError(("FF image-cap fails", n, forced, a, b, d, image_cap))
    return Row(
        n=n,
        forced=forced,
        a=a,
        b=b,
        d=d,
        coeffs=coeffs,
        conditions=conditions,
        degree=degree,
        bound=ceil_div(forced * degree, d),
        ls_slack=coeffs - conditions,
        image_slack=image_cap - conditions,
    )


def verify_degrees(a_value: int) -> dict[str, int]:
    x = sp.symbols("x")
    a = sp.Integer(a_value)
    w = sp.cancel(1 - (a - 1) * (x - 1) / (a + x - 2))
    lam = sp.cancel(a + x + w - 2)
    w_num, w_den = (sp.Poly(part, x) for part in sp.fraction(w))
    lam_num, lam_den = (sp.Poly(part, x) for part in sp.fraction(lam))
    if w_num.degree() > 1 or w_den.degree() != 1:
        raise AssertionError((a_value, w, w_num.degree(), w_den.degree()))
    if (lam_num.degree(), lam_den.degree()) != (2, 1):
        raise AssertionError((a_value, lam, lam_num.degree(), lam_den.degree()))
    if sp.factor(w_den.as_expr() - lam_den.as_expr()) != 0:
        raise AssertionError((a_value, w_den, lam_den))
    return {
        "w_num_degree": w_num.degree(),
        "w_den_degree": w_den.degree(),
        "lambda_num_degree": lam_num.degree(),
        "lambda_den_degree": lam_den.degree(),
    }


def main() -> None:
    print("h=3 repeat forced-fiber Stepanov compiler")
    for a_value in (2, 5, 17):
        degrees = verify_degrees(a_value)
        print(
            f"a={a_value} deg_w={degrees['w_num_degree']}/{degrees['w_den_degree']} "
            f"deg_lambda={degrees['lambda_num_degree']}/{degrees['lambda_den_degree']}"
        )

    rows = [
        row(n=2**13, forced=1, a=1024, b=256, d=512),
        row(n=2**16, forced=1, a=4096, b=512, d=2048),
        row(n=2**23, forced=4, a=16384, b=2048, d=8192),
        row(n=2**32, forced=16, a=65536, b=8192, d=32768),
        row(n=2**41, forced=64, a=262144, b=32768, d=131072),
    ]
    print(" n        |A_forced|      A      B      D        LS_slack     image_slack        bound")
    for item in rows:
        expected_degree = (item.a - 1) + 3 * item.n * (item.b - 1)
        if item.degree != expected_degree:
            raise AssertionError((item, expected_degree))
        print(
            f"{item.n:10d} {item.forced:10d} {item.a:7d} {item.b:6d} {item.d:7d}"
            f" {item.ls_slack:15d} {item.image_slack:15d} {item.bound:12d}"
        )
    print("FF-RED(5) supplied; remaining gate: FF-RANK/FF-NV")
    print("H3_REPEAT_FORCED_FIBER_STEPANOV_COMPILER_PASS")


if __name__ == "__main__":
    main()
