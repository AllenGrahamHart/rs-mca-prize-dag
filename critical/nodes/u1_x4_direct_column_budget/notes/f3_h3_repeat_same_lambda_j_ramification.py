#!/usr/bin/env python3
"""Ramification compiler for the h=3 same-lambda J-invariant."""

from __future__ import annotations

from fractions import Fraction

import sympy as sp

from f3_h3_repeat_same_lambda_j_invariant import j_invariant, norm
from f3_h3_repeat_same_lambda_orbit_domain import ratio_orbit, valid_generic_ratio


Z = sp.symbols("z")


def derivative_factorization() -> tuple[sp.Expr, sp.Expr]:
    numerator, denominator = sp.together(sp.diff(j_invariant(Z), Z)).as_numer_denom()
    return sp.factor(numerator), sp.factor(denominator)


def exceptional_orbit_values() -> tuple[sp.Rational, sp.Rational, sp.Rational]:
    return tuple(sp.factor(j_invariant(value)) for value in (sp.Integer(1), sp.Integer(-2), sp.Rational(-1, 2)))


def s3_orbit_of_one() -> tuple[sp.Rational, sp.Rational, sp.Rational]:
    transforms = (
        Z,
        1 / Z,
        -(1 + Z),
        -1 / (1 + Z),
        -(1 + Z) / Z,
        -Z / (1 + Z),
    )
    return tuple(sorted({sp.Rational(transform.subs(Z, 1)) for transform in transforms}))


def finite_ramification_guardrails() -> dict[str, int]:
    primes = (5, 7, 11, 13, 17, 19, 97)
    checked = 0
    critical_hits = 0
    for p in primes:
        exceptional = ratio_orbit(1, p)
        for z in range(p):
            if not valid_generic_ratio(z, p):
                continue
            checked += 1
            derivative_zero = (
                (z - 1) * (z + 2) * (2 * z + 1) * (1 + z + z * z) ** 2
            ) % p == 0
            if derivative_zero != (z in exceptional):
                raise AssertionError((p, z, exceptional, derivative_zero))
            if derivative_zero:
                critical_hits += 1
    return {
        "primes": len(primes),
        "checked_generic_ratios": checked,
        "critical_hits": critical_hits,
    }


def j_ramification_summary() -> dict[str, int]:
    numerator, denominator = derivative_factorization()
    expected_numerator = sp.factor((Z - 1) * (Z + 2) * (2 * Z + 1) * norm(Z) ** 2)
    expected_denominator = Z**3 * (Z + 1) ** 3
    if sp.expand(numerator - expected_numerator) != 0:
        raise AssertionError((sp.factor(numerator), expected_numerator))
    if sp.expand(denominator - expected_denominator) != 0:
        raise AssertionError((sp.factor(denominator), expected_denominator))

    orbit = s3_orbit_of_one()
    if orbit != (sp.Rational(-2), sp.Rational(-1, 2), sp.Rational(1)):
        raise AssertionError(orbit)

    values = exceptional_orbit_values()
    if values != (sp.Rational(27, 4), sp.Rational(27, 4), sp.Rational(27, 4)):
        raise AssertionError(values)

    finite = finite_ramification_guardrails()
    if finite != {"primes": 7, "checked_generic_ratios": 147, "critical_hits": 21}:
        raise AssertionError(finite)

    critical_value = Fraction(27, 4)
    return {
        "derivative_numerator_degree": sp.degree(numerator, Z),
        "derivative_denominator_degree": sp.degree(denominator, Z),
        "admissible_critical_points": len(orbit),
        "critical_value_num": critical_value.numerator,
        "critical_value_den": critical_value.denominator,
        "finite_checked_generic_ratios": finite["checked_generic_ratios"],
        "finite_critical_hits": finite["critical_hits"],
    }


def main() -> None:
    summary = j_ramification_summary()
    numerator, denominator = derivative_factorization()
    print("h=3 repeat same-lambda J ramification")
    print(f"J'(z) numerator = {numerator}")
    print(f"J'(z) denominator = {denominator}")
    print("generic-domain derivative zeros are the S3 orbit {-2,-1/2,1}")
    print("excluded derivative zeros are roots of z^2+z+1, already outside the generic ratio domain")
    print(
        "summary: "
        f"num_degree={summary['derivative_numerator_degree']} "
        f"den_degree={summary['derivative_denominator_degree']} "
        f"admissible_critical_points={summary['admissible_critical_points']} "
        f"critical_value={summary['critical_value_num']}/{summary['critical_value_den']} "
        f"finite_checked={summary['finite_checked_generic_ratios']} "
        f"finite_critical_hits={summary['finite_critical_hits']}"
    )
    print("This isolates quotient ramification; it does not prove value injectivity.")
    print("H3_REPEAT_SAME_LAMBDA_J_RAMIFICATION_PASS")


if __name__ == "__main__":
    main()
