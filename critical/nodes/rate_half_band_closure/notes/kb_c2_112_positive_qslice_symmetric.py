#!/usr/bin/env python3
"""Bounded symmetric algebra for the aligned positive q-slice.

The roots ``c,d`` occur only through ``p=cd`` and ``t=-(c+d)``.  Working
in ``Q(p,t)`` avoids the large expression tree created by adjoining both
roots. The calculation forms the three possible residual-factor allocations
without a Groebner basis.

The allocation minors and their multivariate gcds are necessary-condition
generators only.  A gcd does not exclude isolated simultaneous zeros, so this
script is not an aligned-positive deletion certificate by itself.
"""

import argparse
import itertools

import sympy as sp


def reduce_pair(left, right, p, t):
    """Multiply linear representatives modulo T^2+tT+p."""
    a0, a1 = left
    b0, b1 = right
    return (
        sp.expand(a0 * b0 - p * a1 * b1),
        sp.expand(a0 * b1 + a1 * b0 - t * a1 * b1),
    )


def add_pair(left, right):
    return tuple(sp.expand(a + b) for a, b in zip(left, right))


def scale_pair(scalar, pair):
    return tuple(sp.expand(scalar * value) for value in pair)


def reconstruct_fraction_free(template):
    """Return one polynomial representative of the reconstructed U form."""
    p, t, b, w = sp.symbols("p t b w", nonzero=True)
    alpha = p + 2 * t + 4
    beta = 1 + 2 * t + 4 * p
    z_numerator = w * beta - alpha
    z_denominator = beta - w * alpha

    f = p - w
    g = 1 - w * p
    m = t * (1 - w)
    l1 = sp.expand(g * z_denominator + f * z_numerator)
    l0 = sp.expand(m * (z_denominator + z_numerator) + 2 * l1)

    # Omit the common nonzero edge denominator and clear the harmless 2 or
    # b denominator.  This only rescales the projective target U(T,z).
    if template == "fixed-moving":
        target0 = 2 * (1 + 2 * b) * l0 + 4 * b * l1
        target1 = -(2 * b + 9) * l0 - 2 * (1 + 3 * b) * l1
        target2 = 4 * l0 + (2 * b + 1) * l1
    else:
        target0 = 2 * (b**2 + 1) * l0 + 4 * b * l1
        target1 = -(b**2 + 4 * b + 1) * l0 - 2 * (b**2 + b + 1) * l1
        target2 = 2 * b * l0 + (b**2 + 1) * l1
    target0, target1, target2 = map(sp.expand, (target0, target1, target2))

    d2 = z_denominator**2
    nd = z_numerator * z_denominator
    n2 = z_numerator**2
    e = 1 - p * w**2
    h = w * (1 - p)
    j = w**2 - p
    rhs0 = target0 * d2
    rhs2 = target2 * d2

    determinant = sp.expand(
        (d2 - n2) * (nd * (j + e) - h * (d2 + n2))
    )
    x0 = sp.expand(rhs0 * (nd * j - d2 * h)
                   + rhs2 * (n2 * h - nd * j))
    x1 = sp.expand(rhs2 * (d2 * j - n2 * e)
                   - rhs0 * (n2 * j - d2 * e))
    x2 = sp.expand(rhs2 * (nd * e - d2 * h)
                   + rhs0 * (n2 * h - nd * e))

    u2_at_w = sp.expand(x2 + w * x1 + w**2 * x0)
    middle_rhs0 = target1 * d2 * determinant
    middle_rhs1 = t * u2_at_w
    middle_determinant = sp.expand(
        w * (d2 + n2) - nd * (1 + w**2)
    )
    x3 = sp.expand(w * middle_rhs0 - nd * middle_rhs1)
    x4 = sp.expand((d2 + n2) * middle_rhs1
                   - (1 + w**2) * middle_rhs0)
    x0, x1, x2 = (sp.expand(middle_determinant * value)
                  for value in (x0, x1, x2))

    # Cramer's rule introduced one common projective content.  Exact
    # division here is the fraction-free analogue of cancelling it from all
    # five rational coefficients before any norm or mismatch is formed.
    common = ((p - 1) * (w - 1)**4 * (w + 1)**4
              * alpha * beta * z_denominator**2)
    if template == "fixed-moving":
        common *= 5 * p + 4 * t + 5
    ring_variables = (b, w, p, t)
    common_poly = sp.Poly(common, *ring_variables)
    primitive = tuple(
        sp.Poly(value, *ring_variables).exquo(common_poly).as_expr()
        for value in (x0, x1, x2, x3, x4)
    )
    return ((p, t, b, w), (f, g, m), primitive,
            (z_numerator, z_denominator))


