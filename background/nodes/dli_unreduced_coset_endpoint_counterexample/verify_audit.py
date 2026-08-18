#!/usr/bin/env python3
"""Independent invariants for the unreduced DLI coset counterexample."""

from __future__ import annotations

import math

import verify


def main() -> None:
    result = verify.build()
    assert sum(math.comb(128, m) for m in range(65, 129)) == (1 << 128) - result["central_count"] - 1
    assert math.comb(128, 64) > 2
    assert result["central_count"] > 1 << 127
    assert verify.T * result["deficit"] < 1 << 255
    assert pow(3, (verify.Q - 1) // 2, verify.Q) == verify.Q - 1
    print("DLI_UNREDUCED_COSET_COUNTEREXAMPLE_AUDIT_PASS")


if __name__ == "__main__":
    main()
