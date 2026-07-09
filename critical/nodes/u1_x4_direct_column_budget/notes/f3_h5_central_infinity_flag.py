#!/usr/bin/env python3
"""Initial-form boundary flag for the h=5 central fixed graph."""

from __future__ import annotations

from dataclasses import dataclass
import sympy as sp

from f3_h5_central_slice_quadratic_normal_form import (
    SLICE_TOP,
    slice_graph_components,
)


NEGATIVE_INFINITY = -10**9


@dataclass(frozen=True)
class BranchSignature:
    zero_variables: tuple[str, ...]
    active_variables: tuple[str, ...]
    top_supports: tuple[tuple[str, ...], ...]
    top_degrees: tuple[int, ...]
    common_zero_options: tuple[tuple[str, ...], ...]


def top_part(
    expression: sp.Expr,
    variables: tuple[sp.Symbol, ...],
    weights: tuple[int, ...],
) -> tuple[sp.Expr, int, int]:
    poly = sp.Poly(sp.expand(expression), *variables, domain=sp.QQ)
    if poly.is_zero:
        return sp.Integer(0), NEGATIVE_INFINITY, 0

    max_weight = NEGATIVE_INFINITY
    terms: list[tuple[tuple[int, ...], sp.Rational]] = []
    for monomial, coefficient in poly.terms():
        if any(exponent and weight == NEGATIVE_INFINITY for exponent, weight in zip(monomial, weights)):
            continue
        weight = sum(exponent * item_weight for exponent, item_weight in zip(monomial, weights))
        if weight > max_weight:
            max_weight = weight
            terms = [(monomial, coefficient)]
        elif weight == max_weight:
            terms.append((monomial, coefficient))

    out = sp.Integer(0)
    for monomial, coefficient in terms:
        term = coefficient
        for variable, exponent in zip(variables, monomial):
            term *= variable**exponent
        out += term
    return sp.factor(out), max_weight, len(terms)


def active_top(
    expression: sp.Expr,
    active_variables: tuple[sp.Symbol, ...],
) -> tuple[sp.Expr, int, int]:
    if not active_variables:
        value = sp.factor(expression)
        return value, 0 if value else NEGATIVE_INFINITY, 1 if value else 0
    return top_part(expression, active_variables, (1,) * len(active_variables))


def restricted_inner_data(
    graph: tuple[sp.Expr, ...],
    zero_variables: tuple[str, ...],
) -> tuple[tuple[sp.Symbol, ...], tuple[int, ...], tuple[sp.Expr, ...]]:
    zero_set = set(zero_variables)
    substitutions = {variable: 0 for variable in SLICE_TOP if str(variable) in zero_set}
    active_variables = tuple(variable for variable in SLICE_TOP if str(variable) not in zero_set)
    degrees: list[int] = []
    leading_parts: list[sp.Expr] = []
    for component in graph:
        restricted = sp.factor(component.subs(substitutions))
        leading, degree, _ = active_top(restricted, active_variables)
        degrees.append(degree)
        leading_parts.append(leading)
    return active_variables, tuple(degrees), tuple(leading_parts)


def top_composition(
    outer: sp.Expr,
    degrees: tuple[int, ...],
    leading_parts: tuple[sp.Expr, ...],
) -> tuple[sp.Expr, int, int]:
    poly = sp.Poly(sp.expand(outer), *SLICE_TOP, domain=sp.QQ)
    candidate_weights = sorted(
        {
            sum(exponent * degree for exponent, degree in zip(monomial, degrees))
            for monomial, _ in poly.terms()
            if all(
                not (exponent and degree == NEGATIVE_INFINITY)
                for exponent, degree in zip(monomial, degrees)
            )
        },
        reverse=True,
    )
    for weight in candidate_weights:
        source = sp.Integer(0)
        source_terms = 0
        for monomial, coefficient in poly.terms():
            if any(
                exponent and degree == NEGATIVE_INFINITY
                for exponent, degree in zip(monomial, degrees)
            ):
                continue
            monomial_weight = sum(
                exponent * degree for exponent, degree in zip(monomial, degrees)
            )
            if monomial_weight != weight:
                continue
            term = coefficient
            for variable, exponent in zip(SLICE_TOP, monomial):
                term *= variable**exponent
            source += term
            source_terms += 1
        composed = sp.factor(
            sp.expand(source.subs(dict(zip(SLICE_TOP, leading_parts)), simultaneous=True))
        )
        if composed != 0:
            return composed, weight, source_terms
    return sp.Integer(0), NEGATIVE_INFINITY, 0