def audit_reconstruction(template, variables, coefficients):
    """Compare the symbolic output with an independent exact matrix solve."""
    p, t, b, w = variables
    a = sp.Rational(2)
    c, d, b_value, w_value = map(sp.Rational, (3, 7, 5, 11))
    substitutions = {
        p: c * d,
        t: -(c + d),
        b: b_value,
        w: w_value,
    }
    f = c * d - w_value
    g = 1 - w_value * c * d
    m = -(c + d) * (1 - w_value)
    z = sp.cancel(-(f + m * a + g * a**2)
                  / (g + m * a + f * a**2))
    v_at_z = sp.Matrix([f + g * z, m * (1 + z), g + f * z])
    l1 = v_at_z[2]
    l0 = v_at_z[1] + a * l1

    def edge(left, right):
        return sp.Matrix([left * right, -(left + right), 1])

    if template == "fixed-moving":
        first, second = edge(a, 1 / a), edge(a, b_value)
        r, s = 1 / a, b_value
    else:
        first, second = edge(a, b_value), edge(a, 1 / b_value)
        r, s = b_value, 1 / b_value
    target = ((l0 + s * l1) * first + (l0 + r * l1) * second) / (s - r)

    def evaluation(point):
        return (
            sp.Matrix([1, point, point**2, 0, 0]).T,
            sp.Matrix([0, 0, 0, 1 + point**2, point]).T,
            sp.Matrix([point**2, point, 1, 0, 0]).T,
        )

    at_w = evaluation(w_value)
    at_z = evaluation(z)
    matrix = sp.Matrix.vstack(
        at_w[0] - c * d * at_w[2],
        at_w[1] + (c + d) * at_w[2],
        *at_z,
    )
    direct = matrix.inv(method="DM") * sp.Matrix([0, 0, *target])
    generated = sp.Matrix([
        value.subs(substitutions) for value in coefficients
    ])
    pivot = next(index for index, value in enumerate(direct) if value != 0)
    if generated[pivot] == 0 or any(
        sp.expand(generated[index] * direct[pivot]
                  - generated[pivot] * direct[index]) != 0
        for index in range(5)
    ):
        raise RuntimeError(f"{template} fraction-free reconstruction mismatch")


def allocation_equations(template, allocation, variables, leading, constant,
                         gamma):
    """Equations for one of the three UFD allocations of the target square."""
    p, t, b, w = variables
    leading_square = scale_pair(w**2, reduce_pair(leading, leading, p, t))
    constant_square = reduce_pair(constant, constant, p, t)
    leading_constant = reduce_pair(leading, constant, p, t)
    gamma_square = reduce_pair(gamma, gamma, p, t)
    middle = add_pair(scale_pair(-2 * w, leading_constant),
                      scale_pair(-w**2, gamma_square))
    root = (sp.Integer(0), sp.Integer(1))
    root_square = (-p, -t)

    if allocation == "same":
        first = add_pair(reduce_pair(root, middle, p, t),
                         scale_pair(2, leading_square))
        second = add_pair(reduce_pair(root_square, constant_square, p, t),
                          scale_pair(-1, leading_square))
    elif allocation == "swap":
        first = add_pair(scale_pair(p, middle),
                         scale_pair(2, reduce_pair(root, leading_square, p, t)))
        second = add_pair(scale_pair(p**2, constant_square),
                          scale_pair(-1, reduce_pair(
                              root_square, leading_square, p, t)))
    else:
        first = add_pair(scale_pair(p, middle),
                         scale_pair(-t, leading_square))
        second = add_pair(scale_pair(p, constant_square),
                          scale_pair(-1, leading_square))

    equations = [sp.Poly(value, b, w, p, t) for value in (*first, *second)]
    common = equations[0]
    for equation in equations[1:]:
        common = sp.gcd(common, equation)
    primitive = [equation.exquo(common) for equation in equations]
    shapes = [
        (item.total_degree(), item.degree(b), item.degree(w), len(item.terms()))
        for item in primitive
    ]
    print(
        f"allocation={allocation} common_degree={common.total_degree()} "
        f"common_terms={len(common.terms())} "
        f"primitive_shapes={shapes}",
        flush=True,
    )
    return common, primitive


