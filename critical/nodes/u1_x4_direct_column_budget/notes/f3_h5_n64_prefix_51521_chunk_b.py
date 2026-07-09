#!/usr/bin/env python3
"""n=64,h=5 certificate chunk B for the p<=51521 prefix."""

from __future__ import annotations

import json
from pathlib import Path

from f3_h5_n64_multirow_certificate import certify_primes


OUT = (
    Path(__file__).resolve().parent
    / "f3_h5_n64_prefix_51521_chunk_b.json"
)

PRIMES = (
    50497,
    50753,
    51137,
    51329,
    51521,
)


def main() -> None:
    rows = certify_primes(PRIMES)
    OUT.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")
    print(f"wrote {len(rows)} rows to {OUT}")
    print("H5_N64_PREFIX_51521_CHUNK_B_PASS")


if __name__ == "__main__":
    main()
