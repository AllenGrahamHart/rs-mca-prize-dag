#!/usr/bin/env python3
"""Exact coprimality certificates for the m=8 quadratic exclusion."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_zero_quadratic_exclusion"
HNF = "l1_mersenne_next_to_maximal_hypergeometric_normal_form"
ROUTER = "l1_mersenne_hnf_order_zero_quadratic_collision_router"
NO_INJECTIVE = "l1_mersenne_hnf_order_zero_quadratic_collisionfree_exclusion"
CONSUMER = "l1_mixed_petal_amplification"
EXPECTED_ROWS = [
    (65536, 8191),
    (1048576, 131071),
    (4194304, 524287),
    (17179869184, 2147483647),
]


@dataclass(frozen=True)
class Fp2:
    """Element a+b*z with z^2-r*z+1=0."""

    a: int
    b: int
    p: int
    r: int

    def __post_init__(self) -> None:
        object.__setattr__(self, "a", self.a % self.p)
        object.__setattr__(self, "b", self.b % self.p)

    def coerce(self, other: int | Fp2) -> Fp2:
        if isinstance(other, Fp2):
            assert (other.p, other.r) == (self.p, self.r)
            return other
        return Fp2(other, 0, self.p, self.r)

    def __add__(self, other: int | Fp2) -> Fp2:
        other = self.coerce(other)
        return Fp2(self.a + other.a, self.b + other.b, self.p, self.r)

    __radd__ = __add__

    def __neg__(self) -> Fp2:
        return Fp2(-self.a, -self.b, self.p, self.r)

    def __sub__(self, other: int | Fp2) -> Fp2:
        return self + (-self.coerce(other))

    def __rsub__(self, other: int | Fp2) -> Fp2:
        return self.coerce(other) - self

    def __mul__(self, other: int | Fp2) -> Fp2:
        other = self.coerce(other)
        return Fp2(
            self.a * other.a - self.b * other.b,
            self.a * other.b + self.b * other.a + self.r * self.b * other.b,
            self.p,
            self.r,
        )

    __rmul__ = __mul__

    def norm(self) -> int:
        return (self.a * self.a + self.r * self.a * self.b + self.b * self.b) % self.p

    def inverse(self) -> Fp2:
        denominator = self.norm()
        assert denominator
        inverse = pow(denominator, -1, self.p)
        return Fp2(
            (self.a + self.r * self.b) * inverse,
            -self.b * inverse,
            self.p,
            self.r,
        )

    def __truediv__(self, other: int | Fp2) -> Fp2:
        return self * self.coerce(other).inverse()

    def __rtruediv__(self, other: int | Fp2) -> Fp2:
        return self.coerce(other) / self

    def __pow__(self, exponent: int) -> Fp2:
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


Polynomial = list[Fp2]


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


def evaluate(poly: Polynomial, value: Fp2) -> Fp2:
    result = value.coerce(0)
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def has_common_root(quadratic: Polynomial, reduced: Polynomial) -> bool:
    """A degree-at-most-one remainder vanishes at a root of quadratic."""

    assert len(quadratic) == 3 and quadratic[-1]
    trim(reduced)
    if len(reduced) == 1:
        return not reduced[0]
    assert len(reduced) == 2 and reduced[1]
    root = -reduced[0] / reduced[1]
    return not evaluate(quadratic, root)


def color_quadratic(zeta: Fp2, i: int, j: int) -> Polynomial:
    one = zeta.coerce(1)
    powers = [one - zeta ** (i * k) - zeta ** (j * k) for k in (1, 2, 3)]
    c2 = powers[1] - powers[0] ** 2 / 7
    c3 = powers[2] - 3 * powers[0] * powers[1] / 7 + 2 * powers[0] ** 3 / 49
    assert c2
    invariant = c3**2 / c2**3
    quadratic = [
        zeta.coerce(49),
        zeta.coerce(28) + 49 * invariant,
        zeta.coerce(4) + 7 * invariant,
    ]
    assert len(trim(quadratic)) == 3
    return quadratic


def b7_mod(quadratic: Polynomial) -> Polynomial:
    one = quadratic[0].coerce(1)
    result = [one]
    for offset in range(7):
        result = remainder(multiply(result, [one.coerce(offset), one]), quadratic)
    inverse_factorial = pow(math.factorial(7), -1, one.p)
    return [coefficient * inverse_factorial for coefficient in result]


def verify_row(n: int, p: int) -> int:
    assert p % 8 == 7
    root_two = pow(2, (p + 1) // 4, p)
    assert root_two * root_two % p == 2
    zeta = Fp2(0, 1, p, root_two)
    one = zeta.coerce(1)
    assert zeta**4 == -one
    assert zeta**8 == one
    assert zeta**p == zeta**-1

    exclusions = 0
    for i, j in combinations(range(1, 8), 2):
        quadratic = color_quadratic(zeta, i, j)
        torsion = power_mod(b7_mod(quadratic), n, quadratic)
        torsion[0] -= one
        trim(torsion)
        assert not has_common_root(quadratic, torsion), (n, p, i, j)
        exclusions += 1
    return exclusions


def atlas_rows() -> list[tuple[int, int]]:
    atlas = ROOT / "background/nodes/l1_official_checkpoint_characteristic_atlas/checkpoint_atlas.tsv"
    rows = []
    for line in atlas.read_text().splitlines()[1:]:
        _, n, p, _, m, residual = map(int, line.split("\t"))
        if m == 8 and residual == 8:
            rows.append((n, p))
    return rows


def main() -> None:
    rows = atlas_rows()
    assert rows == EXPECTED_ROWS
    cases = sum(verify_row(n, p) for n, p in rows)
    assert cases == 84

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    for dependency in (HNF, ROUTER, NO_INJECTIVE):
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = Path(__file__).with_name("statement.md").read_text()
    proof = Path(__file__).with_name("proof.md").read_text()
    assert "deg E_s != 2" in statement
    assert "4*21=84" in proof and "b_7(s)^n=1" in proof

    # Domain and conclusion mutations must be rejected.
    assert len(list(combinations(range(1, 8), 2))) == 21
    one = Fp2(1, 0, 8191, 128)
    assert has_common_root([one, one.coerce(0), one], [one.coerce(0)])

    print(
        "L1_MERSENNE_HNF_M8_ORDER_ZERO_QUADRATIC_EXCLUSION_PASS "
        f"rows={len(rows)} patterns=21 exclusions={cases} mutations=2"
    )


if __name__ == "__main__":
    main()
