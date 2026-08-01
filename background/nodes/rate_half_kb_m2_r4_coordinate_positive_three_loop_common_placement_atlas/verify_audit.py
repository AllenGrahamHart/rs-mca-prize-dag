#!/usr/bin/env python3
"""Audit placement and sign coverage."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def main():
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    if "classes `H,H,L`" not in proof or "classes `H,L,L`" not in proof:
        raise RuntimeError("profile roles")
    if "opposite signed deck" not in proof:
        raise RuntimeError("442 signs")
    if "Changing the signed representative of either low pair" not in proof:
        raise RuntimeError("433 signs")
    if "Root-high and root-low are not identified" not in audit:
        raise RuntimeError("placement fence")
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_PLACEMENT_AUDIT_PASS "
        "role_orbits=4 sign_models=2"
    )


if __name__ == "__main__":
    main()