def ramified_allocation_equations(template, allocation, variables,
                                  coefficients):
    """Allocation equations at the repaired forced label w=0."""
    p, t, b, w = variables
    specialized = [sp.Poly(value.subs(w, 0), b, p, t, domain=sp.QQ)
                   for value in coefficients]
    coefficient_content = specialized[0]
    for value in specialized[1:]:
        coefficient_content = sp.gcd(coefficient_content, value)
    x0, x1, x2, x3, x4 = [
        value.exquo(coefficient_content).as_expr() for value in specialized
    ]
    print(
        f"template={template} ramified_coefficient_content="
        f"{sp.factor(coefficient_content.as_expr())}",
        flush=True,
    )

    leading = (sp.expand(x2 - p * x0), sp.expand(x3 - t * x0))
    linear = (sp.expand((1 - p) * x1), sp.expand(x4 - t * x1))
    gamma = (1 - p**2, t * (1 - p))
    leading_square = reduce_pair(leading, leading, p, t)
    constant_square = reduce_pair(linear, linear, p, t)
    leading_linear = reduce_pair(leading, linear, p, t)
    gamma_square = reduce_pair(gamma, gamma, p, t)
    middle = add_pair(scale_pair(2, leading_linear),
                      scale_pair(-1, gamma_square))
    root = (sp.Integer(0), sp.Integer(1))
    root_square = (-p, -t)

    if allocation == "same":
        first = add_pair(reduce_pair(root, middle, p, t),
                         scale_pair(2, leading_square))
        second = add_pair(reduce_pair(root_square, constant_square, p, t),
                          scale_pair(-1, leading_square))
    elif allocation == "swap":
        first = add_pair(scale_pair(p, middle),
                         scale_pair(2, reduce_pair(root, leading_square, p, t)))
        second = add_pair(scale_pair(p**2, constant_square),
                          scale_pair(-1, reduce_pair(
                              root_square, leading_square, p, t)))
    else:
        first = add_pair(scale_pair(p, middle),
                         scale_pair(-t, leading_square))
        second = add_pair(scale_pair(p, constant_square),
                          scale_pair(-1, leading_square))

    equations = [sp.Poly(value, b, w, p, t)
                 for value in (*first, *second)]
    common = equations[0]
    for equation in equations[1:]:
        common = sp.gcd(common, equation)
    primitive = [equation.exquo(common) for equation in equations]
    shapes = [
        (item.total_degree(), item.degree(b), len(item.terms()))
        for item in primitive
    ]
    print(
        f"allocation={allocation} ramified_common="
        f"{sp.factor(common.as_expr())} ramified_shapes={shapes}",
        flush=True,
    )
    return common, primitive


def reciprocal_trace_equations(name, primitive, variables, exception):
    """Close under b inversion and reduce to trace quadratics."""
    p, t, b, w = variables
    trace = sp.Symbol("trace")
    reduced = []
    for equation in primitive:
        as_b = sp.Poly(equation.as_expr(), b)
        degree = as_b.degree()
        if degree != 4:
            raise RuntimeError(f"allocation {name} has b-degree {degree}, not 4")
        coefficients = [as_b.nth(index) for index in range(5)]
        # The unordered moving template is invariant under b -> 1/b.  Thus
        # both f(b) and b^4 f(1/b) vanish.  Their sum and difference reduce
        # after division by b^2, and in the latter case by b-b^-1.
        palindromic = ((coefficients[0] + coefficients[4])
                       * (trace**2 - 2)
                       + (coefficients[1] + coefficients[3]) * trace
                       + 2 * coefficients[2])
        anti = ((coefficients[4] - coefficients[0]) * trace
                + coefficients[3] - coefficients[1])
        for value in (palindromic, anti):
            polynomial = sp.Poly(
                sp.expand(value), trace, w, p, t, domain=sp.QQ
            )
            if not polynomial.is_zero:
                reduced.append(polynomial)
    common = reduced[0]
    for equation in reduced[1:]:
        common = sp.gcd(common, equation)
    primitive_trace = [equation.exquo(common) for equation in reduced]
    parameters = (p, t)
    if exception:
        if exception == "t-zero":
            substitutions = {t: 0}
            parameters = (p,)
        elif exception == "circle":
            substitutions = {p: (t**2 - 2) / 2}
            parameters = (t,)
        elif exception == "mixed-special":
            substitutions = {p: sp.Rational(16, 25),
                             t: sp.Rational(-41, 20)}
            parameters = ()
        else:
            parameter = sp.Symbol("norm_parameter", nonzero=True)
            substitutions = {p: parameter**2,
                             t: parameter + 1 / parameter}
            parameters = (parameter,)
        specialized = []
        for equation in primitive_trace:
            value = sp.together(equation.as_expr().subs(substitutions))
            value_numerator, _ = sp.fraction(value)
            specialized.append(sp.Poly(
                sp.expand(value_numerator), trace, w, *parameters,
                domain=sp.QQ,
            ))
        specialized_common = specialized[0]
        for equation in specialized[1:]:
            specialized_common = sp.gcd(specialized_common, equation)
        primitive_trace = [
            equation.exquo(specialized_common) for equation in specialized
        ]
        print(
            f"allocation={name} trace_exception={exception} "
            f"specialized_common={sp.factor(specialized_common.as_expr())}",
            flush=True,
        )
    print(
        f"allocation={name} trace_equations={len(primitive_trace)} "
        f"trace_common_factor={sp.factor(common.as_expr())} "
        f"trace_shapes="
        f"{[(item.degree(trace), item.degree(w), len(item.terms())) for item in primitive_trace]}",
        flush=True,
    )
    for index, equation in enumerate(primitive_trace):
        if len(equation.terms()) <= 10:
            print(
                f"allocation={name} trace_small_equation={index} "
                f"factor={sp.factor(equation.as_expr())}",
                flush=True,
            )
    return trace, primitive_trace, parameters


