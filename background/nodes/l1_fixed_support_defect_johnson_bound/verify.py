#!/usr/bin/env python3
"""Verify the L1 defect-set Johnson bound and its strict boundary over F_7."""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, product
from pathlib import Path


HELPER = (
    Path(__file__).resolve().parents[1]
    / "l1_bounded_mark_affine_split_pencil_compiler"
    / "verify.py"
)
SPEC = spec_from_file_location("l1_affine_compiler_verify", HELPER)
assert SPEC is not None and SPEC.loader is not None
V = module_from_spec(SPEC)
SPEC.loader.exec_module(V)


Pair = tuple[tuple[int, ...], tuple[int, ...], frozenset[int]]


def exact_pairs(
    core: tuple[int, ...],
    support: tuple[int, ...],
    labels: tuple[int, ...],
    d: int,
) -> list[Pair]:
    pairs = []
    for defect in combinations(core, d):
        f = V.locator(defect)
        for w in product(range(V.Q), repeat=d + 1):
            if not all(
                V.evaluate(w, point) == label * V.evaluate(f, point) % V.Q
                for point, label in zip(support, labels)
            ):
                continue
            if V.gcd_poly(f, w) == (1,):
                pairs.append((f, w, frozenset(defect)))
    return pairs


def check_cross_divisibility(
    pairs: list[Pair], support: tuple[int, ...], d: int
) -> int:
    r_j = 2 * d - len(support)
    support_locator = V.locator(support)
    for (f_1, w_1, d_1), (f_2, w_2, d_2) in combinations(pairs, 2):
        delta = V.sub(V.mul(w_1, f_2), V.mul(w_2, f_1))
        assert delta != (0,)
        intersection = tuple(sorted(d_1 & d_2))
        divisor = V.mul(support_locator, V.locator(intersection))
        _, remainder = V.divmod_poly(delta, divisor)
        assert remainder == (0,)
        assert len(d_1 & d_2) <= r_j
    return r_j


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


def set_system_audit() -> tuple[int, int]:
    cases = 0
    rows = 0
    for n in range(4, 9):
        for d in range(2, min(n, 5) + 1):
            blocks = [frozenset(row) for row in combinations(range(n), d)]
            for overlap in range(d):
                denominator = d * d - n * overlap
                if denominator <= 0:
                    continue
                adjacency = [0] * len(blocks)
                for i, left in enumerate(blocks):
                    for j in range(i + 1, len(blocks)):
                        if len(left & blocks[j]) <= overlap:
                            adjacency[i] |= 1 << j
                            adjacency[j] |= 1 << i
                maximum = max_clique(adjacency)
                assert maximum * denominator <= n * (d - overlap)
                cases += 1
                rows += len(blocks)
    return cases, rows


def tail_arithmetic() -> tuple[int, int]:
    positive = 0
    tail = 0
    for n in range(2, 61):
        for gap in range(1, n + 1):
            for d in range(gap, n + 1):
                for h in range(d + gap, 2 * d + 1):
                    r_j = 2 * d - h
                    denominator = d * d - n * r_j
                    if denominator > 0:
                        positive += 1
                    else:
                        tail += 1
                        assert 4 * gap <= n
                        assert d * d - n * d + n * gap <= 0
    return positive, tail


def main() -> None:
    support = (3, 4, 5)
    labels = (1, 1, 2)

    sharp = exact_pairs((0, 1, 2), support, labels, d=2)
    sharp_r = check_cross_divisibility(sharp, support, d=2)
    sharp_denominator = 2 * 2 - 3 * sharp_r
    assert len(sharp) == 3
    assert sharp_r == 1 and sharp_denominator == 1
    assert len(sharp) * sharp_denominator == 3 * (2 - sharp_r)

    boundary = exact_pairs((0, 1, 2, 3), (4, 5, 6), labels, d=2)
    boundary_r = check_cross_divisibility(boundary, (4, 5, 6), d=2)
    assert len(boundary) == 6
    assert boundary_r == 1
    assert 2 * 2 - 4 * boundary_r == 0

    # This local payment is strictly broader than the global Johnson gate.
    n_core, ell, petals, d, h = 20, 3, 8, 18, 21
    n = n_core + petals * ell
    agreement = n_core + ell
    local_denominator = d * d - n_core * (2 * d - h)
    assert agreement * agreement <= n * n_core
    assert local_denominator == 24 > 0

    cases, rows = set_system_audit()
    positive, tail = tail_arithmetic()
    assert cases > 10 and rows > 100
    assert positive > 0 and tail > 0

    print(
        "L1_FIXED_SUPPORT_DEFECT_JOHNSON_PASS "
        f"sharp={len(sharp)} boundary={len(boundary)} "
        f"local_not_global={local_denominator} set_cases={cases} "
        f"set_rows={rows} positive={positive} tail={tail}"
    )


if __name__ == "__main__":
    main()
