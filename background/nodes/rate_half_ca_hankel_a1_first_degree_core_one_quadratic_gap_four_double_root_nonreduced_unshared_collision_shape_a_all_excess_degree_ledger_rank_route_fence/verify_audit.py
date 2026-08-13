#!/usr/bin/env python3
"""Independent algebraic audit of the F_211 degree-ledger fence."""

P = 211


def rank_mod(matrix):
    work = [row[:] for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = pow(work[rank][column], -1, P)
        work[rank] = [entry * scale % P for entry in work[rank]]
        for row in range(len(work)):
            if row != rank and work[row][column]:
                factor = work[row][column]
                work[row] = [
                    (left - factor * right) % P
                    for left, right in zip(work[row], work[rank])
                ]
        rank += 1
    return rank


def polynomial_from_roots(roots):
    answer = [1]
    for root in roots:
        following = [0] * (len(answer) + 1)
        for index, coefficient in enumerate(answer):
            following[index] = (following[index] - root * coefficient) % P
            following[index + 1] = (
                following[index + 1] + coefficient
            ) % P
        answer = following
    return answer


def main():
    values = {pow(2, 35 * index, P) for index in range(4)}
    xs = [x for x in range(1, P) if pow(x, 7, P) in values]
    ts = [0] + [t for t in range(1, P) if pow(t, 5, P) in values]
    assert len(xs) == 28 and len(ts) == 21

    roots_by_t = [
        [x for x in xs if pow(t, 5, P) == pow(x, 7, P)]
        for t in ts
    ]
    assert [len(roots) for roots in roots_by_t] == [0] + [7] * 20
    assert all(
        sum(pow(t, 5, P) == pow(x, 7, P) for t in ts) == 5
        for x in xs
    )

    weights = []
    for index, t in enumerate(ts):
        derivative = 1
        for other_index, other in enumerate(ts):
            if index != other_index:
                derivative = derivative * (t - other) % P
        weights.append(pow(derivative, -1, P))

    columns = [(0, degree) for degree in range(8)] + [
        (index, 0) for index in range(1, 21)
    ]
    known = [polynomial_from_roots(roots) for roots in roots_by_t]
    matrix = []
    for x_degree in range(8):
        for t_power in range(15):
            row = []
            for t_index, residual_degree in columns:
                known_degree = x_degree - residual_degree
                coefficient = (
                    known[t_index][known_degree]
                    if 0 <= known_degree < len(known[t_index])
                    else 0
                )
                row.append(
                    coefficient
                    * pow(ts[t_index], t_power, P)
                    * weights[t_index]
                    % P
                )
            matrix.append(row)

    kernel = [0] * 28
    kernel[7] = -1 % P
    for index in range(8, 28):
        kernel[index] = -1 % P
    assert all(
        sum(a * b for a, b in zip(row, kernel)) % P == 0
        for row in matrix
    )
    assert rank_mod(matrix) == 27

    checks = 28 * 21 + 21 + 120 + 1
    print(
        "RATE_HALF_SHAPE_A_ALL_EXCESS_DEGREE_LEDGER_RANK_FENCE_AUDIT_PASS "
        f"checks={checks} rank=27 kernel_blocks=21"
    )


if __name__ == "__main__":
    main()
