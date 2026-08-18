#!/usr/bin/env python3
"""Independent audit of multi-anchor exchange synchronization."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "23f845b7dda0dc7c0b648dd7cdab4b0b1da6326d8cef877912265f8f7986a072"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    sizes = tuple(data["packet_size"] - data["secondary_records_per_type"] * t for t in range(1, 5))
    assert sizes == (29, 26, 23, 20)
    assert data["minimum_anchor_records"] == max(sizes) == 29
    assert min(size - 1 for size in sizes) == 19 >= data["locators_determining_pencil"]
    assert data["high_complexity_threshold"] == 2299571

    proof = (HERE / "proof.md").read_text().lower()
    statement = (HERE / "statement.md").read_text().lower()
    assert "arbitrary triple-owner type" in proof
    assert "same residual anchor core" in proof
    assert "different pair types may have different" in statement
    assert "per first-owned pair type" in data["nonclaim"].lower()
    print("RANK11_MULTI_ANCHOR_SYNC_AUDIT_PASS minimum=29 overlap=19")


if __name__ == "__main__":
    main()
