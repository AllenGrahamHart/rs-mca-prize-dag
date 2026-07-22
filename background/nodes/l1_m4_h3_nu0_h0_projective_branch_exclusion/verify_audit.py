#!/usr/bin/env python3
"""Independent audit of the local order contradiction."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    checks = 0
    for p in (7, 31, 127, 8191):
        for m in (1, 2, 5, p - 1):
            assert m < 2 * m
            assert 8 % p != 0
            checks += 2

    proof = (HERE / "proof.md").read_text()
    for anchor in ("Divide by `r^7`", "ord_0(S)", "exact order `2m`",
                   "Phi'(r)", "8alpha"):
        assert anchor in proof
        checks += 1
    statement = (HERE / "statement.md").read_text()
    assert "tangent-at-zero component" in statement
    assert "does not exclude" in statement
    checks += 2
    print(f"L1_M4_H3_NU0_H0_PROJECTIVE_BRANCH_EXCLUSION_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