def allocation_minors(name, primitive, variables, exception):
    """Eliminate the internal parameter linearly from four quadratics."""
    p, t, b, w = variables
    elimination = b
    equations = primitive
    parameters = (p, t)
    if any(equation.degree(b) > 2 for equation in primitive):
        elimination, equations, parameters = reciprocal_trace_equations(
            name, primitive, variables, exception
        )
    rows = []
    for equation in equations:
        as_b = sp.Poly(equation.as_expr(), elimination)
        if as_b.degree() > 2:
            raise RuntimeError(f"allocation {name} is not quadratic")
        rows.append(tuple(
            sp.Poly(as_b.nth(index), w, *parameters, domain=sp.QQ)
            for index in (2, 1, 0)
        ))

    common = None
    nonzero_minors = 0
    for indices in itertools.combinations(range(len(rows)), 3):
        first, second, third = (rows[index] for index in indices)
        value = (
            first[0] * (second[1] * third[2] - second[2] * third[1])
            - first[1] * (second[0] * third[2] - second[2] * third[0])
            + first[2] * (second[0] * third[1] - second[1] * third[0])
        )
        polynomial = value
        if polynomial.is_zero:
            print(
                f"allocation={name} minor_rows={indices} zero=true",
                flush=True,
            )
            continue
        nonzero_minors += 1
        common = polynomial if common is None else sp.gcd(common, polynomial)
        print(
            f"allocation={name} minor_rows={indices} "
            f"w_degree={polynomial.degree()} "
            f"running_gcd_w_degree={common.degree(w)}",
            flush=True,
        )
        if nonzero_minors >= 2 and common.degree(w) <= 1:
            break
    if common is None:
        raise RuntimeError(f"allocation {name} has no nonzero minors")
    factor = (sp.factor(common.as_expr())
              if common.degree(w) <= 2 or len(common.terms()) <= 50
              else "OMITTED_LARGE")
    print(
        f"allocation={name} minor_gcd_w_degree={common.degree(w)} "
        f"minor_gcd_total_degree={common.total_degree()} "
        f"minor_gcd_terms={len(common.terms())} "
        f"minor_gcd_factor={factor}",
        flush=True,
    )


def run(template, allocation, minors, exception, ramified):
    ((p, t, b, w), (f, g, m), coefficients,
     (z_numerator, z_denominator)) = reconstruct_fraction_free(template)
    audit_reconstruction(template, (p, t, b, w), coefficients)
    x0, _, x2, x3, _ = coefficients
    print(f"template={template} fraction_free_reconstruction=PASS", flush=True)
    print(f"z_numerator={sp.factor(z_numerator)}", flush=True)
    print(f"z_denominator={sp.factor(z_denominator)}", flush=True)

    # At a root of T^2+tT+p, reduce the leading and constant W
    # coefficients of U and the W coefficient of V to linear pairs.
    leading = (sp.expand(x2 - p * x0), sp.expand(x3 - t * x0))
    constant = (sp.expand(x0 - p * x2), sp.expand(x3 - t * x2))
    gamma = (sp.expand(g - p * f), sp.expand(m - t * f))
    allocations = (("same", "swap", "mixed")
                   if allocation == "all" else (allocation,))
    for name in allocations:
        if ramified:
            _, primitive = ramified_allocation_equations(
                template, name, (p, t, b, w), coefficients
            )
        else:
            _, primitive = allocation_equations(
                template, name, (p, t, b, w), leading, constant, gamma
            )
        if minors:
            allocation_minors(name, primitive, (p, t, b, w), exception)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("template", choices=("fixed-moving", "moving-moving"))
    parser.add_argument(
        "--allocation", required=True,
        choices=("same", "swap", "mixed", "all")
    )
    parser.add_argument("--minors", action="store_true")
    parser.add_argument(
        "--exception", choices=("t-zero", "circle", "norm", "mixed-special")
    )
    parser.add_argument("--ramified", action="store_true")
    args = parser.parse_args()
    if args.exception and not args.minors:
        parser.error("--exception requires --minors")
    run(args.template, args.allocation, args.minors, args.exception,
        args.ramified)


if __name__ == "__main__":
    main()
