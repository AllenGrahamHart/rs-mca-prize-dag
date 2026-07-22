#!/usr/bin/env python3
"""Independent multiplication-matrix audit of the value-coset certificate."""

from __future__ import annotations

from pathlib import Path


HERE = Path(__file__).resolve().parent
Fp2 = tuple[int, int]
Matrix = tuple[tuple[Fp2, Fp2], tuple[Fp2, Fp2]]


def add(x: Fp2, y: Fp2, p: int) -> Fp2:
    return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)


def neg(x: Fp2, p: int) -> Fp2:
    return (-x[0] % p, -x[1] % p)


def mul(x: Fp2, y: Fp2, p: int) -> Fp2:
    return ((x[0] * y[0] - x[1] * y[1]) % p,
            (x[0] * y[1] + x[1] * y[0]) % p)


def inverse(x: Fp2, p: int) -> Fp2:
    norm = (x[0] * x[0] + x[1] * x[1]) % p
    assert norm
    scalar = pow(norm, -1, p)
    return (x[0] * scalar % p, -x[1] * scalar % p)


def matrix_mul(left: Matrix, right: Matrix, p: int) -> Matrix:
    rows = []
    for row in range(2):
        values = []
        for column in range(2):
            value = (0, 0)
            for inner in range(2):
                value = add(value, mul(left[row][inner], right[inner][column], p), p)
            values.append(value)
        rows.append(tuple(values))
    return tuple(rows)  # type: ignore[return-value]


def matrix_pow(matrix: Matrix, exponent: int, p: int) -> Matrix:
    zero, one = (0, 0), (1, 0)
    output: Matrix = ((one, zero), (zero, one))
    while exponent:
        if exponent & 1:
            output = matrix_mul(output, matrix, p)
        matrix = matrix_mul(matrix, matrix, p)
        exponent >>= 1
    return output


def remainder(matrix: Matrix, exponent: int, target: Fp2, p: int) -> tuple[Fp2, Fp2]:
    powered = matrix_pow(matrix, exponent, p)
    return add(powered[0][0], neg(target, p), p), powered[1][0]


def evaluate_q(x: Fp2, coefficient: Fp2, constant: Fp2, p: int) -> Fp2:
    return add(add(mul(x, x, p), mul(coefficient, x, p), p), constant, p)


def common_status(first: tuple[Fp2, Fp2], second: tuple[Fp2, Fp2],
                  coefficient: Fp2, constant: Fp2, p: int) -> str:
    zero = (0, 0)
    if first == (zero, zero) and second == (zero, zero):
        return "ALL"
    for remainder_value in (first, second):
        if remainder_value[1] == zero and remainder_value[0] != zero:
            return "NONE"
    selected = first if first[1] != zero else second
    root = mul(neg(selected[0], p), inverse(selected[1], p), p)
    if evaluate_q(root, coefficient, constant, p) != zero:
        return "NONE"
    for constant_part, linear_part in (first, second):
        if add(constant_part, mul(linear_part, root, p), p) != zero:
            return "NONE"
    return "POINT"


def classify(p: int, epsilon: Fp2, eta: Fp2) -> str:
    zero, one = (0, 0), (1, 0)
    coefficient = add(add(one, epsilon, p), neg(eta, p), p)
    # Multiplication by u in the basis (1,u), where u^2=-coefficient*u-epsilon.
    u_matrix: Matrix = ((zero, neg(epsilon, p)),
                        (one, neg(coefficient, p)))
    minus_identity: Matrix = ((neg(one, p), zero), (zero, neg(one, p)))
    v_matrix: Matrix = tuple(
        tuple(add(minus_identity[row][column], neg(u_matrix[row][column], p), p)
              for column in range(2))
        for row in range(2)
    )  # type: ignore[assignment]
    first = remainder(u_matrix, p + 1, epsilon, p)
    second = remainder(v_matrix, p + 1, eta, p)
    return common_status(first, second, coefficient, epsilon, p)


def main() -> None:
    checks = 0
    expected = {
        8191: set(),
        131071: set(),
        524287: {(1, -1), (-1, 1), (-1, -1)},
        2147483647: {(1, -1), (-1, 1), (-1, -1)},
    }
    for p, expected_pairs in expected.items():
        quarters = ((1, 0), (-1 % p, 0), (0, 1), (0, -1 % p))
        pairs = set()
        for epsilon in quarters:
            for eta in quarters:
                status = classify(p, epsilon, eta)
                if status != "NONE":
                    assert status == "ALL"
                    signed_epsilon = -1 if epsilon == (-1 % p, 0) else 1
                    signed_eta = -1 if eta == (-1 % p, 0) else 1
                    assert epsilon[1] == eta[1] == 0
                    pairs.add((signed_epsilon, signed_eta))
                checks += 1
        assert pairs == expected_pairs
        checks += 1

    proof = (HERE / "proof.md").read_text()
    for anchor in ("product of its `p` roots", "w^p=w^(N-1)",
                   "for each `epsilon,eta", "Y^3-2s^2Y+s^3",
                   "a^3+8b^2=0"):
        assert anchor in proof
        checks += 1
    statement = (HERE / "statement.md").read_text()
    assert "no positive-valuation" in statement
    assert "does not exclude `nu=0`" in statement
    checks += 2
    print(f"L1_M4_POSITIVE_VALUE_COSET_CERTIFICATE_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
