#!/usr/bin/env python3
"""Finite replay and official arithmetic for the RS common-root charge."""

from __future__ import annotations

from itertools import combinations, combinations_with_replacement, product
from math import comb


Vector = tuple[int, ...]


def rank(columns: tuple[Vector, ...], prime: int, dimension: int) -> int:
    matrix = [[column[row] for column in columns] for row in range(dimension)]
    pivot = 0
    for column in range(len(columns)):
        choice = next(
            (row for row in range(pivot, dimension) if matrix[row][column] % prime),
            None,
        )
        if choice is None:
            continue
        matrix[pivot], matrix[choice] = matrix[choice], matrix[pivot]
        inverse = pow(matrix[pivot][column], prime - 2, prime)
        matrix[pivot] = [value * inverse % prime for value in matrix[pivot]]
        for row in range(dimension):
            if row == pivot:
                continue
            factor = matrix[row][column] % prime
            if factor:
                matrix[row] = [
                    (left - factor * right) % prime
                    for left, right in zip(matrix[row], matrix[pivot], strict=True)
                ]
        pivot += 1
        if pivot == dimension:
            break
    return pivot


def dot(left: Vector, right: Vector, prime: int) -> int:
    return sum(x * y for x, y in zip(left, right, strict=True)) % prime


def exhaustive_loopless_matroids() -> tuple[int, int]:
    checked = 0
    strict = 0
    regimes = ((2, 3, 7), (3, 2, 6))
    for prime, max_rank, max_size in regimes:
        for dimension in range(1, max_rank + 1):
            vectors = tuple(
                vector
                for vector in product(range(prime), repeat=dimension)
                if any(vector)
            )
            for size in range(dimension, max_size + 1):
                for indices in combinations_with_replacement(range(len(vectors)), size):
                    columns = tuple(vectors[index] for index in indices)
                    if rank(columns, prime, dimension) != dimension:
                        continue
                    bases = sum(
                        rank(tuple(columns[index] for index in choice), prime, dimension)
                        == dimension
                        for choice in combinations(range(size), dimension)
                    )
                    cogirth = min(
                        sum(dot(word, column, prime) != 0 for column in columns)
                        for word in product(range(prime), repeat=dimension)
                        if any(word)
                    )
                    refined = size * comb(dimension + cogirth - 2, dimension - 1)
                    if dimension * bases < refined:
                        raise AssertionError(
                            (prime, dimension, size, columns, cogirth, bases, refined)
                        )
                    old = comb(dimension + cogirth - 1, dimension)
                    if bases > old:
                        strict += 1
                    checked += 1
    if strict == 0:
        raise AssertionError("loopless refinement never improved the old bound")
    return checked, strict


def root_consumption_exhaustion() -> int:
    checked = 0
    for roots in range(0, 8):
        for persistent in range(roots + 1):
            free = roots - persistent
            for slopes in range(1, 6):
                # -1 means unused; otherwise the root vanishes at that slope.
                for assignment in product(range(-1, slopes), repeat=free):
                    loads = [0] * slopes
                    for slope in assignment:
                        if slope >= 0:
                            loads[slope] += 1
                    if sum(loads) > free:
                        raise AssertionError((roots, persistent, slopes, assignment))
                    checked += 1
    return checked


def endpoint_exhaustion() -> int:
    checked = 0
    for redundancy in range(1, 17):
        for dimension in range(1, 13):
            length = redundancy + dimension
            for kernel_rank in range(1, min(dimension, 5) + 1):
                for reserve in range(1, redundancy + 1):
                    q_max = dimension - kernel_rank
                    quotient = comb(
                        kernel_rank + reserve - 1, kernel_rank - 1
                    )
                    for pencil_cap in range(1, 5):
                        corners = common_root_corners(
                            length,
                            dimension,
                            reserve,
                            kernel_rank,
                            pencil_cap,
                        )
                        corner_num, corner_den = rational_max(corners)
                        for u in range(q_max + 1):
                            for v in range(q_max - u + 1):
                                value_num = (
                                    kernel_rank
                                    * pencil_cap
                                    * comb(
                                        redundancy + kernel_rank + u,
                                        kernel_rank,
                                    )
                                    + quotient * v
                                )
                                value_den = quotient * (
                                    kernel_rank + reserve + u + v
                                )
                                if value_num * corner_den > corner_num * value_den:
                                    raise AssertionError(
                                        (
                                            redundancy,
                                            dimension,
                                            kernel_rank,
                                            reserve,
                                            pencil_cap,
                                            u,
                                            v,
                                        )
                                    )
                                checked += 1
    return checked


