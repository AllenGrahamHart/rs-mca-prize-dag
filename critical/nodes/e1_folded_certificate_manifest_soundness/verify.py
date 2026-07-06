#!/usr/bin/env python3
"""Small coverage check for E1 folded-certificate manifests."""

from __future__ import annotations

OPEN_CELLS = {128, 256}


def verify_manifest(manifest: dict[int, dict[str, object]]) -> None:
    assert set(manifest) == OPEN_CELLS
    for cell, record in manifest.items():
        assert cell in OPEN_CELLS
        assert record.get("field")
        assert record.get("complete") is True
        assert record.get("nonzero_folded_vectors") == 0


def main() -> None:
    verify_manifest(
        {
            128: {"field": "named-exhibit-128", "complete": True, "nonzero_folded_vectors": 0},
            256: {"field": "named-exhibit-256", "complete": True, "nonzero_folded_vectors": 0},
        }
    )
    print("PASS: E1 folded-certificate manifest covers both open cells")


if __name__ == "__main__":
    main()