def fixed_equation_tops(
    graph: tuple[sp.Expr, ...],
    zero_variables: tuple[str, ...],
) -> tuple[tuple[sp.Expr, int], ...]:
    active_variables, degrees, leading_parts = restricted_inner_data(graph, zero_variables)
    zero_set = set(zero_variables)
    rows: list[tuple[sp.Expr, int]] = []
    for index, outer in enumerate(graph):
        composed, degree, _ = top_composition(outer, degrees, leading_parts)
        variable = SLICE_TOP[index]
        variable_term = variable if str(variable) not in zero_set else sp.Integer(0)
        variable_degree = 1 if variable_term else NEGATIVE_INFINITY
        if degree > variable_degree:
            top_expression = -composed
            top_degree = degree
        elif degree < variable_degree:
            top_expression = variable_term
            top_degree = variable_degree
        else:
            top_expression = sp.factor(variable_term - composed)
            top_degree = degree
        rows.append((sp.factor(top_expression), top_degree))
    return tuple(rows)


def monomial_support(expression: sp.Expr, active_variables: tuple[sp.Symbol, ...]) -> tuple[str, ...]:
    poly = sp.Poly(expression, *active_variables, domain=sp.QQ)
    terms = poly.terms()
    if len(terms) != 1:
        raise AssertionError(("expected monomial top expression", expression, terms))
    monomial, coefficient = terms[0]
    if coefficient == 0:
        raise AssertionError(expression)
    return tuple(str(variable) for variable, exponent in zip(active_variables, monomial) if exponent)


def coefficient_prime_bound(expressions: tuple[sp.Expr, ...], variables: tuple[sp.Symbol, ...]) -> int:
    max_prime = 1
    for expression in expressions:
        poly = sp.Poly(expression, *variables, domain=sp.QQ)
        for coefficient in poly.coeffs():
            numerator, denominator = sp.Rational(coefficient).as_numer_denom()
            for value in (abs(int(numerator)), abs(int(denominator))):
                if value <= 1:
                    continue
                factors = sp.factorint(value)
                if factors:
                    max_prime = max(max_prime, max(factors))
    return max_prime


def branch_signature(
    graph: tuple[sp.Expr, ...],
    zero_variables: tuple[str, ...],
    common_zero_options: tuple[tuple[str, ...], ...],
) -> BranchSignature:
    active_variables, _, _ = restricted_inner_data(graph, zero_variables)
    tops = fixed_equation_tops(graph, zero_variables)
    top_expressions = tuple(expression for expression, _ in tops)
    supports = tuple(monomial_support(expression, active_variables) for expression in top_expressions)
    degrees = tuple(degree for _, degree in tops)
    max_prime = coefficient_prime_bound(top_expressions, active_variables)
    if max_prime >= 2**13 + 1:
        raise AssertionError(("coefficient prime too large for official-unit guard", max_prime))
    return BranchSignature(
        zero_variables=zero_variables,
        active_variables=tuple(str(variable) for variable in active_variables),
        top_supports=supports,
        top_degrees=degrees,
        common_zero_options=common_zero_options,
    )


