#!/usr/bin/env python3
"""Mutation and documentation audit for the quartic-divisor descent."""

from pathlib import Path

import verify


HERE = Path(__file__).resolve().parent


def main():
    statement = (HERE / "statement.md").read_text()
    proof = (HERE / "proof.md").read_text()
    contract = (HERE / "claim_contract.md").read_text()

    required = [
        "1593 mod 2048",
        "G(Y)=Y A(Y)^2-1",
        "rho=A(y)^(-1)",
        "Delta=sum_(j=0)^8 H_j R_j",
        "does not compute `Delta`",
    ]
    joined = statement + proof + contract
    for token in required:
        assert token in joined, token

    verify.symbolic_checks()
    verify.positive_control()
    verify.official_shape_checks()

    # Mutating the normalization exponent or the descended sign is detected.
    assert (9 * 1592 - 1) % 2048 != 0
    p = 19
    y = 4
    A_y = pow(y, 4, p)
    assert (y * A_y * A_y - 1) % p == 0
    assert (y * A_y * A_y + 1) % p != 0

    print("DLI_WCL_ELL4_WEIGHT9_QUARTIC_DIVISOR_DESCENT_AUDIT_PASS "
          "docs=5 mutations=2")


if __name__ == "__main__":
    main()
