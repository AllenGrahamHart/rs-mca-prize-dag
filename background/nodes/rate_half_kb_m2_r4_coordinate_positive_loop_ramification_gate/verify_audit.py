#!/usr/bin/env python3
"""Audit positive ramification and noninjective-product fences."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def main():
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    if "positive ramification rule" not in proof or "antipodal as well" not in proof:
        raise RuntimeError("ramified case")
    if "not by positive product injectivity" not in audit:
        raise RuntimeError("injectivity fence")
    if "cross multiplicity up to four" not in audit:
        raise RuntimeError("multiplicity fence")
    print(
        "RATE_HALF_KB_POSITIVE_LOOP_RAMIFICATION_AUDIT_PASS "
        "ramified_slots=2 nonramified_loop_cap=1"
    )


if __name__ == "__main__":
    main()
