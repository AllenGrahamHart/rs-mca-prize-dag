#!/usr/bin/env python3
"""n=64,h=5 certificate chunk for the p<=20353 prefix."""

from __future__ import annotations

import json
from pathlib import Path

from f3_h5_n64_multirow_certificate import certify_primes


OUT = (
    Path(__file__).resolve().parent
    / "f3_h5_n64_prefix_20353_chunk_b.json"
)

PRIMES = (
    15233,
    15361,
    15809,
    15937,
    16001,
    16193,
    17729,
    17921,
    18049,
    18433,
)


def main() -> None:
    rows = certify_primes(PRIMES)
    OUT.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")
    print(f"wrote {len(rows)} rows to {OUT}")
    print("H5_N64_PREFIX_20353_CHUNK_B_PASS")


if __name__ == "__main__":
    main()
