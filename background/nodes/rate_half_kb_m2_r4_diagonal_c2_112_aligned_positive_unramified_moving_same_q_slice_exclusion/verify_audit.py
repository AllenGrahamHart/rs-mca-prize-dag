#!/usr/bin/env python3
"""Independent cache-schema audit for the moving-same certificate."""

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NOTES = ROOT / "critical/nodes/rate_half_band_closure/notes"
EXPECTED = {
    "kb_c2_112_aligned_positive_unramified_flint.py":
        "988e60a010ea2793049505b5e9b0ff6d5c28b300e4a00a4b8a3724849ede09f0",
    "kb_c2_112_aligned_positive_unramified_moving_same_minors.json":
        "f5c8285e2d93064f509ecb3ecfad98bb49eb1357777e39e968d06ce769eaba97",
    "kb_c2_112_aligned_positive_unramified_moving_same_conic.json":
        "e754fecd9711b5119e4603d45848d601cb894c1c2b357b696c243b8e4439ca72",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


for name, digest in EXPECTED.items():
    require(hashlib.sha256((NOTES / name).read_bytes()).hexdigest() == digest,
            f"hash {name}")

minor = json.loads(
    (NOTES / "kb_c2_112_aligned_positive_unramified_moving_same_minors.json")
    .read_text(encoding="ascii")
)
conic = json.loads(
    (NOTES / "kb_c2_112_aligned_positive_unramified_moving_same_conic.json")
    .read_text(encoding="ascii")
)
require(minor["template"] == conic["template"] == "moving-moving",
        "template")
require(minor["allocation"] == conic["allocation"] == "same",
        "allocation")
require(minor["prime"] == conic["prime"] == 2130706433, "prime")
require(len(minor["digests"]) == 4, "minor count")

print(
    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_SAME_AUDIT_PASS "
    "hashes=3 minors=4"
)
