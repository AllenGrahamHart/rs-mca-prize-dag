#!/usr/bin/env python3
"""Exact dual-moment check for the F_97 exceptional CRT control."""

from __future__ import annotations

import runpy
from pathlib import Path


P = 97
SOURCE = (
    Path(__file__).resolve().parents[1]
    / "rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_boundary_crt_reconstruction"
    / "verify.py"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    source = runpy.run_path(str(SOURCE))
    fixture = source["build_fixture"]()
    evaluate = source["evaluate"]
    derivative = source["derivative"]

    exceptional = fixture["exceptional"]
    boundary_values = fixture["boundary_values"]
    quotient_values = fixture["quotient_values"]
    a_poly = fixture["a_poly"]
    b_poly = fixture["b_poly"]
    q_e = fixture["q_e"]
    s = fixture["s"]
    x_0 = fixture["x_0"]
    domain_order = fixture["domain_order"]
    a_prime = derivative(a_poly)

    rs_moment: list[int] = []
    cancelled_moment: list[int] = []
    for z_degree in range(2):
        rs_value = 0
        cancelled_value = 0
        for row, omega_row, quotient_row in zip(
            exceptional, boundary_values, quotient_values, strict=True
        ):
            omega_coefficient = (
                omega_row[z_degree] if z_degree < len(omega_row) else 0
            )
            quotient_coefficient = (
                quotient_row[z_degree] if z_degree < len(quotient_row) else 0
            )
            rs_value += omega_coefficient * pow(evaluate(a_prime, row), -1, P)
            cancelled_value += (
                row
                * (row - s)
                * (row - x_0)
                * evaluate(b_poly, row)
                * evaluate(q_e, row) ** 2
                * quotient_coefficient
            )
        rs_value %= P
        cancelled_value %= P
        require(
            cancelled_value == domain_order * rs_value % P,
            "subgroup derivative cancellation mismatch",
        )
        rs_moment.append(rs_value)
        cancelled_moment.append(cancelled_value)

    require(rs_moment == [91, 28], "unexpected degree-five parity syndrome")
    require(all(cancelled_moment), "random packet unexpectedly passed moment gate")
    print(
        "RATE_HALF_DISTANCE_THREE_QUARTIC_BOUNDARY_DUAL_MOMENT_PASS "
        f"field={P} e=3 moments=1 syndrome={rs_moment} rejected=True"
    )


if __name__ == "__main__":
    main()
