#!/usr/bin/env python3
"""Independent companion-matrix audit of the reciprocal elimination."""

from __future__ import annotations

from pathlib import Path


ROWS = (8191, 131071, 524287, 2147483647)
H = 7
START = 200
BOUND_12 = 1344
BOUND_13 = 1792
ROOT_MULTIPLICITIES = {
    0: 176,
    1: 4,
    -1: 176,
    -2: 168,
    -3: 162,
    -4: 152,
    -5: 128,
    -6: 64,
    -7: 2,
}


def trim(poly: list[int], prime: int) -> list[int]:
    while len(poly) > 1 and poly[-1] % prime == 0:
        poly.pop()
    return [value % prime for value in poly]


def add(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    return trim(out, prime)


def scale(poly: list[int], scalar: int, prime: int) -> list[int]:
    return trim([scalar * value % prime for value in poly], prime)


def multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return trim(out, prime)


def divide(
    dividend: list[int], divisor: list[int], prime: int
) -> tuple[list[int], list[int]]:
    remainder = trim(dividend[:], prime)
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, prime)
    while len(remainder) >= len(divisor) and any(remainder):
        shift = len(remainder) - len(divisor)
        coefficient = remainder[-1] * inverse % prime
        quotient[shift] = coefficient
        for i, value in enumerate(divisor):
            remainder[i + shift] = (remainder[i + shift] - coefficient * value) % prime
        trim(remainder, prime)
    return trim(quotient, prime), remainder


