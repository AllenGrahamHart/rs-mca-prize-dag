#!/usr/bin/env python3
"""Exact primary replay for rich-container incidence collisions."""

from math import comb


def packet(count: int):
    n, h = 1_048_576, 42_453
    incidence = count * h
    q, remainder = divmod(incidence, n)
    pair_total = remainder * comb(q + 1, 2) + (n - remainder) * comb(q, 2)
    triple_total = remainder * comb(q + 1, 3) + (n - remainder) * comb(q, 3)
    pair_floor = (pair_total + comb(count, 2) - 1) // comb(count, 2)
    triple_floor = (triple_total + comb(count, 3) - 1) // comb(count, 3)
    return incidence, q, remainder, pair_total, triple_total, pair_floor, triple_floor


full = packet(508)
typed = packet(254)
assert full == (21_566_124, 20, 594_604, 211_121_520, 1_308_351_400, 1_640, 61)
assert typed == (10_783_062, 10, 297_302, 50_158_940, 139_207_710, 1_562, 52)
assert (full[0] + 1_048_576 - 1) // 1_048_576 == 21
assert (typed[0] + 1_048_576 - 1) // 1_048_576 == 11
print("RANK11_RICH_CONTAINER_INCIDENCE_COLLISION_OK", full[-2:], typed[-2:])
