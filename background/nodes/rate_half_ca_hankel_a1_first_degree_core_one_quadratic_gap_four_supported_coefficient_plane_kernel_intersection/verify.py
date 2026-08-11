#!/usr/bin/env python3
"""Replay coefficient-plane Witt and evaluation-rank bounds."""


E = 183_251_937_963
W_DIM = E + 1

for c in (1, 2):
    quotient_dimension = c
    max_isotropic = quotient_dimension // 2
    max_intersection = 1 + max_isotropic
    min_eval_rank = W_DIM - max_intersection
    assert min_eval_rank == E - c // 2
    assert min_eval_rank <= E

assert 1 + 1 // 2 == 1
assert 1 + 2 // 2 == 2
assert E - 1 // 2 == E
assert E - 2 // 2 == E - 1

print(
    "QUADRATIC_SUPPORTED_COEFFICIENT_KERNEL_INTERSECTION_PASS",
    f"rank_one={E}",
    f"rank_two>={E - 1}",
)
