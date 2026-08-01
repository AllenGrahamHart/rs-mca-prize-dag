#!/usr/bin/env python3
"""Independent Rabin audit for the nonlinear cell-9 factors."""


P = 2130706433
FACTORS = (
    (1, 4, 1),
    (1407143830, 1404350966, 1),
    (1534079870, 929941889, 2020652850, 1839969256, 743067152, 1),
    (1, 2130706429, 1),
    (626668491, 1382372662, 1),
    (1579005766, 501462577, 982511408, 936405335, 765045444, 1),
    (1, 2130706429, 1),
    (1407143830, 726355467, 1),
    (596626563, 929941889, 110053583, 1839969256, 1387639281, 1),
    (1, 4, 1),
    (626668491, 748333771, 1),
    (551700667, 501462577, 1148195025, 936405335, 1365660989, 1),
)


def trim(polynomial):
    output = [value % P for value in polynomial]
    while output and output[-1] == 0:
        output.pop()
    return output


def remainder(dividend, divisor):
    output = trim(dividend)
    divisor = trim(divisor)
    inverse = pow(divisor[-1], -1, P)
    while len(output) >= len(divisor):
        shift = len(output)-len(divisor)
        scalar = output[-1]*inverse % P
        for index, coefficient in enumerate(divisor):
            output[index+shift] = (
                output[index+shift]-scalar*coefficient
            ) % P
        output = trim(output)
    return output


def multiply_mod(left, right, modulus):
    product = [0]*(len(left)+len(right)-1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            product[i+j] = (product[i+j]+left_value*right_value) % P
    return remainder(product, modulus)


def power_mod(base, exponent, modulus):
    output = [1]
    factor = base
    while exponent:
        if exponent & 1:
            output = multiply_mod(output, factor, modulus)
        factor = multiply_mod(factor, factor, modulus)
        exponent //= 2
    return output


def gcd(left, right):
    left = trim(left)
    right = trim(right)
    while right:
        left, right = right, remainder(left, right)
    inverse = pow(left[-1], -1, P)
    return [(value*inverse) % P for value in left]


def subtract_x(polynomial):
    output = list(polynomial)+[0]*(max(2, len(polynomial))-len(polynomial))
    output[1] = (output[1]-1) % P
    return trim(output)


def irreducible(polynomial):
    degree = len(polynomial)-1
    first_frobenius = power_mod([0, 1], P, polynomial)
    if gcd(polynomial, subtract_x(first_frobenius)) != [1]:
        return False
    value = [0, 1]
    for _ in range(degree):
        value = power_mod(value, P, polynomial)
    return remainder(subtract_x(value), polynomial) == []


def main():
    if not all(irreducible(factor) for factor in FACTORS):
        raise RuntimeError("Rabin factor audit")
    print(
        "RATE_HALF_KB_ONE_LOOP_433_CELL9_FACTOR_AUDIT_PASS "
        f"field={P} quadratics=8 quintics=4"
    )


if __name__ == "__main__":
    main()
