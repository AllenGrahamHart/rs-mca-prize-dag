#!/usr/bin/env python3
"""Independent Fraction replay of the rigid S6 [5,6,2] pair quotient."""

from __future__ import annotations

from fractions import Fraction


Poly = tuple[Fraction, ...]
Rat = tuple[Poly, Poly]
ZERO: Poly = (Fraction(0),)
ONE: Poly = (Fraction(1),)


def poly(*coefficients: int | Fraction) -> Poly:
    result = tuple(Fraction(value) for value in coefficients)
    while len(result) > 1 and result[-1] == 0:
        result = result[:-1]
    return result


def padd(left: Poly, right: Poly) -> Poly:
    length = max(len(left), len(right))
    return poly(
        *(
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
            for index in range(length)
        )
    )


def pneg(value: Poly) -> Poly:
    return poly(*(-coefficient for coefficient in value))


def psub(left: Poly, right: Poly) -> Poly:
    return padd(left, pneg(right))


def pmul(left: Poly, right: Poly) -> Poly:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return poly(*result)


def pscale(value: Poly, scalar: int | Fraction) -> Poly:
    return poly(*(Fraction(scalar) * coefficient for coefficient in value))


def ppow(value: Poly, exponent: int) -> Poly:
    result = ONE
    base = value
    power = exponent
    while power:
        if power & 1:
            result = pmul(result, base)
        base = pmul(base, base)
        power //= 2
    return result


def pderivative(value: Poly) -> Poly:
    return poly(*(index * value[index] for index in range(1, len(value))))


def pdivmod(numerator: Poly, denominator: Poly) -> tuple[Poly, Poly]:
    if denominator == ZERO:
        raise ZeroDivisionError
    quotient = [Fraction(0)] * max(1, len(numerator) - len(denominator) + 1)
    remainder = numerator
    while remainder != ZERO and len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        coefficient = remainder[-1] / denominator[-1]
        quotient[shift] += coefficient
        term = poly(*([0] * shift + [coefficient]))
        remainder = psub(remainder, pmul(term, denominator))
    return poly(*quotient), remainder


def pgcd(left: Poly, right: Poly) -> Poly:
    a, b = left, right
    while b != ZERO:
        _, remainder = pdivmod(a, b)
        a, b = b, remainder
    if a == ZERO:
        return ZERO
    return pscale(a, 1 / a[-1])


def normalize(value: Rat) -> Rat:
    numerator, denominator = value
    if denominator == ZERO:
        raise ZeroDivisionError
    common = pgcd(numerator, denominator)
    if common != ONE:
        numerator, remainder_n = pdivmod(numerator, common)
        denominator, remainder_d = pdivmod(denominator, common)
        assert remainder_n == remainder_d == ZERO
    if denominator[-1] < 0:
        numerator, denominator = pneg(numerator), pneg(denominator)
    return numerator, denominator


def rpoly(value: Poly) -> Rat:
    return value, ONE


def radd(left: Rat, right: Rat) -> Rat:
    return normalize(
        (padd(pmul(left[0], right[1]), pmul(right[0], left[1])), pmul(left[1], right[1]))
    )


def rneg(value: Rat) -> Rat:
    return pneg(value[0]), value[1]


def rmul(left: Rat, right: Rat) -> Rat:
    return normalize((pmul(left[0], right[0]), pmul(left[1], right[1])))


def rdiv(left: Rat, right: Rat) -> Rat:
    return normalize((pmul(left[0], right[1]), pmul(left[1], right[0])))


def rscale(value: Rat, scalar: int | Fraction) -> Rat:
    return normalize((pscale(value[0], scalar), value[1]))


def rpow(value: Rat, exponent: int) -> Rat:
    result = rpoly(ONE)
    for _ in range(exponent):
        result = rmul(result, value)
    return result


def requal(left: Rat, right: Rat) -> bool:
    return pmul(left[0], right[1]) == pmul(right[0], left[1])


