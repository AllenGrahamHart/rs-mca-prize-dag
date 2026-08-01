#!/usr/bin/env python3
"""Reconstruct the exact Q(i) cell-5 chart from split-prime samples."""

import json
import math
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
COMPILER = DIRECTORY / "rate_half_kb_positive_433_1a_common_vieta_compiler.py"
REMOTE_COMPILER = "/root/rate_half_kb_positive_433_1a_common_vieta_compiler.py"
SEEDS = (100_000, 200_000, 300_000, 400_000, 500_000, 600_000, 700_000, 800_000)

app = modal.App("rs-mca-positive-433-1a-cell5-chart-reconstruct")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMPILER, REMOTE_COMPILER)
)


@app.function(image=image, cpu=1.0, memory=1024, timeout=120)
def sample_prime(seed):
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    import rate_half_kb_positive_433_1a_common_vieta_compiler as compiler

    prime = int(sp.nextprime(seed))
    while prime % 4 != 1:
        prime = int(sp.nextprime(prime))
    roots = sp.sqrt_mod(-1, prime, all_roots=True)
    iota = int(min(roots))

    def chart_at(root):
        compiler.PRIME = prime
        compiler.IOTA = root
        variables, equations, _ = compiler.compile_cell(
            5, -1, -1, strip_fast=True
        )
        charts = []
        for equation in equations[:3]:
            polynomial = sp.Poly(equation, *variables, modulus=prime).monic()
            charts.append({
                ",".join(str(value) for value in monomial): int(coefficient) % prime
                for monomial, coefficient in polynomial.terms()
            })
        return charts

    return {
        "seed": seed,
        "prime": prime,
        "iota": iota,
        "plus": chart_at(iota),
        "minus": chart_at((-iota) % prime),
    }


