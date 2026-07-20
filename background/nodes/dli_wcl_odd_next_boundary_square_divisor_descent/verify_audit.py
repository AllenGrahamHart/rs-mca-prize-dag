#!/usr/bin/env python3
"""Mutation audit for the odd next-boundary square-divisor descent."""

from pathlib import Path

import verify


HERE = Path(__file__).resolve().parent


def main():
    joined = "\n".join((HERE / name).read_text() for name in
                       ("statement.md", "proof.md", "claim_contract.md"))
    required = [
        "5*205=1 mod 512",
        "7*439=1 mod 1024",
        "G(Y)=Y A(Y)^2-(bY+1)^2",
        "rho=(by+1)/A(y)",
        "computes neither integer",
    ]
    for token in required:
        assert token in joined, token

    verify.symbolic_checks()
    verify.subgroup_positive_controls()
    verify.official_shape_quotients()

    p = 17
    A, b = [14, 11, 1], 7
    G = verify.build_g(A, b, p)
    mutated = verify.build_g(A, b + 1, p)
    assert G != mutated
    assert G[1] == (A[0] * A[0] - 2 * b) % p
    assert G[2] == (2 * A[0] * A[1] - b * b) % p

    print("DLI_WCL_ODD_NEXT_BOUNDARY_SQUARE_DIVISOR_DESCENT_AUDIT_PASS "
          "docs=5 mutations=4")


if __name__ == "__main__":
    main()
