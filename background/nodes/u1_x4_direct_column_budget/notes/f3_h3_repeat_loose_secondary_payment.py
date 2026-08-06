#!/usr/bin/env python3
"""Trivial payment for finite loose secondary subcells."""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_repeat_loose_secondary_subcells import residual_degree


OFFICIAL_MIN_N = 2**13
OFFICIAL_MAX_N = 2**41


@dataclass(frozen=True)
class SecondaryPayment:
    label: str
    parameter_degree: int
    per_parameter_x_bound: int

    def point_bound(self, n: int) -> int:
        return self.parameter_degree * self.per_parameter_x_bound * n


def secondary_payments() -> tuple[SecondaryPayment, ...]:
    return (
        SecondaryPayment("A", residual_degree("A"), 1),
        SecondaryPayment("B", residual_degree("B"), 1),
    )


def total_secondary_bound(n: int) -> int:
    return sum(row.point_bound(n) for row in secondary_payments())


def main() -> None:
    print("h=3 repeat loose secondary payment compiler")
    print("fixed secondary parameter: slope 1 alone gives at most n choices of X")
    for row in secondary_payments():
        print(
            f"branch_{row.label}: parameter_degree={row.parameter_degree} "
            f"bound={row.parameter_degree}*n"
        )
    total_degree = sum(row.parameter_degree for row in secondary_payments())
    if total_degree != 53:
        raise AssertionError(total_degree)
    print(f"combined_secondary_bound={total_degree}*n")
    official_ns = [2**s for s in range(13, 42)]
    bad_quadratic = [n for n in official_ns if total_secondary_bound(n) >= n * n]
    if bad_quadratic:
        raise AssertionError(("secondary payment not quadratic-negligible", bad_quadratic[:5]))
    print(
        f"combined secondary payment is below n^2 for official n=2^13..2^41; "
        f"first_bound={total_secondary_bound(OFFICIAL_MIN_N)}"
    )
    print("H3_REPEAT_LOOSE_SECONDARY_PAYMENT_PASS")


if __name__ == "__main__":
    main()
