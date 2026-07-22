#!/usr/bin/env python3
"""Exact finite controls for endpoint derivative-resultant reciprocity."""

from __future__ import annotations

from math import prod


def check_profile(rows: list[tuple[int, int]], swapped: bool) -> None:
    prime = 101
    scales = [2, 3, 5, 7, 11, 13]
    q_1_values = [
        scale * ((-left) % prime) * ((-right) % prime) % prime
        for scale, (left, right) in zip(scales, rows, strict=True)
    ]
    res_q_1 = prod(q_1_values) % prime
    res_q_e = prod(scales) % prime
    p_ord_zero = prod((-root) % prime for root in range(1, 13)) % prime

    if swapped:
        z_min, z_max = 1, 12
        if z_max * res_q_1 % prime != z_min * res_q_e * p_ord_zero % prime:
            raise AssertionError("swapped derivative-resultant identity failed")
    elif res_q_1 != res_q_e * p_ord_zero % prime:
        raise AssertionError("flat derivative-resultant identity failed")


def main() -> None:
    flat_rows = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12)]
    swapped_rows = [(1, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11)]
    check_profile(flat_rows, swapped=False)
    check_profile(swapped_rows, swapped=True)
    official_e = 2**38 - 1
    official_k_0 = (official_e - 1) // 2
    if official_k_0 % 2 != 1:
        raise AssertionError("official square-class exponent is not odd")
    print(
        "RATE_HALF_ENDPOINT_DERIVATIVE_RESULTANT_PASS "
        f"e={official_e} k_0={official_k_0}"
    )


if __name__ == "__main__":
    main()