def main() -> None:
    a2 = poly(15129, -50922, 25444)
    y_cubic = poly(-414973341, 608911992, -276920478, 36517864)
    e5 = poly(
        2391178738527,
        -4974655751100,
        3171741595920,
        -97900305120,
        -559791696960,
        144800664832,
    )
    y_numerator = pmul(a2, y_cubic)
    y = normalize((y_numerator, pscale(e5, 3)))
    linear_zero = poly(-287, 188)
    z_numerator = pscale(pmul(linear_zero, ppow(a2, 2)), -41)
    z = normalize((z_numerator, pscale(e5, 4)))

    curve_terms = (
        (-2780548824, 5, 0),
        (1627638336, 4, 1),
        (4750104241, 4, 0),
        (1389447360, 3, 2),
        (8341646472, 3, 1),
        (-819790080, 2, 3),
        (-7256554248, 2, 2),
        (-14250312723, 2, 1),
        (-137681280, 1, 4),
        (-1378420000, 1, 3),
        (-2780548824, 1, 2),
        (82396160, 0, 5),
        (1054995600, 0, 4),
        (4001277576, 0, 3),
        (4750104241, 0, 2),
    )
    curve_numerator = ZERO
    for coefficient, y_degree, z_degree in curve_terms:
        total_degree = y_degree + z_degree
        cleared_scalar = Fraction(12**5, 3**y_degree * 4**z_degree)
        term = pmul(
            pmul(ppow(y_numerator, y_degree), ppow(z_numerator, z_degree)),
            ppow(e5, 5 - total_degree),
        )
        curve_numerator = padd(
            curve_numerator, pscale(term, coefficient * cleared_scalar)
        )
    assert curve_numerator == ZERO

    def mscale(expression, scalar):
        return {
            monomial: coefficient * scalar
            for monomial, coefficient in expression.items()
            if coefficient * scalar
        }

    def madd(left, right):
        result = dict(left)
        for monomial, coefficient in right.items():
            result[monomial] = result.get(monomial, Fraction(0)) + coefficient
            if result[monomial] == 0:
                del result[monomial]
        return result

    def shift(expression, dy, dz):
        return {(a + dy, b + dz): coefficient for (a, b), coefficient in expression.items()}

    powers = [({(0, 0): Fraction(1)}, {})]
    for _ in range(6):
        constant, coefficient = powers[-1]
        powers.append((mscale(shift(coefficient, 0, 1), -1), madd(constant, shift(coefficient, 1, 0))))
    n_coefficients = (
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        -Fraction(59778, 17689),
        Fraction(34992, 17689),
    )
    d_coefficients = (
        Fraction(4750104241, 18113536),
        -Fraction(347568603, 2264192),
        -Fraction(42386415, 323456),
        Fraction(43764835, 566048),
        Fraction(14700345, 1132096),
        -Fraction(5043, 532),
        Fraction(1),
    )
    remainder_n = [{}, {}]
    remainder_d = [{}, {}]
    for degree in range(7):
        for part in range(2):
            remainder_n[part] = madd(
                remainder_n[part], mscale(powers[degree][part], n_coefficients[degree])
            )
            remainder_d[part] = madd(
                remainder_d[part], mscale(powers[degree][part], d_coefficients[degree])
            )

    def clear_denominator(expression, degree=6):
        result = ZERO
        for (y_degree, z_degree), coefficient in expression.items():
            scalar = coefficient * Fraction(
                12**degree, 3**y_degree * 4**z_degree
            )
            term = pmul(
                pmul(ppow(y_numerator, y_degree), ppow(z_numerator, z_degree)),
                ppow(e5, degree - y_degree - z_degree),
            )
            result = padd(result, pscale(term, scalar))
        return result

    cubic = poly(33495606, -8441982, -31403007, 14658356)
    sextic = poly(
        -119893424310248247,
        379227334439635443,
        -474965645409866205,
        290661295480797960,
        -83250949083482880,
        6554290056691968,
        915512069923328,
    )
    quotient_n = pscale(pmul(ppow(linear_zero, 5), ppow(a2, 5)), 177147)
    quotient_d = pmul(cubic, ppow(sextic, 2))
    for part in range(2):
        cleared_n = clear_denominator(remainder_n[part])
        cleared_d = clear_denominator(remainder_d[part])
        assert pmul(cleared_n, quotient_d) == pmul(cleared_d, quotient_n)

    difference = pscale(
        pmul(
            pmul(ppow(poly(123, 88), 2), ppow(poly(-123, 89), 3)),
            pmul(
                ppow(poly(-369, 208), 6),
                pmul(ppow(poly(-1107, 683), 3), poly(-1599, 980)),
            ),
        ),
        3125,
    )
    assert psub(quotient_n, quotient_d) == difference
    assert len(pgcd(cubic, pderivative(cubic))) == 1
    assert len(pgcd(sextic, pderivative(sextic))) == 1
    assert len(pgcd(cubic, sextic)) == 1
    assert len(pgcd(linear_zero, a2)) == 1
    assert len(pgcd(a2, pderivative(a2))) == 1

    profiles = (
        (5, 5, 5),
        (6, 3, 3, 2, 1),
        (2, 2, 2, 2, 2, 2, 1, 1, 1),
    )
    assert all(sum(profile) == 15 for profile in profiles)
    assert sum(value - 1 for profile in profiles for value in profile) == 28
    assert 50922**2 - 4 * 25444 * 15129 == 14514**2 * 5
    p = 2130706433
    assert all(p % prime for prime in (2, 3, 5, 41, 59))
    assert sum(p**index for index in range(6)) % 2 == 0
    print("RATE_HALF_KB_M4_S6_562_PAIR_QUOTIENT_NORMAL_FORM_AUDIT_PASS")


if __name__ == "__main__":
    main()
