#!/usr/bin/env python3
"""Independent finite-field norm-divisibility and tamper audit."""

Q = 101


def trim(poly):
    while len(poly) > 1 and poly[-1] % Q == 0:
        poly.pop()
    return [value % Q for value in poly]


def mul(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % Q
    return trim(out)


def divmod_poly(numerator, denominator):
    numerator = trim(numerator[:])
    denominator = trim(denominator[:])
    quotient = [0] * max(1, len(numerator) - len(denominator) + 1)
    inv_lead = pow(denominator[-1], -1, Q)
    while len(numerator) >= len(denominator) and numerator != [0]:
        shift = len(numerator) - len(denominator)
        scale = numerator[-1] * inv_lead % Q
        quotient[shift] = scale
        for i, value in enumerate(denominator):
            numerator[i + shift] = (numerator[i + shift] - scale * value) % Q
        numerator = trim(numerator)
    return trim(quotient), trim(numerator)


def evaluate(poly, point):
    value = 0
    for coefficient in reversed(poly):
        value = (value * point + coefficient) % Q
    return value


def derivative(poly):
    out = [(index * value) % Q for index, value in enumerate(poly)][1:]
    return out or [0]


def main():
    generator = pow(2, 10, Q)
    rows = []
    value = 1
    for _ in range(10):
        rows.append(value)
        value = value * generator % Q
    assert len(set(rows)) == 10 and value == 1

    # G(t,X)=t^2-X^2. Every row x in mu_10 has the two roots +/-x in mu_10.
    norm = [1]
    locator = [1]
    for delta in rows:
        norm = mul(norm, [delta * delta % Q, 0, -1])
        locator = mul(locator, [-delta, 1])
    locator_square = mul(locator, locator)
    quotient, remainder = divmod_poly(norm, locator_square)
    assert remainder == [0]
    assert len(quotient) == 1 and quotient[0] != 0

    locator_derivative = derivative(locator)
    for x in rows:
        incident = {x, (-x) % Q}
        tangent_product = 1
        for delta in rows:
            fiber = [delta * delta % Q, 0, -1]
            if delta in incident:
                tangent_product = (
                    tangent_product * evaluate(derivative(fiber), x)
                ) % Q
            else:
                tangent_product = tangent_product * evaluate(fiber, x) % Q
        denominator = pow(evaluate(locator_derivative, x), 2, Q)
        reconstructed = tangent_product * pow(denominator, -1, Q) % Q
        assert reconstructed == quotient[0]

    tampered = [1]
    for index, delta in enumerate(rows):
        constant = (delta * delta + (1 if index == 0 else 0)) % Q
        tampered = mul(tampered, [constant, 0, -1])
    _, bad_remainder = divmod_poly(tampered, locator_square)
    assert bad_remainder != [0]
    print("PASS paired split-biform off-line norm audit tamper=1/1")


if __name__ == "__main__":
    main()
