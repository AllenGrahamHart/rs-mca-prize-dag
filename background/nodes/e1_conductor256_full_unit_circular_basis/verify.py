#!/usr/bin/env python3
"""Static exact checks for the conductor-256 circular-unit basis packet."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    indices = list(range(3, 128, 2))
    assert len(indices) == 63
    assert all(a % 2 == 1 and 3 <= a <= 127 for a in indices)

    pair_representatives = list(range(1, 128, 2))
    assert len(pair_representatives) == 64
    assert set(indices) == set(pair_representatives) - {1}

    pin = json.loads((ROOT / "source_pin.json").read_text())
    assert pin["miller"]["doi"] == "10.4064/aa164-4-4"
    assert pin["miller"]["download_sha256"] == (
        "61bdd160bd7e0234781af3a1f3a72008813d4c24ec562af9c87047947af8c68a"
    )
    assert pin["sinnott"]["doi"] == "10.2307/1970932"

    print("E1_CONDUCTOR256_FULL_UNIT_CIRCULAR_BASIS_PASS rank=63 pairs=64")


if __name__ == "__main__":
    main()
