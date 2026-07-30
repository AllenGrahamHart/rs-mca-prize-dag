#!/usr/bin/env python3
"""Exact near-aligned positive q-slice check for one square allocation.

Normalize the common internal endpoint and the distinguished near-aligned
label to ``a=xi=2``.  Write ``J_1={c,d}``, choose ``eta=c``, and hence set
the forced square label to ``w=1/c``.  This checker treats the allocation in
which the residual over c is a square at ``tau(xi)=1/2`` and the residual
over d is a square at ``tau(d)=1/d``.

The constant-to-leading equations split into two signs at each endpoint.
Run one of the four sign-pair shards at a time.  This is an exploratory exact
elimination helper; it emits INCOMPLETE rather than certifying a deletion.
"""

import argparse
import hashlib
import importlib.util
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
SYMMETRIC = HERE / "kb_c2_112_positive_qslice_symmetric.py"

def load_symmetric():
    spec = importlib.util.spec_from_file_location("positive_symmetric", SYMMETRIC)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load symmetric q-slice helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def monic(expression, *variables):
    return sp.Poly(expression, *variables, domain=sp.QQ).monic().as_expr()


def polynomial_digest(polynomials, *variables):
    payload = []
    for value in polynomials:
        polynomial = sp.Poly(value, *variables, domain=sp.QQ).monic()
        payload.append([
            (monomial, str(coefficient))
            for monomial, coefficient in polynomial.terms()
        ])
    return hashlib.sha256(repr(payload).encode("ascii")).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("left", type=int, choices=(0, 1))
    parser.add_argument("right", type=int, choices=(0, 1))
    args = parser.parse_args()
    pair = (args.left, args.right)

    symmetric = load_symmetric()
    ((p, t, b, w), _, coefficients, _,
     _) = symmetric.reconstruct_fraction_free("fixed-moving")
    print(f"pair={args.left},{args.right} stage=reconstruction", flush=True)
    c, d = sp.symbols("c d", nonzero=True)
    x0, _, x2, x3, _ = coefficients
    leading = (x2 - p * x0, x3 - t * x0)
    constant = (x0 - p * x2, x3 - t * x2)
    leading_square = symmetric.scale_pair(
        w**2, symmetric.reduce_pair(leading, leading, p, t)
    )
    constant_square = symmetric.reduce_pair(constant, constant, p, t)

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
        print(
            f"pair={args.left},{args.right} stage=endpoint_{len(endpoint_factors)}",
            flush=True,
        )

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
    # ``Poly(..., b, c, d).coeff_monomial(b)`` would keep only the exact
    # monomial b*c^0*d^0.  Differentiate in b to retain its full coefficient
    # in QQ[c,d].
    left_lead = sp.Poly(sp.diff(left.as_expr(), b), c, d, domain=sp.QQ)
    left_constant = sp.Poly(left.as_expr().subs(b, 0), c, d, domain=sp.QQ)
    exceptional = sp.groebner(
        [left_lead.as_expr(), left_constant.as_expr()], c, d,
        order="grevlex",
    )
    exceptional_unit = (
        len(exceptional.polys) == 1 and exceptional.polys[0].as_expr() == 1
    )
    exceptional_shapes = [
        (value.total_degree(), len(value.terms()))
        for value in exceptional.polys
    ]
    exceptional_digest = polynomial_digest(
        [value.as_expr() for value in exceptional.polys], c, d
    )
    print(
        f"pair={args.left},{args.right} stage=leading_branch "
        f"unit={exceptional_unit} shapes={exceptional_shapes} "
        f"digest={exceptional_digest}",
        flush=True,
    )

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
    b_numerator, b_denominator = sp.fraction(b_value)
    b_shapes = tuple(
        (sp.Poly(value, c, d, domain=sp.QQ).degree(c),
         sp.Poly(value, c, d, domain=sp.QQ).degree(d))
        for value in (b_numerator, b_denominator)
    )
    print(
        "KB_C2_112_NEAR_FIXED_XI_SQUARE_INCOMPLETE "
        f"pair={args.left},{args.right} endpoint_curve="
        f"{curve.degree(c)},{curve.degree(d)} "
        f"generic_b_shapes={b_shapes} "
        f"leading_branch_unit={exceptional_unit}"
    )


if __name__ == "__main__":
    main()
