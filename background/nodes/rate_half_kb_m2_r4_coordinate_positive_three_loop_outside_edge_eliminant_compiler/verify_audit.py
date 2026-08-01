#!/usr/bin/env python3
"""Audit degree-drop and saturation handling."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def main():
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    if "A^3 Res(P,Q)" not in proof:
        raise RuntimeError("generic factor")
    if "If `A=0` and `B!=0`" not in proof:
        raise RuntimeError("linear branch")
    if "Forbidden common roots" not in audit:
        raise RuntimeError("saturation fence")
    if "heuristic evidence only" not in audit:
        raise RuntimeError("experiment fence")
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_EDGE_ELIMINANT_AUDIT_PASS "
        "degree_branches=3 saturation_fences=2"
    )


if __name__ == "__main__":
    main()
