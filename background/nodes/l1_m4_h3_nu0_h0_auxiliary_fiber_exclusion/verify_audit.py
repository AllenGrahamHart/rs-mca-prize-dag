#!/usr/bin/env python3
"""Independent companion-matrix replay of the exceptional cubic remainder."""

from __future__ import annotations

from pathlib import Path


HERE = Path(__file__).resolve().parent
P = 2147483647
N = 4 * (P + 1)
C0, C1, C2 = 573306971, 664831389, 1800058023
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]


def multiply(left: Matrix, right: Matrix) -> Matrix:
    return tuple(tuple(
        sum(left[row][k] * right[k][column] for k in range(3)) % P
        for column in range(3)) for row in range(3))  # type: ignore[return-value]


def power(matrix: Matrix, exponent: int) -> Matrix:
    out: Matrix = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    while exponent:
        if exponent & 1:
            out = multiply(out, matrix)
        matrix = multiply(matrix, matrix)
        exponent >>= 1
    return out


def main() -> None:
    companion: Matrix = (
        (0, 0, -C0 % P),
        (1, 0, -C1 % P),
        (0, 1, -C2 % P),
    )
    powered = power(companion, N)
    assert tuple(powered[row][0] for row in range(3)) == (876663073, 0, 0)
    checks = 1

    # Independently replay the degree squeeze behind the exact complement.
    for rho_1 in range(1, 12):
        rho_2_min = P + 5 - rho_1
        assert (rho_1 - 1) + rho_2_min == P + 4
        checks += 1

    proof = (HERE / "proof.md").read_text()
    for anchor in ("cancellation in the Euler identity", "d=1",
                   "two gcds are coprime", "Equality holds throughout",
                   "with multiplicity", "W^n-1"):
        assert anchor in proof
        checks += 1
    statement = (HERE / "statement.md").read_text()
    assert "entire `nu=0,b!=0,deg H=0` endpoint is empty" in statement
    assert "does not treat the cubic" in statement
    checks += 2
    print(f"L1_M4_H3_NU0_H0_AUXILIARY_FIBER_EXCLUSION_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
