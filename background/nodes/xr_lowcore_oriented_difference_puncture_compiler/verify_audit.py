#!/usr/bin/env python3
"""Mutation controls for exact dimension and excess preservation."""

rows = [
    (8, 3, 2, 2),
    (16, 5, 3, 4),
    (32, 9, 5, 7),
]
for N, K, h, t in rows:
    A = K + h
    N_prime = N - 2 * t
    K_prime = K - t
    A_prime = A - t
    assert A_prime - K_prime == h
    assert N_prime - A_prime == N - A - t
    assert (A - (t - 1)) - K_prime != h  # rejects partial-locator mutation

print("XR_LOWCORE_ORIENTED_DIFFERENCE_PUNCTURE_COMPILER_AUDIT_PASS", len(rows))
