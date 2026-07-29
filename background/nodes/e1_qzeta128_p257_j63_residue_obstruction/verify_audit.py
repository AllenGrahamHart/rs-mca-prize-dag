#!/usr/bin/env python3
"""Independent polynomial-evaluation audit of the J_63 residue witness."""

from __future__ import annotations

from verify import COEFFICIENTS, ELL, G, P, PAIRS, Q, R, character_logs, psi


def polynomial(a: int, b: int, logs: dict[int, int]) -> list[int]:
    coefficients = [0] * Q
    for x in range(2, P):
        exponent = (a * logs[x] + b * logs[(1 - x) % P]) % Q
        coefficients[exponent] -= 1
    return coefficients


def evaluate(coefficients: list[int], value: int) -> int:
    result = 0
    for coefficient in reversed(coefficients):
        result = (result * value + coefficient) % R
    return result


def main() -> None:
    logs = character_logs()
    polynomials = [polynomial(a, b, logs) for a, b in PAIRS]
    root = pow(G, (R - 1) // Q, R)
    reductions = []
    for s in range(1, 64, 2):
        zeta = pow(root, s, R)
        conjugate = pow(zeta, -1, R)
        alpha = 1
        for coefficient, poly in zip(COEFFICIENTS, polynomials):
            numerator = evaluate(poly, zeta)
            denominator = evaluate(poly, conjugate)
            assert numerator and denominator
            ratio = numerator * pow(denominator, -1, R) % R
            alpha = alpha * pow(ratio, coefficient % (R - 1), R) % R
        reductions.append(alpha)

    witness = psi(reductions)
    assert witness == 500235
    assert pow(witness, ELL, R) == 1
    print(
        "E1_QZETA128_P257_J63_RESIDUE_OBSTRUCTION_AUDIT_PASS "
        f"method=coefficient-polynomials psi_alpha={witness}"
    )


if __name__ == "__main__":
    main()
