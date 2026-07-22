#!/usr/bin/env python3
"""Canonical Kronecker check for the Hankel coefficient plane."""

from __future__ import annotations


def mat_vec(matrix: list[list[int]], vector: list[int], prime: int) -> list[int]:
    return [sum(a * b for a, b in zip(row, vector)) % prime for row in matrix]


def pairing(
    left: list[int], matrix: list[list[int]], right: list[int], prime: int
) -> int:
    image = mat_vec(matrix, right, prime)
    return sum(a * b for a, b in zip(left, image)) % prime


def rank(matrix: list[list[int]], prime: int) -> int:
    work = [row[:] for row in matrix]
    rows = len(work)
    columns = len(work[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next((i for i in range(pivot_row, rows) if work[i][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][column], -1, prime)
        work[pivot_row] = [value * inverse % prime for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [
                (a - factor * b) % prime
                for a, b in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def main() -> None:
    prime = 101
    e = 2
    size = 2 * e + 2
    m_0 = [[0] * size for _ in range(size)]
    m_1 = [[0] * size for _ in range(size)]

    # Symmetric singular block [[0,L^T],[L,0]] with
    # L(z)=[[z,1,0],[0,z,1]], plus the regular block [z].
    for row in range(e):
        m_0[e + 1 + row][row + 1] = 1
        m_0[row + 1][e + 1 + row] = 1
        m_1[e + 1 + row][row] = 1
        m_1[row][e + 1 + row] = 1
    m_1[-1][-1] = 1

    coefficients = []
    for index in range(e + 1):
        vector = [0] * size
        vector[index] = -1 if index % 2 else 1
        coefficients.append([value % prime for value in vector])

    if rank(coefficients, prime) != e + 1:
        raise AssertionError("minimal-vector coefficients are dependent")
    for matrix in (m_0, m_1):
        for left in coefficients:
            for right in coefficients:
                if pairing(left, matrix, right, prime):
                    raise AssertionError("coefficient plane is not isotropic")

    v = [0] * size
    v[-1] = 1
    if rank(m_0, prime) != 2 * e or rank(m_1, prime) != 2 * e + 1:
        raise AssertionError("endpoint ranks are incorrect")
    if pairing(v, m_1, v, prime) == 0:
        raise AssertionError("transverse exceptional line was not detected")
    if mat_vec(m_1, coefficients[-1], prime) != [0] * size:
        raise AssertionError("top coefficient is not the infinity radical")

    print(
        "RATE_HALF_HANKEL_COEFFICIENT_BIISOTROPIC_PASS "
        f"prime={prime} e={e} plane_dimension={e+1}"
    )


if __name__ == "__main__":
    main()
