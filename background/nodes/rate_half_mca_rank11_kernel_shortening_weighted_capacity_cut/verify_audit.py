#!/usr/bin/env python3
"""Independent shifted-power audit of the terminal kernel cut."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import factorial
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    result = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, lhs in enumerate(left):
        for j, rhs in enumerate(right):
            result[i + j] += lhs * rhs
    return result


def add(left: list[Fraction], right: list[Fraction], scale: Fraction = Fraction(1)) -> list[Fraction]:
    size = max(len(left), len(right))
    return [
        (left[index] if index < len(left) else 0)
        + scale * (right[index] if index < len(right) else 0)
        for index in range(size)
    ]


def binomial_polynomial(anchor: int, degree: int) -> list[Fraction]:
    result = [Fraction(1)]
    for offset in range(degree):
        result = multiply(result, [Fraction(anchor - offset), Fraction(1)])
    return [value / factorial(degree) for value in result]


def vector_digest(values: list[Fraction]) -> str:
    payload = json.dumps(
        [[value.numerator, value.denominator] for value in values],
        separators=(",", ":"),
    ).encode()
    return hashlib.sha256(payload).hexdigest()


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    start = p["replay_minimum"]
    s_start = start - 10
    density = Fraction(
        p["residual_record_floor"] * p["lane_density_numerator"],
        p["lane_density_denominator"],
    )
    polynomial = [value * density for value in binomial_polynomial(p["m_offset"] + start, 11)]
    complete = [0, *p["complete_record_caps"]]
    for d in range(1, 10):
        basis_factor = binomial_polynomial(p["n_offset"] + start, 10 - d)
        weighted_factor = binomial_polynomial(s_start if d <= 3 else s_start - 1, d + 1)
        multiplier = Fraction(complete[d]) if d <= 3 else Fraction(*p["t1_F_fractions"][str(d)])
        weighted_factor = [value * multiplier for value in weighted_factor]
        capacity = [value / (d + 2) for value in multiply(basis_factor, weighted_factor)]
        polynomial = add(polynomial, capacity, Fraction(-1))
    require(len(polynomial) == p["positive_shifted_power_coefficients"] == 12, "power count")
    require(all(value > 0 for value in polynomial), "power signs")
    require(vector_digest(polynomial) == p["shifted_power_vector_sha256"], "power digest")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_SHORTENING_WEIGHTED_CAPACITY_CUT_AUDIT_PASS "
        f"positive_power_coefficients={len(polynomial)}"
    )


if __name__ == "__main__":
    main()
