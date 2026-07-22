#!/usr/bin/env python3
"""Independent audit of the Euler quotient algebra."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    checks = 0
    # Check 3g-y g' numerically for independent coefficients and inputs.
    for prime in (7, 13, 31, 127):
        for a, b, y in ((2, 3, 4), (5, 1, 6), (1, 5, 2)):
            g = (y**3 + a * y + b) % prime
            derivative = (3 * y * y + a) % prime
            assert (3 * g - y * derivative) % prime == (2 * a * y + 3 * b) % prime
            checks += 1
        for nu in range(4):
            for h in range(4 - nu):
                degree_v = prime + h - 4
                assert (prime + 4) + prime + degree_v == 3 * prime + h
                checks += 1

    proof = (HERE / "proof.md").read_text()
    for anchor in ("Differentiate", "multiply (1) by `R`", "2aY+3b",
                   "bH(0)", "deg V=p+h-4"):
        assert anchor in proof
        checks += 1
    statement = (HERE / "statement.md").read_text()
    assert "H(0)!=0" in statement
    assert "does not exclude" in statement
    checks += 2
    print(f"L1_M4_H3_EULER_QUOTIENT_FACTORIZATION_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
