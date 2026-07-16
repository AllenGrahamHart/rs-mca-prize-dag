#!/usr/bin/env python3
"""Verify the projective Johnson packing and official M=4 arithmetic."""

from __future__ import annotations

from itertools import combinations, product


NODE = "pma_three_petal_projective_johnson_bound"


def max_clique(adjacency: list[int]) -> int:
    best = 0

    def expand(candidates: int, size: int) -> None:
        nonlocal best
        if size + candidates.bit_count() <= best:
            return
        while candidates:
            if size + candidates.bit_count() <= best:
                return
            bit = candidates & -candidates
            vertex = bit.bit_length() - 1
            candidates ^= bit
            expand(candidates & adjacency[vertex], size + 1)
        best = max(best, size)

    expand((1 << len(adjacency)) - 1, 0)
    return best


def set_system_audit() -> tuple[int, int, bool]:
    cases = 0
    total_sets = 0
    sharp_overlap = False
    for n in range(4, 10):
        for d in range(2, min(n, 5) + 1):
            subsets = [frozenset(row) for row in combinations(range(n), d)]
            for overlap in range(d):
                denominator = d * d - n * overlap
                if denominator <= 0:
                    continue
                adjacency = [0] * len(subsets)
                for i, left in enumerate(subsets):
                    for j in range(i + 1, len(subsets)):
                        intersection = len(left & subsets[j])
                        if intersection <= overlap:
                            adjacency[i] |= 1 << j
                            adjacency[j] |= 1 << i
                        sharp_overlap |= overlap > 0 and intersection == overlap
                maximum = max_clique(adjacency)
                assert maximum * denominator <= n * (d - overlap)
                cases += 1
                total_sets += len(subsets)
    return cases, total_sets, sharp_overlap


def trim(poly: tuple[int, ...]) -> tuple[int, ...]:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def degree(poly: tuple[int, ...]) -> int:
    poly = trim(poly)
    return -1 if poly == (0,) else len(poly) - 1


def primitive_linear_pair(u: tuple[int, int], v: tuple[int, int], p: int) -> bool:
    u_t = trim(u)
    v_t = trim(v)
    if u_t == (0,):
        return degree(v_t) == 0
    if v_t == (0,):
        return degree(u_t) == 0
    if degree(u_t) == 0 or degree(v_t) == 0:
        return True
    return (u[0] * v[1] - u[1] * v[0]) % p != 0


def evaluate(coefficients: tuple[int, ...], x: int, p: int) -> int:
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * x + coefficient) % p
    return value


def polynomial_fixture() -> tuple[int, int, bool]:
    p = 17
    roots_by_pair: list[frozenset[int]] = []
    for raw in product(range(p), repeat=4):
        first = next((value for value in raw if value), None)
        if first != 1:
            continue
        u = (raw[0], raw[1])
        v = (raw[2], raw[3])
        if not primitive_linear_pair(u, v, p):
            continue
        # F=u+v X^3 for the base-point-free pair (F_p,F_q)=(1,X^3).
        f = trim((u[0], u[1], 0, v[0], v[1]))
        if degree(f) != 4:
            continue
        roots = frozenset(x for x in range(p) if evaluate(f, x, p) == 0)
        if len(roots) == 4:
            roots_by_pair.append(roots)

    assert len(roots_by_pair) > 10
    max_intersection = 0
    sharp = False
    for left, right in combinations(roots_by_pair, 2):
        intersection = len(left & right)
        max_intersection = max(max_intersection, intersection)
        assert intersection <= 2
        sharp |= intersection == 2
    assert sharp

    # Multiplying a primitive pair by X preserves its rational function but
    # destroys primitivity; the cross polynomial becomes identically zero.
    u1, v1 = (1, 0), (0, 1)
    u2, v2 = (0, 1, 0), (0, 0, 1)
    cross = [0] * 4
    for i, a in enumerate(u1):
        for j, b in enumerate(v2):
            cross[i + j] = (cross[i + j] + a * b) % p
    for i, a in enumerate(u2):
        for j, b in enumerate(v1):
            cross[i + j] = (cross[i + j] - a * b) % p
    assert all(value == 0 for value in cross)
    return len(roots_by_pair), max_intersection, True


def official_arithmetic() -> tuple[int, int, int, int, int, bool, bool, bool]:
    quarter_cells = 0
    half_cells = 0
    half_paid = 0
    half_tail = 0
    tail_bound_rows = 0
    zero_denominator_seen = False
    b7_counterexample = False
    deleted_a_caught = False

    for ell in range(1, 401):
        for b in range(ell):
            numerator = 4 * ell + b - 1
            if numerator % 3 == 0:
                k = numerator // 3
                n_core = k - 1
                for d in range((3 * ell + 1) // 2, min(2 * ell - 1, n_core) + 1):
                    e_minus_one = 2 * d - 3 * ell
                    denominator = d * d - n_core * e_minus_one
                    identity = (n_core - d) ** 2 + n_core * (3 * ell - n_core)
                    assert denominator == identity and denominator > 0
                    quarter_cells += 1

            n_core = 4 * ell + b - 2
            for d in range((3 * ell + 1) // 2, min(2 * ell - 1, n_core) + 1):
                a = 2 * ell - d
                e_minus_one = 2 * d - 3 * ell
                denominator = d * d - n_core * e_minus_one
                formula = ell * (4 * a - b + 2) + a * a + 2 * a * b - 4 * a
                assert denominator == formula
                half_cells += 1
                if denominator > 0:
                    half_paid += 1
                else:
                    half_tail += 1
                    assert b >= 7
                    assert 1 <= a <= (b - 3) // 4
                    tail_bound_rows += 1
                if b <= 6:
                    assert denominator > 0
                zero_denominator_seen |= denominator == 0
                b7_counterexample |= b == 7 and denominator <= 0
                wrong_without_a = ell * (4 - b + 2) + 1 + 2 * b - 4
                deleted_a_caught |= a != 1 and wrong_without_a != denominator

    return (
        quarter_cells,
        half_cells,
        half_paid,
        half_tail,
        tail_bound_rows,
        zero_denominator_seen,
        b7_counterexample,
        deleted_a_caught,
    )


def main() -> None:
    set_cases, set_count, sharp_set_overlap = set_system_audit()
    fixture_count, fixture_overlap, nonprimitive_caught = polynomial_fixture()
    (
        quarter_cells,
        half_cells,
        half_paid,
        half_tail,
        tail_bound_rows,
        zero_denominator_seen,
        b7_counterexample,
        deleted_a_caught,
    ) = official_arithmetic()

    assert set_cases > 20 and set_count > 1_000
    assert sharp_set_overlap
    assert fixture_overlap == 2
    assert nonprimitive_caught
    assert quarter_cells > 1_000
    assert half_paid > 0 and half_tail > 0
    assert tail_bound_rows == half_tail
    assert zero_denominator_seen
    assert b7_counterexample
    assert deleted_a_caught
    mutations = sum(
        (
            fixture_overlap == 2,
            nonprimitive_caught,
            zero_denominator_seen,
            b7_counterexample,
            deleted_a_caught,
        )
    )
    assert mutations == 5

    print(
        f"{NODE}_PASS set_cases={set_cases} set_rows={set_count} "
        f"fixture_pairs={fixture_count} fixture_overlap={fixture_overlap} "
        f"quarter_cells={quarter_cells} half_cells={half_cells} "
        f"half_paid={half_paid} half_tail={half_tail} mutations={mutations}"
    )


if __name__ == "__main__":
    main()
