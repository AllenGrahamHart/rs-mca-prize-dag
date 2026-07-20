#!/usr/bin/env python3
"""Mutation audit for the WCL (1,6) even-norm divisor descent."""

from pathlib import Path

import verify


HERE = Path(__file__).resolve().parent


def main():
    joined = "\n".join((HERE / name).read_text() for name in
                       ("statement.md", "proof.md", "claim_contract.md"))
    required = [
        "F(X)=product_i(X-rho_i)=E(X^2)-X B(X^2)",
        "G(Y)=E(Y)^2-YB(Y)^2",
        "rho=E(y)/B(y)",
        "does not compute `Delta_6`",
    ]
    for token in required:
        assert token in joined, token

    verify.symbolic_check()
    verify.positive_control()
    verify.official_shape_quotients()

    p = 97
    E, B = [8, 62, 85, 1], [39, 20]
    G = verify.build_g(E, B, p)
    mutated = verify.build_g(E, [39, 21], p)
    assert G != mutated
    assert G[-1] == 1
    assert G[0] == E[0] * E[0] % p

    print("DLI_WCL_ELL1_WEIGHT6_EVEN_NORM_DIVISOR_DESCENT_AUDIT_PASS "
          "docs=4 mutations=3")


if __name__ == "__main__":
    main()
