#!/usr/bin/env python3
"""Finite-field replay for the distance-three MDS-escape router."""

from __future__ import annotations


P = 101


def inv(value: int) -> int:
    return pow(value % P, P - 2, P)


def evaluate(roots: tuple[int, ...], x: int) -> int:
    value = 1
    for root in roots:
        value = value * (x - root) % P
    return value


def column(x: int, r: int, length: int | None = None) -> list[int]:
    if length is None:
        length = 2 * r + 1
    return [pow(x, degree, P) for degree in range(length)]


def rank(columns: list[list[int]]) -> int:
    if not columns:
        return 0
    matrix = [list(row) for row in zip(*columns, strict=True)]
    rows = len(matrix)
    cols = len(columns)
    pivot = 0
    for col in range(cols):
        choice = next(
            (row for row in range(pivot, rows) if matrix[row][col] % P),
            None,
        )
        if choice is None:
            continue
        matrix[pivot], matrix[choice] = matrix[choice], matrix[pivot]
        scale = inv(matrix[pivot][col])
        matrix[pivot] = [(scale * value) % P for value in matrix[pivot]]
        for row in range(rows):
            if row == pivot:
                continue
            factor = matrix[row][col] % P
            if factor:
                matrix[row] = [
                    (left - factor * right) % P
                    for left, right in zip(matrix[row], matrix[pivot], strict=True)
                ]
        pivot += 1
    return pivot


def moments(weights: dict[int, int], r: int) -> list[int]:
    return [
        sum(weight * pow(x, degree, P) for x, weight in weights.items()) % P
        for degree in range(2 * r + 1)
    ]


def hankel_rank(sequence: list[int], r: int) -> int:
    columns = [
        [sequence[row + col] for row in range(r + 1)]
        for col in range(r + 1)
    ]
    return rank(columns)


def main() -> None:
    e = 2
    r = 2 * e + 1
    roots_a = (1, 2, 3, 4)
    triple = (5, 6, 7)
    roots_g = (8, 21, 23, 29, 40)
    support_s = roots_a + triple
    support_u = support_s + roots_g
    theta_2 = 17
    z_external = 3

    ratios = [
        evaluate(roots_g, t) * inv(evaluate(roots_a, t)) % P for t in triple
    ]
    assert ratios == [60, 60, 60]
    kappa = ratios[0]

    omega: dict[int, int] = {}
    for t in triple:
        omega[t] = theta_2 * inv(
            pow(evaluate(roots_a, t), 2, P)
            * evaluate(tuple(x for x in triple if x != t), t)
        ) % P

    circuit_scale = z_external * theta_2 * kappa % P
    circuit = {
        x: circuit_scale
        * inv(evaluate(tuple(y for y in support_u if y != x), x))
        % P
        for x in support_u
    }
    assert all(circuit.values())
    assert all(circuit[t] == z_external * omega[t] % P for t in triple)
    assert moments(circuit, r) == [0] * (2 * r + 1)

    zero_slope = {1: 1, 2: 1, 3: 2, 4: 2}
    alpha = {
        a: circuit[a] * inv(z_external - zero_slope[a]) % P for a in roots_a
    }
    beta = {a: -zero_slope[a] * alpha[a] % P for a in roots_a}
    assert all(beta.values())

    h_0 = moments(beta, r)
    h_1 = moments(alpha | omega, r)
    assert hankel_rank(h_0, r) == r - 1

    for z, deleted in ((1, {1, 2}), (2, {3, 4})):
        source = {
            a: (beta[a] + z * alpha[a]) % P
            for a in roots_a
            if (beta[a] + z * alpha[a]) % P
        }
        source.update({t: z * omega[t] % P for t in triple})
        assert len(source) == r
        assert set(source) == (set(roots_a) - deleted) | set(triple)
        h_z = [(left + z * right) % P for left, right in zip(h_0, h_1)]
        assert moments(source, r) == h_z
        assert hankel_rank(h_z, r) == r

    source_external = {
        a: (beta[a] + z_external * alpha[a]) % P for a in roots_a
    } | {t: z_external * omega[t] % P for t in triple}
    clean_external = {g: -circuit[g] % P for g in roots_g}
    h_external = [
        (left + z_external * right) % P for left, right in zip(h_0, h_1)
    ]
    assert source_external == {x: circuit[x] for x in support_s}
    assert moments(source_external, r) == moments(clean_external, r) == h_external
    assert hankel_rank(h_external, r) == r

    full_columns = [column(x, r) for x in support_u]
    assert len(support_u) == 2 * r + 2
    assert rank(full_columns) == 2 * r + 1
    for omitted in range(len(full_columns)):
        assert rank(full_columns[:omitted] + full_columns[omitted + 1 :]) == 2 * r + 1

    # Losing the last moment destroys the one-circuit boundary.
    short_columns = [column(x, r, 2 * r) for x in support_u]
    assert rank(short_columns) == 2 * r

    # The official count and outside-incidence budget force e + 3e exactly.
    for official_e in range(1, 33):
        official_r = 2 * official_e + 1
        outside = 6 * official_e + 4
        ordinary = 4 * official_e
        internal_cap = (official_r - 1) // 2
        external_floor = ordinary - internal_cap
        external_cap = outside * official_e // official_r
        assert internal_cap == official_e
        assert external_floor == external_cap == 3 * official_e
        assert outside * official_e - external_cap * official_r == official_e

    # Mutating one canonical triple weight breaks the external circuit.
    mutated_h_1 = h_1.copy()
    for degree in range(2 * r + 1):
        mutated_h_1[degree] = (mutated_h_1[degree] + pow(triple[0], degree, P)) % P
    mutated_external = [
        (left + z_external * right) % P
        for left, right in zip(h_0, mutated_h_1)
    ]
    assert mutated_external != moments(clean_external, r)

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_"
        "DISTANCE_THREE_MDS_ESCAPE_ROUTER_PASS "
        f"e={e} r={r} internal=2 external_gate={roots_g} kappa={kappa}"
    )


if __name__ == "__main__":
    main()
