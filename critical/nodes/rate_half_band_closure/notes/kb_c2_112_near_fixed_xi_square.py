#!/usr/bin/env python3
"""Exact near-aligned positive q-slice check for one square allocation.

Normalize the common internal endpoint and the distinguished near-aligned
label to ``a=xi=2``.  Write ``J_1={c,d}``, choose ``eta=c``, and hence set
the forced square label to ``w=1/c``.  This checker treats the allocation in
which the residual over c is a square at ``tau(xi)=1/2`` and the residual
over d is a square at ``tau(d)=1/d``.

The constant-to-leading equations split into two signs at each endpoint.
Run one of the four sign-pair shards at a time.  Every shard proves that its
remaining exact q-slice ideal is supported on forbidden label collisions.
"""

import argparse
import importlib.util
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
SYMMETRIC = HERE / "kb_c2_112_positive_qslice_symmetric.py"

EXPECTED_UNIVARIATES = {
    (0, 0): lambda d: ((d - 2)**8 * (d - 1)**4 * (d + 1)**5
                       * (2 * d - 1)**9),
    (0, 1): lambda d: ((d - 2)**5 * (d - 1)**6 * (d + 1)**4
                       * (2 * d - 1)**8 * (d**2 - 9 * d + 2)**2),
    (1, 0): lambda d: ((d - 2)**9 * (d - 1)**4 * (d + 1)**4
                       * (d + 2)**2 * (2 * d - 1)**9),
    (1, 1): lambda d: ((d - 2)**8 * (d - 1)**6 * (d + 1)**4
                       * (2 * d - 1)**8 * (d**2 + 3 * d - 2)**2),
}

SURVIVOR_BASES = {
    (0, 1): lambda c, d: (2 * c + d - 9, d**2 - 9 * d + 2),
    (1, 0): lambda c, d: (2 * c + 1, d + 2),
    (1, 1): lambda c, d: (2 * c - d - 3, d**2 + 3 * d - 2),
}


