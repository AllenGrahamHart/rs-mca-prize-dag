#!/usr/bin/env python3
"""Finite replay and exact XR thresholds for the collision-line basis ledger."""

from __future__ import annotations

from fractions import Fraction
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


def affine_rank(points: list[Vector], prime: int) -> int:
    origin = points[0]
    return rank(
        [
            tuple((a - b) % prime for a, b in zip(point, origin, strict=True))
            for point in points[1:]
        ],
        prime,
    )


def arrangement_fixture() -> tuple[int, int, int]:
    # L_t(x)=x_0+t*x_1+t^2*x_2+t^3 over F_11. Any three planes meet
    # once, no four meet, and every two-plane line has five rich points.
    prime, n, dimension = 11, 7, 3
    rows = [tuple(pow(t, power, prime) for power in range(dimension)) for t in range(n)]
    offsets = [pow(t, 3, prime) for t in range(n)]
    points = []
    zero_sets = []
    slopes = []
    for point in product(range(prime), repeat=dimension):
        values = [
            (offset + sum(a * b for a, b in zip(row, point, strict=True))) % prime
            for row, offset in zip(rows, offsets, strict=True)
        ]
        zeros = frozenset(index for index, value in enumerate(values) if value == 0)
        if len(zeros) >= 3:
            points.append(point)
            zero_sets.append(zeros)
            slopes.append(point[2])
    if len(points) != comb(n, 3) or affine_rank(points, prime) != dimension:
        raise AssertionError((len(points), affine_rank(points, prime)))
    if any(len(zeros) != 3 for zeros in zero_sets):
        raise AssertionError("four-plane concurrency mutation")

    lines = {
        left & right
        for left, right in combinations(zero_sets, 2)
        if len(left & right) == 2
    }
    if len(lines) != comb(n, 2):
        raise AssertionError(len(lines))

    basis_sum = 0
    incidence_sum = 0
    raw_pairs = 0
    for zero_core in lines:
        core_rows = [rows[index] for index in sorted(zero_core)]
        if rank(core_rows, prime) != dimension - 1:
            raise AssertionError((zero_core, core_rows))
        bases = sum(
            rank([rows[index] for index in choice], prime) == dimension - 1
            for choice in combinations(sorted(zero_core), dimension - 1)
        )
        members = [
            index for index, zeros in enumerate(zero_sets) if zero_core <= zeros
        ]
        if bases != 1 or len(members) != n - 2:
            raise AssertionError((zero_core, bases, len(members)))
        if len({slopes[index] for index in members}) != len(members):
            raise AssertionError("a collision line repeated a slope")
        basis_sum += bases
        incidence_sum += len(members)
        raw_pairs += comb(len(members), 2)

    if basis_sum != comb(n, dimension - 1):
        raise AssertionError(basis_sum)
    if incidence_sum != comb(n, 2) * (n - 2):
        raise AssertionError(incidence_sum)
    if raw_pairs <= incidence_sum:
        raise AssertionError("line dedup mutation was not detected")

    # A rank-deficient core does not define a line and must be excluded.
    deficient = [(1, 0, 0), (2, 0, 0)]
    if rank(deficient, prime) == dimension - 1:
        raise AssertionError("rank-pin mutation was not detected")

    # The low-basis chart lemma is sharp with three loop coordinates.
    loop_core = [(1, 0, 0), (0, 1, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
    nonloops = sum(any(row) for row in loop_core)
    loop_bases = sum(
        rank(list(choice), prime) == dimension - 1
        for choice in combinations(loop_core, dimension - 1)
    )
    if nonloops != loop_bases + dimension - 2 or loop_bases != 1:
        raise AssertionError((nonloops, loop_bases))
    for point in product(range(prime), repeat=dimension):
        values = [sum(a * b for a, b in zip(row, point, strict=True)) % prime
                  for row in loop_core]
        if any(values[index] for index in range(2, len(loop_core))):
            raise AssertionError("a loop escaped the global zero chart")
    return len(points), len(lines), incidence_sum


def grk_depth(n: int, k: int, reserve: int) -> int:
    radius = n - k
    budget = 8 * n**3
    excess = 0
    while Fraction(
        comb(radius + excess, excess) * radius,
        comb(excess + reserve, excess),
    ) <= budget:
        excess += 1
    return excess - 1


def exact_rows() -> tuple[tuple[str, int, int, int, int, str], ...]:
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
        reserve = n // scale_denominator + 1
        radius = n - k
        line_cap = radius // reserve
        budget = 8 * n**3

        required_s4 = 1
        while line_cap * (comb(n, 3) // required_s4) > budget:
            required_s4 += 1
        if required_s4 > comb(k, 3):
            raise AssertionError((name, required_s4, k))

        uniform_paid = 1
        for dimension in range(2, k + 2):
            bases = comb(k, dimension - 1)
            if line_cap * (comb(n, dimension - 1) // bases) <= budget:
                uniform_paid = dimension
            else:
                break
        paid_excess = grk_depth(n, k, reserve)
        localized_s4 = 1
        while line_cap * (
            comb(min(n, radius + localized_s4 + 2), 3) // localized_s4
        ) > budget:
            localized_s4 += 1
        # Before chart saturation, the localized rank-four line bound is
        # decreasing because 2b<=R; after saturation its numerator is fixed.
        if localized_s4 < k - 2 and 2 * localized_s4 > radius:
            raise AssertionError((name, "monotonicity pin", localized_s4))

        low_chart_paid = max(0, paid_excess - 2)
        residual_start = low_chart_paid + 1
        residual_end = localized_s4 - 1
        rank4 = (
            "closed" if residual_start > residual_end
            else f"b{residual_start}-{residual_end}"
        )
        output.append(
            (name, required_s4, localized_s4, uniform_paid, paid_excess, rank4)
        )
    return tuple(output)


def main() -> None:
    points, lines, incidences = arrangement_fixture()
    rows = exact_rows()
    print(
        "XR_HIGHCORE_COLLISION_LINE_BASIS_LEDGER_PASS "
        f"fixture={points},{lines},{incidences} "
        + " ".join(
            f"{name}:B4>={required},localB4>={localized},uniform_s<={uniform},"
            f"grk_d<={paid_excess},r4={rank4}"
            for name, required, localized, uniform, paid_excess, rank4 in rows
        )
    )


if __name__ == "__main__":
    main()
