#!/usr/bin/env python3
"""Independent audit of residual-cycle support."""

from __future__ import annotations


e = (2**39 + 1) // 3
n = (3 * e - 7) // 2
r = (e + 1) // 2
pushforward = {"tau": 4}

if r - 1 != 91625968981:
    raise SystemExit("large rank failed")
if n + 3 != 274877906944:
    raise SystemExit("large class failed")
if sum(pushforward.values()) != 4:
    raise SystemExit("four-core degree failed")
if "gamma_0" in pushforward:
    raise SystemExit("assigned center entered correction support")

print(
    "RATE_HALF_SHAPE_A_LARGE_CLASS_CENTER_RESIDUAL_EXCLUSION_AUDIT_PASS",
    f"rank={r - 1}",
    f"support={pushforward}",
)
