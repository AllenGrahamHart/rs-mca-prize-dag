#!/usr/bin/env python3
"""Arithmetic and finite Vandermonde checks for minimal-support uniqueness."""


def matrix_rank(matrix, p):
    work = [[value % p for value in row] for row in matrix]
    rank = 0
    columns = len(work[0]) if work else 0
    for column in range(columns):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], -1, p)
        work[rank] = [value * inverse % p for value in work[rank]]
        for row in range(len(work)):
            if row == rank or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [
                (x - factor * y) % p for x, y in zip(work[row], work[rank])
            ]
        rank += 1
        if rank == len(work):
            break
    return rank


def vandermonde(points, rows, p):
    return [[pow(point, exponent, p) for point in points] for exponent in range(rows)]


def check_official_arithmetic():
    e = 2**38 - 1
    r = 2 * e + 1
    assert r - 1 == 2 * e
    assert e + 1 == 274877906944
    assert 2 * e // 3 + 3 == 183251937965
    assert 3 * (e + 1) // 2 == 412316860416
    assert (r - 1) + 2 * (e + 1) == 2 * r
    assert (r - 1) + 2 * (e + 2) == 2 * r + 2


def check_vandermonde_threshold():
    p = 101
    e = 3
    r = 2 * e + 1
    rows = 2 * r + 1
    root_support = [1, 2, 3, 4, 5, 6]
    leader = [7, 8, 9, 10]
    other = [11, 12, 13, 14]
    union = root_support + leader + other
    assert len(union) == (r - 1) + 2 * (e + 1)
    assert len(union) <= rows
    assert matrix_rank(vandermonde(union, rows, p), p) == len(union)

    # One step beyond the theorem can exceed the guaranteed column budget.
    beyond_size = (r - 1) + 2 * (e + 2)
    assert beyond_size > rows


def check_mutation_caught():
    e = 3
    r = 2 * e + 1
    correct = (r - 1) + 2 * (e + 1)
    mutated = (r - 1) + 2 * (e + 2)
    assert correct <= 2 * r + 1
    assert mutated > 2 * r + 1


def main():
    check_official_arithmetic()
    check_vandermonde_threshold()
    check_mutation_caught()
    print("PASS exceptional quotient minimal-support uniqueness")


if __name__ == "__main__":
    main()
