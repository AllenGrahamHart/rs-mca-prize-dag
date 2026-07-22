#!/usr/bin/env python3
"""Independent audit of the Cartier missing-slot calculation."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def derivative(coefficients: list[int], p: int) -> list[int]:
    return [(index * coefficients[index]) % p
            for index in range(1, len(coefficients))]


def main() -> None:
    checks = 0
    for p in (7, 13, 31, 127):
        coefficients = [(index * index + 3) % p for index in range(4 * p + 2)]
        derived = derivative(coefficients, p)
        for multiple in range(1, 5):
            slot = multiple * p - 1
            assert derived[slot] == 0
            checks += 1

        choices = (p - 4, p - 1, 2, 5, 8)
        for nu, s in enumerate(choices):
            ell = 4 * (p + 1) - 3 * nu
            assert (s + ell) % p == 0
            top = s - 1 + 2 * (p - nu) + (4 - nu)
            assert (top + 1) % p == 0
            checks += 2

    proof = (HERE / "proof.md").read_text()
    for anchor in ("(X^sA)'", "3p-1", "2p-1", "p+4", "p-5"):
        assert anchor in proof
        checks += 1
    statement = (HERE / "statement.md").read_text()
    assert "nu in {0,1,2,3}" in statement
    assert "delta_A+delta_B<=deg H<=3-nu" in statement
    assert "does not exclude" in statement
    checks += 3
    print(f"L1_M4_H3_CARTIER_RESONANCE_REDUCTION_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
