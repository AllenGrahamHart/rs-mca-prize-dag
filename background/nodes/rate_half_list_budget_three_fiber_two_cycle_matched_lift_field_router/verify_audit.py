#!/usr/bin/env python3
"""Independent small-field audit of the anti-invariant lift exclusion."""

from __future__ import annotations

from dataclasses import dataclass


P = 17
D = 3  # A nonsquare modulo 17.
N = 8


@dataclass(frozen=True)
class Fp2:
    a: int
    b: int = 0

    def __post_init__(self) -> None:
        object.__setattr__(self, "a", self.a % P)
        object.__setattr__(self, "b", self.b % P)

    def __add__(self, other: Fp2 | int) -> Fp2:
        right = other if isinstance(other, Fp2) else Fp2(other)
        return Fp2(self.a + right.a, self.b + right.b)

    def __sub__(self, other: Fp2 | int) -> Fp2:
        right = other if isinstance(other, Fp2) else Fp2(other)
        return Fp2(self.a - right.a, self.b - right.b)

    def __neg__(self) -> Fp2:
        return Fp2(-self.a, -self.b)

    def __mul__(self, other: Fp2 | int) -> Fp2:
        right = other if isinstance(other, Fp2) else Fp2(other)
        return Fp2(
            self.a * right.a + D * self.b * right.b,
            self.a * right.b + self.b * right.a,
        )

    def __pow__(self, exponent: int) -> Fp2:
        assert exponent >= 0
        answer = Fp2(1)
        base = self
        while exponent:
            if exponent & 1:
                answer = answer * base
            base = base * base
            exponent //= 2
        return answer


def equations(r: Fp2, q: Fp2) -> tuple[bool, bool, bool]:
    one = Fp2(1)
    four = Fp2(4)
    return (
        r**2 * (one + q) ** 2 == four * q * (r**2 - r + one) ** 2,
        (r - one) ** 4 * (one + q) ** 2 == four * q * (r + one) ** 4,
        (r**2 + one) ** 2 * (one + q) ** 2
        == four * q * (r**2 - Fp2(4) * r + one) ** 2,
    )


def main() -> None:
    assert pow(D, (P - 1) // 2, P) == P - 1
    assert P % (4 * N) == 1 + 2 * N

    anti = [
        Fp2(a, b)
        for a in range(P)
        for b in range(P)
        if Fp2(a, b) ** (4 * N) == Fp2(1)
        and Fp2(a, b) ** (2 * N) == Fp2(-1)
        and Fp2(a, b) ** 4 != Fp2(1)
    ]
    ratios = [Fp2(q) for q in range(1, P) if pow(q, N, P) == 1 and q != 1]
    assert anti and ratios
    assert all(r**P == -r for r in anti)

    hits = [
        (r, q, branch)
        for r in anti
        for q in ratios
        for branch, holds in enumerate(equations(r, q))
        if holds
    ]
    assert not hits
    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_MATCHED_LIFT_FIELD_ROUTER_AUDIT_PASS "
        f"p={P} N={N} anti_lifts={len(anti)} outer_ratios={len(ratios)} hits=0"
    )


if __name__ == "__main__":
    main()
