#!/usr/bin/env python3
"""Exhaust the first two toy pure harmonic/Fermat support gates."""

from itertools import combinations


EXPECTED = {
    (8, 17): (70, 56, 2, 0),
    (8, 97): (70, 4, 2, 0),
    (8, 113): (70, 0, 2, 0),
    (8, 193): (70, 0, 2, 0),
    (16, 97): (1820, 312, 0, 0),
    (16, 193): (1820, 144, 0, 0),
    (16, 257): (1820, 128, 0, 0),
}


def convolution(left, right, p):
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % p
    return out


def fourth_power(poly, p):
    square = convolution(poly, poly, p)
    return convolution(square, square, p)


def multiply_linear(poly, root, p):
    out = [0] * (len(poly) + 1)
    for i, coefficient in enumerate(poly):
        out[i] = (out[i] + coefficient) % p
        out[i + 1] = (out[i + 1] - root * coefficient) % p
    return out


def divide_exact(numerator, denominator, p):
    work = numerator[:]
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    inverse_lead = pow(denominator[-1], -1, p)
    for shift in range(len(quotient) - 1, -1, -1):
        coefficient = work[shift + len(denominator) - 1] * inverse_lead % p
        quotient[shift] = coefficient
        for j, value in enumerate(denominator):
            work[shift + j] = (work[shift + j] - coefficient * value) % p
    assert not any(work[: len(denominator) - 1])
    return quotient


def prime_factors(value):
    factors = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return factors


def primitive_root(p):
    factors = prime_factors(p - 1)
    return next(
        candidate
        for candidate in range(2, p)
        if all(pow(candidate, (p - 1) // factor, p) != 1 for factor in factors)
    )


def pairing_norm(x, y, z, t, p):
    pair_sum = (x + y) % p
    pair_product = x * y % p
    other_sum = (z + t) % p
    other_product = z * t % p
    a = (4 * pair_product + 4 * other_product - pair_sum * other_sum) % p
    c0 = (
        a * a
        + 4 * other_sum * other_sum * pair_product
        - 4 * other_product * pair_sum * pair_sum
        - 16 * other_product * pair_product
    ) % p
    c1 = (-4 * a * other_sum + 16 * other_product * pair_sum) % p
    return (c0 * c0 - pair_product * c1 * c1) % p


def is_harmonic(roots, p):
    a, b, c, d = roots
    return any(
        pairing_norm(*ordered, p) == 0
        for ordered in ((a, b, c, d), (a, c, b, d), (a, d, b, c))
    )


def degree_one_fermat(quotient, p):
    coefficient = quotient[1] * pow(4, -1, p) % p
    remainder = (quotient[4] - pow(coefficient, 4, p)) % p
    fourth_powers = {pow(value, 4, p) for value in range(1, p)}
    return (
        quotient[2] == 6 * coefficient * coefficient % p
        and quotient[3] == 4 * pow(coefficient, 3, p) % p
        and remainder in fourth_powers
    )


def degree_three_fermat(quotient, p):
    inverse_four = pow(4, -1, p)
    b1 = quotient[1] * inverse_four % p
    b2 = (quotient[2] - 6 * b1 * b1) * inverse_four % p
    b3 = (quotient[3] - 12 * b1 * b2 - 4 * pow(b1, 3, p)) * inverse_four % p
    b_fourth = fourth_power([1, b1, b2, b3], p)
    remainder = [(quotient[i] - b_fourth[i]) % p for i in range(13)]
    if any(remainder[:4]):
        return False

    for c0 in range(1, p):
        if pow(c0, 4, p) != remainder[4]:
            continue
        inverse_linear = pow(4 * pow(c0, 3, p) % p, -1, p)
        c1 = remainder[5] * inverse_linear % p
        c2 = (remainder[6] - 6 * c0 * c0 * c1 * c1) * inverse_linear % p
        if [0] * 4 + fourth_power([c0, c1, c2], p) == remainder:
            return True
    return False


def scan(d, p):
    assert (p - 1) % (2 * d) == 0 and p > d
    generator = primitive_root(p)
    root = pow(generator, (p - 1) // d, p)
    subgroup = [pow(root, exponent, p) for exponent in range(d)]
    numerator = [1] + [0] * (d - 1) + [-1 % p]
    harmonic = fermat = combined = 0

    for roots in combinations(subgroup, 4):
        deletion = [1]
        for value in roots:
            deletion = multiply_linear(deletion, value, p)
        quotient = divide_exact(numerator, deletion, p)
        harmonic_hit = is_harmonic(roots, p)
        fermat_hit = (
            degree_one_fermat(quotient, p)
            if d == 8
            else degree_three_fermat(quotient, p)
        )
        harmonic += harmonic_hit
        fermat += fermat_hit
        combined += harmonic_hit and fermat_hit

    return len(list(combinations(range(d), 4))), harmonic, fermat, combined


def main():
    print("d p supports harmonic fermat combined")
    for key, expected in EXPECTED.items():
        actual = scan(*key)
        assert actual == expected, (key, actual, expected)
        print(*key, *actual)
    print("PASS pure harmonic/Fermat combined toy gate")


if __name__ == "__main__":
    main()
