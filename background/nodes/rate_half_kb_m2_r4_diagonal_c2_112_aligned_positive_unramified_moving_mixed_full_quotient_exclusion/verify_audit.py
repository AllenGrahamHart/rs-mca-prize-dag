#!/usr/bin/env python3
"""Independent artifact audit for the moving-mixed certificate."""

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NOTES = ROOT / "critical/nodes/rate_half_band_closure/notes"
EXPECTED = {
    "kb_c2_112_aligned_positive_unramified_flint.py":
        "988e60a010ea2793049505b5e9b0ff6d5c28b300e4a00a4b8a3724849ede09f0",
    "kb_c2_112_aligned_positive_unramified_moving_mixed_minors.json":
        "799e8feb8f89fee7bf7dab30c3e1e4522380bb490f350a5c93f48f6ff19d3565",
    "kb_c2_112_aligned_positive_unramified_moving_mixed_conic.json":
        "639a9eeacf175fbfa2e427ca8ad6c3dae1110f658bf4edbe7e3136f2c1748880",
    "kb_c2_112_aligned_positive_unramified_moving_mixed_survivors.json":
        "c02e649960b35e3d264472c3c1aa69cfd71d48930df8844c281b901b3e5a5f36",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


for name, digest in EXPECTED.items():
    require(hashlib.sha256((NOTES / name).read_bytes()).hexdigest() == digest,
            f"hash {name}")

payload = json.loads(
    (NOTES / "kb_c2_112_aligned_positive_unramified_moving_mixed_survivors.json")
    .read_text(encoding="ascii")
)
require(payload["allocation"] == "mixed", "allocation")
require(payload["prime"] == 2130706433, "prime")
require(tuple(item["factor_index"] for item in payload["survivors"])
        == (3, 5, 10, 12), "factor indices")
require(tuple(len(item["modulus"]) - 1 for item in payload["survivors"])
        == (3, 3, 7, 7), "field degrees")
require(payload["direct_norm_digest"]
        == "13a295c5219450a00c588cc9661863022d03ddca67429eb9626d398fe4515dae",
        "direct norm")

print(
    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_MIXED_AUDIT_PASS "
    "hashes=4 survivors=4 deployed_traces=2"
)
