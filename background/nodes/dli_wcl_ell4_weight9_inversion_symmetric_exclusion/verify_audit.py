#!/usr/bin/env python3
"""Independent stdlib audit of the WCL (4,9) inversion certificate."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction as F
from functools import reduce
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "experiments/prize_resolution/wcl49_inversion_symmetric_divisibility_result.json"


def trim(values):
    output = list(values)
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def padd(left, right):
    output = [F(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        output[index] += value
    for index, value in enumerate(right):
        output[index] += value
    return trim(output)


def pscale(polynomial, scalar):
    return trim([F(scalar) * value for value in polynomial])


def pmul(left, right):
    output = [F(0)] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            output[i + j] += left_value * right_value
    return trim(output)


def ppow(polynomial, exponent):
    output = [F(1)]
    base = polynomial
    while exponent:
        if exponent & 1:
            output = pmul(output, base)
        exponent >>= 1
        if exponent:
            base = pmul(base, base)
    return output


class Ring:
    def __init__(self, modulus=None):
        self.modulus = None if modulus is None else [F(value) for value in modulus]
        if self.modulus is not None:
            assert self.modulus[-1] == 1

    def red(self, polynomial):
        output = trim([F(value) for value in polynomial])
        if self.modulus is None:
            assert len(output) == 1
            return output
        while len(output) >= len(self.modulus):
            leading = output[-1]
            offset = len(output) - len(self.modulus)
            if leading:
                for index, value in enumerate(self.modulus):
                    output[offset + index] -= leading * value
            output = trim(output)
        return output

    def add(self, left, right):
        return self.red(padd(left, right))

    def mul(self, left, right):
        return self.red(pmul(left, right))

    def scale(self, value, scalar):
        return self.red(pscale(value, scalar))


def badd(left, right):
    output = dict(left)
    for monomial, value in right.items():
        output[monomial] = output.get(monomial, F(0)) + value
        if output[monomial] == 0:
            del output[monomial]
    return output


def bscale(polynomial, scalar):
    return {monomial: value * F(scalar) for monomial, value in polynomial.items() if value}


def bmul(left, right):
    output = {}
    for (x_left, z_left), left_value in left.items():
        for (x_right, z_right), right_value in right.items():
            monomial = (x_left + x_right, z_left + z_right)
            output[monomial] = output.get(monomial, F(0)) + left_value * right_value
    return {monomial: value for monomial, value in output.items() if value}


def bpow(polynomial, exponent):
    output = {(0, 0): F(1)}
    base = polynomial
    while exponent:
        if exponent & 1:
            output = bmul(output, base)
        exponent >>= 1
        if exponent:
            base = bmul(base, base)
    return output


def bcoefficient(polynomial, z_degree):
    maximum = max((x_degree for (x_degree, degree) in polynomial if degree == z_degree), default=0)
    output = [F(0)] * (maximum + 1)
    for (x_degree, degree), value in polynomial.items():
        if degree == z_degree:
            output[x_degree] = value
    return trim(output)


def determinant_bareiss(matrix):
    values = [list(row) for row in matrix]
    size = len(values)
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        if values[pivot_index][pivot_index] == 0:
            swap = next(
                (row for row in range(pivot_index + 1, size) if values[row][pivot_index]),
                None,
            )
            if swap is None:
                return 0
            values[pivot_index], values[swap] = values[swap], values[pivot_index]
            sign *= -1
        pivot = values[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = values[row][column] * pivot - values[row][pivot_index] * values[pivot_index][column]
                assert numerator % previous == 0
                values[row][column] = numerator // previous
        previous = pivot
    return sign * values[-1][-1]


def resultant(left, right):
    left = trim(left)
    right = trim(right)
    m = len(left) - 1
    n = len(right) - 1
    size = m + n
    rows = []
    left_high = list(reversed(left))
    right_high = list(reversed(right))
    for shift in range(n):
        rows.append([0] * shift + left_high + [0] * (size - shift - len(left_high)))
    for shift in range(m):
        rows.append([0] * shift + right_high + [0] * (size - shift - len(right_high)))
    return determinant_bareiss(rows)


def denominator(polynomial):
    output = 1
    for value in polynomial:
        output = math.lcm(output, value.denominator)
    return output


def y_power_remainder(ring, p_coefficients):
    def y_reduce(coefficients):
        output = [ring.red(value) for value in coefficients]
        while len(output) > 9:
            degree = len(output) - 1
            leading = output.pop()
            if leading != [F(0)]:
                offset = degree - 9
                for index in range(9):
                    output[offset + index] = ring.add(
                        output[offset + index],
                        ring.scale(ring.mul(leading, p_coefficients[index]), -1),
                    )
        output += [[F(0)]] * (9 - len(output))
        return output

    def multiply(left, right):
        output = [[F(0)] for _ in range(len(left) + len(right) - 1)]
        for i, left_value in enumerate(left):
            for j, right_value in enumerate(right):
                output[i + j] = ring.add(output[i + j], ring.mul(left_value, right_value))
        return y_reduce(output)

    one = [F(1)]
    zero = [F(0)]
    power = [one] + [zero] * 8
    base = [zero, one] + [zero] * 7
    exponent = 1024
    while exponent:
        if exponent & 1:
            power = multiply(power, base)
        exponent >>= 1
        if exponent:
            base = multiply(base, base)
    power[0] = ring.add(power[0], [F(-1)])
    return power


def factor_small(value):
    output = []
    remaining = abs(value)
    for prime in (2, 3, 17, 19):
        exponent = 0
        while remaining % prime == 0:
            exponent += 1
            remaining //= prime
        if exponent:
            output.append([prime, exponent])
    assert remaining == 1
    return output


BRANCHES = [
    ("x - 2", None, [F(2)], [F(0)], [F(-2)], [F(-2)], "0", "-2", "-2"),
    ("x - 2", None, [F(2)], [F(-2)], [F(2)], [F(-2)], "-2", "2", "-2"),
    ("x", None, [F(0)], [F(0)], [F(0)], [F(0)], "0", "0", "0"),
    ("x", None, [F(0)], [F(-2)], [F(0)], [F(0)], "-2", "0", "0"),
    ("x**3 - 6*x**2 + 8", [8, 0, -6, 1], [0, 1], [2, 0, -1], [-2, -1, F(3, 2)], [0, 0, F(-1, 2)], "2 - x**2", "3*x**2/2 - x - 2", "-x**2/2"),
    ("x**3 - 6*x**2 + 24", [24, 0, -6, 1], [0, 1], [4, 0, -1], [-6, -1, F(3, 2)], [0, 0, F(-1, 2)], "4 - x**2", "3*x**2/2 - x - 6", "-x**2/2"),
    ("x**3 - 12*x - 8", [-8, -12, 0, 1], [0, 1], [-2, -2], [0, 1, F(1, 2)], [0, 0, F(-1, 2)], "-2*x - 2", "x**2/2 + x", "-x**2/2"),
    ("x**3 - 12*x + 8", [8, -12, 0, 1], [0, 1], [0, -2], [0, 1, F(1, 2)], [0, 0, F(-1, 2)], "-2*x", "x**2/2 + x", "-x**2/2"),
]


def audit(data, emit=True):
    # Reconstruct the anti-reciprocity router without SymPy.
    bx = {(1, 0): F(1)}
    bz = {(0, 1): F(1)}
    bc3 = bscale(bpow(bx, 2), F(-1, 2))
    bc2 = badd(bscale(bmul(bx, bz), -1), bscale(bpow(bx, 4), F(-1, 8)))
    e3 = badd(
        badd(bscale(bmul(bx, bc2), 2), bpow(bz, 2)),
        badd(bscale(bz, 2), bscale(bmul(bc2, bc3), 2)),
    )
    e4 = badd(
        badd(bscale(bmul(bx, bc3), 2), bscale(bx, 2)),
        badd(
            badd(bscale(bmul(bz, bc2), 2), bscale(bmul(bz, bc3), 2)),
            bpow(bc2, 2),
        ),
    )
    q = bscale(e3, 8)
    r = bscale(e4, 64)
    q_lc = bcoefficient(q, 2)
    r_lc = bcoefficient(r, 2)
    linear_raw = badd(bscale(bmul({(i, 0): value for i, value in enumerate(q_lc)}, r), 1), bscale(bmul({(i, 0): value for i, value in enumerate(r_lc)}, q), -1))
    linear = bscale(linear_raw, F(1, 8))
    q0, q1, q2 = (bcoefficient(q, index) for index in range(3))
    l0, l1 = (bcoefficient(linear, index) for index in range(2))
    eliminant = padd(padd(pmul(q2, ppow(l0, 2)), pscale(pmul(pmul(q1, l1), l0), -1)), pmul(q0, ppow(l1, 2)))
    factors = ([0, 1], [-2, 1], [8, 0, -6, 1], [24, 0, -6, 1], [-8, -12, 0, 1], [8, -12, 0, 1])
    product = pmul(ppow(factors[0], 2), ppow(factors[1], 2))
    for factor in factors[2:]:
        product = pmul(product, factor)
    assert eliminant == pscale(product, 8)
    assert data["router"]["exception_integer"] == 32768
    assert len(data["branches"]) == len(BRANCHES)

    d_polynomial = l1
    exception_primes = {2}
    for record, specification in zip(data["branches"], BRANCHES):
        factor_text, modulus, c0, c1, c2, c3, c1_text, c2_text, c3_text = specification
        assert record["factor"] == factor_text
        assert record["z"] == c1_text and record["c2"] == c2_text and record["c3"] == c3_text
        ring = Ring(modulus)
        c0, c1, c2, c3 = (ring.red(value) for value in (c0, c1, c2, c3))
        anti = [
            ring.add(ring.mul(c0, c0), ring.scale(c3, 2)),
            ring.add(ring.add(ring.scale(ring.mul(c0, c1), 2), ring.scale(c2, 2)), ring.mul(c3, c3)),
            ring.add(ring.add(ring.add(ring.scale(ring.mul(c0, c2), 2), ring.mul(c1, c1)), ring.scale(c1, 2)), ring.scale(ring.mul(c2, c3), 2)),
            ring.add(ring.add(ring.add(ring.add(ring.scale(ring.mul(c0, c3), 2), ring.scale(c0, 2)), ring.scale(ring.mul(c1, c2), 2)), ring.scale(ring.mul(c1, c3), 2)), ring.mul(c2, c2)),
        ]
        assert all(value == [F(0)] for value in anti)
        a = [c0, c1, c2, c3, [F(1)]]
        square = [[F(0)] for _ in range(9)]
        for i, left in enumerate(a):
            for j, right in enumerate(a):
                square[i + j] = ring.add(square[i + j], ring.mul(left, right))
        p_coefficients = [[F(-1)]] + square
        remainder = y_power_remainder(ring, p_coefficients)
        recorded_remainder = record["remainder"]
        assert [item["index"] for item in recorded_remainder] == [index for index, value in enumerate(remainder) if value != [F(0)]]
        obstructions = []
        for item in recorded_remainder:
            value = remainder[item["index"]]
            scale = denominator(value)
            numerator = [int(coefficient * scale) for coefficient in value]
            if modulus is None:
                assert item["denominator"] == scale
                assert item["numerator"] == str(numerator[0])
                obstruction = abs(numerator[0])
            else:
                obstruction = abs(resultant(modulus, numerator))
                assert item["denominator"] == scale
                assert abs(int(item["resultant"])) == obstruction
            obstructions.append(obstruction)
        assert reduce(math.gcd, obstructions, 0) == 1
        assert record["obstruction_gcd"] == "1"
        if modulus is None:
            denominator_integer = 1
        else:
            coefficient_resultant = abs(resultant(modulus, [int(value) for value in d_polynomial]))
            assert record["linear_coefficient_resultant"] == str(coefficient_resultant)
            all_values = [c1, c2, c3] + p_coefficients + remainder
            denominator_integer = coefficient_resultant * reduce(
                math.lcm, (denominator(value) for value in all_values), 1
            )
        assert record["denominator_integer"] == str(denominator_integer)
        expected_factors = factor_small(denominator_integer)
        assert record["exception_factors"] == expected_factors
        exception_primes.update(prime for prime, _ in expected_factors)

    assert data["exception_primes"] == sorted(exception_primes) == [2, 3, 17, 19]
    assert data["exception_prime_v2"] == {"2": 0, "3": 1, "17": 4, "19": 1}
    assert data["official_compatible_exception_primes"] == []
    payload = json.dumps(
        {"router": data["router"], "branches": data["branches"]},
        sort_keys=True,
        separators=(",", ":"),
    )
    assert data["certificate_sha256"] == hashlib.sha256(payload.encode()).hexdigest()
    if emit:
        print(
            "DLI_WCL_ELL4_WEIGHT9_INVERSION_SYMMETRIC_EXCLUSION_AUDIT_PASS "
            "branches=8 obstruction_gcds=1 exceptions=2,3,17,19 official=0"
        )


if __name__ == "__main__":
    audit(json.loads(RESULT.read_text()))
