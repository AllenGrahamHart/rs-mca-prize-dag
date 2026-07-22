#!/usr/bin/env python3
"""Verify the arbitrary-line syndrome router and its F_7 toy census."""

from __future__ import annotations

import json
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_arbitrary_line_syndrome_router"


def rref_basis(vectors: list[tuple[int, ...]], prime: int, rank: int) -> tuple[tuple[int, ...], ...]:
    rows = [list(vector) for vector in vectors]
    pivot_row = 0
    for column in range(rank):
        pivot = next(
            (row for row in range(pivot_row, len(rows)) if rows[row][column] % prime),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = pow(rows[pivot_row][column] % prime, -1, prime)
        rows[pivot_row] = [(value * scale) % prime for value in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row:
                continue
            scale = rows[row][column] % prime
            if scale:
                rows[row] = [
                    (left - scale * right) % prime
                    for left, right in zip(rows[row], rows[pivot_row], strict=True)
                ]
        pivot_row += 1
    return tuple(tuple(row) for row in rows[:pivot_row])


def vector_span(
    basis: tuple[tuple[int, ...], ...], prime: int, rank: int
) -> frozenset[tuple[int, ...]]:
    return frozenset(
        tuple(
            sum(coefficients[i] * basis[i][j] for i in range(len(basis))) % prime
            for j in range(rank)
        )
        for coefficients in product(range(prime), repeat=len(basis))
    )


def error_spaces(prime: int, n: int, redundancy: int, radius: int):
    columns = [
        tuple(pow(point, degree, prime) for degree in range(redundancy))
        for point in range(1, n + 1)
    ]
    spaces = []
    for size in range(radius + 1):
        for support in combinations(range(n), size):
            basis = rref_basis([columns[index] for index in support], prime, redundancy)
            spaces.append((support, vector_span(basis, prime, redundancy)))
    return columns, spaces


def bad_slopes(
    first: tuple[int, ...],
    second: tuple[int, ...],
    prime: int,
    spaces,
) -> tuple[int, ...]:
    bad = []
    for slope in range(prime):
        combined = tuple(
            (left + slope * right) % prime
            for left, right in zip(first, second, strict=True)
        )
        if any(
            combined in space and not (first in space and second in space)
            for _, space in spaces
        ):
            bad.append(slope)
    return tuple(bad)


def syndrome(
    word: tuple[int, ...], columns: list[tuple[int, ...]], prime: int
) -> tuple[int, ...]:
    return tuple(
        sum(value * column[row] for value, column in zip(word, columns, strict=True))
        % prime
        for row in range(len(columns[0]))
    )


def check_support_span_equivalence() -> int:
    """Directly compare the span test with codeword agreement on a tiny MDS code."""
    prime, n, redundancy, radius = 5, 4, 2, 1
    columns, spaces = error_spaces(prime, n, redundancy, radius)
    words = tuple(product(range(prime), repeat=n))
    codewords = tuple(word for word in words if syndrome(word, columns, prime) == (0, 0))
    assert len(codewords) == prime ** (n - redundancy)

    checks = 0
    for word in words:
        word_syndrome = syndrome(word, columns, prime)
        for support, space in spaces:
            outside = tuple(index for index in range(n) if index not in support)
            direct = any(
                all(word[index] == codeword[index] for index in outside)
                for codeword in codewords
            )
            assert (word_syndrome in space) == direct
            checks += 1
    return checks


def main() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    status = {node["id"]: node["status"] for node in dag["nodes"]}
    assert status[NODE] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (NODE, "rate_half_band_closure", "ev") in edges

    launcher = (
        ROOT
        / "critical/nodes/rate_half_band_closure/notes/witness_hunt_20260712"
        / "rh_band_witness_census_modal.py"
    ).read_text()
    assert "polynomial words" in launcher
    assert "zero_sum_ladder" in launcher

    prime, n, k, agreement = 7, 6, 3, 4
    redundancy, radius = n - k, n - agreement
    columns, spaces = error_spaces(prime, n, redundancy, radius)
    assert all(
        len(rref_basis([columns[index] for index in support], prime, redundancy))
        == redundancy
        for support in combinations(range(n), redundancy)
    )

    witness = ((0, 1, 0), (0, 0, 1))
    assert bad_slopes(*witness, prime, spaces) == tuple(range(prime))
    explicit_supports = {
        0: (1, 6),
        1: (2, 6),
        2: (3, 6),
        3: (4, 6),
        4: (5, 6),
        5: (1, 4),
        6: (1, 5),
    }
    spaces_by_support = {
        tuple(index + 1 for index in support): space for support, space in spaces
    }
    for slope, support in explicit_supports.items():
        left, right = support
        assert left != right and (left + right) % prime == slope
        combined = (0, 1, slope)
        space = spaces_by_support[support]
        assert combined in space
        assert not (witness[0] in space and witness[1] in space)

    histogram: dict[int, int] = {}
    syndromes = tuple(product(range(prime), repeat=redundancy))
    maximum = 0
    for first in syndromes:
        for second in syndromes:
            count = len(bad_slopes(first, second, prime, spaces))
            histogram[count] = histogram.get(count, 0) + 1
            maximum = max(maximum, count)
    assert sum(histogram.values()) == prime ** (2 * redundancy)
    assert maximum == prime
    assert histogram == {0: 343, 1: 2394, 5: 6048, 6: 37296, 7: 71568}
    support_checks = check_support_span_equivalence()

    print(
        "RATE_HALF_ARBITRARY_LINE_SYNDROME_ROUTER_PASS "
        f"pairs={len(syndromes) ** 2} max_bad={maximum} "
        f"tangent_baseline={radius + 1} support_checks={support_checks}"
    )


if __name__ == "__main__":
    main()
