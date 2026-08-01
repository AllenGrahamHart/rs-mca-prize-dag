#!/usr/bin/env python3
"""Audit sign discipline and scope fences for the common kernel."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def main():
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    statement = (NODE / "statement.md").read_text()
    if "A_0(W)-p A_2(W)=0" not in proof:
        raise RuntimeError("product sign")
    if "z B_1(z^2)+s A_2(z^2)=0" not in proof:
        raise RuntimeError("sum sign")
    if "corrected coefficient row" not in audit:
        raise RuntimeError("correction pin")
    if "Determinant vanishing alone" not in audit:
        raise RuntimeError("admissibility fence")
    if "Other loop placements are covered" not in statement:
        raise RuntimeError("placement fence")
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_COMMON_KERNEL_AUDIT_PASS "
        "signs=2 placement_fence=1 admissibility_fence=1"
    )


if __name__ == "__main__":
    main()