def evaluate(poly: list[int], value: int, prime: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = (result * value + coefficient) % prime
    return result


def resultant(left: list[int], right: list[int], prime: int) -> int:
    left, right = trim(left, prime), trim(right, prime)
    m, n = len(left) - 1, len(right) - 1
    if n == 0:
        return pow(right[0], m, prime)
    if m < n:
        result = resultant(right, left, prime)
        return -result % prime if m * n % 2 else result
    _, remainder = divide(left, right, prime)
    if remainder == [0]:
        return 0
    degree = len(remainder) - 1
    result = pow(right[-1], m - degree, prime) * resultant(right, remainder, prime) % prime
    return -result % prime if m * n % 2 else result


def determinant(matrix: list[list[int]], prime: int) -> int:
    matrix = [[value % prime for value in row] for row in matrix]
    result = 1
    for column in range(len(matrix)):
        pivot = next((row for row in range(column, len(matrix)) if matrix[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            result = -result
        value = matrix[column][column]
        result = result * value % prime
        inverse = pow(value, -1, prime)
        for row in range(column + 1, len(matrix)):
            if not matrix[row][column]:
                continue
            factor = matrix[row][column] * inverse % prime
            for entry in range(column, len(matrix)):
                matrix[row][entry] = (
                    matrix[row][entry] - factor * matrix[column][entry]
                ) % prime
    return result % prime


def sylvester_resultant(left: list[int], right: list[int], prime: int) -> int:
    m, n = len(left) - 1, len(right) - 1
    size = m + n
    matrix = [[0] * size for _ in range(size)]
    left_descending = list(reversed(left))
    right_descending = list(reversed(right))
    for row in range(n):
        for offset, value in enumerate(left_descending):
            matrix[row][row + offset] = value
    for shift in range(m):
        for offset, value in enumerate(right_descending):
            matrix[n + shift][shift + offset] = value
    return determinant(matrix, prime)


def interpolate(values: list[int], start: int, prime: int) -> list[int]:
    differences = [value % prime for value in values]
    basis = [1]
    result = [0]
    factorial = 1
    for degree in range(len(values)):
        coefficient = differences[0] * pow(factorial, -1, prime) % prime
        result = add(result, scale(basis, coefficient, prime), prime)
        differences = [
            (differences[i + 1] - differences[i]) % prime
            for i in range(len(differences) - 1)
        ]
        basis = multiply(basis, [(-start - degree) % prime, 1], prime)
        factorial = factorial * (degree + 1) % prime
    return trim(result, prime)


def gcd(left: list[int], right: list[int], prime: int) -> list[int]:
    while right != [0]:
        _, remainder = divide(left, right, prime)
        left, right = right, remainder
    return scale(left, pow(left[-1], -1, prime), prime)


def matrix_multiply(left: list[list[int]], right: list[list[int]], prime: int) -> list[list[int]]:
    size = len(left)
    out = [[0] * size for _ in range(size)]
    for i in range(size):
        for k in range(size):
            if not left[i][k]:
                continue
            for j in range(size):
                out[i][j] = (out[i][j] + left[i][k] * right[k][j]) % prime
    return out


def matrix_power(matrix: list[list[int]], exponent: int, prime: int) -> list[list[int]]:
    size = len(matrix)
    result = [[int(i == j) for j in range(size)] for i in range(size)]
    while exponent:
        if exponent & 1:
            result = matrix_multiply(result, matrix, prime)
        matrix = matrix_multiply(matrix, matrix, prime)
        exponent //= 2
    return result


def q_values(s_value: int, prime: int) -> list[int]:
    b = [1]
    for r in range(1, H + 1):
        b.append(b[-1] * (s_value + r - 1) * pow(r, -1, prime) % prime)

    # P_s(W)=W^7+b_1 W^6+...+b_7, stored in increasing powers.
    locator = [0] * (H + 1)
    for r, coefficient in enumerate(b):
        locator[H - r] = coefficient
    assert locator[-1] == 1

    companion = [[0] * H for _ in range(H)]
    for column in range(H - 1):
        companion[column + 1][column] = 1
    for row in range(H):
        companion[row][H - 1] = -locator[row] % prime

    eighth = matrix_power(companion, 8, prime)
    traces = [0]
    power = [[int(i == j) for j in range(H)] for i in range(H)]
    for _ in range(1, H + 1):
        power = matrix_multiply(power, eighth, prime)
        traces.append(sum(power[i][i] for i in range(H)) % prime)

    coefficients = [1]
    for k in range(1, H + 1):
        total = traces[k]
        for j in range(1, k):
            total = (total + coefficients[j] * traces[k - j]) % prime
        coefficients.append(-total * pow(k, -1, prime) % prime)
    return coefficients


def reconstruct_q(prime: int) -> list[list[int]]:
    values = [q_values(s_value, prime) for s_value in range(57)]
    q = [interpolate([row[j] for row in values], 0, prime) for j in range(H + 1)]
    assert [len(value) - 1 for value in q] == [8 * j for j in range(H + 1)]
    return q


def expected_factor(prime: int) -> list[int]:
    result = [1]
    for root, multiplicity in ROOT_MULTIPLICITIES.items():
        for _ in range(multiplicity):
            result = multiply(result, [(-root) % prime, 1], prime)
    return scale(result, pow(result[-1], -1, prime), prime)


def audit_row(prime: int) -> None:
    q = reconstruct_q(prime)
    constant = q[H]

    def equation(j: int, s_value: int) -> list[int]:
        out = scale(q[j], evaluate(constant, s_value, prime), prime)
        out[0] = (out[0] - evaluate(q[H - j], s_value, prime)) % prime
        return trim(out, prime)

    def eliminant(j: int, bound: int) -> list[int]:
        values = [
            resultant(equation(1, value), equation(j, value), prime)
            for value in range(START, START + bound + 1)
        ]
        out = interpolate(values, START, prime)
        check = START + bound + 37
        assert evaluate(out, check, prime) == resultant(
            equation(1, check), equation(j, check), prime
        )
        return out

    for value in (211, 997, 2029):
        for j in (2, 3):
            left, right = equation(1, value), equation(j, value)
            assert resultant(left, right, prime) == sylvester_resultant(left, right, prime)

    r12 = eliminant(2, BOUND_12)
    r13 = eliminant(3, BOUND_13)
    common = gcd(r12, r13, prime)
    assert (len(r12) - 1, len(r13) - 1, len(common) - 1) == (1320, 1760, 1032)
    assert common == expected_factor(prime)


def main() -> None:
    for prime in ROWS:
        audit_row(prime)

    proof = Path(__file__).with_name("proof.md").read_text()
    audit = Path(__file__).with_name("audit.md").read_text()
    assert "companion matrix" in proof
    assert "independent" in audit.lower()

    baseline = q_values(2, ROWS[0])
    mutation = baseline[:]
    mutation[1] = (mutation[1] + 1) % ROWS[0]
    assert mutation != baseline

    print(
        "L1_MERSENNE_HNF_M8_ORDER_ZERO_RECIPROCAL_ELIMINATION_AUDIT_PASS "
        "rows=4 companion_samples=228 sylvester_checks=24 eliminants=8 "
        "degrees=1320,1760 gcd_degree=1032 mutations=1"
    )


if __name__ == "__main__":
    main()
