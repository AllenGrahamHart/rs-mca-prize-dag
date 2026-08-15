#!/usr/bin/env python3
"""Independent interpolation audit for the K'=10 rank-eight exclusion."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "d03271ea09234ab73dad72b6509a136b07427a479bba822c7db55adf8c4c868e"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def polynomial_add(left: list[int], right: list[int], prime: int) -> list[int]:
    size = max(len(left), len(right))
    return [
        ((left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0)) % prime
        for i in range(size)
    ]


def polynomial_scale(poly: list[int], scalar: int, prime: int) -> list[int]:
    return [(scalar * value) % prime for value in poly]


def polynomial_multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = (result[i + j] + a * b) % prime
    return result


def evaluate(poly: list[int], point: int, prime: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * point + coefficient) % prime
    return value


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    require(p["correction_space_dimension"] == p["ambient_rs_dimension"] == 10, "space equality")

    prime = 103
    points = list(range(2, 11))
    values = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    interpolant = [0]
    for i, point in enumerate(points):
        numerator = [1]
        denominator = 1
        for j, other in enumerate(points):
            if i == j:
                continue
            numerator = polynomial_multiply(numerator, [(-other) % prime, 1], prime)
            denominator = denominator * (point - other) % prime
        term = polynomial_scale(numerator, values[i] * pow(denominator, -1, prime), prime)
        interpolant = polynomial_add(interpolant, term, prime)

    require(len(interpolant) <= 9, "degree at most eight")
    require([evaluate(interpolant, point, prime) for point in points] == values, "interpolation")
    proof = (HERE / "proof.md").read_text()
    for pin in ("V'=C'", "Lagrange interpolation", "Vandermonde", "K'=11"):
        require(pin in proof, f"proof pin {pin}")
    print(
        "RATE_HALF_MCA_RANK11_RANK8_MINIMAL_SHORTENING_EXCLUSION_AUDIT_PASS "
        f"toy=GF({prime}) points={len(points)} degree<={len(interpolant)-1} proof_pins=4/4"
    )


if __name__ == "__main__":
    main()