def sparse_graph_summary(graph: tuple[sp.Expr, ...]) -> dict[str, int | tuple[int, ...]]:
    aux = sp.symbols("m6 m7 m8 m9")
    variables = tuple(SLICE_TOP) + aux
    substitutions = dict(zip(SLICE_TOP, aux))
    equations: list[sp.Expr] = []
    for variable, component in zip(aux, graph):
        equations.append(variable - component)
    for variable, component in zip(SLICE_TOP, graph):
        equations.append(variable - component.subs(substitutions))

    term_counts = []
    degrees = []
    max_coeff_bits = 0
    for equation in equations:
        poly = sp.Poly(equation, *variables, domain=sp.QQ)
        denominator_lcm = 1
        for coefficient in poly.coeffs():
            denominator_lcm = sp.ilcm(denominator_lcm, coefficient.q)
        integral = sp.Poly(denominator_lcm * equation, *variables, domain=sp.QQ)
        term_counts.append(len(integral.terms()))
        degrees.append(integral.total_degree())
        max_coeff_bits = max(max_coeff_bits, *(abs(int(c)).bit_length() for c in integral.coeffs()))

    expected_terms = (11, 14, 19, 23, 11, 14, 19, 23)
    expected_degrees = (6, 7, 8, 9, 6, 7, 8, 9)
    if tuple(term_counts) != expected_terms:
        raise AssertionError(term_counts)
    if tuple(degrees) != expected_degrees:
        raise AssertionError(degrees)
    return {
        "equations": len(equations),
        "term_counts": tuple(term_counts),
        "degrees": tuple(degrees),
        "max_coeff_bits": max_coeff_bits,
    }


def infinity_flag_summary() -> dict[str, int]:
    graph = slice_graph_components()
    sparse = sparse_graph_summary(graph)
    checks = (
        branch_signature(graph, (), (("l9",),)),
        branch_signature(graph, ("l9",), (("l7",), ("l8",))),
        branch_signature(graph, ("l7", "l9"), (("l8",),)),
        branch_signature(graph, ("l8", "l9"), (("l6",),)),
        branch_signature(graph, ("l7", "l8", "l9"), (("l6",),)),
        branch_signature(graph, ("l6", "l8", "l9"), (("l7",),)),
    )
    expected_supports = {
        (): (("l9",), ("l9",), ("l9",), ("l9",)),
        ("l9",): (("l7", "l8"), ("l7", "l8"), ("l7", "l8"), ("l7", "l8")),
        ("l7", "l9"): (("l8",), ("l8",), ("l8",), ("l8",)),
        ("l8", "l9"): (("l6",), ("l6",), ("l6",), ("l6",)),
        ("l7", "l8", "l9"): (("l6",), ("l6",), ("l6",), ("l6",)),
        ("l6", "l8", "l9"): (("l7",), ("l7",), ("l7",), ("l7",)),
    }
    actual_supports = {row.zero_variables: row.top_supports for row in checks}
    if actual_supports != expected_supports:
        raise AssertionError(actual_supports)
    return {
        "sparse_equations": int(sparse["equations"]),
        "min_terms": min(sparse["term_counts"]),
        "max_terms": max(sparse["term_counts"]),
        "min_degree": min(sparse["degrees"]),
        "max_degree": max(sparse["degrees"]),
        "branch_checks": len(checks),
        "split_options": len(checks[1].common_zero_options),
        "max_coeff_bits": int(sparse["max_coeff_bits"]),
    }


def main() -> None:
    graph = slice_graph_components()
    summary = infinity_flag_summary()
    print("h=5 central infinity flag")
    print(
        "sparse graph system: "
        f"equations={summary['sparse_equations']} "
        f"terms={summary['min_terms']}..{summary['max_terms']} "
        f"degrees={summary['min_degree']}..{summary['max_degree']} "
        f"max_coeff_bits={summary['max_coeff_bits']}"
    )
    for zero_variables, options in (
        ((), (("l9",),)),
        (("l9",), (("l7",), ("l8",))),
        (("l7", "l9"), (("l8",),)),
        (("l8", "l9"), (("l6",),)),
        (("l7", "l8", "l9"), (("l6",),)),
        (("l6", "l8", "l9"), (("l7",),)),
    ):
        row = branch_signature(graph, zero_variables, options)
        print(
            f"zero={row.zero_variables or ('-',)} "
            f"active={row.active_variables} "
            f"top_supports={row.top_supports} "
            f"common_zero_options={row.common_zero_options}"
        )
    print("This is an initial-form boundary guide, not a proof of saturated finiteness.")
    print("H5_CENTRAL_INFINITY_FLAG_PASS")


if __name__ == "__main__":
    main()
