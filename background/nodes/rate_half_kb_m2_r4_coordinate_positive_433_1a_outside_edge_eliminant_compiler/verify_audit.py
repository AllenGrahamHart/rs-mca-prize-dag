#!/usr/bin/env python3
"""Independent finite-field audit of the edge-eliminant identities."""

from pathlib import Path


PRIME = 101
NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def determinant(matrix):
    matrix = [[value % PRIME for value in row] for row in matrix]
    result = 1
    for column in range(len(matrix)):
        pivot = next((row for row in range(column, len(matrix))
                      if matrix[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            result = -result
        value = matrix[column][column]
        result = result * value % PRIME
        inverse = pow(value, PRIME - 2, PRIME)
        for entry in range(column, len(matrix)):
            matrix[column][entry] = matrix[column][entry] * inverse % PRIME
        for row in range(column + 1, len(matrix)):
            scale = matrix[row][column]
            for entry in range(column, len(matrix)):
                matrix[row][entry] = (
                    matrix[row][entry] - scale * matrix[column][entry]
                ) % PRIME
    return result % PRIME


def resultant(A, B, C, q):
    q0, q1, q2, q3, q4 = q
    return determinant([
        [A, B, C, 0, 0, 0],
        [0, A, B, C, 0, 0],
        [0, 0, A, B, C, 0],
        [0, 0, 0, A, B, C],
        [q4, q3, q2, q1, q0, 0],
        [0, q4, q3, q2, q1, q0],
    ])


def compact(A, B, C, q):
    q0, q1, q2, q3, q4 = q
    r1 = (
        q4 * (-B**3 + 2 * A * B * C)
        + q3 * A * (B**2 - A * C)
        - q2 * A**2 * B + q1 * A**3
    )
    r0 = (
        q4 * (-B**2 * C + A * C**2)
        + q3 * A * B * C - q2 * A**2 * C + q0 * A**3
    )
    return (A * r0**2 - B * r0 * r1 + C * r1**2) % PRIME


def evaluate(coefficients, value):
    return sum(coefficient * value**index
               for index, coefficient in enumerate(coefficients)) % PRIME


def main():
    checks = 0
    for seed in range(1, 41):
        A = seed % PRIME or 1
        B = (7 * seed + 3) % PRIME
        C = (11 * seed + 5) % PRIME
        q = tuple((seed * (index + 2) ** 2 + 3 * index + 1) % PRIME
                  for index in range(5))
        require(compact(A, B, C, q)
                == pow(A, 3, PRIME) * resultant(A, B, C, q) % PRIME,
                "generic norm/resultant identity")
        checks += 1

        linear_B = B or 1
        root = -C * pow(linear_B, PRIME - 2, PRIME) % PRIME
        q0, q1, q2, q3, q4 = q
        cleared = (
            q4 * C**4 - q3 * C**3 * linear_B
            + q2 * C**2 * linear_B**2
            - q1 * C * linear_B**3 + q0 * linear_B**4
        ) % PRIME
        require(cleared == pow(linear_B, 4, PRIME) * evaluate(q, root) % PRIME,
                "linear degree-drop identity")
        checks += 1

    statement = (NODE / "statement.md").read_text()
    audit = (NODE / "audit.md").read_text()
    for marker in ("C!=0", "distinct supported common products",
                   "heuristic guidance only"):
        require(marker in statement + audit, f"scope marker {marker}")
    print(f"positive 433-1a edge-eliminant audit verified checks={checks}")


if __name__ == "__main__":
    main()
