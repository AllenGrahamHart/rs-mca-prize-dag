#!/usr/bin/env python3
"""Independent audit of the uniform corank-two projective cap."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def cap_fraction(t: int, r: int, w: int) -> Fraction:
    numerator = 1
    for value in range(r + t, r + t + 3):
        numerator *= value
    return Fraction(numerator, 3 * w * (w + t + 1))


def main() -> None:
    p = json.loads(CONTRACT.read_text())["parameters"]
    r, w, target = p["R"], p["w"], p["uniform_record_cap"]
    endpoint_checks = 0
    for name in ("complete_row", "adjacent_row", "official_endpoint"):
        expected = p[name]
        value = cap_fraction(expected["t"], r, w)
        require(value.numerator // value.denominator == expected["record_cap"], name)
        require(value < target + 1, f"{name} next integer")
        endpoint_checks += 1

    signs = [2 * t + 3 * w + 3 - r for t in (0, p["turn_left"], p["turn_right"], p["t_maximum"])]
    require(signs == [-846157, -1, 1, 1250975], "one-turn signs")
    require(cap_fraction(0, r, w) > cap_fraction(p["t_maximum"], r, w), "endpoint order")
    require(3 * w * (w + 1) == p["complete_row"]["ordered_basis_floor"], "matroid specialization")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_CORANK2_UNIFORM_PROJECTIVE_BASIS_CAP_AUDIT_PASS "
        f"endpoint_checks={endpoint_checks} turn={p['turn_left']}/{p['turn_right']}"
    )


if __name__ == "__main__":
    main()
