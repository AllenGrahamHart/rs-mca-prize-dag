#!/usr/bin/env python3
"""Independent quadratic-field replay of the rigid A6 pair quotient."""

from __future__ import annotations

from fractions import Fraction


K = tuple[Fraction, Fraction]
Poly = tuple[K, ...]
KZERO: K = (Fraction(0), Fraction(0))
KONE: K = (Fraction(1), Fraction(0))


def k(constant: int | Fraction, nu: int | Fraction = 0) -> K:
    return Fraction(constant), Fraction(nu)


def kadd(left: K, right: K) -> K:
    return left[0] + right[0], left[1] + right[1]


def kneg(value: K) -> K:
    return -value[0], -value[1]


def kmul(left: K, right: K) -> K:
    a, b = left
    c, d = right
    return a * c - 4 * b * d, a * d + b * c + b * d


def kinv(value: K) -> K:
    a, b = value
    norm = a * a + a * b + 4 * b * b
    if norm == 0:
        raise ZeroDivisionError
    return (a + b) / norm, -b / norm


def kdiv(left: K, right: K) -> K:
    return kmul(left, kinv(right))


def poly(*coefficients: K) -> Poly:
    result = tuple(coefficients)
    while len(result) > 1 and result[-1] == KZERO:
        result = result[:-1]
    return result


PZERO: Poly = poly(KZERO)
PONE: Poly = poly(KONE)


def padd(left: Poly, right: Poly) -> Poly:
    return poly(
        *(
            kadd(
                left[index] if index < len(left) else KZERO,
                right[index] if index < len(right) else KZERO,
            )
            for index in range(max(len(left), len(right)))
        )
    )


def pneg(value: Poly) -> Poly:
    return poly(*(kneg(coefficient) for coefficient in value))


def psub(left: Poly, right: Poly) -> Poly:
    return padd(left, pneg(right))


def pmul(left: Poly, right: Poly) -> Poly:
    result = [KZERO] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = kadd(result[i + j], kmul(a, b))
    return poly(*result)


def pscale(value: Poly, scalar: K) -> Poly:
    return poly(*(kmul(coefficient, scalar) for coefficient in value))


def ppow(value: Poly, exponent: int) -> Poly:
    result = PONE
    base = value
    power = exponent
    while power:
        if power & 1:
            result = pmul(result, base)
        base = pmul(base, base)
        power //= 2
    return result


def pderivative(value: Poly) -> Poly:
    return poly(*(kmul(value[index], k(index)) for index in range(1, len(value))))


def pdivmod(numerator: Poly, denominator: Poly) -> tuple[Poly, Poly]:
    if denominator == PZERO:
        raise ZeroDivisionError
    quotient = [KZERO] * max(1, len(numerator) - len(denominator) + 1)
    remainder = numerator
    while remainder != PZERO and len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        coefficient = kdiv(remainder[-1], denominator[-1])
        quotient[shift] = kadd(quotient[shift], coefficient)
        term = poly(*([KZERO] * shift + [coefficient]))
        remainder = psub(remainder, pmul(term, denominator))
    return poly(*quotient), remainder


def pmonic(value: Poly) -> Poly:
    if value == PZERO:
        return PZERO
    return pscale(value, kinv(value[-1]))


def pgcd(left: Poly, right: Poly) -> Poly:
    a, b = left, right
    while b != PZERO:
        _, remainder = pdivmod(a, b)
        a, b = b, remainder
    return pmonic(a)


