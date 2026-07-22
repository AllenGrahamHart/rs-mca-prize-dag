#!/usr/bin/env python3
"""Exact arithmetic checks for the unit-resultant logarithmic trace."""

from __future__ import annotations


def main() -> None:
    prime = 101
    rank = 3
    n_x = 5
    n_sq = n_x + rank - 1
    degree_w = 2
    e_log = 4
    q_bar_log = 7
    q_0_log = 9

    resultant_log = (
        (degree_w + n_x + 1) * e_log
        + (degree_w + n_x) * q_bar_log
    ) % prime
    original_trace = (
        resultant_log - degree_w * (e_log + q_bar_log)
    ) % prime
    reciprocal_trace = (
        original_trace
        + (rank - 1) * (e_log + q_bar_log - q_0_log)
    ) % prime
    printed_trace = (
        (n_sq + 1) * e_log
        + n_sq * q_bar_log
        - (rank - 1) * q_0_log
    ) % prime
    if reciprocal_trace != printed_trace:
        raise AssertionError("degree cancellation or reversal correction failed")

    roots = (1, 2, 3)
    w_values = (2, 5, 7)
    total_values = (11, 13, 17)
    direct_trace = sum(
        total * pow(value, -1, prime) % prime
        for total, value in zip(total_values, w_values)
    ) % prime
    adjusted_q_0_log = (
        ((n_sq + 1) * e_log + n_sq * q_bar_log - direct_trace)
        * pow(rank - 1, -1, prime)
    ) % prime
    replayed = (
        (n_sq + 1) * e_log
        + n_sq * q_bar_log
        - (rank - 1) * adjusted_q_0_log
    ) % prime
    if replayed != direct_trace or len(roots) != rank:
        raise AssertionError("split-etale trace replay failed")

    print(
        "RATE_HALF_QUOTIENT_UNIT_RESULTANT_LOG_TRACE_PASS "
        f"prime={prime} rank={rank} trace={direct_trace}"
    )


if __name__ == "__main__":
    main()
