#!/usr/bin/env python3
"""Independent integer audit for the source-head router."""

assert 72_428**2 - 1_053_557 * 4_979 == 154_881
assert 1_053_557 * 67_449 == 71_061_366_093
assert 458_812 * 154_881 + 104_721 == 71_061_366_093

assert 107_897 * 4_980 == 537_327_060
assert 2_238_862 * 240 < 537_327_060 <= 2_238_863 * 240
assert 35_821_804 * 15 == 537_327_060

print("L1_M31_TOP_PAIR_SOURCE_HEAD_SATURATION_AUDIT_PASS")
