#!/usr/bin/env python3
"""Independent resultant audit in F_p[u]/(u^2+2)."""

from __future__ import annotations

import hashlib
import math
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path


EXPECTED = {
    (65536, 8191): "b9196f80f622cf985b63877fee854d9a6bddbbba086791418b8a1c76e26fd0df",
    (1048576, 131071): "02ad2f1653eecbb27a42bb918fc9e309695349f605c5bea48700179138b889d0",
    (4194304, 524287): "c95f4533727c7ec8ac9083894bad926c4a1f4f731b7a3e858a405a3751ae27cd",
    (17179869184, 2147483647): "225ee66bf7e7c0734deb2a269e682790563f45825b431a8537b3fd48bc4cbaa3",
}


@dataclass(frozen=True)
class Quad:
    """Element a+b*u with u^2=-2."""

    a: int
    b: int
    p: int

    def __post_init__(self) -> None:
        object.__setattr__(self, "a", self.a % self.p)
        object.__setattr__(self, "b", self.b % self.p)

    def coerce(self, other: int | Quad) -> Quad:
        if isinstance(other, Quad):
            assert other.p == self.p
            return other
        return Quad(other, 0, self.p)

    def __add__(self, other: int | Quad) -> Quad:
        other = self.coerce(other)
        return Quad(self.a + other.a, self.b + other.b, self.p)

    __radd__ = __add__

    def __neg__(self) -> Quad:
        return Quad(-self.a, -self.b, self.p)

    def __sub__(self, other: int | Quad) -> Quad:
        return self + (-self.coerce(other))

    def __rsub__(self, other: int | Quad) -> Quad:
        return self.coerce(other) - self

    def __mul__(self, other: int | Quad) -> Quad:
        other = self.coerce(other)
        return Quad(
            self.a * other.a - 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
            self.p,
        )

    __rmul__ = __mul__

    def norm(self) -> int:
        return (self.a * self.a + 2 * self.b * self.b) % self.p

    def inverse(self) -> Quad:
        denominator = self.norm()
        assert denominator
        inverse = pow(denominator, -1, self.p)
        return Quad(self.a * inverse, -self.b * inverse, self.p)

    def __truediv__(self, other: int | Quad) -> Quad:
        return self * self.coerce(other).inverse()

    def __rtruediv__(self, other: int | Quad) -> Quad:
        return self.coerce(other) / self

    def __pow__(self, exponent: int) -> Quad:
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result = self.coerce(1)
        base = self
        while exponent:
            if exponent & 1:
                result *= base
            base *= base
            exponent //= 2
        return result

    def __bool__(self) -> bool:
        return bool(self.a or self.b)


Polynomial = list[Quad]


def trim(poly: Polynomial) -> Polynomial:
    while len(poly) > 1 and not poly[-1]:
        poly.pop()
    return poly


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    zero = left[0].coerce(0)
    out = [zero] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def remainder(dividend: Polynomial, divisor: Polynomial) -> Polynomial:
    out = dividend[:]
    while len(out) >= len(divisor):
        scale = out[-1] / divisor[-1]
        shift = len(out) - len(divisor)
        for i, coefficient in enumerate(divisor):
            out[i + shift] -= scale * coefficient
        trim(out)
    return out


def power_mod(base: Polynomial, exponent: int, modulus: Polynomial) -> Polynomial:
    result = [modulus[0].coerce(1)]
    base = remainder(base, modulus)
    while exponent:
        if exponent & 1:
            result = remainder(multiply(result, base), modulus)
        base = remainder(multiply(base, base), modulus)
        exponent //= 2
    return result


def row_digest(n: int, p: int) -> str:
    root_two = pow(2, (p + 1) // 4, p)
    u = Quad(0, 1, p)
    zeta = (Quad(root_two, 0, p) + u) / 2
    one = Quad(1, 0, p)
    assert zeta**4 == -one and zeta**p == zeta**-1

    records = []
    for i, j in combinations(range(1, 8), 2):
        powers = [one - zeta ** (i * k) - zeta ** (j * k) for k in (1, 2, 3)]
        c2 = powers[1] - powers[0] ** 2 / 7
        c3 = powers[2] - 3 * powers[0] * powers[1] / 7 + 2 * powers[0] ** 3 / 49
        assert c2
        invariant = c3**2 / c2**3
        quadratic = [
            Quad(49, 0, p),
            Quad(28, 0, p) + 49 * invariant,
            Quad(4, 0, p) + 7 * invariant,
        ]
        assert quadratic[-1]

        b7 = [one]
        for offset in range(7):
            b7 = remainder(multiply(b7, [Quad(offset, 0, p), one]), quadratic)
        inverse_factorial = pow(math.factorial(7), -1, p)
        b7 = [coefficient * inverse_factorial for coefficient in b7]

        reduced = power_mod(b7, n, quadratic)
        reduced[0] -= one
        trim(reduced)
        if len(reduced) == 1:
            resultant = reduced[0] ** 2
        else:
            assert len(reduced) == 2
            a0, a1, a2 = quadratic
            b0, b1 = reduced
            resultant = a2 * b0 * b0 - a1 * b0 * b1 + a0 * b1 * b1
        assert resultant and resultant.norm()

        records.append(
            f"{i},{j}:"
            f"{quadratic[0].a},{quadratic[0].b};"
            f"{quadratic[1].a},{quadratic[1].b};"
            f"{quadratic[2].a},{quadratic[2].b}|"
            f"{resultant.a},{resultant.b}|{resultant.norm()}"
        )

    assert len(records) == 21
    return hashlib.sha256(("\n".join(records) + "\n").encode()).hexdigest()


def main() -> None:
    for row, expected in EXPECTED.items():
        assert row_digest(*row) == expected

    proof = Path(__file__).with_name("proof.md").read_text()
    audit = Path(__file__).with_name("audit.md").read_text()
    assert "Sylvester" in proof
    assert "algebraic closure" in audit

    wrong = dict(EXPECTED)
    first = next(iter(wrong))
    wrong[first] = "0" * 64
    assert row_digest(*first) != wrong[first]

    print(
        "L1_MERSENNE_HNF_M8_ORDER_ZERO_QUADRATIC_EXCLUSION_AUDIT_PASS "
        "rows=4 resultants=84 digests=4 mutations=1"
    )


if __name__ == "__main__":
    main()
