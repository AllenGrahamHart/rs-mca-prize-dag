#!/usr/bin/env python3
"""Independent audit of the carrier-position case arithmetic."""

from __future__ import annotations

import json
import hashlib
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    q = 61
    impossible = []
    for s2 in range(q):
        for s3 in range(q):
            M2 = q - s2
            M3 = q - s3
            if M3 <= M2 and s2 + s3 < q:
                impossible.append((s2, s3))
    digest = hashlib.sha256(
        "".join(f"{s2},{s3}\n" for s2, s3 in impossible).encode()
    ).hexdigest()
    need(p["K71_impossible_defect_pair_count"] == len(impossible) == 961, "pruning census")
    need(p["K71_impossible_defect_pair_digest_sha256"] == digest, "pruning digest")
    M2 = p["K71_active_completions"]["M2"]
    b2, b3, b4 = M2 + 1, M2 + 3, M2 + 4
    expected = {
        "T23": (b2 + b3, 7),
        "A23": (b2 + b3 - 1, 8),
        "T24": (b2 + b4, 6),
        "A24": (b2 + b4 - 1, 7),
        "N34": (b2 + 5, 6),
        "N34A": (b2 + 4, 7),
    }
    for name, (union, dimension) in expected.items():
        row = p["K71_cases"][name]
        need(row == {"union_size": union, "fixed_dimension": dimension}, name)
    need(p["nested_anchor_intersection_sizes"] == [0, 1], "anchor intersection")
    print(
        "RATE_HALF_MCA_SPARSE_CIRCUIT_K71_CARRIER_POSITION_TRICHOTOMY_AUDIT_PASS "
        f"impossible={len(impossible)} cases={len(expected)}"
    )


if __name__ == "__main__":
    main()
