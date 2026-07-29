#!/usr/bin/env python3
"""Independent cross-multiplication audit for the core-shadow payment."""

numerator = 1_048_578 * 1_048_577
denominator = 67_449 * 67_448

assert 241 * denominator <= numerator < 242 * denominator
assert numerator == 1_099_514_773_506
assert denominator == 4_549_300_152

incidences = 215_793 * 4_980
assert incidences == 1_074_649_140
assert 240 * 4_477_704 < incidences <= 240 * 4_477_705

print("L1_M31_TOP_NEIGHBOR_CORE_SHADOW_AUDIT_PASS")
