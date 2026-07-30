#!/usr/bin/env python3
"""Verify the KoalaBear degree-six common-pole exclusion."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


NODE = Path(__file__).resolve().parent
P = 2_130_706_433
T2 = Fraction(-27, 5)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


@dataclass(frozen=True)
class Quad:
    """An element a+b*t of Q[t]/(t^2+27/5)."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __add__(self, other: Quad) -> Quad:
        return Quad(self.a + other.a, self.b + other.b)

    def __neg__(self) -> Quad:
        return Quad(-self.a, -self.b)

    def __sub__(self, other: Quad) -> Quad:
        return self + (-other)

    def __mul__(self, other: Quad) -> Quad:
        return Quad(self.a * other.a + self.b * other.b * T2, self.a * other.b + self.b * other.a)

    def inverse(self) -> Quad:
        norm = self.a * self.a - T2 * self.b * self.b
        require(norm != 0, "quadratic inverse")
        return Quad(self.a / norm, -self.b / norm)

    def __truediv__(self, other: Quad) -> Quad:
        return self * other.inverse()


ZERO = Quad()
ONE = Quad(Fraction(1))


def determinant(matrix: list[list[Quad]]) -> Quad:
    rows = [row[:] for row in matrix]
    det = ONE
    for column in range(len(rows)):
        pivot = next((row for row in range(column, len(rows)) if rows[row][column] != ZERO), None)
        require(pivot is not None, "singular Sylvester matrix")
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            det = -det
        value = rows[column][column]
        det = det * value
        for row in range(column + 1, len(rows)):
            factor = rows[row][column] / value
            for entry in range(column + 1, len(rows)):
                rows[row][entry] = rows[row][entry] - factor * rows[column][entry]
    return det


def resultant(first: list[Quad], second: list[Quad]) -> Quad:
    """Sylvester resultant for low-to-high coefficient lists."""
    m = len(first) - 1
    n = len(second) - 1
    first_high = list(reversed(first))
    second_high = list(reversed(second))
    matrix = [[ZERO for _ in range(m + n)] for _ in range(m + n)]
    for row in range(n):
        matrix[row][row : row + m + 1] = first_high
    for row in range(m):
        matrix[n + row][row : row + n + 1] = second_high
    return determinant(matrix)


