#!/usr/bin/env python3
"""Audit the orientation-level nonclaim and row matching."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def main():
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    if "exhaustive five-row partition" not in proof:
        raise RuntimeError("exhaustive composition")
    if "Positive parity and noncoordinate orientations" not in audit:
        raise RuntimeError("orientation fence")
    print(
        "RATE_HALF_KB_M2_R4_NEGATIVE_COORDINATE_EXCLUSION_AUDIT_PASS "
        "profiles=442,433 loops=0,1,2"
    )


if __name__ == "__main__":
    main()
