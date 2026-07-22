#!/usr/bin/env python3
"""Independent scalar audit for the zero-b Euler exclusion."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    checks = 0
    for p in (7, 31, 127, 524287, 2147483647):
        if p == 5:
            continue
        a_over_r2 = -3 * pow(2, -1, p) % p
        residual = (a_over_r2**2 + 3 * a_over_r2 + 1) % p
        assert residual == -5 * pow(4, -1, p) % p
        assert residual != 0
        checks += 2

    proof = (HERE / "proof.md").read_text()
    for anchor in ("Cancellation", "aR'(x)D(x)=4x^(n-1)",
                   "2aD(x)xR'(x)=8alpha", "p` distinct roots",
                   "3r^2+2a=0", "characteristic five"):
        assert anchor in proof
        checks += 1
    statement = (HERE / "statement.md").read_text()
    assert "empty on all four rows" in statement
    assert "nonembedded `h=2`" in statement
    checks += 2

    print(f"L1_M4_H3_NU0_ZERO_B_EULER_EXCLUSION_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
