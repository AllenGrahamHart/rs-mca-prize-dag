#!/usr/bin/env python3
"""Replay the exact rate-half unique-decoding scope fence."""

from __future__ import annotations


def main() -> None:
    n = 1 << 41
    k = 1 << 40
    lo = k + (1 << 34)
    endpoint = 3 * n // 4

    assert n == 2 * k
    assert (n + k) % 2 == 0
    assert (n + k) // 2 == endpoint
    assert 2 * (n - endpoint) == n - k
    assert 2 * (n - (endpoint - 1)) - (n - k) == 2
    assert lo < endpoint
    assert 2 * (n - lo) > n - k

    # The gate is monotone in a, so checking the largest interior integer
    # excludes every point in the complete live interval.
    assert not (2 * (n - (endpoint - 1)) <= n - k)

    print(
        "RATE_HALF_UNIQUE_DECODING_CA_MCA_SCOPE_FENCE_PASS "
        f"n={n} k={k} live_lo={lo} endpoint={endpoint} "
        "nearest_failure=2"
    )


if __name__ == "__main__":
    main()
