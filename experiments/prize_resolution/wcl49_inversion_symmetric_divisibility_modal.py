#!/usr/bin/env python3
"""Certify the finite branch obstructions for inversion-symmetric WCL (4,9)."""

from __future__ import annotations

import hashlib
import json
import math
import resource
import signal
import time
from functools import reduce

import modal


APP_NAME = "wcl49-inversion-symmetric-divisibility"

app = modal.App(APP_NAME)
image = modal.Image.debian_slim(python_version="3.12").pip_install("sympy==1.14.0")


def v2(value: int) -> int:
    count = 0
    while value and value % 2 == 0:
        count += 1
        value //= 2
    return count


def lcm(values: list[int]) -> int:
    return reduce(lambda left, right: left * right // math.gcd(left, right), values, 1)


@app.function(image=image, cpu=1, memory=1024, timeout=90, max_containers=1)
def certify() -> dict[str, object]:
    import sympy as sp

    started = time.monotonic()
    x, z, y = sp.symbols("x z y")
    c3 = -x**2 / 2
    c2 = -x * z - x**4 / 8
    e3 = sp.expand(2 * x * c2 + z**2 + 2 * z + 2 * c2 * c3)
    e4 = sp.expand(2 * x * c3 + 2 * x + 2 * z * c2 + 2 * z * c3 + c2**2)

    def primitive_integer_poly(expr, *variables):
        polynomial = sp.Poly(expr, *variables, domain=sp.QQ)
        denominator, integer_polynomial = polynomial.clear_denoms(convert=True)
        content, primitive = integer_polynomial.primitive()
        if primitive.LC() < 0:
            primitive = -primitive
            content = -content
        return int(denominator), abs(int(content)), primitive

    q_denominator, q_content, q_poly = primitive_integer_poly(e3, z, x)
    r_denominator, r_content, r_poly = primitive_integer_poly(e4, z, x)
    q_lc = sp.Poly(q_poly.as_expr(), z).LC()
    r_lc = sp.Poly(r_poly.as_expr(), z).LC()
    linear_combination = sp.expand(q_lc * r_poly.as_expr() - r_lc * q_poly.as_expr())
    l_denominator, l_content, l_poly = primitive_integer_poly(linear_combination, z, x)
    if sp.Poly(l_poly.as_expr(), z).degree() != 1:
        raise RuntimeError("substituted router did not reduce to one linear equation")

    eliminant_raw = sp.Poly(
        sp.resultant(q_poly.as_expr(), l_poly.as_expr(), z), x, domain=sp.ZZ
    )
    eliminant_content, eliminant_primitive = eliminant_raw.primitive()
    if eliminant_primitive.LC() < 0:
        eliminant_primitive = -eliminant_primitive
        eliminant_content = -eliminant_content
    factor_constant, factor_pairs = sp.factor_list(eliminant_primitive.as_expr(), x)
    factors = []
    for factor_expr, multiplicity in factor_pairs:
        factor = sp.Poly(factor_expr, x, domain=sp.QQ).monic()
        factors.append((factor, int(multiplicity)))

    router_exception_integer = abs(
        int(q_denominator)
        * int(q_content)
        * int(r_denominator)
        * int(r_content)
        * int(l_denominator)
        * int(l_content)
        * int(eliminant_content)
        * int(factor_constant)
    )
    router = {
        "q_denominator": q_denominator,
        "q_content": q_content,
        "q": str(q_poly.as_expr()),
        "r_denominator": r_denominator,
        "r_content": r_content,
        "r": str(r_poly.as_expr()),
        "l_denominator": l_denominator,
        "l_content": l_content,
        "l": str(l_poly.as_expr()),
        "eliminant_content": abs(int(eliminant_content)),
        "eliminant": str(eliminant_primitive.as_expr()),
        "factor_constant": int(factor_constant),
        "factors": [
            {"polynomial": str(factor.as_expr()), "multiplicity": multiplicity}
            for factor, multiplicity in factors
        ],
        "exception_integer": router_exception_integer,
    }
    print("WCL49_DIV_ROUTER " + json.dumps(router, sort_keys=True), flush=True)

    def reduce_mod(expr, modulus):
        return sp.rem(sp.Poly(expr, x, domain=sp.QQ), modulus).as_expr()

    def expression_denominator(expr) -> int:
        polynomial = sp.Poly(expr, x, domain=sp.QQ)
        return lcm([int(value.q) for value in polynomial.all_coeffs()])

    def quotient_remainder(c0_expr, c1_expr, c2_expr, c3_expr, modulus):
        def red(expr):
            if modulus is None:
                return sp.cancel(expr)
            return reduce_mod(expr, modulus)

        def add(left, right):
            return red(left + right)

        def mul(left, right):
            return red(left * right)

        a = [red(c0_expr), red(c1_expr), red(c2_expr), red(c3_expr), sp.Integer(1)]
        square = [sp.Integer(0)] * 9
        for left_index, left in enumerate(a):
            for right_index, right in enumerate(a):
                square[left_index + right_index] = add(
                    square[left_index + right_index], mul(left, right)
                )
        p = [sp.Integer(-1)] + square
        if p[-1] != 1:
            raise RuntimeError("P is not monic")

        def y_reduce(coefficients):
            output = [red(value) for value in coefficients]
            while len(output) > 9:
                degree = len(output) - 1
                leading = output[-1]
                output.pop()
                if leading != 0:
                    offset = degree - 9
                    for index in range(9):
                        output[offset + index] = add(
                            output[offset + index], -mul(leading, p[index])
                        )
            output += [sp.Integer(0)] * (9 - len(output))
            return output

        def y_multiply(left, right):
            product = [sp.Integer(0)] * (len(left) + len(right) - 1)
            for left_index, left_value in enumerate(left):
                for right_index, right_value in enumerate(right):
                    product[left_index + right_index] = add(
                        product[left_index + right_index],
                        mul(left_value, right_value),
                    )
            return y_reduce(product)

        power = [sp.Integer(1)] + [sp.Integer(0)] * 8
        base = [sp.Integer(0), sp.Integer(1)] + [sp.Integer(0)] * 7
        exponent = 1024
        while exponent:
            if exponent & 1:
                power = y_multiply(power, base)
            exponent >>= 1
            if exponent:
                base = y_multiply(base, base)
        power[0] = add(power[0], -1)
        return p, power

    def factor_integer(value: int) -> list[list[int]]:
        if abs(value) == 1:
            return []
        return [[int(prime), int(exponent)] for prime, exponent in sp.factorint(abs(value)).items()]

    branches: list[dict[str, object]] = []
    global_exception_primes = set(factor for factor, _ in factor_integer(router_exception_integer))

    for factor_index, (factor, multiplicity) in enumerate(factors):
        degree = factor.degree()
        if degree == 1:
            root = -factor.nth(0) / factor.nth(1)
            q_at_root = sp.Poly(q_poly.as_expr().subs(x, root), z, domain=sp.QQ)
            l_at_root = sp.Poly(l_poly.as_expr().subs(x, root), z, domain=sp.QQ)
            common = sp.gcd(q_at_root, l_at_root)
            if common.degree() < 1:
                raise RuntimeError(f"linear factor {factor.as_expr()} has no common z branch")
            common_factor_constant, common_factor_pairs = sp.factor_list(common.as_expr(), z)
            special_exception = abs(int(common_factor_constant.p))
            for z_factor_expr, z_multiplicity in common_factor_pairs:
                z_factor = sp.Poly(z_factor_expr, z, domain=sp.QQ)
                if z_factor.degree() != 1:
                    raise RuntimeError("special branch is not rational")
                z_value = -z_factor.nth(0) / z_factor.nth(1)
                c3_value = sp.cancel(c3.subs(x, root))
                c2_value = sp.cancel(c2.subs({x: root, z: z_value}))
                p_coefficients, remainder = quotient_remainder(
                    root, z_value, c2_value, c3_value, None
                )
                denominators = [
                    expression_denominator(value)
                    for value in p_coefficients + remainder
                ]
                nonzero_numerators = []
                remainder_records = []
                for index, value in enumerate(remainder):
                    numerator, denominator = sp.fraction(sp.cancel(value))
                    if numerator != 0:
                        nonzero_numerators.append(abs(int(numerator)))
                        remainder_records.append(
                            {
                                "index": index,
                                "value": str(value),
                                "numerator": str(numerator),
                                "denominator": int(denominator),
                            }
                        )
                obstruction = reduce(math.gcd, nonzero_numerators, 0)
                denominator_integer = lcm(denominators) * special_exception
                exception_factors = factor_integer(denominator_integer * obstruction)
                global_exception_primes.update(prime for prime, _ in exception_factors)
                record = {
                    "kind": "rational",
                    "factor_index": factor_index,
                    "factor": str(factor.as_expr()),
                    "factor_multiplicity": multiplicity,
                    "z_factor": str(z_factor.as_expr()),
                    "z_factor_multiplicity": int(z_multiplicity),
                    "x": str(root),
                    "z": str(z_value),
                    "c2": str(c2_value),
                    "c3": str(c3_value),
                    "p_coefficients": [str(value) for value in p_coefficients],
                    "remainder": remainder_records,
                    "obstruction_gcd": str(obstruction),
                    "denominator_integer": str(denominator_integer),
                    "exception_factors": exception_factors,
                }
                branches.append(record)
                print("WCL49_DIV_BRANCH " + json.dumps(record, sort_keys=True), flush=True)
        elif degree == 3:
            l_as_z = sp.Poly(l_poly.as_expr(), z)
            d = sp.Poly(l_as_z.coeff_monomial(z), x, domain=sp.QQ)
            h = sp.Poly(l_as_z.coeff_monomial(1), x, domain=sp.QQ)
            denominator_resultant = abs(int(sp.resultant(factor.as_expr(), d.as_expr(), x)))
            inverse = sp.invert(d, factor)
            z_value = reduce_mod(-h.as_expr() * inverse.as_expr(), factor)
            c3_value = reduce_mod(c3, factor)
            c2_value = reduce_mod(c2.subs(z, z_value), factor)
            q_residue = reduce_mod(q_poly.as_expr().subs(z, z_value), factor)
            l_residue = reduce_mod(l_poly.as_expr().subs(z, z_value), factor)
            if q_residue != 0 or l_residue != 0:
                raise RuntimeError(f"cubic parameterization failed for {factor.as_expr()}")
            p_coefficients, remainder = quotient_remainder(
                x, z_value, c2_value, c3_value, factor
            )
            denominator_values = [
                expression_denominator(value)
                for value in [z_value, c2_value, c3_value] + p_coefficients + remainder
            ]
            remainder_records = []
            resultants = []
            for index, value in enumerate(remainder):
                if value == 0:
                    continue
                denominator, integer_value = sp.Poly(value, x, domain=sp.QQ).clear_denoms(
                    convert=True
                )
                resultant = int(sp.resultant(factor.as_expr(), integer_value.as_expr(), x))
                resultants.append(abs(resultant))
                remainder_records.append(
                    {
                        "index": index,
                        "value": str(value),
                        "integer_numerator": str(integer_value.as_expr()),
                        "denominator": int(denominator),
                        "resultant": str(resultant),
                    }
                )
            obstruction = reduce(math.gcd, resultants, 0)
            denominator_integer = lcm(denominator_values) * denominator_resultant
            exception_factors = factor_integer(denominator_integer * obstruction)
            global_exception_primes.update(prime for prime, _ in exception_factors)
            record = {
                "kind": "cubic",
                "factor_index": factor_index,
                "factor": str(factor.as_expr()),
                "factor_multiplicity": multiplicity,
                "linear_coefficient": str(d.as_expr()),
                "linear_constant": str(h.as_expr()),
                "linear_coefficient_resultant": str(denominator_resultant),
                "z": str(z_value),
                "c2": str(c2_value),
                "c3": str(c3_value),
                "p_coefficients": [str(value) for value in p_coefficients],
                "remainder": remainder_records,
                "obstruction_gcd": str(obstruction),
                "denominator_integer": str(denominator_integer),
                "exception_factors": exception_factors,
            }
            branches.append(record)
            print("WCL49_DIV_BRANCH " + json.dumps(record, sort_keys=True), flush=True)
        else:
            raise RuntimeError(f"unexpected eliminant factor degree {degree}")

    all_exception_primes = sorted(global_exception_primes)
    official_compatible = [
        prime
        for prime in all_exception_primes
        if prime > 9 and prime < 2**256 and v2(prime - 1) >= 41
    ]
    canonical_payload = json.dumps(
        {"router": router, "branches": branches}, sort_keys=True, separators=(",", ":")
    )
    result = {
        "app": APP_NAME,
        "status": "COMPLETE",
        "seconds": round(time.monotonic() - started, 6),
        "peak_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024,
        "router": router,
        "branches": branches,
        "branch_count": len(branches),
        "exception_primes": all_exception_primes,
        "exception_prime_v2": {str(prime): v2(prime - 1) for prime in all_exception_primes},
        "official_compatible_exception_primes": official_compatible,
        "certificate_sha256": hashlib.sha256(canonical_payload.encode()).hexdigest(),
    }
    print("WCL49_DIV_RESULT " + json.dumps(result, sort_keys=True), flush=True)
    return result


@app.local_entrypoint()
def main() -> None:
    def alarm_handler(_signum, _frame):
        raise TimeoutError("85-second client alarm")

    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(85)
    try:
        print(json.dumps(certify.remote(), indent=2, sort_keys=True))
    finally:
        signal.alarm(0)
