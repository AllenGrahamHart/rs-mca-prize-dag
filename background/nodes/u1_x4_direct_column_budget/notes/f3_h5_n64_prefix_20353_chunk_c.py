#!/usr/bin/env python3
"""n=64,h=5 certificate chunk for the p<=20353 prefix."""

from __future__ import annotations

import json
from pathlib import Path

from f3_h5_n64_multirow_certificate import certify_primes


OUT = (
    Path(__file__).resolve().parent
    / "f3_h5_n64_prefix_20353_chunk_c.json"
)

PRIMES = (
    19009,
    19073,
    19457,
    19777,
    19841,
    20161,
    20353,
)


def main() -> None:
    rows = certify_primes(PRIMES)
    OUT.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")
    print(f"wrote {len(rows)} rows to {OUT}")
    print("H5_N64_PREFIX_20353_CHUNK_C_PASS")


if __name__ == "__main__":
    main()
