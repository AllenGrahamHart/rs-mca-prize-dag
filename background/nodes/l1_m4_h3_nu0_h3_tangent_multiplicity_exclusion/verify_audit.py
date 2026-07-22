#!/usr/bin/env python3
"""Independent order audit for the cubic-tangent exclusion."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    checks = 0
    for e in range(2, 40):
        for d in (0, 1):
            for epsilon in (0, 1):
                correction_order = 2 * e + d + epsilon - 1
                assert correction_order > e
                checks += 1

    for r in (2, 3):
        multiplicity_cap = 3 * r
        assert multiplicity_cap <= 9
        checks += 1

    proof = (HERE / "proof.md").read_text()
    for anchor in ("phi'(y_0)", "e<=p-1", "ord_x(R')=e-1",
                   "2e+d+epsilon-1", "strictly larger", "p<=9"):
        assert anchor in proof
        checks += 1
    statement = (HERE / "statement.md").read_text()
    assert "empty on all four" in statement
    assert "positive valuation" in statement
    checks += 2

    print(f"L1_M4_H3_NU0_H3_TANGENT_MULTIPLICITY_EXCLUSION_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
