#!/usr/bin/env python3
"""Independent exact replay of the WCL (4,9) inversion branch certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from functools import reduce
from pathlib import Path

import sympy as sp


APP_NAME = "wcl49-inversion-symmetric-divisibility"


def v2(value: int) -> int:
    count = 0
    while value and value % 2 == 0:
        count += 1
        value //= 2
    return count


def lcm(values: list[int]) -> int:
    return reduce(lambda left, right: left * right // math.gcd(left, right), values, 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("result", type=Path)
    args = parser.parse_args()
    result = json.loads(args.result.read_text())

    assert result["app"] == APP_NAME
    assert result["status"] == "COMPLETE"
    assert 0 <= float(result["seconds"]) <= 90
    assert 0 <= int(result["peak_mb"]) <= 1024

    x, z, y = sp.symbols("x z y")
    c3 = -x**2 / 2
    c2 = -x * z - x**4 / 8
    e3 = sp.expand(2 * x * c2 + z**2 + 2 * z + 2 * c2 * c3)
    e4 = sp.expand(2 * x * c3 + 2 * x + 2 * z * c2 + 2 * z * c3 + c2**2)

    def primitive(expr, *variables):
        denominator, integer = sp.Poly(expr, *variables, domain=sp.QQ).clear_denoms(
            convert=True
        )
        content, output = integer.primitive()
        if output.LC() < 0:
            output = -output
            content = -content
        return int(denominator), abs(int(content)), output

    q_den, q_content, q = primitive(e3, z, x)
    r_den, r_content, r = primitive(e4, z, x)
    q_lc = sp.Poly(q.as_expr(), z).LC()
    r_lc = sp.Poly(r.as_expr(), z).LC()
    l_den, l_content, linear = primitive(
        sp.expand(q_lc * r.as_expr() - r_lc * q.as_expr()), z, x
    )
    eliminant_raw = sp.Poly(sp.resultant(q.as_expr(), linear.as_expr(), z), x)
    eliminant_content, eliminant = eliminant_raw.primitive()
    if eliminant.LC() < 0:
        eliminant = -eliminant
        eliminant_content = -eliminant_content
    factor_constant, factor_pairs = sp.factor_list(eliminant.as_expr(), x)
    expected_factors = [
        {
            "polynomial": str(sp.Poly(factor, x, domain=sp.QQ).monic().as_expr()),
            "multiplicity": int(multiplicity),
        }
        for factor, multiplicity in factor_pairs
    ]
    router = result["router"]
    assert router["q_denominator"] == q_den
    assert router["q_content"] == q_content
    assert router["q"] == str(q.as_expr())
    assert router["r_denominator"] == r_den
    assert router["r_content"] == r_content
    assert router["r"] == str(r.as_expr())
    assert router["l_denominator"] == l_den
    assert router["l_content"] == l_content
    assert router["l"] == str(linear.as_expr())
    assert router["eliminant_content"] == abs(int(eliminant_content))
    assert router["eliminant"] == str(eliminant.as_expr())
    assert router["factor_constant"] == int(factor_constant)
    assert router["factors"] == expected_factors
    expected_router_exception = abs(
        q_den
        * q_content
        * r_den
        * r_content
        * l_den
        * l_content
        * int(eliminant_content)
        * int(factor_constant)
    )
    assert router["exception_integer"] == expected_router_exception

    exception_primes = set()
    branch_coverage = Counter()
    for branch in result["branches"]:
        factor = sp.Poly(sp.sympify(branch["factor"]), x, domain=sp.QQ)
        factor_index = int(branch["factor_index"])
        assert branch["factor"] == expected_factors[factor_index]["polynomial"]
        assert branch["factor_multiplicity"] == expected_factors[factor_index]["multiplicity"]
        branch_coverage[factor_index] += 1
        c0_value = sp.sympify(branch.get("x", "x"))
        c1_value = sp.sympify(branch["z"])
        c2_value = sp.sympify(branch["c2"])
        c3_value = sp.sympify(branch["c3"])

        def red(expr):
            if branch["kind"] == "rational":
                return sp.cancel(expr)
            return sp.rem(sp.Poly(expr, x, domain=sp.QQ), factor).as_expr()

        anti = [
            c0_value**2 + 2 * c3_value,
            2 * c0_value * c1_value + 2 * c2_value + c3_value**2,
            2 * c0_value * c2_value
            + c1_value**2
            + 2 * c1_value
            + 2 * c2_value * c3_value,
            2 * c0_value * c3_value
            + 2 * c0_value
            + 2 * c1_value * c2_value
            + 2 * c1_value * c3_value
            + c2_value**2,
        ]
        assert all(red(value) == 0 for value in anti)
        a = y**4 + c3_value * y**3 + c2_value * y**2 + c1_value * y + c0_value
        p = sp.Poly(sp.expand(y * a**2 - 1), y)
        assert [str(red(p.nth(index))) for index in range(10)] == branch["p_coefficients"]

        coefficients = [red(p.nth(index)) for index in range(10)]
        power = [sp.Integer(1)] + [sp.Integer(0)] * 8
        base = [sp.Integer(0), sp.Integer(1)] + [sp.Integer(0)] * 7

        def multiply(left, right):
            product = [sp.Integer(0)] * 17
            for i, left_value in enumerate(left):
                for j, right_value in enumerate(right):
                    product[i + j] = red(product[i + j] + left_value * right_value)
            for degree in range(16, 8, -1):
                leading = product[degree]
                if leading:
                    for index in range(9):
                        product[degree - 9 + index] = red(
                            product[degree - 9 + index] - leading * coefficients[index]
                        )
            return [red(value) for value in product[:9]]

        exponent = 1024
        while exponent:
            if exponent & 1:
                power = multiply(power, base)
            exponent >>= 1
            if exponent:
                base = multiply(base, base)
        power[0] = red(power[0] - 1)
        recorded = branch["remainder"]
        assert [item["index"] for item in recorded] == [
            index for index, value in enumerate(power) if value != 0
        ]

        obstruction_values = []
        for item in recorded:
            index = item["index"]
            assert item["value"] == str(power[index])
            if branch["kind"] == "rational":
                numerator, denominator = sp.fraction(sp.cancel(power[index]))
                assert item["numerator"] == str(numerator)
                assert item["denominator"] == int(denominator)
                obstruction_values.append(abs(int(numerator)))
            else:
                denominator, numerator = sp.Poly(
                    power[index], x, domain=sp.QQ
                ).clear_denoms(convert=True)
                resultant_value = int(sp.resultant(factor.as_expr(), numerator.as_expr(), x))
                assert item["integer_numerator"] == str(numerator.as_expr())
                assert item["denominator"] == int(denominator)
                assert item["resultant"] == str(resultant_value)
                obstruction_values.append(abs(resultant_value))
        obstruction = reduce(math.gcd, obstruction_values, 0)
        assert branch["obstruction_gcd"] == str(obstruction)
        if branch["kind"] == "rational":
            root = -factor.nth(0) / factor.nth(1)
            assert c0_value == root
            q_at_root = sp.Poly(q.as_expr().subs(x, root), z, domain=sp.QQ)
            l_at_root = sp.Poly(linear.as_expr().subs(x, root), z, domain=sp.QQ)
            common = sp.gcd(q_at_root, l_at_root)
            common_constant, common_factors = sp.factor_list(common.as_expr(), z)
            recorded_z_factor = sp.Poly(sp.sympify(branch["z_factor"]), z, domain=sp.QQ)
            assert any(
                sp.Poly(item, z, domain=sp.QQ) == recorded_z_factor
                and int(multiplicity) == branch["z_factor_multiplicity"]
                for item, multiplicity in common_factors
            )
            assert recorded_z_factor.eval(c1_value) == 0
            denominator_values = [
                int(sp.denom(sp.cancel(value))) for value in coefficients + power
            ]
            expected_denominator = lcm(denominator_values) * abs(
                int(sp.numer(common_constant))
            )
        else:
            linear_in_z = sp.Poly(linear.as_expr(), z)
            d = sp.Poly(linear_in_z.coeff_monomial(z), x, domain=sp.QQ)
            h = sp.Poly(linear_in_z.coeff_monomial(1), x, domain=sp.QQ)
            assert branch["linear_coefficient"] == str(d.as_expr())
            assert branch["linear_constant"] == str(h.as_expr())
            denominator_resultant = abs(int(sp.resultant(factor.as_expr(), d.as_expr(), x)))
            assert branch["linear_coefficient_resultant"] == str(denominator_resultant)
            inverse = sp.invert(d, factor)
            expected_z = sp.rem(
                sp.Poly(-h.as_expr() * inverse.as_expr(), x, domain=sp.QQ), factor
            ).as_expr()
            assert c1_value == expected_z
            denominator_values = []
            for value in [c1_value, c2_value, c3_value] + coefficients + power:
                denominator_values.extend(
                    int(coefficient.q)
                    for coefficient in sp.Poly(value, x, domain=sp.QQ).all_coeffs()
                )
            expected_denominator = lcm(denominator_values) * denominator_resultant
        assert branch["denominator_integer"] == str(expected_denominator)
        factors = [[int(prime), int(exponent)] for prime, exponent in sp.factorint(
            int(branch["denominator_integer"]) * obstruction
        ).items()]
        assert branch["exception_factors"] == factors
        exception_primes.update(prime for prime, _ in factors)

    router_factors = sp.factorint(int(router["exception_integer"]))
    exception_primes.update(int(prime) for prime in router_factors)
    assert result["branch_count"] == len(result["branches"])
    expected_coverage = Counter()
    for index, item in enumerate(expected_factors):
        degree = sp.Poly(sp.sympify(item["polynomial"]), x).degree()
        expected_coverage[index] = 2 if degree == 1 else 1
    assert branch_coverage == expected_coverage
    assert result["exception_primes"] == sorted(exception_primes)
    assert result["exception_prime_v2"] == {
        str(prime): v2(prime - 1) for prime in sorted(exception_primes)
    }
    expected_official = [
        prime
        for prime in sorted(exception_primes)
        if prime > 9 and prime < 2**256 and v2(prime - 1) >= 41
    ]
    assert result["official_compatible_exception_primes"] == expected_official
    payload = json.dumps(
        {"router": router, "branches": result["branches"]},
        sort_keys=True,
        separators=(",", ":"),
    )
    assert result["certificate_sha256"] == hashlib.sha256(payload.encode()).hexdigest()
    print(
        "WCL49_INVERSION_SYMMETRIC_DIVISIBILITY_CHECK_PASS "
        f"branches={len(result['branches'])} exceptions={len(exception_primes)} "
        f"official={len(expected_official)}"
    )


if __name__ == "__main__":
    main()
