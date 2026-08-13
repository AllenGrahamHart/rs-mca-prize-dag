#!/usr/bin/env python3
"""Independent audit of surviving rank/support-router gates."""

rows = ((1048576, 4337, 1044239), (1048576, 4334, 1044242))
if any(R - j != e for R, j, e in rows):
    raise ValueError("support conversion")
print("RATE_HALF_MCA_GLOBAL_CORE_RANK_SUPPORT_REPLACEMENT_TARGET_AUDIT_PASS gates=2")
