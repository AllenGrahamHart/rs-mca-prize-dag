#!/usr/bin/env python3
"""Hash and schema audit for the fixed-mixed certificates."""

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NOTES = ROOT / "critical/nodes/rate_half_band_closure/notes"
EXPECTED = {
    "kb_c2_112_aligned_positive_unramified_flint.py":
        "988e60a010ea2793049505b5e9b0ff6d5c28b300e4a00a4b8a3724849ede09f0",
    "kb_c2_112_aligned_positive_unramified_quartic_router.py":
        "412c96175f61cf83b4964d3d6f7df8a75c310c20bf2aa70c4d4d3d03b2ee898e",
    "kb_c2_112_aligned_positive_unramified_fixed_direct_router.py":
        "8b3fd59b19fa2317f18278de3bc92615af2ae134e4b1ffddd55d2e75188891e6",
    "kb_c2_112_aligned_positive_unramified_fixed_mixed_minors.json":
        "b44414abc54949c3a111e15a012bd6e96e060f1c9a3b81172ab05ffe7d2dcfb2",
    "kb_c2_112_aligned_positive_unramified_fixed_mixed_conic.json":
        "4f091eee7d93b05939cb15303befc75f0b37628112496ac8b5c703f9b2acafd5",
    "kb_c2_112_aligned_positive_unramified_fixed_mixed_component_pair23.json":
        "8510195c58cedb3b1759bf182113be5f820ed5157a5d0c20b11fa63ef2ada08e",
    "kb_c2_112_aligned_positive_unramified_fixed_mixed_degree5_survivors.json":
        "8ec4e97be7cf2adebe40a450ada0b385268686f44566ca520c964896e53fffe9",
    "kb_c2_112_aligned_positive_unramified_fixed_mixed_degree5_full_quotient_probe.py":
        "0b516fcdbf890854faec25a5fbff315096c056de4fc91d1fa4b386e801686ede",
    "kb_c2_112_aligned_positive_unramified_fixed_mixed_linear_router.py":
        "97ad3cc0199365e0304e065148fc1256b2c2fd8eb43914ace22767538fd2f148",
    "kb_c2_112_aligned_positive_unramified_fixed_off_common.py":
        "d75a8ae2ee7a8b25a98d515cae54e76acf7fc9cafe7763b461dcc45b7af53a1a",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


for name, digest in EXPECTED.items():
    require(hashlib.sha256((NOTES / name).read_bytes()).hexdigest() == digest,
            f"hash {name}")

payload = json.loads(
    (NOTES / "kb_c2_112_aligned_positive_unramified_fixed_mixed_degree5_survivors.json")
    .read_text(encoding="ascii")
)
require(payload["allocation"] == "mixed", "allocation")
require(payload["prime"] == 2130706433, "prime")
require(tuple(item["factor_index"] for item in payload["survivors"])
        == (1, 2, 3, 4), "factor indices")
require(all(len(item["modulus"]) == 3 for item in payload["survivors"]),
        "quadratic moduli")
require(payload["direct_norm_digest"]
        == "a6d9a723529fe31a1c3b5e7e6740ec4c87512f3f00e8473dad75b7ed71750d63",
        "direct norm")

print(
    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_MIXED_AUDIT_PASS "
    "hashes=10 survivors=4"
)
