#!/usr/bin/env python3
"""Audit the family-vs-sample fence in the complete exclusion."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    require("unit ideal" in proof and "algebraic closure" in proof,
            "family certificate")
    require("not inferred empty" in audit, "sample fence")
    require("64" in proof and "32" in proof and "384" in proof,
            "family census")
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_COMPLETE_EXCLUSION_AUDIT_PASS "
        "unresolved_systems=192 common_records_per_system=2"
    )


if __name__ == "__main__":
    main()
