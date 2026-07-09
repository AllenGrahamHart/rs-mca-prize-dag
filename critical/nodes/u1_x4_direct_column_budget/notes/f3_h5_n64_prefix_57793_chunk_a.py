#!/usr/bin/env python3
"""n=64,h=5 certificate chunk A for the p<=57793 prefix."""

from __future__ import annotations

import json
from pathlib import Path

from f3_h5_n64_multirow_certificate import certify_primes


OUT = (
    Path(__file__).resolve().parent
    / "f3_h5_n64_prefix_57793_chunk_a.json"
)

PRIMES = (
    55681,
    56897,
    57089,
    57601,
    57793,
)


def main() -> None:
    rows = certify_primes(PRIMES)
    OUT.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")
    print(f"wrote {len(rows)} rows to {OUT}")
    print("H5_N64_PREFIX_57793_CHUNK_A_PASS")


if __name__ == "__main__":
    main()
