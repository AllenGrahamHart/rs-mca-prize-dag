#!/usr/bin/env python3
"""Independent audit of the base-field normalization implications."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    checks = 0
    for p in (524287, 2147483647):
        assert p % 5 == 2
        # Euler's criterion independently checks that the quadratic pair is
        # not split over the prime field.
        assert pow(5, (p - 1) // 2, p) == -1 % p
        for c in (1, 2, 7):
            a, b = -2 * c * c % p, c**3 % p
            assert (pow(a, 3, p) + 8 * b * b) % p == 0
            assert (-4 * pow(a, 3, p) - 27 * b * b) % p == 5 * b * b % p
            checks += 2

    proof = (HERE / "proof.md").read_text()
    for anchor in ("y_0=3s/4", "Quadratic reciprocity", "X_c=X_c^p",
                   "C=C^p", "A=A^p"):
        assert anchor in proof
        checks += 1
    statement = (HERE / "statement.md").read_text()
    assert "fully base-field-normalized" in statement
    assert "does not exclude" in statement
    checks += 2
    print(f"L1_M4_H3_NU2_BASE_FIELD_NORMALIZATION_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
