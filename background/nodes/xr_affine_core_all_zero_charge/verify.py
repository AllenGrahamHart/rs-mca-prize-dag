#!/usr/bin/env python3
"""Finite replay and exact XR arithmetic for the all-zero charge."""

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


def persistent_cap_exhaustion() -> tuple[int, int]:
    checked = 0
    mutations = 0
    for length in range(2, 41):
        for radius in range(length):
            for kernel_rank in range(length - radius):
                reserve = length - radius - kernel_rank
                for persistent in range(reserve):
                    cap = (length - kernel_rank - persistent) // (
                        reserve - persistent
                    )
                    if cap > radius + 1:
                        raise AssertionError(
                            (length, radius, kernel_rank, persistent, cap)
                        )
                    checked += 1
                if radius and (
                    length - kernel_rank - (reserve - 1)
                ) // 1 > radius:
                    mutations += 1
    if mutations == 0:
        raise AssertionError("the false r cap survived")
    return checked, mutations


def exhaustive_small_families() -> tuple[int, int]:
    prime, length, radius, distance = 3, 4, 2, 4
    vectors = tuple(product(range(prime), repeat=length))
    syndromes = tuple(product(range(prime), repeat=length - 1))
    families = 0
    subfamilies = 0
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
                    if len({gamma for gamma, _ in chosen}) < 2:
                        continue
                    dimension = affine_rank([error for _, error in chosen], prime)
                    kernel_rank = dimension - 1
                    if length - radius < kernel_rank + 1:
                        continue
                    lower = comb(
                        distance - radius + kernel_rank - 1, kernel_rank
                    )
                    upper = comb(length, kernel_rank) * (radius + 1)
                    if len(chosen) * lower > upper:
                        raise AssertionError((y0, y1, chosen, lower, upper))
                    subfamilies += 1

    # Removing genericity permits seven slopes in a rank-one pencil, while
    # the a=0 all-zero charge permits only r+1=2.
    tangent_errors = [((1 + gamma) % 7, 0) for gamma in range(7)]
    if affine_rank(tangent_errors, 7) != 1 or len(tangent_errors) <= 2:
        raise AssertionError("genericity mutation was not detected")
    return families, subfamilies


def official_rows() -> tuple[tuple[str, int, int, int], ...]:
    rows = (
        ("rowc-r1_4", 1024, 4, 256),
        ("rowc-r1_8", 1024, 8, 256),
        ("rowc-r1_16", 1024, 16, 512),
        ("prize-r1_4", 1 << 41, 4, 256),
        ("prize-r1_8", 1 << 41, 8, 256),
        ("prize-r1_16", 1 << 41, 16, 512),
    )
    expected = (4, 4, 4, 11, 11, 10)
    output = []
    for (name, length, rate_denominator, scale_denominator), wanted in zip(
        rows, expected, strict=True
    ):
        dimension = length // rate_denominator
        redundancy = length - dimension
        reserve = length // scale_denominator + 1
        radius = redundancy - reserve
        budget = 8 * length**3
        paid = 0
        first_failure = None
        for affine_dimension in range(1, 64):
            kernel_rank = affine_dimension - 1
            numerator = comb(length, kernel_rank) * (radius + 1)
            denominator = comb(reserve + kernel_rank, kernel_rank)
            if numerator <= budget * denominator:
                paid = affine_dimension
            else:
                first_failure = affine_dimension
                break
        if paid != wanted or first_failure != wanted + 1:
            raise AssertionError((name, paid, first_failure, wanted))
        output.append((name, paid, radius, budget))

    length, radius, budget = 1024, 957, 8 * 1024**3
    denominator4 = comb(6, 3)
    new4 = comb(length, 3) * (radius + 1)
    old4 = comb(length, 3) * (length - 3)
    new5 = comb(length, 4) * (radius + 1)
    if not (new4 <= budget * denominator4 < old4):
        raise AssertionError("RowC 1/16 rank-four improvement was not isolated")
    if new5 <= budget * comb(7, 4):
        raise AssertionError("rank-five mutation unexpectedly passed")
    return tuple(output)


def main() -> None:
    cap_cases, cap_mutations = persistent_cap_exhaustion()
    families, subfamilies = exhaustive_small_families()
    rows = official_rows()
    print(
        "XR_AFFINE_CORE_ALL_ZERO_CHARGE_PASS "
        f"cap_cases={cap_cases} cap_mutations={cap_mutations} "
        f"families={families} subfamilies={subfamilies} "
        + " ".join(f"{name}:sigma<={paid}" for name, paid, _, _ in rows)
    )


if __name__ == "__main__":
    main()
