#!/usr/bin/env python3
"""Independent Sylvester-minor and interpolation audit."""

from __future__ import annotations

from pathlib import Path


P = 8191
DEGREE_BOUND = 160


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % P == 0:
        poly.pop()
    return [value % P for value in poly]


def add(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    return trim(out)


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([(scalar * value) % P for value in poly])


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % P
    return trim(out)


def divide(dividend: list[int], divisor: list[int]) -> tuple[list[int], list[int]]:
    remainder = trim(dividend[:])
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, P)
    while len(remainder) >= len(divisor) and any(remainder):
        shift = len(remainder) - len(divisor)
        coefficient = remainder[-1] * inverse % P
        quotient[shift] = coefficient
        for i, value in enumerate(divisor):
            remainder[i + shift] = (remainder[i + shift] - coefficient * value) % P
        trim(remainder)
    return trim(quotient), trim(remainder)


def monic(poly: list[int]) -> list[int]:
    return scale(poly, pow(poly[-1], -1, P))


def gcd(left: list[int], right: list[int]) -> list[int]:
    left, right = trim(left), trim(right)
    while any(right):
        _, remainder = divide(left, right)
        left, right = right, remainder
    return monic(left)


def determinant(matrix: list[list[int]]) -> int:
    matrix = [[value % P for value in row] for row in matrix]
    result = 1
    for column in range(len(matrix)):
        pivot = next((row for row in range(column, len(matrix)) if matrix[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            result = -result
        value = matrix[column][column]
        result = result * value % P
        inverse = pow(value, -1, P)
        for row in range(column + 1, len(matrix)):
            if not matrix[row][column]:
                continue
            factor = matrix[row][column] * inverse % P
            for entry in range(column, len(matrix)):
                matrix[row][entry] = (matrix[row][entry] - factor * matrix[column][entry]) % P
    return result % P


def locator_parts(s: int) -> tuple[list[int], list[int]]:
    b = [1]
    for r in range(1, 16):
        b.append(b[-1] * (s + r - 1) * pow(r, -1, P) % P)

    odd = [0] * 8
    even = [0] * 8
    for r in range(0, 15, 2):
        odd[(14 - r) // 2] = b[r]
    for r in range(1, 16, 2):
        even[(15 - r) // 2] = b[r]
    reduced_even = [(even[i] - s * odd[i]) % P for i in range(8)]
    return odd, reduced_even


def shifted_row(poly: list[int], shift: int) -> list[int]:
    row = [0] * 12
    for exponent, coefficient in enumerate(poly):
        degree = exponent + shift
        row[11 - degree] = coefficient
    return row


def first_subresultant_minors(s: int) -> tuple[int, int]:
    odd, reduced_even = locator_parts(s)
    rows = [shifted_row(odd, shift) for shift in range(5)]
    rows += [shifted_row(reduced_even, shift) for shift in range(6)]
    assert len(rows) == 11 and all(len(row) == 12 for row in rows)

    # Deleting the degree-one and degree-zero columns gives -c0 and -c1.
    minors = []
    for deleted in (10, 11):
        square = [[value for column, value in enumerate(row) if column != deleted] for row in rows]
        minors.append(determinant(square))
    return minors[0], minors[1]


def interpolate_consecutive(values: list[int]) -> list[int]:
    """Newton interpolation at 0,1,... in the monomial basis."""

    differences = [value % P for value in values]
    basis = [1]
    result = [0]
    factorial = 1
    for degree in range(len(values)):
        coefficient = differences[0] * pow(factorial, -1, P) % P
        result = add(result, scale(basis, coefficient))
        differences = [
            (differences[i + 1] - differences[i]) % P
            for i in range(len(differences) - 1)
        ]
        basis = multiply(basis, [(-degree) % P, 1])
        factorial = factorial * (degree + 1) % P
    return trim(result)


def expected_factor() -> list[int]:
    result = [1]
    roots = {
        0: 6,
        3: 1,
        2: 1,
        1: 6,
        -1: 6,
        -2: 5,
        -3: 5,
        -4: 4,
        -5: 4,
        -6: 3,
        -7: 3,
        -8: 2,
        -9: 2,
        -10: 1,
        -11: 1,
    }
    for root, multiplicity in roots.items():
        for _ in range(multiplicity):
            result = multiply(result, [(-root) % P, 1])
    return monic(result)


def main() -> None:
    assert first_subresultant_minors(123) == (159, 5645)
    values = [first_subresultant_minors(s) for s in range(DEGREE_BOUND + 1)]
    c0 = interpolate_consecutive([value[0] for value in values])
    c1 = interpolate_consecutive([value[1] for value in values])
    assert len(c0) - 1 == 80
    assert len(c1) - 1 == 78

    common = gcd(c0, c1)
    expected = expected_factor()
    assert len(common) - 1 == 50
    assert common == expected

    proof = Path(__file__).with_name("proof.md").read_text()
    audit = Path(__file__).with_name("audit.md").read_text()
    assert "5*14+6*15=160" in proof
    assert "stdlib" in audit

    wrong_values = [value[0] for value in values]
    wrong_values[100] = (wrong_values[100] + 1) % P
    assert interpolate_consecutive(wrong_values) != c0

    print(
        "L1_MERSENNE_HNF_M16_ORDER_ZERO_EVEN_QUADRATIC_EXCLUSION_AUDIT_PASS "
        "samples=161 determinants=322 degrees=80,78 gcd_degree=50 mutations=1"
    )


if __name__ == "__main__":
    main()
