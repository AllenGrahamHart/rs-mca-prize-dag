#!/usr/bin/env python3
"""Independent hash and cache-schema audit for the exact router."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NOTES = ROOT / "critical/nodes/rate_half_band_closure/notes"

EXPECTED = {
    "kb_c2_112_aligned_positive_unramified_flint.py":
        "988e60a010ea2793049505b5e9b0ff6d5c28b300e4a00a4b8a3724849ede09f0",
    "kb_c2_112_aligned_positive_unramified_moving_router.py":
        "1309bd5e7366ce9852fd0f7f030059d0ecafa2685370b8935af19665e7bcf933",
    "kb_c2_112_aligned_positive_unramified_moving_swap_minors.json":
        "cafb0e48b2be45a98e72dbe5a1689f3ffe9a6bda64e685ea152873af48ab3d86",
    "kb_c2_112_aligned_positive_unramified_moving_swap_conic.json":
        "aacf8976e2fe3933055fb8e7d1a90d2b176dad8699ce37cbf2c0f7f3d6fd521e",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


for name, digest in EXPECTED.items():
    require(hashlib.sha256((NOTES / name).read_bytes()).hexdigest() == digest,
            f"hash {name}")

minor = json.loads(
    (NOTES / "kb_c2_112_aligned_positive_unramified_moving_swap_minors.json")
    .read_text(encoding="ascii")
)
conic = json.loads(
    (NOTES / "kb_c2_112_aligned_positive_unramified_moving_swap_conic.json")
    .read_text(encoding="ascii")
)
require(minor["template"] == conic["template"] == "moving-moving",
        "template")
require(minor["allocation"] == conic["allocation"] == "swap",
        "allocation")
require(minor["prime"] == conic["prime"] == 2130706433, "prime")
require(len(minor["polynomials"]) == len(minor["digests"]) == 4,
        "minor count")
require(conic["schema"] ==
        "kb-c2-112-aligned-positive-kernel-conic-v1", "conic schema")

print(
    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_SWAP_AUDIT_PASS "
    "hashes=4 minors=4"
)
