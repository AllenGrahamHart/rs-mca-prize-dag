#!/usr/bin/env python3
"""Replay the shape-A pure-split component floor."""

def require(condition, message):
    if not condition:
        raise AssertionError(message)


e = (2**39 + 1) // 3
m = e - 2
n = (3 * e - 7) // 2
rows = (9 * e - 7) // 2
pure_fibers = e + 7
pair_floor = (pure_fibers * n * (n - 1) + m - 1) // m
component_floor = (pair_floor + (n - 1) - 1) // (n - 1)

require(3 * e - e - (e - 7) == pure_fibers, "pure-fiber floor")
require(pair_floor == 75557863727701029814224, "pair floor")
require(component_floor == n + 14 == 274877906955, "component floor")
require(13 * (e - 2) < 9 * n < 14 * (e - 2), "n+14 ceiling")
require(rows * m > m * n // 2, "absolute-irreducibility Bezout margin")
require(m * (n - 1) == 50371909149418411349340, "resultant bidegree")

print(
    "RATE_HALF_SHAPE_A_PURE_SPLIT_COMPONENT_PASS "
    f"pure_fibers={pure_fibers} pair_floor={pair_floor} "
    f"component_floor={component_floor}"
)
