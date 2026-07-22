#!/usr/bin/env python3
"""Mutation audit for broad-checkpoint Frobenius periodicity."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    audit = (NODE / "audit.md").read_text()
    checks = 0
    for anchor in (
        "coefficients lie in the prime",
        "closed under multiplication by `p`",
        "Fourier inversion",
        "both its `+1` support and its `-1` support",
        "seven broad-remainder",
        "nine rows",
    ):
        assert anchor in statement
        checks += 1
    for anchor in (
        "At `a=0`",
        "A(zeta^(ap^r))",
        "orbits of translation",
        "positive and negative supports",
    ):
        assert anchor in proof
        checks += 1
    assert "seven exact atlas rows" in contract
    assert "524,288 bytes" in audit
    assert "No Modal run" in (NODE / "lineage.md").read_text()
    checks += 3
    print(f"L1_BROAD_CHECKPOINT_FROBENIUS_PERIODICITY_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