def rational_poly_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    result = [Fraction(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index] += value
    return result


def rational_poly_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def rational_poly_pow(base: list[Fraction], exponent: int) -> list[Fraction]:
    result = [Fraction(1)]
    for _ in range(exponent):
        result = rational_poly_mul(result, base)
    return result


def scaled_poly(poly: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return [scalar * value for value in poly]


def quad_poly_add(left: list[Quad], right: list[Quad]) -> list[Quad]:
    result = [ZERO] * max(len(left), len(right))
    for index, value in enumerate(left):
        result[index] = result[index] + value
    for index, value in enumerate(right):
        result[index] = result[index] + value
    return result


def quad_poly_mul(left: list[Quad], right: list[Quad]) -> list[Quad]:
    result = [ZERO] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = result[i + j] + a * b
    return result


def quad_poly_pow(base: list[Quad], exponent: int) -> list[Quad]:
    result = [ONE]
    for _ in range(exponent):
        result = quad_poly_mul(result, base)
    return result


def scaled_quad_poly(poly: list[Quad], scalar: Quad) -> list[Quad]:
    return [scalar * value for value in poly]


def d2_pullback() -> None:
    plus = [Fraction(1), Fraction(1)]
    minus = [Fraction(-1), Fraction(1)]
    terms = [
        scaled_poly(rational_poly_pow(plus, 6), Fraction(-27, 8)),
        scaled_poly(rational_poly_mul(rational_poly_pow(plus, 4), rational_poly_pow(minus, 2)), Fraction(-27, 2)),
        scaled_poly(rational_poly_mul(rational_poly_pow(plus, 2), rational_poly_pow(minus, 4)), Fraction(-27, 2)),
        scaled_poly(rational_poly_pow(minus, 6), Fraction(-27, 8)),
    ]
    total = [Fraction(0)]
    for term in terms:
        total = rational_poly_add(total, term)
    expected = scaled_poly([Fraction(5), 0, 11, 0, 11, 0, 5], Fraction(-27, 4))
    require(total == expected, "commuting pullback")
    require(11 * 11 != 4 * 5 * 11, "scaling invariant")
    require(11 * 11 != 4 * 11 * 5, "inversion invariant")


def order_three_automorphism() -> None:
    t = Quad(Fraction(0), Fraction(1))
    x_numerator = [Quad(T2), t]
    denominator = [t, Quad(Fraction(-3))]
    c = Quad(Fraction(756, 125))
    terms = [
        quad_poly_pow(x_numerator, 6),
        scaled_quad_poly(quad_poly_mul(quad_poly_pow(x_numerator, 4), quad_poly_pow(denominator, 2)), Quad(Fraction(-6))),
        scaled_quad_poly(quad_poly_mul(quad_poly_pow(x_numerator, 2), quad_poly_pow(denominator, 4)), Quad(Fraction(9))),
        scaled_quad_poly(quad_poly_pow(denominator, 6), -c),
    ]
    transformed = [ZERO]
    for term in terms:
        transformed = quad_poly_add(transformed, term)
    standard = [-c, ZERO, Quad(Fraction(9)), ZERO, Quad(Fraction(-6)), ZERO, ONE]
    scale = transformed[6]
    require(transformed == scaled_quad_poly(standard, scale), "order-three sextic automorphism")


def inversion_resultant() -> None:
    first = [Quad(Fraction(-9)), Quad(Fraction(-8)), ZERO, Quad(Fraction(8))]
    second = [Quad(Fraction(-12)), Quad(Fraction(-12)), Quad(Fraction(-3)), ZERO, Quad(Fraction(16))]
    value = resultant(first, second)
    require(value.b == 0 and abs(value.a) == 22_371_648, "reciprocal twist resultant")
    require(22_371_648 % P != 0, "reciprocal resultant mod p")


def order_three_resultant() -> None:
    e = [
        Quad(Fraction(-198), Fraction(-140)),
        Quad(Fraction(-60), Fraction(-70)),
        Quad(Fraction(-45), Fraction(50)),
        Quad(Fraction(150), Fraction(25)),
    ]
    h = [
        Quad(Fraction(-2268, 5), Fraction(1296)),
        Quad(Fraction(-2592), Fraction(2088)),
        Quad(Fraction(-459), Fraction(1260)),
        Quad(Fraction(3240), Fraction(-1530)),
        Quad(Fraction(-2295), Fraction(-900)),
    ]
    value = resultant(e, h)
    scale = Fraction(76_527_504_000)
    expected = Quad(scale * 1_585_334_079, scale * 1_472_792_180)
    require(value in (expected, -expected), "order-three resultant")
    norm = 5 * 1_585_334_079**2 + 27 * 1_472_792_180**2
    require(norm == 71_132_574_457_861_006_005, "primitive norm")
    require(norm % P == 1_274_367_339, "primitive norm mod p")


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    proof = (NODE / "proof.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("only `n=3` remains" in statement, "surviving profile")
    require("71132574457861006005" in proof, "norm pin")
    require("Not claimed" in contract, "scope boundary")

    # The order-three odd-coefficient equations leave s=3 or s=-27/5.
    roots = [Fraction(3), Fraction(-27, 5)]
    require(all((s - 3) * (5 * s + 27) == 0 for s in roots), "order-three roots")
    c_values = [-(s**3 + 2 * s**2 - 15 * s) / 3 for s in roots]
    require(c_values == [Fraction(0), Fraction(756, 125)], "order-three fibers")

    d2_pullback()
    order_three_automorphism()
    inversion_resultant()
    order_three_resultant()
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_DEGREE6_COMMON_POLE_EXCLUSION_PASS")


if __name__ == "__main__":
    main()
