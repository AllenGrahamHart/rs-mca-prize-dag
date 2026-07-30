#!/usr/bin/env python3
"""Two-variable slices of the aligned positive q-slice constant mismatch."""

import argparse

import sympy as sp


def edge(left, right):
    return sp.Matrix([left * right, -(left + right), 1])


def reciprocal_reduce(expression, b, w, trace):
    poly = sp.Poly(expression, b)
    degree = poly.degree()
    if degree % 2:
        raise RuntimeError(f"odd reciprocal degree {degree}")
    middle = degree // 2
    for index in range(degree + 1):
        if sp.expand(poly.nth(index) - poly.nth(degree - index)) != 0:
            raise RuntimeError("non-palindromic moving mismatch")
    traces = [sp.Integer(2), trace]
    for _ in range(2, middle + 1):
        traces.append(sp.expand(trace * traces[-1] - traces[-2]))
    reduced = poly.nth(middle)
    for offset in range(1, middle + 1):
        reduced += poly.nth(middle + offset) * traces[offset]
    return sp.Poly(sp.expand(reduced), trace, w, domain=sp.QQ)


def mismatch_slice(template, c_value, d_value, full, saturate, lex_audit,
                   moving_invariant_audit, symbolic_d):
    a = sp.Rational(2)
    c = sp.Rational(c_value)
    d = sp.Symbol("d", nonzero=True) if symbolic_d else sp.Rational(d_value)
    b, w, W = sp.symbols("b w W", nonzero=True)
    q0, q1 = c * d, -(c + d)
    f, g, m = q0 - w, 1 - w * q0, q1 * (1 - w)
    v = sp.Matrix([f + g * W, m * (1 + W), g + f * W])
    z = sp.cancel(-(f + m * a + g * a**2) / (g + m * a + f * a**2))
    vz = v.subs(W, z)
    l1, l0 = vz[2], vz[1] + a * vz[2]
    if template == "fixed-moving":
        first, second, r, s = edge(a, 1 / a), edge(a, b), 1 / a, b
    else:
        first, second, r, s = edge(a, b), edge(a, 1 / b), b, 1 / b
    target = sp.Matrix([
        sp.cancel(value)
        for value in (((l0 + s * l1) * first
                       + (l0 + r * l1) * second) / (s - r))
    ])
    print(f"template={template} c={c} d={d} target=READY", flush=True)

    x1, x4 = sp.symbols("x1 x4")
    target0, target2 = target[0] - x1 * z, target[2] - x1 * z
    pair_denominator = 1 - z**4
    x0 = (target0 - z**2 * target2) / pair_denominator
    x2 = (target2 - z**2 * target0) / pair_denominator
    x3 = (target[1] - x4 * z) / (1 + z**2)
    equations = sp.Matrix([
        sp.together(x0 + x1 * w + x2 * w**2
                    - q0 * (x2 + x1 * w + x0 * w**2)),
        sp.together(x3 * (1 + w**2) + x4 * w
                    - q1 * (x2 + x1 * w + x0 * w**2)),
    ])
    coefficient = equations.jacobian([x1, x4])
    constant = equations.subs({x1: 0, x4: 0})
    solution = coefficient.inv(method="DM") * (-constant)
    substitutions = {x1: solution[0], x4: solution[1]}
    x0, x2, x3 = [sp.cancel(value.subs(substitutions))
                  for value in (x0, x2, x3)]
    x1_solution, x4_solution = solution
    print(f"template={template} c={c} d={d} forced_solve=PASS", flush=True)

    def endpoint(root):
        return (x0 + root * x3 + root**2 * x2,
                x2 + root * x3 + root**2 * x0)

    c0, c2 = endpoint(c)
    d0, d2 = endpoint(d)
    mismatch = sp.cancel((c0 * d0 / (w**2 * c2 * d2))**2
                         - 1 / (c**2 * d**2))
    numerator, denominator = sp.fraction(mismatch)
    print(f"constant_mismatch_numerator={sp.factor(numerator)}", flush=True)
    print(f"constant_mismatch_denominator={sp.factor(denominator)}", flush=True)
    if not full:
        return

    field = sp.QQ.frac_field(b, w)
    u = sp.Matrix([
        x0 + x1_solution * W + x2 * W**2,
        x3 * (1 + W**2) + x4_solution * W,
        x2 + x1_solution * W + x0 * W**2,
    ])
    residuals = []
    for name, root in (("c", c), ("d", d)):
        u_root = sum(u[index] * root**index for index in range(3))
        v_root = sum(v[index] * root**index for index in range(3))
        norm = sp.Poly(u_root, W, domain=field)**2
        norm -= sp.Poly(W, W, domain=field) * sp.Poly(v_root, W, domain=field)**2
        residual, remainder = norm.div(sp.Poly((W - w)**2, W, domain=field))
        if not remainder.is_zero:
            raise RuntimeError(f"forced division failed at {name}")
        residuals.append(residual)
    observed = (residuals[0] * residuals[1]).monic()
    expected = sp.Poly((W - 1 / c)**2 * (W - 1 / d)**2,
                       W, domain=field).monic()
    differences = observed - expected
    mismatch_numerators = []
    mismatch_denominators = []
    for degree in range(4):
        value = sp.cancel(differences.nth(degree))
        value_numerator, value_denominator = sp.fraction(value)
        mismatch_numerators.append(value_numerator)
        mismatch_denominators.append(value_denominator)
        poly = sp.Poly(value_numerator, b, w, domain=sp.QQ)
        print(
            f"full_mismatch_W_degree={degree} total_degree={poly.total_degree()} "
            f"terms={len(poly.terms())}",
            flush=True,
        )
    denominator_product = sp.Poly(
        sp.prod(mismatch_denominators), b, w, domain=sp.QQ
    ).sqf_part().as_expr()
    if moving_invariant_audit:
        if template != "moving-moving":
            raise RuntimeError("moving invariant audit requires moving-moving")
        trace = sp.Symbol("trace")
        reduced = [reciprocal_reduce(value, b, w, trace)
                   for value in mismatch_numerators]
        for index, poly in enumerate(reduced):
            print(
                f"moving_trace_W_degree={index} "
                f"total_degree={poly.total_degree()} terms={len(poly.terms())}",
                flush=True,
            )
        print(f"template={template} c={c} d={d} trace_groebner=START", flush=True)
        trace_basis = sp.groebner(
            [poly.as_expr() for poly in reduced], trace, w, order="grevlex"
        )
        print(
            f"trace_groebner_zero_dimensional={trace_basis.is_zero_dimensional} "
            f"trace_groebner_basis_size={len(trace_basis.polys)}",
            flush=True,
        )
        trace_lex = trace_basis.fglm(order="lex")
        for index, poly in enumerate(trace_lex.polys):
            as_poly = sp.Poly(poly.as_expr(), trace, w, domain=sp.QQ)
            print(
                f"trace_lex_polynomial={index} "
                f"trace_degree={as_poly.degree(trace)} "
                f"w_degree={as_poly.degree(w)} terms={len(as_poly.terms())}",
                flush=True,
            )
        trace_univariate = next(
            poly.as_expr() for poly in trace_lex.polys
            if sp.Poly(poly.as_expr(), trace, w).degree(trace) == 0
        )
        trace_linear = next(
            poly.as_expr() for poly in trace_lex.polys
            if sp.Poly(poly.as_expr(), trace, w).degree(trace) == 1
        )
        linear_in_trace = sp.Poly(
            trace_linear, trace, domain=sp.QQ.frac_field(w)
        )
        trace_lead = linear_in_trace.coeff_monomial(trace)
        trace_constant = linear_in_trace.coeff_monomial(1)
        trace_univariate_poly = sp.Poly(trace_univariate, w, domain=sp.QQ)
        trace_lead_numerator, _ = sp.fraction(sp.cancel(trace_lead))
        trace_lead_gcd = sp.gcd(
            trace_univariate_poly, sp.Poly(trace_lead_numerator, w)
        )
        reduced_denominator = reciprocal_reduce(
            denominator_product, b, w, trace
        ).as_expr()
        denominator_substitution = sp.cancel(
            reduced_denominator.subs(trace, -trace_constant / trace_lead)
        )
        denominator_numerator, _ = sp.fraction(denominator_substitution)
        trace_denominator_gcd = sp.gcd(
            trace_univariate_poly, sp.Poly(denominator_numerator, w)
        )
        print(
            f"trace_lex_basis_size={len(trace_lex.polys)} "
            f"trace_univariate={sp.factor(trace_univariate)}",
            flush=True,
        )
        print(
            f"trace_linear_lead_gcd={sp.factor(trace_lead_gcd.as_expr())} "
            f"trace_denominator_gcd="
            f"{sp.factor(trace_denominator_gcd.as_expr())}",
            flush=True,
        )
        rational_roots = []
        _, factors = sp.factor_list(trace_univariate_poly.as_expr())
        for factor, _ in factors:
            factor_poly = sp.Poly(factor, w, domain=sp.QQ)
            if factor_poly.degree() != 1:
                continue
            root = -factor_poly.nth(0) / factor_poly.nth(1)
            if root in (1, -1):
                continue
            trace_value = sp.cancel(
                (-trace_constant / trace_lead).subs(w, root)
            )
            z_value = sp.cancel(z.subs(w, root))
            forbidden = (a, 1 / a, c, 1 / c, d, 1 / d,
                         root, 1 / root, z_value, 1 / z_value)
            forbidden_traces = {sp.cancel(value + 1 / value)
                                for value in forbidden}
            admissible = (trace_value not in forbidden_traces
                          and trace_value not in (2, -2)
                          and z_value not in (1, -1)
                          and len(set(forbidden)) == len(forbidden))
            rational_roots.append({
                "w": root,
                "trace": trace_value,
                "z": z_value,
                "b_discriminant": sp.factor(trace_value**2 - 4),
                "labels_distinct": admissible,
            })
        print(f"moving_rational_survivors={rational_roots}", flush=True)
        return
    print(f"template={template} c={c} d={d} groebner=START", flush=True)
    basis = sp.groebner(mismatch_numerators, b, w, order="grevlex")
    print(
        f"groebner_zero_dimensional={basis.is_zero_dimensional} "
        f"groebner_basis_size={len(basis.polys)}",
        flush=True,
    )
    if lex_audit:
        print(f"template={template} c={c} d={d} fglm=START", flush=True)
        lex_basis = basis.fglm(order="lex")
        print(f"lex_basis_size={len(lex_basis.polys)}", flush=True)
        for index, poly in enumerate(lex_basis.polys):
            expression = poly.as_expr()
            as_poly = sp.Poly(expression, b, w, domain=sp.QQ)
            print(
                f"lex_polynomial={index} b_degree={as_poly.degree(b)} "
                f"w_degree={as_poly.degree(w)} terms={len(as_poly.terms())}",
                flush=True,
            )
        univariate = next(poly.as_expr() for poly in lex_basis.polys
                          if sp.Poly(poly.as_expr(), b, w).degree(b) == 0)
        linear = next(poly.as_expr() for poly in lex_basis.polys
                      if sp.Poly(poly.as_expr(), b, w).degree(b) == 1)
        linear_in_b = sp.Poly(linear, b, domain=sp.QQ.frac_field(w))
        linear_lead = linear_in_b.coeff_monomial(b)
        linear_constant = linear_in_b.coeff_monomial(1)
        univariate_poly = sp.Poly(univariate, w, domain=sp.QQ)
        lead_numerator, _ = sp.fraction(sp.cancel(linear_lead))
        lead_gcd = sp.gcd(univariate_poly, sp.Poly(lead_numerator, w))
        denominator_substitution = sp.cancel(
            denominator_product.subs(b, -linear_constant / linear_lead)
        )
        denominator_numerator, _ = sp.fraction(denominator_substitution)
        denominator_gcd = sp.gcd(
            univariate_poly, sp.Poly(denominator_numerator, w)
        )
        complementary_factor = univariate_poly.exquo(lead_gcd)
        complementary_denominator_gcd = sp.gcd(
            complementary_factor, sp.Poly(denominator_numerator, w)
        )
        print(
            f"lex_univariate_degree={univariate_poly.degree()} "
            f"linear_lead_gcd_degree={lead_gcd.degree()} "
            f"denominator_gcd_degree={denominator_gcd.degree()} "
            f"complementary_degree={complementary_factor.degree()} "
            f"complementary_denominator_gcd_degree="
            f"{complementary_denominator_gcd.degree()}",
            flush=True,
        )
        print(
            f"complementary_factor={sp.factor(complementary_factor.as_expr())}",
            flush=True,
        )
        print(f"linear_lead_gcd={sp.factor(lead_gcd.as_expr())}", flush=True)
        print(f"denominator_gcd={sp.factor(denominator_gcd.as_expr())}", flush=True)
    if not saturate:
        return
    saturation_variable = sp.Symbol("saturation_variable")
    print(
        f"template={template} c={c} d={d} saturation=START "
        f"denominator_degree={sp.Poly(denominator_product, b, w).total_degree()}",
        flush=True,
    )
    saturated_basis = sp.groebner(
        [*mismatch_numerators,
         saturation_variable * denominator_product - 1],
        saturation_variable,
        b,
        w,
        order="grevlex",
    )
    saturated_unit = (len(saturated_basis.polys) == 1
                      and saturated_basis.polys[0].as_expr() == 1)
    print(
        f"saturated_unit_ideal={saturated_unit} "
        f"saturated_basis_size={len(saturated_basis.polys)}",
        flush=True,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("template", choices=("fixed-moving", "moving-moving"))
    parser.add_argument("c", type=int)
    parser.add_argument("d", type=int)
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--saturate", action="store_true")
    parser.add_argument("--lex-audit", action="store_true")
    parser.add_argument("--moving-invariant-audit", action="store_true")
    parser.add_argument("--symbolic-d", action="store_true")
    args = parser.parse_args()
    mismatch_slice(args.template, args.c, args.d,
                   args.full or args.saturate or args.lex_audit
                   or args.moving_invariant_audit,
                   args.saturate,
                   args.lex_audit,
                   args.moving_invariant_audit,
                   args.symbolic_d)


if __name__ == "__main__":
    main()
