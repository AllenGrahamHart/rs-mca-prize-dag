#!/usr/bin/env python3
"""Hash and schema audit for the fixed-swap certificate."""

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NOTES = ROOT / "critical/nodes/rate_half_band_closure/notes"
EXPECTED = {
    "kb_c2_112_aligned_positive_unramified_flint.py":
        "988e60a010ea2793049505b5e9b0ff6d5c28b300e4a00a4b8a3724849ede09f0",
    "kb_c2_112_aligned_positive_unramified_fixed_swap_minors.json":
        "c231e80bb7a0ce77412e63c196261c0c2c561e358dcc719b98db3b5f01f4db30",
    "kb_c2_112_aligned_positive_unramified_fixed_swap_conic.json":
        "bb53aa14bcfd96b890bb5ba895d2b8bfbfc1e46d4d7ba394a4ad156e3293faba",
    "kb_c2_112_aligned_positive_unramified_fixed_swap_survivors.json":
        "30519893654add8a06c5bc56413363eb48aeed9b457ca0eb1797a2119f40843f",
    "kb_c2_112_aligned_positive_unramified_fixed_swap_full_quotient_probe.py":
        "4be1d2b0d2ba0998f2821d4658c50612953c75122b0743fe58583c629f02e96e",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


for name, digest in EXPECTED.items():
    require(hashlib.sha256((NOTES / name).read_bytes()).hexdigest() == digest,
            f"hash {name}")

payload = json.loads(
    (NOTES / "kb_c2_112_aligned_positive_unramified_fixed_swap_survivors.json")
    .read_text(encoding="ascii")
)
require(payload["allocation"] == "swap", "allocation")
require(payload["prime"] == 2130706433, "prime")
require(tuple(item["factor_index"] for item in payload["survivors"]) == (5,),
        "factor indices")
require(all(len(item["modulus"]) == 3 for item in payload["survivors"]),
        "quadratic moduli")
require(payload["direct_norm_digest"]
        == "8c64015ee8ae65f509fb16b6d526df6efbb734b5dde51c8f99c0c1b98613a51a",
        "direct norm")

print(
    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_SWAP_AUDIT_PASS "
    "hashes=5 survivors=1"
)
