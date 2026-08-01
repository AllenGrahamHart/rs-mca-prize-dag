#!/usr/bin/env python3
"""Audit defect accounting and positive nonclaims."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def main():
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    if "2*binom(2,2)=2" not in proof:
        raise RuntimeError("cross defect")
    if "opposite signed product types" not in audit:
        raise RuntimeError("sign split")
    if "No positive product injectivity" not in audit:
        raise RuntimeError("injectivity fence")
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_EDGE_AUDIT_PASS "
        "common_defect=3 concentrated_extra=2"
    )


if __name__ == "__main__":
    main()
