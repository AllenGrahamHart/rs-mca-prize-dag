#!/usr/bin/env python3
"""Finite replay and exact XR arithmetic for the post-strip pencil charge."""

from __future__ import annotations

from itertools import combinations, product
from math import comb


Vector = tuple[int, ...]


def rank(rows: list[Vector], prime: int) -> int:
    matrix = [list(row) for row in rows]
    if not matrix:
        return 0
    pivot = 0
    for column in range(len(matrix[0])):
        choice = next(
            (row for row in range(pivot, len(matrix)) if matrix[row][column] % prime),
            None,
        )
        if choice is None:
            continue
        matrix[pivot], matrix[choice] = matrix[choice], matrix[pivot]
        inverse = pow(matrix[pivot][column], prime - 2, prime)
        matrix[pivot] = [value * inverse % prime for value in matrix[pivot]]
        for row in range(len(matrix)):
            if row == pivot:
                continue
            factor = matrix[row][column] % prime
            if factor:
                matrix[row] = [
                    (left - factor * right) % prime
                    for left, right in zip(matrix[row], matrix[pivot], strict=True)
                ]
        pivot += 1
        if pivot == len(matrix):
            break
    return pivot


def affine_rank(vectors: list[Vector], prime: int) -> int:
    origin = vectors[0]
    return rank(
        [
            tuple((x - y) % prime for x, y in zip(vector, origin, strict=True))
            for vector in vectors[1:]
        ],
        prime,
    )


def add(left: Vector, right: Vector, prime: int) -> Vector:
    return tuple((x + y) % prime for x, y in zip(left, right, strict=True))


def scale(value: int, vector: Vector, prime: int) -> Vector:
    return tuple(value * coordinate % prime for coordinate in vector)


def parity(vector: Vector, prime: int) -> Vector:
    return tuple((vector[index] - vector[0]) % prime for index in range(1, 4))


def in_support_image(target: Vector, support: tuple[int, ...], prime: int) -> bool:
    columns = []
    for coordinate in support:
        basis = tuple(1 if index == coordinate else 0 for index in range(4))
        columns.append(parity(basis, prime))
    return rank(columns + [target], prime) == rank(columns, prime)


def core_cap_exhaustion() -> tuple[int, int]:
    checked = 0
    mutations = 0
    for length in range(4, 45):
        for dimension in range(1, length):
            redundancy = length - dimension
            for reserve in range(1, redundancy + 1):
                for kernel_rank in range(min(dimension, dimension + reserve - 1) + 1):
                    for core_cap in range(kernel_rank, dimension + 1):
                        pencil_cap = (length - core_cap) // (
                            dimension + reserve - core_cap
                        )
                        for persistent in range(core_cap - kernel_rank + 1):
                            direct = (length - kernel_rank - persistent) // (
                                dimension + reserve - kernel_rank - persistent
                            )
                            if direct > pencil_cap:
                                raise AssertionError(
                                    (
                                        length,
                                        dimension,
                                        reserve,
                                        kernel_rank,
                                        core_cap,
                                        persistent,
                                        direct,
                                        pencil_cap,
                                    )
                                )
                            checked += 1
                        if core_cap < dimension:
                            escaped = core_cap - kernel_rank + 1
                            if (
                                length - kernel_rank - escaped
                            ) // (
                                dimension + reserve - kernel_rank - escaped
                            ) > pencil_cap:
                                mutations += 1
    if mutations == 0:
        raise AssertionError("dropping the core cap did not fire a mutation")
    return checked, mutations


