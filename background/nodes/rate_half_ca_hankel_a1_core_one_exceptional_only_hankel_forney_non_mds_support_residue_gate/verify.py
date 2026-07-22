#!/usr/bin/env python3
"""Exact finite control for the non-MDS support-residue gate."""

from __future__ import annotations

from math import prod


def evaluate_locator(roots: list[int], value: int, prime: int) -> int:
    return prod((value - root) % prime for root in roots) % prime


def check_case(
    exceptional: list[int],
    support: list[int],
    k_degree: int,
    expected_shift: int,
    expected_exceptional_sum: int,
    prime: int,
) -> None:
    sum_constant = 0
    sum_linear = 0
    for root in support:
        a_value = evaluate_locator(exceptional, root, prime)
        derivative = prod((root - other) % prime for other in support if other != root) % prime
        denominator_inverse = pow(a_value * derivative % prime, prime - 2, prime) * pow(root, k_degree, prime) % prime
        sum_constant = (sum_constant + denominator_inverse) % prime
        sum_linear = (sum_linear + root * denominator_inverse) % prime

    shift = -sum_linear * pow(sum_constant, prime - 2, prime) % prime
    if shift != expected_shift:
        raise AssertionError("Forney control shift changed")

    residue_sum = 0
    for root in support:
        phi_value = (root + shift) % prime
        a_value = evaluate_locator(exceptional, root, prime)
        derivative = prod((root - other) % prime for other in support if other != root) % prime
        residue_sum = (
            residue_sum
            + phi_value * pow(root, k_degree, prime) * pow(a_value * derivative % prime, prime - 2, prime)
        ) % prime
    if residue_sum:
        raise AssertionError("support residue gate failed")
    if any((root + shift) % prime == 0 for root in exceptional + support):
        raise AssertionError("Forney numerator lost coprimality")

    exceptional_sum = 0
    for root in exceptional:
        a_derivative = prod((root - other) % prime for other in exceptional if other != root) % prime
        b_value = evaluate_locator(support, root, prime)
        beta = (root + shift) * pow(a_derivative * b_value % prime, prime - 2, prime) % prime
        exceptional_sum = (exceptional_sum + beta * pow(root, k_degree, prime)) % prime
    if exceptional_sum != expected_exceptional_sum:
        raise AssertionError("exceptional boundary identity failed")


def main() -> None:
    prime = 101
    exceptional = [1, 2, 3, 4, 5, 6]
    check_case(exceptional, [10, 11, 12, 13], 0, 42, 0, prime)
    check_case(exceptional, [10, 11, 12, 14], 8, 20, 1, prime)

    print(
        "RATE_HALF_NON_MDS_SUPPORT_RESIDUE_PASS "
        f"prime={prime} e=3 h=4 low_boundary=0 top_boundary=1"
    )


if __name__ == "__main__":
    main()
