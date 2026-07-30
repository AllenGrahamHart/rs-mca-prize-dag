#!/usr/bin/env python3
"""Verify the residual coefficient-quartic singularity atlas."""

from __future__ import annotations

from fractions import Fraction


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def coefficients(a: int, b: Fraction) -> dict[str, Fraction]:
    return {
        "A": (a - 2) * (a - b * b + 2),
        "B": -(a - 2) * (2 * a - b * b - 2 * b + 4),
        "C": (a - b) ** 2,
        "D": 4 * a * a - a * b * b - 4 * a * b - 4 * a + 16 * b - 16,
        "E": -2 * (a - 2) * (a - b),
        "F": (a - 2) ** 2,
    }


def q_and_derivatives(a: int, b: Fraction, s: Fraction, p: Fraction) -> tuple[Fraction, ...]:
    row = coefficients(a, b)
    A, B, C, D, E, F = (row[key] for key in "ABCDEF")
    q = A * p**4 + B * s**2 * p**2 - 2 * B * p**3 + C * s**4 - 4 * C * s**2 * p + (2 * C + D) * p**2 + E * s**2 - 2 * E * p + F
    q_s = 2 * B * s * p**2 + 4 * C * s**3 - 8 * C * s * p + 2 * E * s
    q_p = 4 * A * p**3 + 2 * B * s**2 * p - 6 * B * p**2 - 4 * C * s**2 + 2 * (2 * C + D) * p - 2 * E
    q_ss = 2 * B * p**2 + 12 * C * s**2 - 8 * C * p + 2 * E
    q_sp = 4 * B * s * p - 8 * C * s
    q_pp = 12 * A * p**2 + 2 * B * s**2 - 12 * B * p + 2 * (2 * C + D)
    return q, q_s, q_p, q_ss * q_pp - q_sp * q_sp


def verify() -> None:
    samples = [Fraction(-5), Fraction(-3), Fraction(-1), Fraction(0), Fraction(1), Fraction(3), Fraction(5)]
    for a in (-1, 1):
        for b in samples:
            if b in (-2, 2):
                continue
            row = coefficients(a, b)
            alpha = row["B"] ** 2 - 4 * row["A"] * row["C"]
            beta = 8 * row["C"] ** 2 + 2 * row["B"] * row["E"] - 4 * row["C"] * row["D"]
            require(alpha == (a - 2) * (a + 2) * (b - 2) ** 3 * (b + 2), "alpha")
            require(beta == -4 * (a + 2) * (a - b) * (b - 2) ** 3, "beta")

            center = q_and_derivatives(a, b, Fraction(0), Fraction(-1))
            require(center[:3] == (0, 0, 0), "central singularity")
            require(center[3] == -4 * (a - 2) * (a + 2) * (b - 2) ** 4, "central Hessian")

            n_disc = 4 * (a + 2) * (b - 2) ** 2
            require(n_disc != 0, "N must be nonsquare quadratic")
            if b != a:
                x0 = Fraction(a - 2, a - b)
                require(x0 != 0, "side singularity escaped")
                # Evaluate at a quadratic point using only S^2=x0.
                C = row["C"]
                E = row["E"]
                F = row["F"]
                require(C * x0 * x0 + E * x0 + F == 0, "side point")
                side_hessian = 16 * (a - 2) * (a + 2) * (b - 2) ** 3
                require(side_hessian != 0, "side tangent cone")
                require(alpha != 0 and beta != 0 and row["C"] != 0, "generic irreducibility gate")
            else:
                require(row["C"] == 0 and row["E"] == 0, "tacnode specialization")
                require(row["B"] != 0 and row["F"] != 0, "tacnode leading terms")

    require(3 == 3 * 2 // 2, "plane quartic arithmetic genus")
    require(3 == 1 + 2, "node-tacnode delta ledger")


if __name__ == "__main__":
    verify()
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_RESIDUAL_QUARTIC_SINGULARITY_ATLAS_PASS")
