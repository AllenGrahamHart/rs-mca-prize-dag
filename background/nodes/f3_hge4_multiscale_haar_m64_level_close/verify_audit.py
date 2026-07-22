#!/usr/bin/env python3
"""Mutation guards for the multiscale Haar m=64 close."""

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
mutations = 0

# Independent moment-index partition: every 1<=j<=H appears once.
for H in range(1, 257):
    counts = []
    for a in range(H.bit_length()):
        counts.append(((H // (1 << a)) + 1) // 2)
    assert sum(counts) == H
    mutations += 1

# The raw h=4 energy maximum still misses after only the baseline two powers
# of two; the support-Taylor refinement is load-bearing.
assert (1 << 80) < 10**16 * 12**8

# The old independent-L relaxation also misses h=5.
old_h5 = Fraction(80, 7) ** 16 * Fraction(120, 7) ** 8 * Fraction(240, 7) ** 4
assert (1 << 104) < old_h5
mutations += 2

# The exact two-adic endpoint gain reverses the h=4 comparison.
assert 10**24 // 4 < 1 << 78
assert (1 << 16) * (1 << 26) ** 2 > 16**16
mutations += 2

# Scope guard: the packet must not advertise a higher-level payment.
statement = (
    ROOT
    / "background"
    / "nodes"
    / "f3_hge4_multiscale_haar_m64_level_close"
    / "statement.md"
).read_text()
assert "does not pay any level `m>=128`" in statement
mutations += 1

print("F3_HGE4_MULTISCALE_HAAR_M64_LEVEL_CLOSE_AUDIT_PASS", mutations)
