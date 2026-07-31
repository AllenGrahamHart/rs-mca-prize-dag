#!/usr/bin/env python3
"""Independent symbolic audit of the projective-root reconstruction."""

import sympy as sp


b, d, T, W = sp.symbols("b d T W", nonzero=True)
a = sp.Rational(2)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def edge(left, right):
    return sp.Matrix([left * right, -left - right, 1])


def residual(expression):
    numerator, denominator = sp.fraction(sp.cancel(expression))
    quotient, remainder = sp.div(sp.Poly(numerator, W), sp.Poly(W**2, W))
    require(remainder.is_zero, "W^2 audit")
    return sp.cancel(quotient.as_expr() / denominator)


z = sp.cancel((d - 2) / (2 - 4 * d))
V = sp.Matrix([-d, 1 + W, -d * W])
checked = 0
for template in ("fixed-moving", "moving-moving"):
    at_z = V.subs(W, z)
    ell_1 = at_z[2]
    ell_0 = at_z[1] + a * ell_1
    if template == "fixed-moving":
        first, second, r, s = edge(a, 1 / a), edge(a, b), 1 / a, b
    else:
        first, second, r, s = edge(a, b), edge(a, 1 / b), b, 1 / b
    target = sp.Matrix([
        sp.cancel(value)
        for value in (
            ((ell_0 + s * ell_1) * first
             + (ell_0 + r * ell_1) * second) / (s - r)
        )
    ])

    coefficients = sp.symbols("x0:5")
    x0, x1, x2, x3, x4 = coefficients
    U_raw = sp.Matrix([
        x0 + x1 * W + x2 * W**2,
        x3 * (1 + W**2) + x4 * W,
        x2 + x1 * W + x0 * W**2,
    ])
    equations = [
        x2,
        x0 + d * x3,
        *(U_raw[index].subs(W, z) - target[index] for index in range(3)),
    ]
    matrix, right = sp.linear_eq_to_matrix(equations, coefficients)
    solution = [sp.cancel(value) for value in matrix.inv(method="DM") * right]
    U = sp.Matrix([
        sp.cancel(value.subs(dict(zip(coefficients, solution))))
        for value in U_raw
    ])
    require(all(sp.cancel(equation.subs(dict(zip(coefficients, solution)))) == 0
                for equation in equations), "five-equation reconstruction")

    U_T = sp.expand(U[0] + T * U[1] + T**2 * U[2])
    V_T = sp.expand(V[0] + T * V[1] + T**2 * V[2])
    G = sp.expand(U_T**2 - W * V_T**2)
    finite = sp.expand(G.subs(T, d))
    infinity = sp.Poly(G, T).nth(4)
    require(sp.cancel(infinity - (U[2]**2 - W * V[2]**2)) == 0,
            "infinity coefficient")
    finite_residual = residual(finite)
    infinity_residual = residual(infinity)
    product = sp.Poly(
        sp.cancel(finite_residual * infinity_residual), W,
        domain=sp.QQ.frac_field(b, d),
    )
    require(product.degree() == 4, "projective product degree")

    if template == "moving-moving":
        for xi in (a, 1 / a):
            target_poly = sp.Poly(
                (W - 1 / xi)**2 * (W - 1 / d)**2, W,
                domain=sp.QQ.frac_field(b, d),
            )
            for degree in range(4):
                value = sp.cancel(
                    product.nth(degree)
                    - product.nth(4) * target_poly.nth(degree)
                )
                numerator, _ = sp.fraction(value)
                poly = sp.Poly(numerator, b, domain=sp.QQ.frac_field(d))
                require(all(
                    sp.cancel(poly.nth(index) - poly.nth(poly.degree() - index)) == 0
                    for index in range(poly.degree() + 1)
                ), "moving reciprocity")

        sx0, sx1, sx2, sx3, sx4 = solution
        finite_constant = sp.cancel(sx1 * (1 + d*d) + d * sx4)
        finite_leading = sp.cancel(sx2 + d * sx3 + d*d * sx0)
        require(
            sp.cancel(product.nth(0) - (finite_constant * sx1)**2) == 0,
            "constant square",
        )
        require(
            sp.cancel(product.nth(4) - (finite_leading * sx0)**2) == 0,
            "leading square",
        )
        left = b * d * finite_constant * sx1
        right_factor = finite_leading * sx0
        constant_gate = sp.cancel(
            product.nth(0) - product.nth(4) / (b*b*d*d)
        )
        require(
            sp.cancel(constant_gate - (left-right_factor)*(left+right_factor)
                      / (b*b*d*d)) == 0,
            "other-xi sign split",
        )
    checked += 1

print(
    "KB_C2_112_NEAR_POSITIVE_PROJECTIVE_AUDIT_PASS "
    f"templates={checked} finite_root=true infinity_root=true sign_split=true"
)