def rational_max(values: tuple[tuple[int, int], ...]) -> tuple[int, int]:
    maximum = values[0]
    for candidate in values[1:]:
        if candidate[0] * maximum[1] > maximum[0] * candidate[1]:
            maximum = candidate
    return maximum


def common_root_corners(
    length: int,
    dimension: int,
    reserve: int,
    kernel_rank: int,
    pencil_cap: int,
) -> tuple[tuple[int, int], ...]:
    redundancy = length - dimension
    quotient = comb(kernel_rank + reserve - 1, kernel_rank - 1)
    chart_bases = comb(redundancy + kernel_rank, kernel_rank)
    common_roots = dimension - kernel_rank
    return (
        (
            kernel_rank * pencil_cap * chart_bases,
            quotient * (kernel_rank + reserve),
        ),
        (
            kernel_rank * pencil_cap * comb(length, kernel_rank),
            quotient * (dimension + reserve),
        ),
        (
            kernel_rank * pencil_cap * chart_bases + quotient * common_roots,
            quotient * (dimension + reserve),
        ),
    )


def official_rows() -> tuple[tuple[str, int, int, int], ...]:
    rows = (
        ("rowc-r1_4", 1024, 4, 256),
        ("rowc-r1_8", 1024, 8, 256),
        ("rowc-r1_16", 1024, 16, 512),
        ("prize-r1_4", 1 << 41, 4, 256),
        ("prize-r1_8", 1 << 41, 8, 256),
        ("prize-r1_16", 1 << 41, 16, 512),
    )
    expected = (4, 4, 4, 16, 16, 14)
    output = []
    for (name, length, rate_denominator, scale_denominator), wanted in zip(
        rows, expected, strict=True
    ):
        dimension = length // rate_denominator
        redundancy = length - dimension
        reserve = length // scale_denominator + 1
        budget = 8 * length**3
        caps = (
            redundancy // reserve,
            (redundancy + 1) // (reserve + 1),
        )
        paid = []
        for pencil_cap in caps:
            paid_ranks = []
            for affine_dimension in range(2, 80):
                kernel_rank = affine_dimension - 1
                numerator, denominator = rational_max(
                    common_root_corners(
                        length,
                        dimension,
                        reserve,
                        kernel_rank,
                        pencil_cap,
                    )
                )
                if numerator // denominator <= budget:
                    paid_ranks.append(affine_dimension)
            if not paid_ranks or max(paid_ranks) != wanted:
                raise AssertionError((name, pencil_cap, paid_ranks, wanted))
            if wanted + 1 in paid_ranks:
                raise AssertionError((name, "next-rank mutation", wanted + 1))
            paid.append(max(paid_ranks))
        if paid != [wanted, wanted]:
            raise AssertionError((name, paid, wanted))
        output.append((name, wanted, caps[0], caps[1]))
    if output[3][1] != 16 or output[4][1] != 16:
        raise AssertionError("prize rank-sixteen improvement missing")
    return tuple(output)


def main() -> None:
    matroids, strict = exhaustive_loopless_matroids()
    root_cases = root_consumption_exhaustion()
    endpoint_cases = endpoint_exhaustion()
    rows = official_rows()
    print(
        "XR_RS_COMMON_ROOT_BASIS_CHARGE_PASS "
        f"matroids={matroids} strict={strict} root_cases={root_cases} "
        f"endpoint_cases={endpoint_cases} "
        + " ".join(
            f"{name}:sigma<={paid},caps={high}/{low}"
            for name, paid, high, low in rows
        )
    )


if __name__ == "__main__":
    main()
