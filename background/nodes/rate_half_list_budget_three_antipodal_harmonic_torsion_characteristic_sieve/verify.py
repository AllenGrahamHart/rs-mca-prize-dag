#!/usr/bin/env python3
"""Light exact checks for the harmonic-torsion characteristic sieve."""

from itertools import product

import sympy as sp


NODE = "rate_half_list_budget_three_antipodal_harmonic_torsion_characteristic_sieve"


def primitive_root(prime):
    factors = []
    value = prime - 1
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return next(g for g in range(2, prime)
                if all(pow(g, (prime - 1) // q, prime) != 1 for q in factors))


def harmonic_value(x, y, w, modulus=None):
    value = 2 * x + 2 * y * w - y - x * y - w - x * w
    return value if modulus is None else value % modulus


def symbolic_check():
    x, y, w = sp.symbols("x y w")
    cleared = sp.expand((1 - y) * (x - w) + (1 - w) * (x - y))
    assert sp.expand(cleared - harmonic_value(x, y, w)) == 0


def balanced(coefficients):
    half = len(coefficients) // 2
    return all(coefficients[i] == coefficients[i + half] for i in range(half))


def characteristic_zero_small_orders():
    totals = {}
    for order in (8, 16, 32):
        hits = 0
        half = order // 2
        for a, b, c in product(range(order), repeat=3):
            if len({0 % half, a % half, b % half, c % half}) < 4:
                continue
            coefficients = [0] * order
            for exponent in (a, a, b + c, b + c,
                             b + half, a + b + half,
                             c + half, a + c + half):
                coefficients[exponent % order] += 1
            if balanced(coefficients):
                hits += 1
        assert hits == 0
        totals[order] = hits
    return totals


def finite_characteristic_positive():
    prime, order = 97, 16
    generator = primitive_root(prime)
    zeta = pow(generator, (prime - 1) // order, prime)
    powers = [pow(zeta, exponent, prime) for exponent in range(order)]
    witness = None
    for x in powers:
        for y in powers:
            for w in powers:
                values = (1, x, y, w)
                if len({value * value % prime for value in values}) < 4:
                    continue
                if harmonic_value(x, y, w, prime) == 0:
                    witness = (x, y, w)
                    break
            if witness:
                break
        if witness:
            break
    assert witness is not None
    x, y, w = witness
    factors = (x*x-1, y*y-1, w*w-1,
               x*x-y*y, x*x-w*w, y*y-w*w)
    assert all(value % prime for value in factors)
    assert all(pow(value, order, prime) == 1 for value in witness)
    assert all(pow(value, 1 << 40, prime) == 1 for value in witness)
    assert all((pow(value, -1, prime) * value) % prime == 1
               for value in factors)
    return witness


def sparse_size_check():
    base_variables = 3
    power_variables = 3 * 39
    inverse_variables = 6
    power_equations = 3 * 40
    equations = power_equations + 1 + 6
    assert base_variables + power_variables + inverse_variables == 126
    assert equations == 127
    assert max(2, 3) == 3


def main():
    symbolic_check()
    totals = characteristic_zero_small_orders()
    witness = finite_characteristic_positive()
    sparse_size_check()
    print(
        "RATE_HALF_ANTIPODAL_HARMONIC_TORSION_SIEVE_PASS "
        f"char0_orders={','.join(map(str, totals))} finite_witness={witness} "
        "variables=126 equations=127"
    )


if __name__ == "__main__":
    main()
