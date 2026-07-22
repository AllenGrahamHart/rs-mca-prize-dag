#!/usr/bin/env python3
"""Independent multiplication-matrix audit of the zero-b quarter table."""

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
    return x[0] * scalar % p, -x[1] * scalar % p


def matrix_mul(left: Matrix, right: Matrix, p: int) -> Matrix:
    return tuple(tuple(
        add(mul(left[row][0], right[0][column], p),
            mul(left[row][1], right[1][column], p), p)
        for column in range(2)) for row in range(2))  # type: ignore[return-value]


def matrix_pow(matrix: Matrix, exponent: int, p: int) -> Matrix:
    zero, one = (0, 0), (1, 0)
    out: Matrix = ((one, zero), (zero, one))
    while exponent:
        if exponent & 1:
            out = matrix_mul(out, matrix, p)
        matrix = matrix_mul(matrix, matrix, p)
        exponent >>= 1
    return out


def remainder(matrix: Matrix, exponent: int, target: Fp2,
              p: int) -> tuple[Fp2, Fp2]:
    powered = matrix_pow(matrix, exponent, p)
    return add(powered[0][0], neg(target, p), p), powered[1][0]


def evaluate_q(x: Fp2, coefficient: Fp2,
               constant: Fp2, p: int) -> Fp2:
    return add(add(mul(x, x, p), mul(coefficient, x, p), p), constant, p)


def common_status(first: tuple[Fp2, Fp2], second: tuple[Fp2, Fp2],
                  coefficient: Fp2, constant: Fp2,
                  p: int) -> tuple[str, Fp2 | None]:
    zero = (0, 0)
    if first == (zero, zero) and second == (zero, zero):
        return "ALL", None
    for constant_part, linear_part in (first, second):
        if linear_part == zero and constant_part != zero:
            return "NONE", None
    selected = first if first[1] != zero else second
    root = mul(neg(selected[0], p), inverse(selected[1], p), p)
    if evaluate_q(root, coefficient, constant, p) != zero:
        return "NONE", None
    for constant_part, linear_part in (first, second):
        if add(constant_part, mul(linear_part, root, p), p) != zero:
            return "NONE", None
    return "POINT", root


def statuses(p: int) -> dict[tuple[Fp2, Fp2], tuple[str, Fp2 | None]]:
    zero, one = (0, 0), (1, 0)
    quarters = (one, (-1 % p, 0), (0, 1), (0, -1 % p))
    out = {}
    for epsilon in quarters:
        for eta in quarters:
            coefficient = mul(
                add(add(eta, neg(epsilon, p), p), (-4 % p, 0), p),
                (pow(2, -1, p), 0), p)
            u: Matrix = ((zero, neg(epsilon, p)),
                         (one, neg(coefficient, p)))
            two_identity: Matrix = (((2, 0), zero), (zero, (2, 0)))
            v: Matrix = tuple(tuple(
                add(two_identity[row][column], neg(u[row][column], p), p)
                for column in range(2)) for row in range(2))  # type: ignore[assignment]
            first = remainder(u, p + 1, epsilon, p)
            second = remainder(v, p + 1, eta, p)
            out[(epsilon, eta)] = common_status(
                first, second, coefficient, epsilon, p
            )
    return out


def main() -> None:
    checks = 0
    for p in (8191, 131071, 524287, 2147483647):
        table = statuses(p)
        nonempty = {key for key, (kind, _) in table.items() if kind != "NONE"}
        expected_all = set() if p in (8191, 131071) else {
            ((1, 0), (-1 % p, 0)), ((-1 % p, 0), (1, 0))
        }
        degenerate = ((1, 0), (1, 0))
        assert nonempty == expected_all | {degenerate}
        assert table[degenerate] == ("POINT", (1, 0))
        assert {key for key, (kind, _) in table.items() if kind == "ALL"} == expected_all
        checks += 3

    proof = (HERE / "proof.md").read_text()
    for anchor in ("root products", "u+v=2", "all 16 pairs",
                   "z^2+z-1", "clearing `r^4`"):
        assert anchor in proof
        checks += 1
    statement = (HERE / "statement.md").read_text()
    assert "no nu=0,b=0 record" in statement
    assert "does not exclude the latter" in statement
    checks += 2
    print(f"L1_M4_H3_NU0_ZERO_B_VALUE_COSET_CERTIFICATE_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