def exhaustive_small_selectors() -> tuple[int, int]:
    prime, length, dimension, redundancy, reserve = 3, 4, 1, 3, 1
    radius = redundancy - reserve
    vectors = tuple(product(range(prime), repeat=length))
    syndromes = tuple(product(range(prime), repeat=length - 1))
    families = 0
    selectors = 0
    for y0 in syndromes:
        for y1 in syndromes:
            if not any(y1):
                continue
            pairs = []
            for gamma in range(prime):
                target = add(y0, scale(gamma, y1, prime), prime)
                for error in vectors:
                    support = tuple(index for index, value in enumerate(error) if value)
                    if len(support) > radius or parity(error, prime) != target:
                        continue
                    if in_support_image(y0, support, prime) and in_support_image(
                        y1, support, prime
                    ):
                        continue
                    pairs.append((gamma, error))
            if len({gamma for gamma, _ in pairs}) < 2:
                continue
            families += 1
            for size in range(2, len(pairs) + 1):
                for chosen in combinations(pairs, size):
                    if len({gamma for gamma, _ in chosen}) != size:
                        continue
                    zero_sets = [
                        {index for index, value in enumerate(error) if value == 0}
                        for _, error in chosen
                    ]
                    core_cap = max(
                        len(left & right)
                        for left, right in combinations(zero_sets, 2)
                    )
                    if core_cap > dimension:
                        continue
                    affine_dimension = affine_rank(
                        [error for _, error in chosen], prime
                    )
                    kernel_rank = affine_dimension - 1
                    if length - radius < kernel_rank + 1:
                        continue
                    lower = comb(reserve + kernel_rank, kernel_rank)
                    cap = (length - core_cap) // (
                        dimension + reserve - core_cap
                    )
                    upper = comb(length, kernel_rank) * cap
                    if len(chosen) * lower > upper:
                        raise AssertionError((chosen, core_cap, lower, upper))
                    selectors += 1
    return families, selectors


def official_rows() -> tuple[tuple[str, int, int, int], ...]:
    rows = (
        ("rowc-r1_4", 1024, 4, 256),
        ("rowc-r1_8", 1024, 8, 256),
        ("rowc-r1_16", 1024, 16, 512),
        ("prize-r1_4", 1 << 41, 4, 256),
        ("prize-r1_8", 1 << 41, 8, 256),
        ("prize-r1_16", 1 << 41, 16, 512),
    )
    expected = (4, 4, 4, 15, 15, 14)
    output = []
    for (name, length, rate_denominator, scale_denominator), wanted in zip(
        rows, expected, strict=True
    ):
        dimension = length // rate_denominator
        redundancy = length - dimension
        reserve = length // scale_denominator + 1
        budget = 8 * length**3
        high_cap = redundancy // reserve
        low_cap = (redundancy + 1) // (reserve + 1)
        paid = []
        for pencil_cap in (high_cap, low_cap):
            rank_paid = 0
            for affine_dimension in range(1, 80):
                kernel_rank = affine_dimension - 1
                if (
                    comb(length, kernel_rank) * pencil_cap
                    <= budget * comb(reserve + kernel_rank, kernel_rank)
                ):
                    rank_paid = affine_dimension
                else:
                    break
            paid.append(rank_paid)
        if paid != [wanted, wanted]:
            raise AssertionError((name, paid, wanted))
        output.append((name, wanted, high_cap, low_cap))

    # The post-strip cap extends every prize row and still rejects RowC rank 5.
    if output[3][1] <= 11 or output[4][1] <= 11 or output[5][1] <= 10:
        raise AssertionError("prize-rank extension mutation")
    length, reserve, pencil_cap = 1024, 3, 320
    if comb(length, 4) * pencil_cap <= 8 * length**3 * comb(7, 4):
        raise AssertionError("RowC rank-five mutation unexpectedly passed")
    return tuple(output)


def main() -> None:
    cap_cases, cap_mutations = core_cap_exhaustion()
    families, selectors = exhaustive_small_selectors()
    rows = official_rows()
    print(
        "XR_POSTSTRIP_AFFINE_PENCIL_CHARGE_PASS "
        f"cap_cases={cap_cases} cap_mutations={cap_mutations} "
        f"families={families} selectors={selectors} "
        + " ".join(
            f"{name}:sigma<={paid},caps={high}/{low}"
            for name, paid, high, low in rows
        )
    )


if __name__ == "__main__":
    main()
