#!/usr/bin/env python3
"""Finite cogirth-basis replay and exact XR affine-core thresholds."""

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
                    (a - factor * b) % prime
                    for a, b in zip(matrix[row], matrix[pivot], strict=True)
                ]
        pivot += 1
        if pivot == len(matrix):
            break
    return pivot


def code_distance(columns: tuple[Vector, ...], dimension: int, prime: int) -> int:
    return min(
        sum(
            sum(a * b for a, b in zip(message, column, strict=True)) % prime != 0
            for column in columns
        )
        for message in product(range(prime), repeat=dimension)
        if any(message)
    )


def basis_count(columns: tuple[Vector, ...], dimension: int, prime: int) -> int:
    return sum(
        rank(list(choice), prime) == dimension
        for choice in combinations(columns, dimension)
    )


def add(left: Vector, right: Vector, prime: int) -> Vector:
    return tuple((a + b) % prime for a, b in zip(left, right, strict=True))


def scale(value: int, vector: Vector, prime: int) -> Vector:
    return tuple(value * coordinate % prime for coordinate in vector)


def parity(vector: Vector, prime: int) -> Vector:
    return tuple((vector[index] - vector[0]) % prime for index in range(1, 4))


def in_support_image(target: Vector, support: tuple[int, ...], prime: int) -> bool:
    columns = []
    for coordinate in support:
        basis = tuple(1 if index == coordinate else 0 for index in range(4))
        columns.append(parity(basis, prime))
    base = rank(columns, prime)
    return rank(columns + [target], prime) == base


def affine_rank(vectors: list[Vector], prime: int) -> int:
    origin = vectors[0]
    return rank(
        [
            tuple((a - b) % prime for a, b in zip(vector, origin, strict=True))
            for vector in vectors[1:]
        ],
        prime,
    )


def exhaustive_matroids() -> tuple[int, int]:
    checked = 0
    equality = 0
    for prime, dimension, length in ((3, 2, 4), (2, 3, 5)):
        vectors = tuple(product(range(prime), repeat=dimension))
        for columns in product(vectors, repeat=length):
            if rank(list(columns), prime) != dimension:
                continue
            distance = code_distance(columns, dimension, prime)
            bases = basis_count(columns, dimension, prime)
            lower = comb(distance + dimension - 1, dimension)
            if bases < lower:
                raise AssertionError(
                    (prime, dimension, length, columns, distance, bases, lower)
                )
            checked += 1
            equality += bases == lower
    if equality == 0:
        raise AssertionError("no sharp cogirth fixture")
    return checked, equality


def exhaustive_affine_lines() -> tuple[int, int]:
    prime, radius, distance, length = 3, 2, 4, 4
    vectors = tuple(product(range(prime), repeat=length))
    syndromes = tuple(product(range(prime), repeat=length - 1))
    checked = 0
    maximum_pairs = 0
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
            affine_dimension = affine_rank([error for _, error in pairs], prime)
            kernel_dimension = affine_dimension - 1
            if length - radius < kernel_dimension + 1:
                continue
            lower = comb(
                distance - radius + kernel_dimension - 1, kernel_dimension
            )
            upper = comb(length, kernel_dimension) * (length - kernel_dimension)
            if len(pairs) * lower > upper:
                raise AssertionError(
                    (y0, y1, len(pairs), affine_dimension, lower, upper)
                )
            checked += 1
            maximum_pairs = max(maximum_pairs, len(pairs))

    # Without genericity, the tangent family e_gamma=(1+gamma,0) carries all
    # seven field slopes, while the a=0 ACG expression permits only |U|=2.
    tangent_errors = [((1 + gamma) % 7, 0) for gamma in range(7)]
    tangent_rank = affine_rank(tangent_errors, 7)
    tangent_kernel_rank = tangent_rank - 1
    tangent_upper = comb(2, tangent_kernel_rank) * (2 - tangent_kernel_rank)
    if len(tangent_errors) <= tangent_upper:
        raise AssertionError("genericity mutation was not detected")
    return checked, maximum_pairs


def highcore_overlap_rank(
    n: int, k: int, reserve: int, budget: int
) -> int:
    radius = n - k
    line_cap = radius // reserve
    quotient = budget // line_cap
    paid_rank = 1
    for affine_dimension in range(2, k + 2):
        kernel_dimension = affine_dimension - 1
        total_subsets = comb(n, kernel_dimension)
        line_threshold = total_subsets // (quotient + 1) + 1
        maximum_bases = comb(k, kernel_dimension)
        largest_low_basis = min(maximum_bases, line_threshold - 1)
        if largest_low_basis:
            chart_size = min(
                n, radius + largest_low_basis + kernel_dimension - 1
            )
            acg_paid = (
                comb(chart_size, kernel_dimension)
                * (chart_size - kernel_dimension)
                <= budget * comb(reserve + kernel_dimension, kernel_dimension)
            )
        else:
            acg_paid = True
        if not acg_paid:
            break
        paid_rank = affine_dimension
    return paid_rank


