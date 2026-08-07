#!/usr/bin/env python3
"""Exact algebra and Burnside checks for the squared-root router."""

from __future__ import annotations

import itertools
from collections import defaultdict


Monomial = tuple[int, ...]
Polynomial = dict[Monomial, int]
VARIABLES = 5


def add(left: Polynomial, right: Polynomial, scale: int = 1) -> Polynomial:
    out = defaultdict(int, left)
    for monomial, coefficient in right.items():
        out[monomial] += scale * coefficient
        if out[monomial] == 0:
            del out[monomial]
    return dict(out)


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    out: defaultdict[Monomial, int] = defaultdict(int)
    for a, ca in left.items():
        for b, cb in right.items():
            out[tuple(x + y for x, y in zip(a, b))] += ca * cb
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def power(value: Polynomial, exponent: int) -> Polynomial:
    out = {(0,) * VARIABLES: 1}
    base = value
    while exponent:
        if exponent & 1:
            out = multiply(out, base)
        base = multiply(base, base)
        exponent //= 2
    return out


def variable(index: int, exponent: int = 1) -> Polynomial:
    monomial = [0] * VARIABLES
    monomial[index] = exponent
    return {tuple(monomial): 1}


def scalar(value: Polynomial, coefficient: int) -> Polynomial:
    return {monomial: coefficient * entry for monomial, entry in value.items()}


def elementary_square(degree: int) -> Polynomial:
    out: Polynomial = {}
    for indices in itertools.combinations(range(VARIABLES), degree):
        monomial = [0] * VARIABLES
        for index in indices:
            monomial[index] = 2
        out[tuple(monomial)] = 1
    return out


def restrict_product_one(value: Polynomial) -> Polynomial:
    """Substitute x_4=(x_0*x_1*x_2*x_3)^-1 as a Laurent polynomial."""
    out: defaultdict[tuple[int, int, int, int], int] = defaultdict(int)
    for monomial, coefficient in value.items():
        tail = monomial[4]
        key = tuple(monomial[index] - tail for index in range(4))
        out[key] += coefficient
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def check_factor_identity() -> tuple[int, int]:
    e1, e2, e3, e4 = (elementary_square(degree) for degree in range(1, 5))
    d = add(scalar(e2, 4), power(e1, 2), scale=-1)
    left_inner = add(power(d, 2), scalar(e4, -64))
    left = power(left_inner, 2)
    left = add(left, scalar(e3, -16384))
    left = add(left, scalar(multiply(e1, d), 2048))

    right = {(0,) * VARIABLES: 1}
    sign_rows = 0
    for signs in itertools.product((1, -1), repeat=VARIABLES):
        sign_product = 1
        linear: Polynomial = {}
        for index, sign in enumerate(signs):
            sign_product *= sign
            linear = add(linear, scalar(variable(index), sign))
        if sign_product == 1:
            right = multiply(right, linear)
            sign_rows += 1
    if sign_rows != 16 or restrict_product_one(left) != restrict_product_one(right):
        raise AssertionError("factor identity")
    return len(left), len(right)


def burnside_count(modulus: int = 256, weight: int = 5) -> tuple[int, int, int]:
    fixed_sum = 0
    identity_fixed = None
    for multiplier in range(1, modulus, 2):
        seen = [False] * modulus
        cycles: list[list[int]] = []
        for start in range(modulus):
            if seen[start]:
                continue
            cycle = []
            value = start
            while not seen[value]:
                seen[value] = True
                cycle.append(value)
                value = multiplier * value % modulus
            cycles.append(cycle)

        counts = [[0] * modulus for _ in range(weight + 1)]
        counts[0][0] = 1
        for cycle in cycles:
            width = len(cycle)
            if width > weight:
                continue
            residue = sum(cycle) % modulus
            for size in range(weight - width, -1, -1):
                for old_residue, count in enumerate(counts[size]):
                    if count:
                        counts[size + width][(old_residue + residue) % modulus] += count
        fixed = counts[weight][0]
        fixed_sum += fixed
        if multiplier == 1:
            identity_fixed = fixed

    group_order = modulus // 2
    if fixed_sum % group_order:
        raise AssertionError("Burnside divisibility")
    if identity_fixed is None:
        raise AssertionError("identity multiplier")
    return identity_fixed, fixed_sum, fixed_sum // group_order


def subgroup_generator(prime: int, order: int) -> int:
    for candidate in range(2, prime):
        value = pow(candidate, (prime - 1) // order, prime)
        if pow(value, order, prime) == 1 and pow(value, order // 2, prime) != 1:
            return value
    raise AssertionError((prime, order))


def psi(values: tuple[int, ...], prime: int) -> int:
    e = [1]
    for value in values:
        e.append(0)
        for degree in range(len(e) - 1, 0, -1):
            e[degree] = (e[degree] + value * e[degree - 1]) % prime
    e1, e2, e3, e4 = e[1:5]
    d = (4 * e2 - e1 * e1) % prime
    return ((d * d - 64 * e4) ** 2 - 16384 * e3 + 2048 * e1 * d) % prime


def finite_field_check() -> tuple[int, int]:
    prime, half_order = 97, 16
    omega = subgroup_generator(prime, 2 * half_order)
    roots = tuple(pow(omega, 2 * exponent, prime) for exponent in range(half_order))
    checked = zeros = 0
    for exponents in itertools.combinations(range(half_order), 5):
        if sum(exponents) % half_order:
            continue
        values = tuple(roots[index] for index in exponents)
        base_lifts = tuple(pow(omega, index, prime) for index in exponents)
        base_product = 1
        for value in base_lifts:
            base_product = base_product * value % prime
        direct = False
        for signs in itertools.product((1, -1), repeat=5):
            sign_product = 1
            total = 0
            for sign, value in zip(signs, base_lifts):
                sign_product *= sign
                total += sign * value
            if sign_product % prime == pow(base_product, -1, prime) and total % prime == 0:
                direct = True
                break
        routed = psi(values, prime) == 0
        if direct != routed:
            raise AssertionError((exponents, direct, routed))
        checked += 1
        zeros += routed
    if not checked or not zeros:
        raise AssertionError((checked, zeros))
    return checked, zeros


def main() -> None:
    terms = check_factor_identity()
    identity, fixed_sum, orbits = burnside_count()
    if (identity, fixed_sum, orbits) != (34_412_301, 36_997_504, 289_043):
        raise AssertionError((identity, fixed_sum, orbits))
    checked, zeros = finite_field_check()
    print(
        "DLI_WCL_WEIGHT5_SQUARED_ROOT_HYPERSURFACE_ROUTER_PASS "
        f"terms={terms} subsets={identity} fixed_sum={fixed_sum} "
        f"orbits={orbits} finite_rows={checked} finite_zeros={zeros}"
    )


if __name__ == "__main__":
    main()
