#!/usr/bin/env python3
"""Replay source-weight reconstruction on the exact F_17 route fence."""

from __future__ import annotations


P = 17


def inv(value: int) -> int:
    return pow(value % P, P - 2, P)


def locator(roots: tuple[int, ...], x: int) -> int:
    value = 1
    for root in roots:
        value = value * (x - root) % P
    return value


def moments(weights: dict[int, int], r: int) -> list[int]:
    return [
        sum(weight * pow(x, degree, P) for x, weight in weights.items()) % P
        for degree in range(2 * r + 1)
    ]


def rank(matrix: list[list[int]]) -> int:
    work = [row[:] for row in matrix]
    pivot = 0
    for col in range(len(work[0])):
        choice = next(
            (row for row in range(pivot, len(work)) if work[row][col] % P),
            None,
        )
        if choice is None:
            continue
        work[pivot], work[choice] = work[choice], work[pivot]
        scale = inv(work[pivot][col])
        work[pivot] = [(scale * value) % P for value in work[pivot]]
        for row in range(len(work)):
            if row == pivot:
                continue
            factor = work[row][col] % P
            if factor:
                work[row] = [
                    (left - factor * right) % P
                    for left, right in zip(work[row], work[pivot], strict=True)
                ]
        pivot += 1
    return pivot


def hankel(sequence: list[int], r: int) -> list[list[int]]:
    return [[sequence[i + j] for j in range(r + 1)] for i in range(r + 1)]


def det3(matrix: list[list[int]]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    ) % P


def adjugate4(matrix: list[list[int]]) -> list[list[int]]:
    out = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            minor = [
                [matrix[row][col] for col in range(4) if col != i]
                for row in range(4)
                if row != j
            ]
            out[i][j] = ((-1) ** (i + j) * det3(minor)) % P
    return out


def main() -> None:
    r = 3
    roots_a = (2, 5)
    triple = (3, 13, 15)
    pair = roots_a
    xi = 1
    lambda_i = 1
    theta_2 = 14
    external = {15: (4, 9, 11), 2: (6, 7, 10), 4: (8, 12, 16)}

    delta_0 = -xi % P
    alpha: dict[int, int] = {}
    beta: dict[int, int] = {}
    for a in pair:
        a_prime = locator(tuple(root for root in roots_a if root != a), a)
        b_value = locator(triple, a)
        quotient_value = 1  # A/D_1=1 when e=1.
        denominator = (
            delta_0
            * a_prime
            * b_value
            * b_value
            * (lambda_i * inv(xi) % P)
            * quotient_value
        ) % P
        k_a = theta_2 * inv(denominator) % P
        alpha[a] = k_a
        beta[a] = -xi * k_a % P

    omega: dict[int, int] = {}
    for t in triple:
        a_value = locator(roots_a, t)
        b_prime = locator(tuple(root for root in triple if root != t), t)
        omega[t] = theta_2 * inv(a_value * a_value * b_prime) % P

    assert alpha == {2: 9, 5: 8}
    assert beta == {2: 8, 5: 9}
    assert omega == {3: 12, 13: 2, 15: 1}

    h_0 = moments(beta, r)
    h_1 = moments(alpha | omega, r)
    assert h_0 == [0, 10, 2, 16, 7, 8, 3]
    assert h_1 == [15, 16, 6, 2, 14, 12, 1]

    # For e=1, Phi=1-z, L_1=1, and q_bar=1.
    for z, roots_g in external.items():
        phi = (1 - z) % P
        q_bar = 1
        circuit_scalar = theta_2 * phi * inv(q_bar) % P
        support = roots_a + triple + roots_g
        circuit = {
            x: circuit_scalar
            * inv(locator(tuple(y for y in support if y != x), x))
            % P
            for x in support
        }
        for a in roots_a:
            assert circuit[a] == (beta[a] + z * alpha[a]) % P
        for t in triple:
            assert circuit[t] == z * omega[t] % P

        # The circuit vanishes in all seven moment coordinates.
        assert moments(circuit, r) == [0] * (2 * r + 1)

    # Reconstructed moments annihilate q(z)=A+z(B-A) identically.
    a_coeff = [10, 10, 1, 0]
    q_1 = [0, 14, 2, 1]
    c_h = None
    for z in range(P):
        h_z = [(left + z * right) % P for left, right in zip(h_0, h_1, strict=True)]
        q_z = [(left + z * right) % P for left, right in zip(a_coeff, q_1, strict=True)]
        for row in range(r + 1):
            assert sum(q_z[col] * h_z[row + col] for col in range(r + 1)) % P == 0
        matrix = hankel(h_z, r)
        assert rank(matrix) == (r - 1 if z == 0 else r)
        adj = adjugate4(matrix)
        if z == 1:
            c_h = adj[0][0] * inv(q_z[0] * q_z[0]) % P
            assert c_h
        if z == 0:
            assert adj == [[0] * 4 for _ in range(4)]
        elif c_h is not None:
            expected = [
                [c_h * z * q_z[i] * q_z[j] % P for j in range(4)]
                for i in range(4)
            ]
            assert adj == expected
    assert c_h == 11

    m_1 = hankel(h_1, r)
    u = a_coeff
    v = [0, *a_coeff[:r]]
    pair = lambda left, right: sum(
        left[i] * m_1[i][j] * right[j]
        for i in range(r + 1)
        for j in range(r + 1)
    ) % P
    assert pair(u, u) == pair(v, u) == 0
    assert pair(v, v) == 14

    # Changing one internal scalar changes the forced source pencil.
    mutated_lambda = 2
    mutated_denominator = delta_0 * (mutated_lambda * inv(xi) % P) % P
    assert mutated_denominator != delta_0

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_"
        "DISTANCE_THREE_MDS_SOURCE_WEIGHT_RECONSTRUCTION_PASS "
        f"field={P} alpha={alpha} beta={beta} omega={omega} "
        f"external={len(external)} c_H={c_h}"
    )


if __name__ == "__main__":
    main()
