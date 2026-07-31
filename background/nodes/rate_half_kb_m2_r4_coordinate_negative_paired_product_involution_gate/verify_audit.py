#!/usr/bin/env python3
"""Independent audit of the paired-product involution identity."""


P = 29


def rank(matrix: list[list[int]]) -> int:
    work = [[value % P for value in row] for row in matrix]
    pivot_row = 0
    for column in range(3):
        pivot = next(
            (row for row in range(pivot_row, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][column], -1, P)
        work[pivot_row] = [value * inverse % P for value in work[pivot_row]]
        for row in range(len(work)):
            if row != pivot_row and work[row][column]:
                scale = work[row][column]
                work[row] = [
                    (left - scale * right) % P
                    for left, right in zip(work[row], work[pivot_row])
                ]
        pivot_row += 1
    return pivot_row


def main() -> None:
    values = (1, 4, 6, 9, 7, 5)
    a, b, c, d, e, f = values
    pairs = (
        (d * e, d * f), (-d * f, e * f), (-e * f, a * b),
        (a * c, -a * c), (b * c, -b * c), (a * d, b * e),
    )
    matrix = [[y * z, -(y + z), -1] for y, z in pairs]
    if rank(matrix) != 3:
        raise RuntimeError("fixture rank")

    alpha, beta, gamma = 3, 5, 7
    if (alpha * alpha + beta * gamma) % P == 0:
        raise RuntimeError("singular audit involution")
    sample_y = 2
    sample_z = (alpha * sample_y + beta) * pow(gamma * sample_y - alpha, -1, P) % P
    identity = gamma * sample_y * sample_z - alpha * (sample_y + sample_z) - beta
    if identity % P:
        raise RuntimeError("trace-zero identity")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_PAIRED_PRODUCT_AUDIT_PASS "
        f"fixture_rank=3 involution_sample={sample_y}/{sample_z}"
    )


if __name__ == "__main__":
    main()
