#!/usr/bin/env python3
"""Independent finite-field irreducibility audit for cell-4 cubics."""


P = 2130706433
CUBICS = (
    (-1, 33423359, 33423357, 1),
    (1, -33423357, 33423359, 1),
    (1, 33423359, -33423357, 1),
    (-1, -33423357, -33423359, 1),
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
    if not left:
        return []
    inverse = pow(left[-1], -1, P)
    return [(value*inverse) % P for value in left]


def main():
    for cubic in CUBICS:
        frobenius = power_mod([0, 1], P, cubic)
        difference = list(frobenius)+[0]*(max(2, len(frobenius))-len(frobenius))
        difference[1] = (difference[1]-1) % P
        if gcd(cubic, difference) != [1]:
            raise RuntimeError(f"base-field cubic root {cubic}")
    print(
        "RATE_HALF_KB_ONE_LOOP_433_CELL4_CUBIC_AUDIT_PASS "
        f"field={P} cubics={len(CUBICS)} base_roots=0"
    )


if __name__ == "__main__":
    main()
