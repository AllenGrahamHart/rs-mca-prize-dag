#!/usr/bin/env python3
"""Hash and schema audit for the fixed-same certificate."""

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NOTES = ROOT / "critical/nodes/rate_half_band_closure/notes"
EXPECTED = {
    "kb_c2_112_aligned_positive_unramified_flint.py":
        "988e60a010ea2793049505b5e9b0ff6d5c28b300e4a00a4b8a3724849ede09f0",
    "kb_c2_112_aligned_positive_unramified_fixed_same_minors.json":
        "f9767957f0946595c9e3618a469cdc69ecde3809b7726e1ef5f9061054a6ad2f",
    "kb_c2_112_aligned_positive_unramified_fixed_same_conic.json":
        "0ba5df80a91444b44c5e8e8e2b5124e68ea7cfd891fca8a448730b973b9e4c00",
    "kb_c2_112_aligned_positive_unramified_fixed_same_survivors.json":
        "79369e3c0e39d8525c069e2bb4878b43263fee6ab9ab04065f0ede9cbde5b008",
    "kb_c2_112_aligned_positive_unramified_fixed_same_full_quotient_probe.py":
        "bd1a945e6b09578278d3bfee6b9d7307c2abd365941a8ce143bb4ae390fc40e0",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


for name, digest in EXPECTED.items():
    require(hashlib.sha256((NOTES / name).read_bytes()).hexdigest() == digest,
            f"hash {name}")

payload = json.loads(
    (NOTES / "kb_c2_112_aligned_positive_unramified_fixed_same_survivors.json")
    .read_text(encoding="ascii")
)
require(payload["allocation"] == "same", "allocation")
require(payload["prime"] == 2130706433, "prime")
require(tuple(item["factor_index"] for item in payload["survivors"])
        == (1, 2, 3, 4), "factor indices")
require(all(len(item["modulus"]) == 2 for item in payload["survivors"]),
        "base-field moduli")
require(payload["direct_norm_digest"]
        == "a04c532e08a8bf9fff2337895559c14e32e4242c51e1be747890e329e40ba6b0",
        "direct norm")

print(
    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_SAME_AUDIT_PASS "
    "hashes=5 survivors=4"
)
