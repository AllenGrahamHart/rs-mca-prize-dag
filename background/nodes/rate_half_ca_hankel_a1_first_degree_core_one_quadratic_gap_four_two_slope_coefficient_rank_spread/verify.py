#!/usr/bin/env python3
"""Replay the symmetric nullity and strengthened line arithmetic."""


E = 183_251_937_963
RHO = 3 * E - 1
T = RHO + 4

for rank_loss in range(0, 3):
    for union_excess in range(2, 8):
        difference = rank_loss + union_excess
        left_kernel = rank_loss + 1
        assert difference >= left_kernel + 1
        assert difference - left_kernel == union_excess - 1

for pair_deficit in range(0, 5):
    line_cap = (RHO + 2 - pair_deficit) // 2
    expanders = T - line_cap
    expected = (RHO + 6 + pair_deficit + 1) // 2
    assert expanders == expected
    assert 2 * line_cap <= RHO + 2 - pair_deficit

print(
    "QUADRATIC_GAP_FOUR_TWO_SLOPE_COEFFICIENT_RANK_SPREAD_PASS",
    f"rho={RHO}",
    f"minimum_expanders={T - (RHO + 2) // 2}",
)
