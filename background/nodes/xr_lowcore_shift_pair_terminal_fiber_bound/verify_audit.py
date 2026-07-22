#!/usr/bin/env python3
"""Mutation control for the strict Plotkin fiber bound."""

family = [frozenset(S) for S in ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))]
X = frozenset((0,))
Y = frozenset((1,))
residuals = {
    S & T
    for S in family
    for T in family
    if S - T == X and T - S == Y
}

assert residuals == {frozenset((2,)), frozenset((3,))}
N, H, t = 4, 1, 1
K = 2
bound = (4 * H) // (4 * H - (N - 2 * t))
assert bound == len(residuals) == 2
assert len(residuals) > 1  # rejects the registered over-sharp mutation
assert t == K - 1  # the multiplicity-one cutoff t>=K is sharp here

print("XR_LOWCORE_SHIFT_PAIR_TERMINAL_FIBER_BOUND_AUDIT_PASS", len(residuals))
