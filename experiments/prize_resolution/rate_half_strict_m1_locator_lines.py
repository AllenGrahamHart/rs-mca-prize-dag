#!/usr/bin/env python3
"""Exact F_17 line census for the strict m=1 locator analogue."""

from collections import Counter
from itertools import combinations, product


P = 17
DOMAIN = tuple(range(1, P))


def mul(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % P
    return tuple(out)


def locator(roots: tuple[int, ...]) -> tuple[int, ...]:
    out = (1,)
    for root in roots:
        out = mul(out, ((-root) % P, 1))
    return out


def affine_line(p: tuple[int, ...], q: tuple[int, ...]):
    direction = tuple((y - x) % P for x, y in zip(p, q))
    for t in range(P):
        yield tuple((x + t * d) % P for x, d in zip(p, direction))


def matrix_rank(matrix: list[list[int]]) -> int:
    rows = [row[:] for row in matrix]
    rank = 0
    width = len(rows[0]) if rows else 0
    for column in range(width):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column] % P), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, P)
        rows[rank] = [(x * inverse) % P for x in rows[rank]]
        for i, row in enumerate(rows):
            if i == rank or not row[column] % P:
                continue
            scale = row[column] % P
            rows[i] = [(x - scale * y) % P for x, y in zip(row, rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def nullspace(matrix: list[list[int]]) -> list[tuple[int, ...]]:
    rows = [row[:] for row in matrix]
    height = len(rows)
    width = len(rows[0])
    pivot_columns = []
    rank = 0
    for column in range(width):
        pivot = next((i for i in range(rank, height) if rows[i][column] % P), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, P)
        rows[rank] = [(x * inverse) % P for x in rows[rank]]
        for i, row in enumerate(rows):
            if i == rank or not row[column] % P:
                continue
            scale = row[column] % P
            rows[i] = [(x - scale * y) % P for x, y in zip(row, rows[rank])]
        pivot_columns.append(column)
        rank += 1

    free_columns = [column for column in range(width) if column not in pivot_columns]
    basis = []
    for free in free_columns:
        vector = [0] * width
        vector[free] = 1
        for row_index, pivot in enumerate(pivot_columns):
            vector[pivot] = (-rows[row_index][free]) % P
        basis.append(tuple(vector))
    return basis


def projective_span(basis: list[tuple[int, ...]]):
    seen = set()
    for scalars in product(range(P), repeat=len(basis)):
        if not any(scalars):
            continue
        vector = tuple(
            sum(scale * basis[j][i] for j, scale in enumerate(scalars)) % P
            for i in range(len(basis[0]))
        )
        first = next(x for x in vector if x)
        normalized = tuple((x * pow(first, -1, P)) % P for x in vector)
        if normalized not in seen:
            seen.add(normalized)
            yield normalized


def hankel(sequence: tuple[int, ...]) -> list[list[int]]:
    return [[sequence[i + j] for j in range(4)] for i in range(5)]


def hankel_compatibility(p: tuple[int, ...], q: tuple[int, ...]):
    direction = tuple((y - x) % P for x, y in zip(p, q))
    equations = []
    for i in range(5):
        first = [0] * 16
        middle = [0] * 16
        last = [0] * 16
        for j in range(4):
            first[i + j] = p[j]
            middle[i + j] = direction[j]
            middle[8 + i + j] = p[j]
            last[8 + i + j] = direction[j]
        equations.extend((first, middle, last))

    basis = nullspace(equations)
    witnesses = []
    for vector in projective_span(basis):
        y_0, y_1 = vector[:8], vector[8:]
        m_0 = hankel(y_0)
        m_1 = hankel(y_1)
        ranks = []
        for t in range(P):
            ranks.append(matrix_rank([[(a + t * b) % P for a, b in zip(x, y)] for x, y in zip(m_0, m_1)]))
        infinity_rank = matrix_rank(m_1)
        if set(ranks) == {3} and infinity_rank == 3:
            witnesses.append((y_0, y_1))
    return len(basis), witnesses


def main() -> None:
    records = []
    by_coeff = {}
    for roots in combinations(DOMAIN, 3):
        coeff = locator(roots)
        by_coeff[coeff] = roots
        records.append((coeff, roots))

    assert len(records) == 560
    assert len(by_coeff) == len(records)

    rich_lines: set[tuple[tuple[int, ...], ...]] = set()
    pair_histogram: Counter[int] = Counter()
    maximum = 0

    for (p, _), (q, _) in combinations(records, 2):
        hits = tuple(sorted(by_coeff[x] for x in affine_line(p, q) if x in by_coeff))
        count = len(hits)
        pair_histogram[count] += 1
        maximum = max(maximum, count)
        if count >= 3:
            rich_lines.add(hits)

    core_histogram = Counter()
    core_free_maximum = 0
    for line in rich_lines:
        common = set(line[0])
        for roots in line[1:]:
            common.intersection_update(roots)
        core_histogram[(len(line), len(common))] += 1
        if not common:
            core_free_maximum = max(core_free_maximum, len(line))

    line_histogram = Counter(len(line) for line in rich_lines)
    witnesses = sorted(line for line in rich_lines if len(line) == maximum)
    core_free_witnesses = sorted(
        line
        for line in rich_lines
        if len(line) == core_free_maximum
        and not set.intersection(*(set(roots) for roots in line))
    )

    assert dict(sorted(line_histogram.items())) == {
        3: 12_192,
        4: 960,
        5: 1_360,
        6: 2_800,
        7: 480,
        14: 120,
    }
    assert dict(sorted(core_histogram.items())) == {
        (3, 0): 12_192,
        (4, 0): 960,
        (5, 0): 16,
        (5, 1): 1_344,
        (6, 1): 2_800,
        (7, 1): 480,
        (14, 2): 120,
    }
    assert core_free_maximum == 5
    assert len(core_free_witnesses) == 16

    expected_line = (
        (1, 2, 5),
        (3, 7, 11),
        (4, 6, 16),
        (8, 10, 15),
        (9, 12, 13),
    )
    assert core_free_witnesses[0] == expected_line
    p_0 = locator(expected_line[0])
    q_0 = locator(expected_line[1])
    supported_0 = {
        t: by_coeff[coeff]
        for t, coeff in enumerate(affine_line(p_0, q_0))
        if coeff in by_coeff
    }
    assert supported_0 == {
        0: (1, 2, 5),
        1: (3, 7, 11),
        2: (9, 12, 13),
        4: (4, 6, 16),
        15: (8, 10, 15),
    }

    print(
        "RATE_HALF_STRICT_M1_LOCATOR_LINES_PASS "
        f"points={len(records)} max={maximum} core_free_max={core_free_maximum} "
        f"rich_line_histogram={dict(sorted(line_histogram.items()))}"
    )
    print(f"pair_histogram={dict(sorted(pair_histogram.items()))}")
    print(f"core_histogram={dict(sorted(core_histogram.items()))}")
    for index, line in enumerate(witnesses[:1]):
        print(f"max_line_{index}={line}")
    for index, line in enumerate(core_free_witnesses[:1]):
        print(f"core_free_max_line_{index}={line}")

    compatible = []
    nullity_histogram = Counter()
    for line in core_free_witnesses:
        p = locator(line[0])
        q = locator(line[1])
        nullity, hankel_witnesses = hankel_compatibility(p, q)
        nullity_histogram[nullity] += 1
        if hankel_witnesses:
            compatible.append((line, hankel_witnesses))

    assert dict(nullity_histogram) == {1: 16}
    assert len(compatible) == 16
    assert compatible[0][0] == expected_line
    assert compatible[0][1] == [
        (
            (1, 10, 16, 2, 14, 0, 3, 11),
            (0, 14, 9, 7, 13, 12, 15, 0),
        )
    ]

    print(
        f"hankel_nullity_histogram={dict(sorted(nullity_histogram.items()))} "
        f"compatible_lines={len(compatible)}"
    )
    for index, (line, hankel_witnesses) in enumerate(compatible[:1]):
        print(f"compatible_line_{index}={line}")
        print(f"compatible_y0_{index}={hankel_witnesses[0][0]}")
        print(f"compatible_y1_{index}={hankel_witnesses[0][1]}")


if __name__ == "__main__":
    main()