def highcore_local_envelope_rank(
    n: int, k: int, reserve: int, budget: int
) -> int:
    radius = n - k
    line_cap = radius // reserve
    paid_rank = 1
    for affine_dimension in range(2, k + 2):
        kernel_dimension = affine_dimension - 1
        maximum_bases = comb(k, kernel_dimension)
        saturation = max(1, k - kernel_dimension + 1)
        endpoint = min(maximum_bases, saturation)
        denominator = comb(reserve + kernel_dimension, kernel_dimension)

        candidates = {1, endpoint, maximum_bases}
        target = line_cap * denominator
        if endpoint >= 1 and endpoint * (radius + endpoint - 1) >= target:
            low, high = 1, endpoint
            while low < high:
                middle = (low + high) // 2
                if middle * (radius + middle - 1) >= target:
                    high = middle
                else:
                    low = middle + 1
            candidates.update((max(1, low - 1), low))

        worst = 0
        for bases in candidates:
            if not 1 <= bases <= maximum_bases:
                continue
            chart_size = min(
                n, radius + bases + kernel_dimension - 1
            )
            subsets = comb(chart_size, kernel_dimension)
            acg = subsets * (chart_size - kernel_dimension) // denominator
            line = line_cap * (subsets // bases)
            worst = max(worst, min(acg, line))
        if worst > budget:
            break
        paid_rank = affine_dimension
    return paid_rank


def official_rows() -> tuple[tuple[str, int, int, int, bool], ...]:
    rows = (
        ("rowc-r1_4", 1024, 4, 256),
        ("rowc-r1_8", 1024, 8, 256),
        ("rowc-r1_16", 1024, 16, 512),
        ("prize-r1_4", 1 << 41, 4, 256),
        ("prize-r1_8", 1 << 41, 8, 256),
        ("prize-r1_16", 1 << 41, 16, 512),
    )
    output = []
    for name, n, rate_denominator, scale_denominator in rows:
        k = n // rate_denominator
        radius = n - k
        reserve = n // scale_denominator + 1
        budget = 8 * n**3

        paid_rank = 0
        for affine_rank in range(1, k + 2):
            kernel_rank = affine_rank - 1
            bound_numerator = comb(n, kernel_rank) * (n - kernel_rank)
            bound_denominator = comb(reserve + kernel_rank, kernel_rank)
            if bound_numerator <= budget * bound_denominator:
                paid_rank = affine_rank
            else:
                break

        # CLB leaves only these worst rank-four chart excesses. Rows already
        # closed before ACG use zero, which is harmless and independently paid.
        residual_excess = {
            "rowc-r1_4": 0,
            "rowc-r1_8": 4,
            "rowc-r1_16": 7,
            "prize-r1_4": 0,
            "prize-r1_8": 0,
            "prize-r1_16": 10,
        }[name]
        chart_size = radius + residual_excess if residual_excess else n
        kernel_rank = 3
        rank4_chart = (
            comb(chart_size, kernel_rank) * (chart_size - kernel_rank)
            <= budget * comb(reserve + kernel_rank, kernel_rank)
        )
        if not rank4_chart:
            raise AssertionError((name, paid_rank, residual_excess))
        combined_rank = highcore_overlap_rank(n, k, reserve, budget)
        local_rank = highcore_local_envelope_rank(n, k, reserve, budget)
        if combined_rank < 4:
            raise AssertionError((name, "combined rank regression", combined_rank))
        if local_rank < combined_rank:
            raise AssertionError((name, "local envelope regression", local_rank))
        output.append((name, paid_rank, combined_rank, local_rank, rank4_chart))
    return tuple(output)


def main() -> None:
    checked, equality = exhaustive_matroids()
    affine_lines, maximum_pairs = exhaustive_affine_lines()
    rows = official_rows()
    print(
        "XR_AFFINE_CORE_COGIRTH_RAY_BOUND_PASS "
        f"matroids={checked} equality={equality} "
        f"affine_lines={affine_lines} max_pairs={maximum_pairs} "
        + " ".join(
            f"{name}:ambient_s<={paid},PA_s<={combined},local_PA_s<={local},"
            f"rank4={'closed' if closed else 'open'}"
            for name, paid, combined, local, closed in rows
        )
    )


if __name__ == "__main__":
    main()
