#!/usr/bin/env python3
"""Verify XR explanation Plotkin width and terminal-tree arithmetic."""

from __future__ import annotations

from itertools import combinations, product


def affine_hyperplane_boundary() -> tuple[int, int, int]:
    points = tuple(product((0, 1), repeat=3))
    supports = []
    for normal in points[1:]:
        for offset in (0, 1):
            support = frozenset(
                i
                for i, point in enumerate(points)
                if sum(x * y for x, y in zip(normal, point)) % 2 == offset
            )
            supports.append(support)
    assert len(set(supports)) == 14
    assert all(len(support) == 4 for support in supports)
    assert all(
        len(left & right) <= 2 and len(left ^ right) >= 4
        for left, right in combinations(supports, 2)
    )
    n, h, capital_h = 8, 1, 2
    assert n == 4 * capital_h
    assert len(supports) <= 2 * n
    return len(supports), n, capital_h


def plotkin_arithmetic() -> tuple[int, int]:
    strict = 0
    logarithmic = 0
    for capital_h in range(1, 31):
        for n_state in range(capital_h, 4 * capital_h):
            bound = (4 * capital_h) // (4 * capital_h - n_state)
            assert bound >= 1
            if n_state <= 3 * capital_h:
                assert bound <= 4
            if n_state <= 2 * capital_h:
                assert bound <= 2
            strict += 1
    for log_n in range(1, 13):
        n = 1 << log_n
        for cap in range(5):
            for excess in range(cap * log_n + 1):
                assert (1 << excess) * 8 * n <= 8 * n ** (cap + 1)
                logarithmic += 1
    return strict, logarithmic


def terminal_tree() -> tuple[int, int]:
    checked = 0
    for capital_h in range(1, 100):
        instances = 1 + 8 * capital_h + 32 * capital_h + 64 * capital_h
        tangent = 4 * capital_h * instances
        assert instances == 1 + 104 * capital_h
        assert tangent <= 420 * capital_h * capital_h
        checked += 1
    return checked, 420


def logarithmic_tree() -> int:
    checked = 0
    for log_n in range(1, 13):
        n = 1 << log_n
        for cap in range(5):
            margin = cap * log_n
            capital_h = max(1, 2 * margin)
            if capital_h > n:
                continue
            n_1 = 3 * capital_h + margin
            n_2 = 2 * capital_h + margin
            n_3 = capital_h + margin
            branch_1 = (4 * capital_h) // (4 * capital_h - n_1)
            branch_2 = (4 * capital_h) // (4 * capital_h - n_2)
            branch_3 = (4 * capital_h) // (4 * capital_h - n_3)
            assert branch_1 <= 8
            assert branch_2 <= 2
            assert branch_3 <= 1
            assert margin <= capital_h // 2
            root_width = 8 * n ** (cap + 1)
            instances = 1 + 25 * root_width
            assert instances <= 1 + 200 * n ** (cap + 1)
            assert n * instances <= 201 * n ** (cap + 2)
            checked += 1
    return checked


def main() -> None:
    family, n, capital_h = affine_hyperplane_boundary()
    strict, logarithmic = plotkin_arithmetic()
    trees, tangent_constant = terminal_tree()
    logarithmic_trees = logarithmic_tree()
    assert strict > 0 and logarithmic > 0 and trees > 0 and logarithmic_trees > 0
    print(
        "XR_NONGENERIC_EXPLANATION_PLOTKIN_WIDTH_PASS "
        f"boundary={family}/{2 * n}:H{capital_h} "
        f"strict={strict} logarithmic={logarithmic} "
        f"trees={trees} logarithmic_trees={logarithmic_trees} "
        f"tangent_constant={tangent_constant}"
    )


if __name__ == "__main__":
    main()