def load_symmetric():
    spec = importlib.util.spec_from_file_location("positive_symmetric", SYMMETRIC)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load symmetric q-slice helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def monic(expression, *variables):
    return sp.Poly(expression, *variables, domain=sp.QQ).monic().as_expr()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("left", type=int, choices=(0, 1))
    parser.add_argument("right", type=int, choices=(0, 1))
    args = parser.parse_args()
    pair = (args.left, args.right)

    symmetric = load_symmetric()
    ((p, t, b, w), odd, coefficients, (z_numerator, z_denominator),
     relative_scale) = symmetric.reconstruct_fraction_free("fixed-moving")
    c, d, scale = sp.symbols("c d lambda_scale", nonzero=True)
    f, g, m = odd
    x0, _, x2, x3, _ = coefficients
    leading = (x2 - p * x0, x3 - t * x0)
    constant = (x0 - p * x2, x3 - t * x2)
    gamma = symmetric.scale_pair(scale, (g - p * f, m - t * f))
    leading_square = symmetric.scale_pair(
        w**2, symmetric.reduce_pair(leading, leading, p, t)
    )
    constant_square = symmetric.reduce_pair(constant, constant, p, t)
    leading_constant = symmetric.reduce_pair(leading, constant, p, t)
    gamma_square = symmetric.reduce_pair(gamma, gamma, p, t)
    middle = symmetric.add_pair(
        symmetric.scale_pair(-2 * w, leading_constant),
        symmetric.scale_pair(-w**2, gamma_square),
    )

    substitutions = {p: c * d, t: -c - d, w: 1 / c}

    def evaluate(pair_value, root):
        return sp.cancel(
            (pair_value[0] + root * pair_value[1]).subs(substitutions)
        )

    targets = ((c, sp.Rational(1, 2)), (d, 1 / d))
    endpoint_factors = []
    collision_factors = []
    for root, target in targets:
        condition = sp.cancel(
            evaluate(constant_square, root)
            - target**2 * evaluate(leading_square, root)
        )
        numerator, _ = sp.fraction(condition)
        local = []
        discarded = []
        for factor, exponent in sp.factor_list(numerator)[1]:
            polynomial = sp.Poly(factor, b, c, d, domain=sp.QQ)
            if polynomial.degree(b) == 1:
                local.append(polynomial)
            else:
                discarded.append((polynomial, exponent))
        if len(local) != 2:
            raise RuntimeError("endpoint condition did not split into two b-lines")
        endpoint_factors.append(local)
        collision_factors.append(discarded)

    # The discarded factors are q-root/J0 collisions or cd=1.
    allowed_discarded = {
        monic(value, b, c, d)
        for value in (c - 2, 2 * c - 1, d - 2, 2 * d - 1, c * d - 1)
    }
    for discarded in collision_factors:
        for polynomial, _ in discarded:
            if polynomial.monic().as_expr() not in allowed_discarded:
                raise RuntimeError("unexpected endpoint factor")
    print(f"pair={args.left},{args.right} stage=endpoint_factors", flush=True)

    left = endpoint_factors[0][args.left]
    right = endpoint_factors[1][args.right]
    left_lead = sp.Poly(left.coeff_monomial(b), c, d, domain=sp.QQ)
    left_constant = sp.Poly(left.coeff_monomial(1), c, d, domain=sp.QQ)
    exceptional = sp.groebner(
        [left_lead.as_expr(), left_constant.as_expr()], c, d,
        order="grevlex",
    )
    if len(exceptional.polys) != 1 or exceptional.polys[0].as_expr() != 1:
        raise RuntimeError("unresolved vanishing b-coefficient branch")

    endpoint_resultant = sp.resultant(left.as_expr(), right.as_expr(), b)
    factors = [
        sp.Poly(factor, c, d, domain=sp.QQ)
        for factor, exponent in sp.factor_list(endpoint_resultant)[1]
        for _ in range(exponent)
    ]
    known = {
        monic(c - 1, c, d),
        monic(c * d - 1, c, d),
        monic(5 * c * d - 4 * c - 4 * d + 5, c, d),
    }
    curves = [factor for factor in factors if factor.monic().as_expr() not in known]
    if len(curves) != 1 or len(factors) != 4:
        raise RuntimeError("unexpected endpoint resultant factorization")
    curve = curves[0]
    print(f"pair={args.left},{args.right} stage=endpoint_curve", flush=True)

    b_value = sp.cancel(-left_constant.as_expr() / left_lead.as_expr())
    scale_value = sp.cancel(
        (relative_scale[0] / relative_scale[1]).subs(substitutions)
    )
    middle_equations = []
    for root, target in targets:
        value = sp.cancel(
            (evaluate(middle, root) + 2 * target * evaluate(leading_square, root))
            .subs(scale, scale_value)
            .subs(b, b_value)
        )
        numerator, _ = sp.fraction(value)
        middle_equations.append(
            sp.Poly(sp.expand(numerator), c, d, domain=sp.QQ)
        )

    basis = sp.groebner(
        [curve.as_expr(), *(value.as_expr() for value in middle_equations)],
        c, d, order="grevlex",
    )
    if not basis.is_zero_dimensional:
        raise RuntimeError("middle equations did not cut the endpoint curve")
    print(f"pair={args.left},{args.right} stage=grevlex", flush=True)
    lex = basis.fglm(order="lex")
    univariate = next(
        sp.Poly(value.as_expr(), c, d, domain=sp.QQ)
        for value in lex.polys
        if sp.Poly(value.as_expr(), c, d).degree(c) == 0
    )
    expected = sp.Poly(EXPECTED_UNIVARIATES[pair](d), c, d, domain=sp.QQ)
    if univariate.monic() != expected.monic():
        raise RuntimeError("univariate certificate changed")

    survivor = "none"
    if pair in SURVIVOR_BASES:
        printed = SURVIVOR_BASES[pair](c, d)
        survivor_basis = sp.groebner(
            [curve.as_expr(), *(value.as_expr() for value in middle_equations),
             printed[1]],
            c, d, order="lex",
        )
        observed = {monic(value.as_expr(), c, d) for value in survivor_basis.polys}
        wanted = {monic(value, c, d) for value in printed}
        if observed != wanted:
            raise RuntimeError("exceptional survivor basis changed")
        if survivor_basis.reduce(c * d - 1)[1] != 0:
            raise RuntimeError("exceptional survivor does not force cd=1")
        survivor = "cd=1"

    print(
        "KB_C2_112_NEAR_FIXED_XI_SQUARE_PASS "
        f"pair={args.left},{args.right} endpoint_curve="
        f"{curve.degree(c)},{curve.degree(d)} "
        f"univariate_degree={univariate.degree(d)} survivor={survivor}"
    )


if __name__ == "__main__":
    main()
