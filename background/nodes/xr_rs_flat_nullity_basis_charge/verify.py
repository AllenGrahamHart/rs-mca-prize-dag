#!/usr/bin/env python3
"""Finite replay and RowC residual table for the RS flat-nullity charge."""

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


def exhaustive_flat_nullity() -> tuple[int, int]:
    checked = 0
    strict = 0
    for prime, max_rank, max_size in ((2, 3, 7), (3, 2, 6)):
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
                    flat_nullity = 0
                    for subset_size in range(size + 1):
                        for subset in combinations(range(size), subset_size):
                            subset_rank = rank(
                                tuple(columns[index] for index in subset),
                                prime,
                                dimension,
                            )
                            if subset_rank < dimension:
                                flat_nullity = max(
                                    flat_nullity, subset_size - subset_rank
                                )
                    lower = size * comb(
                        size - flat_nullity - 1, dimension - 1
                    )
                    if dimension * bases < lower:
                        raise AssertionError(
                            (
                                prime,
                                dimension,
                                size,
                                flat_nullity,
                                bases,
                                lower,
                            )
                        )
                    if dimension * bases > lower:
                        strict += 1
                    checked += 1
    if strict == 0:
        raise AssertionError("flat-nullity bound never had strict slack")
    return checked, strict


def packing_exhaustion() -> tuple[int, int]:
    checked = 0
    mutations = 0
    for length, block_size, threshold in ((5, 3, 2), (6, 3, 2), (7, 4, 3)):
        blocks = tuple(combinations(range(length), block_size))
        for family_size in range(1, 5):
            for family in combinations(blocks, family_size):
                cap_ok = all(
                    len(set(left) & set(right)) < threshold
                    for left, right in combinations(family, 2)
                )
                packed = family_size * comb(block_size, threshold)
                if cap_ok and packed > comb(length, threshold):
                    raise AssertionError((length, block_size, threshold, family))
                if not cap_ok and packed > comb(length, threshold):
                    mutations += 1
                checked += 1
    if mutations == 0:
        raise AssertionError("packing hypothesis removal did not fire")
    return checked, mutations


def selector_bound(
    length: int,
    dimension: int,
    reserve: int,
    kernel_rank: int,
    core_cap: int,
    u: int,
    v: int,
) -> tuple[int, int, int]:
    redundancy = length - dimension
    common_roots = dimension - kernel_rank - u
    persistent = common_roots - v
    pencil_cap = (length - core_cap) // (dimension + reserve - core_cap)
    chart = redundancy + kernel_rank + u
    good_size = kernel_rank + reserve + u + v
    minimum_size = kernel_rank + reserve + u
    good_weight = good_size * comb(
        good_size - u - 1, kernel_rank - 1
    )
    minimum_weight = minimum_size * comb(
        minimum_size - u - 1, kernel_rank - 1
    )
    basis_bound = max(
        v,
        (
            kernel_rank * pencil_cap * comb(chart, kernel_rank)
            + v * (good_weight - minimum_weight)
        )
        // good_weight,
    )
    threshold = core_cap - persistent + 1
    packing_bound = comb(length - persistent, threshold) // comb(
        dimension + reserve - persistent, threshold
    )
    return min(basis_bound, packing_bound), basis_bound, packing_bound


def rowc_residuals() -> tuple[tuple[str, int, int, int, int, int, int], ...]:
    rows = (
        ("rowc-r1_4", 1024, 4, 256, (14, 8, 10, 7, 1, 1)),
        ("rowc-r1_8", 1024, 8, 256, (70, 49, 38, 29, 3, 2)),
        ("rowc-r1_16", 1024, 16, 512, (323, 274, 60, 60, 7, 6)),
    )
    output = []
    for name, length, rate_denominator, scale_denominator, expected in rows:
        dimension = length // rate_denominator
        reserve = length // scale_denominator + 1
        kernel_rank = 4
        budget = 8 * length**3
        q_max = dimension - kernel_rank
        total = (q_max + 1) * (q_max + 2) // 2
        summaries = []
        for core_cap in (dimension, dimension - 1):
            failures = []
            for u in range(q_max + 1):
                for v in range(q_max - u + 1):
                    bound, _, _ = selector_bound(
                        length,
                        dimension,
                        reserve,
                        kernel_rank,
                        core_cap,
                        u,
                        v,
                    )
                    if bound > budget:
                        failures.append((u, v))
            summaries.append(
                (
                    len(failures),
                    max(u for u, _ in failures),
                    max(v for _, v in failures),
                )
            )
        actual = (
            summaries[0][0],
            summaries[1][0],
            summaries[0][1],
            summaries[1][1],
            summaries[0][2],
            summaries[1][2],
        )
        if actual != expected:
            raise AssertionError((name, actual, expected))
        output.append((name, total, *actual))
    return tuple(output)


def main() -> None:
    matroids, strict = exhaustive_flat_nullity()
    packing_cases, packing_mutations = packing_exhaustion()
    rows = rowc_residuals()
    print(
        "XR_RS_FLAT_NULLITY_BASIS_CHARGE_PASS "
        f"matroids={matroids} strict={strict} packing_cases={packing_cases} "
        f"packing_mutations={packing_mutations} "
        + " ".join(
            f"{name}:all={total},A={count_a},B={count_b},"
            f"umax={umax_a}/{umax_b},vmax={vmax_a}/{vmax_b}"
            for (
                name,
                total,
                count_a,
                count_b,
                umax_a,
                umax_b,
                vmax_a,
                vmax_b,
            ) in rows
        )
    )


if __name__ == "__main__":
    main()
