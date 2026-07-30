#!/usr/bin/env python3
"""Verify the degree-three geometric realization fence."""

from fractions import Fraction
from pathlib import Path


NODE = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def h(value: Fraction) -> Fraction:
    return (value * value + 2) / (1 - value * value)


def psi(value: Fraction) -> Fraction:
    return Fraction(2, value * value + 1)


def d3(value: Fraction) -> Fraction:
    return value**3 - 3 * value


def component(t: Fraction, x: Fraction) -> Fraction:
    u = x * x + 1
    return 2 * u * t * t - 2 * x * (x * x + 3) * t + u * u


def correspondence(y: Fraction, z: Fraction) -> Fraction:
    return y * y + y * z + z * z - 3


def verify_identities() -> None:
    t_values = [Fraction(value) for value in range(-7, 8) if value not in (-1, 1)]
    x_values = [Fraction(value) for value in range(-8, 9) if value not in (-1, 1)]
    for t in t_values:
        for x in x_values:
            left = correspondence(h(t), h(psi(x)))
            denominator = (t * t - 1) ** 2 * (x * x - 1) ** 2 * (x * x + 3) ** 2
            right = Fraction(9) * component(t, x) * component(t, -x) / denominator
            require(left == right, "component pullback")
            require(d3(h(t)) - d3(h(psi(x))) == (h(t) - h(psi(x))) * left, "D3 factorization")

    # The cleared identity has degree at most 8 in t and 12 in x. The grids
    # above contain more points than either bound, so exact interpolation
    # upgrades the evaluations to a polynomial identity.
    require(len(t_values) > 8 and len(x_values) > 12, "interpolation grid")


def verify_quartic() -> None:
    for x in [Fraction(value, 2) for value in range(-11, 12)]:
        u = x * x + 1
        p = u / 2
        s = x * (x * x + 3) / u
        q = 9 * (s * s * p * p - 2 * p**3 - 3 * p * p + 1)
        require(q == 0, "special coefficient quartic")
        discriminant = 4 * x * x * (x * x + 3) ** 2 - 8 * u**3
        require(discriminant == -4 * (x * x - 1) ** 2 * (x * x + 2), "source discriminant")


def verify_branch_values() -> None:
    for t in [Fraction(value, 3) for value in range(-12, 13) if value not in (-3, 3)]:
        phi = d3(h(t))
        derivative = Fraction(54) * t * (2 * t * t + 1) / (t * t - 1) ** 4
        if t == 0:
            require(phi == 2 and derivative == 0, "positive branch")
    require(d3(h(Fraction(0))) == 2, "h branch value")
    require(d3(h(Fraction(2))) == -2, "psi branch value")


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("fixed deployed active numerator" in contract, "scope fence")
    verify_identities()
    verify_quartic()
    verify_branch_values()
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_DEGREE3_GEOMETRIC_REALIZATION_FENCE_PASS")


if __name__ == "__main__":
    main()
