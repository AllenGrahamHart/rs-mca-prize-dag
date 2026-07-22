#!/usr/bin/env python3
"""Exact small-frame checks for split incidence and replication ledgers."""

from __future__ import annotations


def polynomial_from_roots(roots: tuple[int, ...], prime: int) -> list[int]:
    out = [1]
    for root in roots:
        next_out = [0] * (len(out) + 1)
        for index, value in enumerate(out):
            next_out[index] = (next_out[index] - root * value) % prime
            next_out[index + 1] = (next_out[index + 1] + value) % prime
        out = next_out
    return out


def rank(matrix: list[list[int]], prime: int) -> int:
    work = [row[:] for row in matrix]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(pivot_row, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][column], -1, prime)
        work[pivot_row] = [value * inverse % prime for value in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [
                (a - factor * b) % prime
                for a, b in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
    return pivot_row


def main() -> None:
    prime = 101
    e = 3
    blocks = ((1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12))
    columns = [polynomial_from_roots(block, prime) for block in blocks]
    generator = [[column[row] for column in columns] for row in range(e)]
    weights = [100, 5, 91, 10, 96, 1]
    replications = {
        slope: sum(slope in block for block in blocks)
        for slope in range(1, 4 * e + 1)
    }

    if any(len(set(block)) != e - 1 for block in blocks):
        raise AssertionError("a split incidence polynomial has repeated roots")
    if any(column[0] == 0 or column[-1] == 0 for column in columns):
        raise AssertionError("a split incidence polynomial lost an endpoint coefficient")
    if sorted(replications.values()) != [(e - 1) // 2] * (4 * e):
        raise AssertionError("flat replication ledger failed")
    if rank(generator, prime) != e:
        raise AssertionError("coefficient frame does not have full row rank")
    gram = [
        [
            sum(
                weights[k] * generator[i][k] * generator[j][k]
                for k in range(2 * e)
            ) % prime
            for j in range(e)
        ]
        for i in range(e)
    ]
    if any(weight == 0 for weight in weights) or any(
        value for row in gram for value in row
    ):
        raise AssertionError("flat frame is not weighted self-dual")

    swapped = dict(replications)
    swapped[1] += 1
    swapped[2] -= 1
    expected = [(e - 3) // 2, (e + 1) // 2] + [(e - 1) // 2] * (4 * e - 2)
    if sorted(swapped.values()) != sorted(expected):
        raise AssertionError("swapped replication ledger failed")

    print(
        "RATE_HALF_HANKEL_SPLIT_SELF_DUAL_FRAME_PASS "
        f"prime={prime} e={e} columns={len(columns)} rank={e} weights=nonzero"
    )


if __name__ == "__main__":
    main()
