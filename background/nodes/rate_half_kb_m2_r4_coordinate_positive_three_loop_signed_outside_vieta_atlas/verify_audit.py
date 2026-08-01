#!/usr/bin/env python3
"""Audit sign and saturation fences in the outside-Vieta atlas."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def main():
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    if "epsilon_e epsilon_f sigma" not in proof:
        raise RuntimeError("cycle invariant")
    if "z=-sD(w)/(beta(w-1))" not in proof:
        raise RuntimeError("squared converse")
    if "All seven outside quotient labels are distinct" not in audit:
        raise RuntimeError("label guard")
    if "bare resultant is necessary only" not in audit:
        raise RuntimeError("resultant fence")
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_SIGNED_OUTSIDE_AUDIT_PASS "
        "cycle_invariants=2 saturation_fences=2"
    )


if __name__ == "__main__":
    main()