def main() -> None:
    linear_zero = poly(k(-7525603, 3231308), k(26828299))
    quadratic_zero = poly(
        k(245313368811, 2125523128760),
        k(-824138157082, 7855063570280),
        k(63975032888671),
    )
    pole_linear = poly(k(-315829, -714826), k(9994287))
    pole_simple_quadratic = poly(
        k(132674139060063, 26804277479260),
        k(-417059633688806, -83725261001260),
        k(1991382275400503),
    )
    pole_double_quadratic = poly(
        k(12231162711693, -32963869775350),
        k(-462396480179036, 244927114639150),
        k(1132252914780903),
    )
    pole_double_quartic = poly(
        k(-1822586629728176676821274861, 1518418512706836664928299688),
        k(29110362047987136464064202740, 305715256120089609322000856),
        k(-11490078199717284397847774254, -48409713450897291507014287016),
        k(-126036323962081416795984038348, 58730298647562103476728792872),
        k(89003185037860639199185563123),
    )
    one_simple = poly(k(-15954935, 15312886), k(80312277))
    one_double = poly(k(-7890011, 5302214), k(33120709))
    one_four_linear = poly(k(-133093, 97604), k(875841))
    one_four_quadratic = poly(
        k(41237398279331, -13362808229176),
        k(-142615106443814, 55888632283576),
        k(360429781037043),
    )

    scalar_denominator = (
        38291961532478173866738244146012452994162275508013680941480795766620042899277
    )
    scalar = k(
        -Fraction(
            303676164503275686857828761462277732742134748079423674177208826215100553982356192,
            scalar_denominator,
        ),
        -Fraction(
            74513842597659582802909998886996270271709813890474407398463247982555397872842400,
            scalar_denominator,
        ),
    )
    numerator = pscale(pmul(ppow(linear_zero, 5), ppow(quadratic_zero, 5)), scalar)
    denominator = pmul(
        pmul(pole_linear, pole_simple_quadratic),
        pmul(ppow(pole_double_quadratic, 2), ppow(pole_double_quartic, 2)),
    )
    difference = psub(numerator, denominator)
    expected_difference = pmul(
        pmul(one_simple, ppow(one_double, 2)),
        pmul(ppow(one_four_linear, 4), ppow(one_four_quadratic, 4)),
    )
    assert pmonic(difference) == pmonic(expected_difference)
    assert len(numerator) - 1 == len(denominator) - 1 == len(difference) - 1 == 15

    fibers = (
        ((linear_zero, 5), (quadratic_zero, 5)),
        (
            (one_simple, 1),
            (one_double, 2),
            (one_four_linear, 4),
            (one_four_quadratic, 4),
        ),
        (
            (pole_linear, 1),
            (pole_simple_quadratic, 1),
            (pole_double_quadratic, 2),
            (pole_double_quartic, 2),
        ),
    )
    expected_profiles = (
        [5, 5, 5],
        [4, 4, 4, 2, 1],
        [2, 2, 2, 2, 2, 2, 1, 1, 1],
    )
    for fiber, expected_profile in zip(fibers, expected_profiles):
        profile = sorted(
            (exponent for factor, exponent in fiber for _ in range(len(factor) - 1)),
            reverse=True,
        )
        assert profile == expected_profile
        factors = [factor for factor, _ in fiber]
        for index, factor in enumerate(factors):
            assert pgcd(factor, pderivative(factor)) == PONE
            for other in factors[index + 1 :]:
                assert pgcd(factor, other) == PONE
    assert pgcd(numerator, denominator) == PONE
    branch_index = sum(
        sum(value - 1 for value in profile) for profile in expected_profiles
    )
    assert branch_index == 28 == 2 * 15 - 2

    p = 2130706433
    nu_residues = [463918232, 1666788202]
    assert all((value * value - value + 4) % p == 0 for value in nu_residues)

    def mod_field(value: K, nu_residue: int) -> int:
        return (
            int(value[0].numerator) * pow(int(value[0].denominator), -1, p)
            + int(value[1].numerator)
            * pow(int(value[1].denominator), -1, p)
            * nu_residue
        ) % p

    discriminants = []
    separations = []
    for nu_residue in nu_residues:
        a, b, c = (mod_field(value, nu_residue) for value in quadratic_zero[::-1])
        inverse_a = pow(a, -1, p)
        b = b * inverse_a % p
        c = c * inverse_a % p
        discriminants.append((b * b - 4 * c) % p)
        l0, l1 = (mod_field(value, nu_residue) for value in linear_zero)
        root = -l0 * pow(l1, -1, p) % p
        separations.append((root * root + b * root + c) % p)
        assert mod_field(scalar, nu_residue)
    assert discriminants == [149224915, 1898905147]
    assert separations == [1501399179, 1964168949]
    assert 6 % 2 == 0
    print("RATE_HALF_KB_M4_A6_542_PAIR_QUOTIENT_AUDIT_PASS")


if __name__ == "__main__":
    main()
