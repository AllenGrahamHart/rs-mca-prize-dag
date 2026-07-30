#!/usr/bin/env python3
"""Independent Fraction replay of the rigid S6 pair quotient."""

from __future__ import annotations

from fractions import Fraction


Poly = tuple[Fraction, ...]
Rat = tuple[Poly, Poly]
ZERO: Poly = (Fraction(0),)
ONE: Poly = (Fraction(1),)
U: Poly = (Fraction(0), Fraction(1))


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
        numerator, rem_n = pdivmod(numerator, common)
        denominator, rem_d = pdivmod(denominator, common)
        assert rem_n == rem_d == ZERO
    if denominator[-1] < 0:
        numerator = pneg(numerator)
        denominator = pneg(denominator)
    return numerator, denominator


def rpoly(value: Poly) -> Rat:
    return value, ONE


def radd(left: Rat, right: Rat) -> Rat:
    return normalize(
        (padd(pmul(left[0], right[1]), pmul(right[0], left[1])), pmul(left[1], right[1]))
    )


def rneg(value: Rat) -> Rat:
    return pneg(value[0]), value[1]


def rsub(left: Rat, right: Rat) -> Rat:
    return radd(left, rneg(right))


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


def linear(constant: int) -> Poly:
    return poly(constant, 1)


def main() -> None:
    e = poly(1257325157, 28623155, -425920, -9680, 55, 1)
    y = normalize(
        (
            pscale(pmul(pmul(linear(-55), linear(44)), ppow(linear(55), 2)), -192),
            e,
        )
    )
    z = normalize(
        (pscale(pmul(ppow(linear(44), 2), linear(55)), 12288), e)
    )
    m = normalize((pscale(linear(44), -64), pmul(linear(-55), linear(55))))
    assert requal(rdiv(z, y), m)

    curve = rpoly(ZERO)
    terms = (
        (-4194304, 5, 0),
        (7434240, 3, 2),
        (16777216, 3, 1),
        (6814720, 2, 3),
        (2635380, 1, 4),
        (-14868480, 1, 3),
        (-12582912, 1, 2),
        (483153, 0, 5),
        (-6814720, 0, 4),
    )
    for coefficient, y_degree, z_degree in terms:
        curve = radd(
            curve,
            rscale(rmul(rpow(y, y_degree), rpow(z, z_degree)), coefficient),
        )
    assert curve[0] == ZERO

    powers: list[tuple[Rat, Rat]] = [(rpoly(ONE), rpoly(ZERO))]
    for _ in range(6):
        constant, coefficient = powers[-1]
        powers.append((rneg(rmul(coefficient, z)), radd(constant, rmul(coefficient, y))))

    numerator_remainder = tuple(rscale(part, Fraction(625, 624)) for part in powers[6])
    d_coefficients = (
        Fraction(67108864, 345454395),
        Fraction(0),
        -Fraction(65536, 190333),
        -Fraction(16384, 51909),
        -Fraction(192, 1573),
        -Fraction(16, 715),
        Fraction(1),
    )
    denominator_remainder = [rpoly(ZERO), rpoly(ZERO)]
    for degree, coefficient in enumerate(d_coefficients):
        for part in range(2):
            denominator_remainder[part] = radd(
                denominator_remainder[part], rscale(powers[degree][part], coefficient)
            )

    quartic = poly(12576619, 660176, 14520, 176, 1)
    sextic = poly(
        -870224422859,
        -39333485730,
        -372423117,
        3380740,
        22143,
        -330,
        1,
    )
    quotient_n = pscale(pmul(ppow(linear(44), 6), ppow(linear(55), 3)), -9566429400000)
    quotient_d = pmul(pmul(linear(143), ppow(quartic, 2)), sextic)
    quotient = normalize((quotient_n, quotient_d))
    assert requal(rdiv(numerator_remainder[0], denominator_remainder[0]), quotient)
    assert requal(rdiv(numerator_remainder[1], denominator_remainder[1]), quotient)

    difference = pneg(pmul(ppow(linear(77), 5), ppow(poly(-4961, -44, 1), 5)))
    assert psub(quotient_n, quotient_d) == difference
    denominator_factors = (linear(143), quartic, sextic)
    for factor in denominator_factors:
        assert len(pgcd(factor, pderivative(factor))) == 1
    for left in range(3):
        for right in range(left + 1, 3):
            assert len(pgcd(denominator_factors[left], denominator_factors[right])) == 1

    zero_profile = (6, 6, 3)
    one_profile = (5, 5, 5)
    infinity_profile = (2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1)
    assert sum(zero_profile) == sum(one_profile) == sum(infinity_profile) == 15
    assert sum(value - 1 for value in zero_profile + one_profile + infinity_profile) == 28
    assert 44**2 + 4 * 4961 == 66**2 * 5
    p = 2130706433
    assert all(p % prime for prime in (2, 3, 5, 11))
    assert sum(p**index for index in range(6)) % 2 == 0
    print("RATE_HALF_KB_M4_S6_652_PAIR_QUOTIENT_NORMAL_FORM_AUDIT_PASS")


if __name__ == "__main__":
    main()
