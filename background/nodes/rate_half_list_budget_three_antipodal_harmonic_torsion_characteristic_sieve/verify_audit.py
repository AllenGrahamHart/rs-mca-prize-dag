#!/usr/bin/env python3
"""Mutation audit for the harmonic-torsion characteristic sieve."""

from pathlib import Path

import verify


HERE = Path(__file__).resolve().parent


def main():
    joined = "\n".join(
        (HERE / name).read_text()
        for name in ("statement.md", "proof.md", "claim_contract.md", "audit.md")
    )
    required = [
        "Phi_N(X)=X^(N/2)+1",
        "yw=-x",
        "pairwise distinct squares",
        "126` variables and `127` equations",
        "does not promote",
        "finite-characteristic harmonic lifts are not excluded",
    ]
    for token in required:
        assert token in joined, token

    verify.symbolic_check()
    verify.sparse_size_check()
    x, y, w = verify.finite_characteristic_positive()
    assert verify.harmonic_value(x, y, w, 97) == 0

    mutations = 0
    for candidate in range(1, 97):
        if candidate * candidate % 97 in {1, x*x % 97, y*y % 97}:
            continue
        if verify.harmonic_value(x, y, candidate, 97) != 0:
            mutations += 1
            break
    assert mutations == 1

    coefficients = [0] * 16
    coefficients[1] = 2
    coefficients[9] = 1
    assert not verify.balanced(coefficients)

    print(
        "RATE_HALF_ANTIPODAL_HARMONIC_TORSION_SIEVE_AUDIT_PASS "
        "docs=6 mutations=2"
    )


if __name__ == "__main__":
    main()
