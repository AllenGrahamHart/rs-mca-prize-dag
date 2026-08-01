#!/usr/bin/env python3
"""Independent Rabin audit for the nonlinear cell-11 factors."""


P = 2130706433
FACTORS = (
    (2113994754, 1889258816, 1),
    (2130706432, 457119785, 1480824898, 291582651, 1),
    (16711679, 1723721688, 1),
    (2130706432, 291582651, 649881535, 457119785, 1),
    (2113994754, 241447617, 1),
    (2130706432, 1673586648, 1480824898, 1839123782, 1),
    (16711679, 406984745, 1),
    (2130706432, 1839123782, 649881535, 1673586648, 1),
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


def prime_divisors(value):
    output = []
    divisor = 2
    while divisor*divisor <= value:
        if value % divisor == 0:
            output.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        output.append(value)
    return output


def frobenius_power(iterations, polynomial):
    value = [0, 1]
    for _ in range(iterations):
        value = power_mod(value, P, polynomial)
    return value


def irreducible(polynomial):
    degree = len(polynomial)-1
    for divisor in prime_divisors(degree):
        value = frobenius_power(degree//divisor, polynomial)
        if gcd(polynomial, subtract_x(value)) != [1]:
            return False
    final = frobenius_power(degree, polynomial)
    return remainder(subtract_x(final), polynomial) == []


def main():
    if not all(irreducible(factor) for factor in FACTORS):
        raise RuntimeError("Rabin factor audit")
    print(
        "RATE_HALF_KB_ONE_LOOP_433_CELL11_FACTOR_AUDIT_PASS "
        f"field={P} quadratics=4 quartics=4"
    )


if __name__ == "__main__":
    main()
