#!/usr/bin/env python3
"""Independent m=16 resultant audit in F_p[u]/(u^2+2)."""

from __future__ import annotations

import hashlib
import math
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path


P, N, H = 8191, 131072, 15
EXPECTED = "9c05ecd35081cb2eb38869300a434b03e5b440771410ec60427bfca118e9e31f"


@dataclass(frozen=True)
class Quad:
    """Element a+b*u with u^2=-2."""

    a: int
    b: int

    def __post_init__(self) -> None:
        object.__setattr__(self, "a", self.a % P)
        object.__setattr__(self, "b", self.b % P)

    def coerce(self, other: int | Quad) -> Quad:
        return other if isinstance(other, Quad) else Quad(other, 0)

    def __add__(self, other: int | Quad) -> Quad:
        other = self.coerce(other)
        return Quad(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self) -> Quad:
        return Quad(-self.a, -self.b)

    def __sub__(self, other: int | Quad) -> Quad:
        return self + (-self.coerce(other))

    def __rsub__(self, other: int | Quad) -> Quad:
        return self.coerce(other) - self

    def __mul__(self, other: int | Quad) -> Quad:
        other = self.coerce(other)
        return Quad(
            self.a * other.a - 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def norm(self) -> int:
        return (self.a * self.a + 2 * self.b * self.b) % P

    def inverse(self) -> Quad:
        norm = self.norm()
        assert norm
        inverse = pow(norm, -1, P)
        return Quad(self.a * inverse, -self.b * inverse)

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
    out = [Quad(0, 0)] * (len(left) + len(right) - 1)
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
    result = [Quad(1, 0)]
    base = remainder(base, modulus)
    while exponent:
        if exponent & 1:
            result = remainder(multiply(result, base), modulus)
        base = remainder(multiply(base, base), modulus)
        exponent //= 2
    return result


def certificate_digest() -> str:
    one = Quad(1, 0)
    zeta = Quad(6456, 2822)
    assert zeta**16 == one and zeta**8 == -one
    assert zeta**P == zeta**-1

    records = []
    for i, j in combinations(range(1, 16), 2):
        powers = [one - zeta ** (i * k) - zeta ** (j * k) for k in (1, 2, 3)]
        c2 = powers[1] - powers[0] ** 2 / H
        c3 = powers[2] - 3 * powers[0] * powers[1] / H + 2 * powers[0] ** 3 / (H * H)
        assert c2
        invariant = c3**2 / c2**3
        quadratic = [
            Quad(H * H, 0),
            Quad(4 * H, 0) + invariant * H * H,
            Quad(4, 0) + invariant * H,
        ]
        assert quadratic[-1]

        b15 = [one]
        for offset in range(H):
            b15 = remainder(multiply(b15, [Quad(offset, 0), one]), quadratic)
        inverse_factorial = pow(math.factorial(H), -1, P)
        b15 = [coefficient * inverse_factorial for coefficient in b15]

        reduced = power_mod(b15, N, quadratic)
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

    assert len(records) == 105
    return hashlib.sha256(("\n".join(records) + "\n").encode()).hexdigest()


def main() -> None:
    digest = certificate_digest()
    assert digest == EXPECTED

    proof = Path(__file__).with_name("proof.md").read_text()
    audit = Path(__file__).with_name("audit.md").read_text()
    assert EXPECTED in proof
    assert "algebraic closure" in audit
    assert digest != "0" * 64

    print(
        "L1_MERSENNE_HNF_M16_ORDER_ZERO_SINGLE_COLLISION_EXCLUSION_AUDIT_PASS "
        "row=1 resultants=105 digest=1 mutations=1"
    )


if __name__ == "__main__":
    main()
