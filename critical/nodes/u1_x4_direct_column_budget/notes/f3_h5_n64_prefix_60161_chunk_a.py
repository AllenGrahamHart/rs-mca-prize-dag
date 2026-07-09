#!/usr/bin/env python3
"""n=64,h=5 certificate chunk A for the p<=60161 prefix."""

from __future__ import annotations

import json
from pathlib import Path

from f3_h5_n64_multirow_certificate import certify_primes


OUT = (
    Path(__file__).resolve().parent
    / "f3_h5_n64_prefix_60161_chunk_a.json"
)

PRIMES = (
    58049,
    58369,
    59009,
    59393,
    60161,
)


def main() -> None:
    rows = certify_primes(PRIMES)
    OUT.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")
    print(f"wrote {len(rows)} rows to {OUT}")
    print("H5_N64_PREFIX_60161_CHUNK_A_PASS")


if __name__ == "__main__":
    main()
