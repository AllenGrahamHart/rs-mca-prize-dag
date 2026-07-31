#!/usr/bin/env python3
"""Emit one sparse FLINT resultant for an aligned-positive unramified cell.

Proof status: EXPERIMENTAL compiler; a pairwise resultant is not a deletion.
Reproducibility: deterministic exact arithmetic over the deployed prime.
JSON certificate: none until a complete saturated component router exists.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import flint
import sympy as sp
from sympy.polys.agca.extensions import FiniteExtension


DEPLOYED_PRIME = 2130706433
HERE = Path(__file__).resolve().parent
SOURCE = HERE / "kb_c2_112_positive_qslice_symmetric.py"
SOURCE_SHA256 = "bc5f958f834d978b2bb2e054cafd8ee47f46469b26c9798257f10436cc8eb45d"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def require_associate(left, right, message: str) -> None:
    quotient, remainder = divmod(left, right)
    require(remainder.is_zero() and quotient.is_constant() and not quotient.is_zero(),
            message)


def load_source():
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256,
            "source hash")
    spec = importlib.util.spec_from_file_location("positive_qslice", SOURCE)
    require(spec is not None and spec.loader is not None, "source loader")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def divide_open_factors(poly: sp.Poly, variables, factors):
    counts = []
    result = poly.primitive()[1]
    for factor in factors:
        divisor = sp.Poly(factor, *variables, domain=sp.QQ)
        count = 0
        while sp.rem(result, divisor).is_zero:
            result = result.exquo(divisor)
            count += 1
        counts.append(count)
    return result.primitive()[1], counts


def eliminate_scale(equation: sp.Poly, scale, numerator, denominator):
    ring = sp.QQ.poly_ring(*sorted(
        equation.as_expr().free_symbols - {scale}, key=lambda item: item.name
    ))
    in_scale = sp.Poly(equation.as_expr(), scale, domain=ring)
    degree = in_scale.degree()
    require(0 <= degree <= 2, "scale degree")
    cleared = sp.Integer(0)
    for exponent in range(degree + 1):
        coefficient = in_scale.nth(exponent).as_expr()
        cleared += coefficient * numerator**exponent * denominator**(
            degree - exponent
        )
    return sp.expand(cleared), degree


def sympy_to_flint(poly: sp.Poly, context):
    integer_poly = poly.clear_denoms(convert=True)[1].primitive()[1]
    terms = {
        monomial: int(coefficient) % DEPLOYED_PRIME
        for monomial, coefficient in integer_poly.terms()
        if int(coefficient) % DEPLOYED_PRIME
    }
    return context.from_dict(terms)


def sympy_orbit_coefficients_to_flint(poly: sp.Poly, context):
    integer_poly = poly.clear_denoms(convert=True)[1].primitive()[1]
    coefficients = []
    for exponent in (2, 1, 0):
        terms = {
            (0, *monomial[1:]): int(coefficient) % DEPLOYED_PRIME
            for monomial, coefficient in integer_poly.terms()
            if monomial[0] == exponent and int(coefficient) % DEPLOYED_PRIME
        }
        coefficients.append(context.from_dict(terms))
    return coefficients


def trace_reduce(poly: sp.Poly, b, trace, remaining_variables):
    """Descend a reciprocal quartic in b through trace=b+b^-1."""
    coefficient_ring = sp.QQ.poly_ring(*remaining_variables)
    as_b = sp.Poly(poly.as_expr(), b, domain=coefficient_ring)
    require(as_b.degree() == 4, "moving orbit degree")
    require(
        all(as_b.nth(index) == as_b.nth(4 - index) for index in range(5)),
        "moving equation is not reciprocal after scale elimination",
    )
    reduced = sp.expand(
        as_b.nth(4).as_expr() * (trace**2 - 2)
        + as_b.nth(3).as_expr() * trace
        + as_b.nth(2).as_expr()
    )
    return sp.Poly(reduced, trace, *remaining_variables, domain=sp.QQ).primitive()[1]


def polynomial_digest(poly) -> str:
    terms = sorted(
        (tuple(monomial), int(coefficient))
        for monomial, coefficient in poly.to_dict().items()
    )
    return hashlib.sha256(repr(terms).encode("ascii")).hexdigest()


def extension_polynomial_digest(coefficients) -> str:
    payload = [repr(coefficient.rep) for coefficient in coefficients]
    return hashlib.sha256(repr(payload).encode("ascii")).hexdigest()


def extension_trim(coefficients, extension):
    result = list(coefficients)
    while result and result[-1] == extension.zero:
        result.pop()
    return result


def field_poly_trim(coefficients, field):
    result = list(coefficients)
    while result and result[-1] == field.zero:
        result.pop()
    return result


def field_poly_add(left, right, field, sign=1):
    result = [field.zero for _ in range(max(len(left), len(right)))]
    for index, coefficient in enumerate(left):
        result[index] += coefficient
    for index, coefficient in enumerate(right):
        result[index] += sign * coefficient
    return field_poly_trim(result, field)


def field_poly_multiply(left, right, field):
    if not left or not right:
        return []
    result = [field.zero for _ in range(len(left) + len(right) - 1)]
    for left_index, left_coefficient in enumerate(left):
        for right_index, right_coefficient in enumerate(right):
            result[left_index + right_index] += (
                left_coefficient * right_coefficient
            )
    return field_poly_trim(result, field)


def field_poly_divrem(numerator, denominator, field):
    remainder = field_poly_trim(numerator, field)
    denominator = field_poly_trim(denominator, field)
    require(denominator, "zero field-polynomial divisor")
    quotient = [
        field.zero for _ in range(max(0, len(remainder) - len(denominator) + 1))
    ]
    leading_inverse = field.one / denominator[-1]
    while len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        quotient_term = remainder[-1] * leading_inverse
        quotient[shift] += quotient_term
        for index, coefficient in enumerate(denominator):
            remainder[index + shift] -= quotient_term * coefficient
        remainder = field_poly_trim(remainder, field)
    return field_poly_trim(quotient, field), remainder


def extension_element_inverse(element, extension):
    field = extension.domain
    modulus = list(reversed(extension.mod.to_list()))
    value = list(reversed(element.rep.to_list()))
    require(value, "zero extension inverse")
    old_remainder, remainder = modulus, value
    old_bezout, bezout = [], [field.one]
    while remainder:
        quotient, next_remainder = field_poly_divrem(
            old_remainder, remainder, field
        )
        old_remainder, remainder = remainder, next_remainder
        old_bezout, bezout = (
            bezout,
            field_poly_add(
                old_bezout,
                field_poly_multiply(quotient, bezout, field),
                field,
                sign=-1,
            ),
        )
    require(len(old_remainder) == 1, "noninvertible extension element")
    scale = field.one / old_remainder[0]
    inverse_coefficients = [coefficient * scale for coefficient in old_bezout]
    expression = sum(
        coefficient.as_expr() * extension.symbol**index
        for index, coefficient in enumerate(inverse_coefficients)
    )
    return extension(expression)


def extension_monic(coefficients, extension):
    result = extension_trim(coefficients, extension)
    require(result, "zero extension polynomial")
    inverse = extension_element_inverse(result[-1], extension)
    return [coefficient * inverse for coefficient in result]


def extension_remainder(numerator, denominator, extension):
    remainder = extension_trim(numerator, extension)
    denominator = extension_trim(denominator, extension)
    require(denominator, "zero extension divisor")
    leading_inverse = extension_element_inverse(denominator[-1], extension)
    while len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        quotient_term = remainder[-1] * leading_inverse
        for index, coefficient in enumerate(denominator):
            remainder[index + shift] -= quotient_term * coefficient
        remainder = extension_trim(remainder, extension)
    return remainder


def extension_gcd(left, right, extension):
    left = extension_trim(left, extension)
    right = extension_trim(right, extension)
    while right:
        left, right = right, extension_remainder(left, right, extension)
    return extension_monic(left, extension)


def flint_to_extension_w_coefficients(poly, p, t, extension):
    coefficients = [extension.zero for _ in range(poly.degrees()[3] + 1)]
    for monomial, coefficient in poly.to_dict().items():
        require(monomial[0] == 0, "unexpected b term in residual minor")
        value = extension(
            int(coefficient) * p**monomial[1] * t**monomial[2]
        )
        coefficients[monomial[3]] += value
    return extension_trim(coefficients, extension)


def emit_factorization(poly, label: str, context):
    print(f"{label} factorization=START", flush=True)
    unit, factors = poly.factor()
    reconstructed = context.constant(unit)
    for factor, exponent in factors:
        reconstructed *= factor**exponent
    require(reconstructed == poly, "factor reconstruction")
    print(
        f"{label} factor_count={len(factors)} unit={unit}",
        flush=True,
    )
    for index, (factor, exponent) in enumerate(factors):
        term_count = len(factor.to_dict())
        expression = f" expression={factor}" if term_count <= 20 else ""
        print(
            f"factor={index} exponent={exponent} terms={term_count} "
            f"total_degree={factor.total_degree()} "
            f"degrees={factor.degrees()} digest={polynomial_digest(factor)}"
            f"{expression}",
            flush=True,
        )
    return factors


def determinant_3_by_3(rows):
    return (
        rows[0][0] * rows[1][1] * rows[2][2]
        + rows[0][1] * rows[1][2] * rows[2][0]
        + rows[0][2] * rows[1][0] * rows[2][1]
        - rows[0][2] * rows[1][1] * rows[2][0]
        - rows[0][1] * rows[1][0] * rows[2][2]
        - rows[0][0] * rows[1][2] * rows[2][1]
    )


def build_cell(template: str, allocation: str):
    source = load_source()
    variables, odd, coefficients, _, relative_scale = (
        source.reconstruct_fraction_free(template)
    )
    p, t, b, w = variables
    scale = sp.Symbol("lambda_scale")
    source.audit_reconstruction(template, variables, coefficients, relative_scale)
    print(f"template={template} reconstruction=PASS", flush=True)
    equations = source.allocation_equations(
        allocation, (p, t, b, w, scale), odd, coefficients, relative_scale
    )
    normalization = sp.Poly(equations[-1].as_expr(), scale)
    require(normalization.degree() == 1, "normalization degree")
    scale_value = sp.cancel(-normalization.nth(0) / normalization.nth(1))
    scale_numerator, scale_denominator = map(sp.expand, sp.fraction(scale_value))
    expected_numerator, expected_denominator = relative_scale
    require(
        sp.cancel(
            scale_numerator * expected_denominator
            - scale_denominator * expected_numerator
        ) == 0,
        "relative scale",
    )
    print(
        f"scale_numerator={sp.factor(scale_numerator)} "
        f"scale_denominator={sp.factor(scale_denominator)}",
        flush=True,
    )

    ring_variables = (b, p, t, w)
    reduced = []
    for index, equation in enumerate(equations[:-1]):
        cleared, scale_degree = eliminate_scale(
            equation, scale, scale_numerator, scale_denominator
        )
        poly = sp.Poly(cleared, *ring_variables, domain=sp.QQ)
        poly, open_counts = divide_open_factors(
            poly, ring_variables, (w, p - 1)
        )
        reduced.append(poly)
        print(
            f"equation={index} scale_degree={scale_degree} "
            f"open_counts={open_counts} total_degree={poly.total_degree()} "
            f"b_degree={poly.degree(b)} terms={len(poly.terms())}",
            flush=True,
        )
    require(len(reduced) == 4, "equation count")
    if template == "moving-moving":
        trace = sp.Symbol("trace")
        reduced = [
            trace_reduce(poly, b, trace, (p, t, w)) for poly in reduced
        ]
        ring_variables = (trace, p, t, w)
        for index, poly in enumerate(reduced):
            print(
                f"trace_equation={index} total_degree={poly.total_degree()} "
                f"trace_degree={poly.degree(trace)} terms={len(poly.terms())}",
                flush=True,
            )
    require(
        all(poly.degree(ring_variables[0]) <= 2 for poly in reduced),
        "quadratic orbit-coordinate gate",
    )
    return ring_variables, reduced


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "template", choices=("fixed-moving", "moving-moving")
    )
    parser.add_argument(
        "--allocation", choices=("same", "swap", "mixed"), required=True
    )
    parser.add_argument(
        "--pair",
        choices=("01", "02", "03", "12", "13", "23", "star", "all"),
        default="star",
    )
    parser.add_argument("--factor", action="store_true")
    parser.add_argument("--minors", action="store_true")
    parser.add_argument("--cascade", action="store_true")
    parser.add_argument("--linear-component", action="store_true")
    parser.add_argument("--quartic-component", action="store_true")
    parser.add_argument("--dump-minor-cache", type=Path)
    parser.add_argument("--dump-conic-cache", type=Path)
    args = parser.parse_args()
    require(
        args.allocation == "same"
        or not args.quartic_component,
        "quartic router is pinned to the same allocation",
    )

    require(flint.__version__ == "0.9.0", "python-flint version")
    ring_variables, equations = build_cell(args.template, args.allocation)
    context = flint.nmod_mpoly_ctx.get(
        tuple(str(variable) for variable in ring_variables),
        DEPLOYED_PRIME,
        "lex",
    )
    flint_equations = []
    for index, equation in enumerate(equations):
        converted = sympy_to_flint(equation, context)
        flint_equations.append(converted)
        print(
            f"flint_equation={index} terms={len(converted.to_dict())} "
            f"degrees={converted.degrees()}",
            flush=True,
        )

    if (args.minors or args.cascade or args.linear_component
            or args.quartic_component or args.dump_minor_cache
            or args.dump_conic_cache):
        coefficient_rows = [
            sympy_orbit_coefficients_to_flint(equation, context)
            for equation in equations
        ]
        if args.dump_conic_cache:
            first, second = coefficient_rows[:2]
            kernel = (
                first[1] * second[2] - first[2] * second[1],
                first[2] * second[0] - first[0] * second[2],
                first[0] * second[1] - first[1] * second[0],
            )
            conic = kernel[0] * kernel[2] - kernel[1]**2
            require(not conic.is_zero(), "zero kernel conic")
            payload = {
                "schema": "kb-c2-112-aligned-positive-kernel-conic-v1",
                "prime": DEPLOYED_PRIME,
                "source_sha256": SOURCE_SHA256,
                "template": args.template,
                "allocation": args.allocation,
                "digest": polynomial_digest(conic),
                "polynomial": [
                    [[int(exponent) for exponent in monomial],
                     int(coefficient)]
                    for monomial, coefficient in sorted(
                        conic.to_dict().items()
                    )
                ],
            }
            encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"))
            args.dump_conic_cache.write_text(
                encoded + "\n", encoding="ascii"
            )
            print(
                "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FLINT_"
                "CONIC_CACHE_PASS "
                f"terms={len(conic.to_dict())} degrees={conic.degrees()} "
                f"digest={polynomial_digest(conic)} "
                f"path={args.dump_conic_cache} "
                f"sha256={hashlib.sha256((encoded + chr(10)).encode('ascii')).hexdigest()}",
                flush=True,
            )
            if not (args.minors or args.cascade or args.linear_component
                    or args.quartic_component or args.dump_minor_cache):
                return
        residual_minors = []
        for indices in itertools.combinations(range(4), 3):
            minor = determinant_3_by_3(
                [coefficient_rows[index] for index in indices]
            )
            require(not minor.is_zero(), "zero coefficient minor")
            label = "minor=" + "".join(map(str, indices))
            print(
                "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FLINT_MINOR_PASS "
                f"template={args.template} allocation={args.allocation} "
                f"{label} terms={len(minor.to_dict())} "
                f"total_degree={minor.total_degree()} "
                f"degrees={minor.degrees()} digest={polynomial_digest(minor)}",
                flush=True,
            )
            factors = emit_factorization(minor, label, context)
            large_factors = [
                factor for factor, exponent in factors
                if len(factor.to_dict()) > 100 and exponent == 1
            ]
            require(len(large_factors) == 1, "unique residual minor")
            residual_minors.append(large_factors[0])
        if args.dump_minor_cache:
            payload = {
                "schema": "kb-c2-112-aligned-positive-minor-residuals-v1",
                "prime": DEPLOYED_PRIME,
                "source_sha256": SOURCE_SHA256,
                "template": args.template,
                "allocation": args.allocation,
                "digests": [
                    polynomial_digest(poly) for poly in residual_minors
                ],
                "polynomials": [
                    [
                        [[int(exponent) for exponent in monomial],
                         int(coefficient)]
                        for monomial, coefficient in sorted(
                            poly.to_dict().items()
                        )
                    ]
                    for poly in residual_minors
                ],
            }
            encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"))
            args.dump_minor_cache.write_text(encoded + "\n", encoding="ascii")
            print(
                "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FLINT_"
                "MINOR_CACHE_PASS "
                f"path={args.dump_minor_cache} "
                f"sha256={hashlib.sha256((encoded + chr(10)).encode('ascii')).hexdigest()}",
                flush=True,
            )
            if not (args.minors or args.cascade or args.linear_component
                    or args.quartic_component):
                return
        if args.linear_component:
            b_generator, _, t_generator, w_generator = context.gens()
            inverse_four = pow(4, -1, DEPLOYED_PRIME)
            p_value = -(5 * t_generator + 4) * inverse_four
            specialized = [
                minor.compose(
                    b_generator, p_value, t_generator, w_generator
                )
                for minor in residual_minors
            ]
            require(
                all(poly.degrees()[1] == 0 for poly in specialized),
                "linear component substitution",
            )
            common_minor = specialized[0]
            for poly in specialized[1:]:
                common_minor = common_minor.gcd(poly)
            print(
                "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FLINT_"
                "LINEAR_COMPONENT_MINOR_GCD_PASS "
                f"template={args.template} allocation={args.allocation} "
                f"terms={len(common_minor.to_dict())} "
                f"degrees={common_minor.degrees()} "
                f"digest={polynomial_digest(common_minor)}",
                flush=True,
            )
            emit_factorization(
                common_minor, "linear_component_minor_gcd", context
            )
            if args.allocation == "mixed":
                mixed_curve_expression = (
                    4 * t_generator**3 * w_generator**2
                    + 22 * t_generator**3 * w_generator
                    + 99 * t_generator**3
                    + 124 * t_generator**2 * w_generator**2
                    + 200 * t_generator**2 * w_generator
                    + 76 * t_generator**2
                    + 320 * t_generator * w_generator**2
                    + 160 * t_generator * w_generator
                    - 160 * t_generator
                    + 128 * w_generator**2 - 128
                )
                mixed_curve = mixed_curve_expression
                require_associate(
                    common_minor,
                    t_generator**2 * (t_generator + 1)
                    * (t_generator + 4) * (w_generator - 1)
                    * mixed_curve,
                    "mixed linear common-minor support",
                )
                first, second = coefficient_rows[:2]
                kernel = (
                    first[1] * second[2] - first[2] * second[1],
                    first[2] * second[0] - first[0] * second[2],
                    first[0] * second[1] - first[1] * second[0],
                )
                conic = kernel[0] * kernel[2] - kernel[1]**2
                conic_specialized = conic.compose(
                    b_generator, p_value, t_generator, w_generator
                )
                curve_gcd = mixed_curve.gcd(conic_specialized)
                require(curve_gcd.is_constant(),
                        "mixed linear curve lies on kernel conic")
                norm = mixed_curve.resultant(conic_specialized, 3)
                require(not norm.is_zero(), "zero mixed linear conic norm")
                print(
                    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FLINT_"
                    "MIXED_LINEAR_CONIC_TEST_PASS generic_conic_root=false "
                    f"norm_terms={len(norm.to_dict())} "
                    f"degrees={norm.degrees()} "
                    f"digest={polynomial_digest(norm)}",
                    flush=True,
                )
                emit_factorization(
                    norm, "mixed_linear_conic_norm", context
                )
                return
            expected_common_minor = (
                t_generator**3 * (t_generator + 1) * (t_generator + 4)
                * (w_generator - 1)
            )
            require_associate(
                common_minor, expected_common_minor,
                "linear common-minor support",
            )
            projections = []
            for index in range(1, len(specialized)):
                print(
                    f"linear_component_projection=0,{index} variable=w "
                    "status=START",
                    flush=True,
                )
                resultant = specialized[0].resultant(specialized[index], 3)
                if resultant.is_zero():
                    pair_gcd = specialized[0].gcd(specialized[index])
                    require(not pair_gcd.is_constant(), "missing pair gcd")
                    emit_factorization(
                        pair_gcd,
                        f"linear_component_pair_gcd=0{index}",
                        context,
                    )
                    resultant = (specialized[0] / pair_gcd).resultant(
                        specialized[index] / pair_gcd, 3
                    )
                require(not resultant.is_zero(), "zero reduced linear projection")
                projections.append(resultant)
                print(
                    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FLINT_"
                    "LINEAR_COMPONENT_PROJECTION_PASS "
                    f"template={args.template} allocation={args.allocation} "
                    f"pair=0{index} terms={len(resultant.to_dict())} "
                    f"degrees={resultant.degrees()} "
                    f"digest={polynomial_digest(resultant)}",
                    flush=True,
                )
            common = projections[0]
            for resultant in projections[1:]:
                common = common.gcd(resultant)
            require(not common.is_zero(), "zero linear projection gcd")
            print(
                "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FLINT_"
                "LINEAR_COMPONENT_GCD_PASS "
                f"template={args.template} allocation={args.allocation} "
                f"terms={len(common.to_dict())} degrees={common.degrees()} "
                f"digest={polynomial_digest(common)}",
                flush=True,
            )
            emit_factorization(common, "linear_component_gcd", context)
            expected_projection = (
                t_generator**5 * (t_generator + 1) * (t_generator + 4)
                * (5 * t_generator + 8)**4
            )
            require_associate(
                common, expected_projection,
                "linear reduced-projection support",
            )
            require_associate(
                t_generator**2 - 4 * p_value,
                (t_generator + 1) * (t_generator + 4),
                "linear discriminant support",
            )
            require_associate(
                p_value + t_generator + 1,
                t_generator,
                "linear q(1) support",
            )
            require_associate(
                p_value - 1,
                5 * t_generator + 8,
                "linear reciprocal-orbit support",
            )
            print(
                "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FLINT_"
                "LINEAR_COMPONENT_EXCLUSION_PASS "
                f"template={args.template} allocation={args.allocation} "
                "component=4*p+5*t+4 support="
                "w-1,discriminant,q(1),p-1",
                flush=True,
            )
            return
        if args.quartic_component:
            _, p_symbol, t_symbol, w_symbol = ring_variables
            quartic_expression = (
                16 * p_symbol**4 + 220 * p_symbol**3 * t_symbol
                - 20 * p_symbol**3 + 579 * p_symbol**2 * t_symbol**2
                + 684 * p_symbol**2 * t_symbol - 72 * p_symbol**2
                + 503 * p_symbol * t_symbol**3
                + 1218 * p_symbol * t_symbol**2
                + 684 * p_symbol * t_symbol - 20 * p_symbol
                + 140 * t_symbol**4 + 503 * t_symbol**3
                + 579 * t_symbol**2 + 220 * t_symbol + 16
            )
            quartic = sympy_to_flint(
                sp.Poly(quartic_expression, *ring_variables), context
            )
            for index in range(1, len(residual_minors)):
                projection = residual_minors[0].resultant(
                    residual_minors[index], 3
                )
                quotient, remainder = divmod(projection, quartic)
                require(remainder.is_zero(), "missing quartic projection factor")
                require(not (quotient % quartic).is_zero(),
                        "quartic projection multiplicity")
            coefficient_field = sp.GF(DEPLOYED_PRIME).frac_field(t_symbol)
            extension = FiniteExtension(
                sp.Poly(
                    quartic_expression, p_symbol,
                    domain=coefficient_field,
                ).monic()
            )
            extension_minors = [
                flint_to_extension_w_coefficients(
                    minor, p_symbol, t_symbol, extension
                )
                for minor in residual_minors
            ]
            pair_gcds = []
            for index in range(1, len(extension_minors)):
                pair_gcd = extension_gcd(
                    extension_minors[0], extension_minors[index], extension
                )
                pair_gcds.append(pair_gcd)
                print(
                    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FLINT_"
                    "QUARTIC_PAIR_GCD_PASS "
                    f"template={args.template} allocation={args.allocation} "
                    f"pair=0{index} degree={len(pair_gcd) - 1} "
                    f"digest={extension_polynomial_digest(pair_gcd)}",
                    flush=True,
                )
            common = pair_gcds[0]
            for pair_gcd in pair_gcds[1:]:
                common = extension_gcd(common, pair_gcd, extension)
            print(
                "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FLINT_"
                "QUARTIC_GENERIC_GCD_PASS "
                f"template={args.template} allocation={args.allocation} "
                f"degree={len(common) - 1} "
                f"digest={extension_polynomial_digest(common)}",
                flush=True,
            )
            return
        if args.cascade:
            projected = []
            for index in range(1, len(residual_minors)):
                print(f"minor_projection=0,{index} variable=w status=START",
                      flush=True)
                resultant = residual_minors[0].resultant(
                    residual_minors[index], 3
                )
                require(not resultant.is_zero(), "zero minor projection")
                projected.append(resultant)
                print(
                    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FLINT_"
                    "MINOR_PROJECTION_PASS "
                    f"template={args.template} allocation={args.allocation} "
                    f"pair=0{index} terms={len(resultant.to_dict())} "
                    f"total_degree={resultant.total_degree()} "
                    f"degrees={resultant.degrees()} "
                    f"digest={polynomial_digest(resultant)}",
                    flush=True,
                )
                if args.factor:
                    emit_factorization(
                        resultant, f"minor_projection=0{index}", context
                    )
        return

    if args.pair == "star":
        pairs = ("01", "02", "03")
    elif args.pair == "all":
        pairs = ("01", "02", "03", "12", "13", "23")
    else:
        pairs = (args.pair,)
    resultants = []
    for pair in pairs:
        left, right = map(int, pair)
        print(f"resultant_pair={left},{right} status=START", flush=True)
        resultant = flint_equations[left].resultant(flint_equations[right], 0)
        require(not resultant.is_zero(), "zero pairwise resultant")
        resultants.append(resultant)
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FLINT_RESULTANT_PASS "
            f"template={args.template} allocation={args.allocation} "
            f"pair={pair} terms={len(resultant.to_dict())} "
            f"total_degree={resultant.total_degree()} "
            f"degrees={resultant.degrees()} digest={polynomial_digest(resultant)}",
            flush=True,
        )
        if args.factor:
            emit_factorization(resultant, f"resultant_pair={pair}", context)
    if len(resultants) > 1:
        common = resultants[0]
        for resultant in resultants[1:]:
            common = common.gcd(resultant)
        require(not common.is_zero(), "zero resultant gcd")
        print(
            "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FLINT_GCD_PASS "
            f"template={args.template} allocation={args.allocation} "
            f"pairs={','.join(pairs)} terms={len(common.to_dict())} "
            f"total_degree={common.total_degree()} degrees={common.degrees()} "
            f"digest={polynomial_digest(common)}",
            flush=True,
        )
        emit_factorization(common, "resultant_gcd", context)


if __name__ == "__main__":
    main()
