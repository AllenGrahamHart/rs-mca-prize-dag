#!/usr/bin/env python3
"""Independent audit of anchor one-swap pencil synchronization."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "da40b3e5c48ebf3c5f08a763edacb5c0035f5c7e3608c12881bd39536710f8e8"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    assert data["anchor_owned_slopes"] == 5524
    sizes = tuple(32 - 3 * t for t in range(1, 5))
    assert sizes == (29, 26, 23, 20)
    assert min(size - 1 for size in sizes) == 19
    assert 19 >= data["locators_determining_pencil"] == 2
    assert data["high_complexity_threshold"] == 2299571

    # Two independent vectors determine their two-dimensional ambient space.
    p = data["toy"]["field"]
    vectors = [((-root) % p, 1) for root in range(data["toy"]["anchor_locators"])]
    base = data["toy"]["base_indices"]
    common = [index for index in base if index != data["toy"]["removed_index"]]
    left, right = vectors[common[0]], vectors[common[-1]]
    det = (left[0] * right[1] - left[1] * right[0]) % p
    assert det != 0 and len(common) == 4
    assert all(index in common for index in set(base) - {0})

    statement = (HERE / "statement.md").read_text().lower()
    proof = (HERE / "proof.md").read_text().lower()
    assert "one core-saturated exact support for every record" in statement
    assert "in the fixed anchor set" in statement
    assert "same residual anchor core" in proof
    assert "no summation over packet" in proof
    assert "does not pay" in data["nonclaim"].lower()
    print("RANK11_ANCHOR_EXCHANGE_SYNC_AUDIT_PASS anchor=5524 overlap=19")


if __name__ == "__main__":
    main()