@app.function(image=image, cpu=1.0, memory=1024, timeout=120)
def reconstruct(samples):
    from fractions import Fraction
    import hashlib

    import sympy as sp
    from sympy.ntheory.modular import crt

    def rational_reconstruct(residue, modulus):
        residue %= modulus
        bound = math.isqrt(modulus // 2)
        old_r, current_r = modulus, residue
        old_s, current_s = 0, 1
        while current_r > bound:
            quotient = old_r // current_r
            old_r, current_r = current_r, old_r - quotient * current_r
            old_s, current_s = current_s, old_s - quotient * current_s
        numerator, denominator = current_r, current_s
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        common = math.gcd(numerator, denominator)
        numerator //= common
        denominator //= common
        if (
            denominator == 0
            or abs(numerator) > bound
            or denominator > bound
            or (denominator * residue - numerator) % modulus
        ):
            raise RuntimeError(
                f"rational reconstruction failed for {residue} mod {modulus}"
            )
        return Fraction(numerator, denominator)

    primes = [sample["prime"] for sample in samples]
    modulus = math.prod(primes)
    t, r, c, b = sp.symbols("t r c b")
    variables = (t, r, c, b)
    labels = (1, t**2, r**2, -r**2, -1)
    guard_expressions = [
        labels[left] - labels[right]
        for left in range(5) for right in range(left + 1, 5)
    ]
    guard_expressions.extend((
        r, t, b, c, b-1, b+1, c-1, c+1, b-c, b+c,
    ))
    guard_factors = []
    for guard in guard_expressions:
        for factor, _ in sp.factor_list(guard, *variables, extension=sp.I)[1]:
            monic = sp.Poly(factor, *variables, extension=sp.I).monic().as_expr()
            if monic not in guard_factors:
                guard_factors.append(monic)
    charts = []
    for chart_index in range(3):
        support = set(samples[0]["plus"][chart_index])
        for sample in samples:
            if set(sample["plus"][chart_index]) != support:
                raise RuntimeError("plus support changed across primes")
            if set(sample["minus"][chart_index]) != support:
                raise RuntimeError("minus support changed across primes")
        expression = sp.Integer(0)
        coefficients = []
        for key in sorted(support, reverse=True):
            real_residues = []
            imag_residues = []
            for sample in samples:
                prime = sample["prime"]
                iota = sample["iota"]
                plus = sample["plus"][chart_index][key]
                minus = sample["minus"][chart_index][key]
                real_residues.append((plus + minus) * pow(2, -1, prime) % prime)
                imag_residues.append(
                    (plus - minus) * pow(2 * iota, -1, prime) % prime
                )
            real = rational_reconstruct(int(crt(primes, real_residues)[0]), modulus)
            imag = rational_reconstruct(int(crt(primes, imag_residues)[0]), modulus)
            coefficient = (
                sp.Rational(real.numerator, real.denominator)
                + sp.I * sp.Rational(imag.numerator, imag.denominator)
            )
            monomial = tuple(int(value) for value in key.split(","))
            term = coefficient
            for variable, exponent in zip(variables, monomial):
                term *= variable**exponent
            expression += term
            coefficients.append({
                "monomial": monomial,
                "real": [real.numerator, real.denominator],
                "imag": [imag.numerator, imag.denominator],
            })
        expression = sp.expand(expression)
        localized = sp.Poly(expression, *variables, extension=sp.I)
        removed_factors = []
        for factor in guard_factors:
            divisor = sp.Poly(factor, *variables, extension=sp.I)
            while True:
                quotient, remainder = localized.div(divisor)
                if not remainder.is_zero:
                    break
                localized = quotient
                removed_factors.append(str(factor))
        localized = localized.monic()
        localized_expression = sp.expand(localized.as_expr())
        charts.append({
            "index": chart_index,
            "terms": len(support),
            "degree": sp.Poly(expression, *variables, extension=sp.I).total_degree(),
            "expression": str(expression),
            "expression_sha256": hashlib.sha256(
                str(expression).encode()
            ).hexdigest(),
            "localized_degree": localized.total_degree(),
            "localized_terms": len(localized.terms()),
            "localized_expression": str(localized_expression),
            "localized_sha256": hashlib.sha256(
                str(localized_expression).encode()
            ).hexdigest(),
            "removed_guard_factors": removed_factors,
        })
    return {
        "status": "COMPLETE",
        "field": "Q(i)",
        "primes": primes,
        "modulus_bits": modulus.bit_length(),
        "guard_factors": [str(value) for value in guard_factors],
        "charts": charts,
    }


@app.function(image=image, cpu=1.0, memory=1024, timeout=120)
def analyze_ratio(reconstruction):
    import hashlib

    import sympy as sp

    t, r, c, b, x = sp.symbols("t r c b x")
    source_variables = (t, r, x)
    quotient_polynomials = []
    coefficient_ledgers = []
    for item in reconstruction["charts"]:
        expression = sp.sympify(
            item["localized_expression"],
            locals={"t": t, "r": r, "c": c, "b": b, "I": sp.I},
        )
        substituted = sp.Poly(
            sp.expand(expression.subs(c, b*x)), b, t, r, x,
            extension=sp.I,
        )
        minimum_b_degree = min(monomial[0] for monomial, _ in substituted.terms())
        if minimum_b_degree != 2:
            raise RuntimeError(f"unexpected b valuation {minimum_b_degree}")
        quotient = sp.expand(substituted.as_expr() / b**2)
        polynomial = sp.Poly(quotient, b, domain="EX")
        quotient_polynomials.append(polynomial)
        ledger = []
        for degree in range(polynomial.degree() + 1):
            coefficient = sp.factor(polynomial.nth(degree), extension=sp.I)
            coefficient_poly = sp.Poly(
                coefficient, *source_variables, extension=sp.I
            )
            ledger.append({
                "b_degree": degree,
                "degree": coefficient_poly.total_degree(),
                "terms": len(coefficient_poly.terms()),
                "factorization": str(coefficient),
            })
        coefficient_ledgers.append(ledger)

    linear = quotient_polynomials[0]
    if linear.degree() != 1:
        raise RuntimeError("first ratio equation is not linear in b")
    a0 = linear.nth(0)
    a1 = linear.nth(1)
    eliminants = []
    for index, quadratic in enumerate(quotient_polynomials[1:], start=1):
        if quadratic.degree() != 2:
            raise RuntimeError(f"ratio equation {index} is not quadratic in b")
        q0, q1, q2 = (quadratic.nth(degree) for degree in range(3))
        eliminant = sp.Poly(
            sp.expand(q0*a1**2 - q1*a0*a1 + q2*a0**2),
            *source_variables, extension=sp.I,
        ).monic()
        text = str(sp.expand(eliminant.as_expr()))
        eliminants.append({
            "source_chart": index,
            "degree": eliminant.total_degree(),
            "terms": len(eliminant.terms()),
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
        })
    return {
        "status": "COMPLETE",
        "coordinate": "x=c/b",
        "unit_removed": "b^2",
        "degrees_in_b": [value.degree() for value in quotient_polynomials],
        "coefficients": coefficient_ledgers,
        "b_reconstruction": f"b=-({sp.factor(a0, extension=sp.I)})/({sp.factor(a1, extension=sp.I)})",
        "eliminants": eliminants,
        "nonclaim": "denominator branch and source-curve emptiness remain open",
    }


@app.local_entrypoint()
def main():
    samples = list(sample_prime.map(SEEDS))
    result = reconstruct.remote(samples)
    ratio_analysis = analyze_ratio.remote(result)
    print(json.dumps({
        "scope": (
            "three monic guarded cell-5 common-chart minors reconstructed "
            "from split-prime samples; no outside, route, K3, row, or Prize claim"
        ),
        "samples": [
            {key: sample[key] for key in ("seed", "prime", "iota")}
            for sample in samples
        ],
        "result": result,
        "ratio_analysis": ratio_analysis,
    }, sort_keys=True))
