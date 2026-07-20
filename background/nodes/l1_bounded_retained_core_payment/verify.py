#!/usr/bin/env python3
"""Verify retained-core counting and numerator uniqueness over F_7."""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, product
from math import comb
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


def numerator_counts(
    core: tuple[int, ...],
    support: tuple[int, ...],
    labels: tuple[int, ...],
    d: int,
) -> dict[tuple[int, ...], int]:
    counts = {}
    for defect in combinations(core, d):
        f = V.locator(defect)
        count = 0
        for w in product(range(V.Q), repeat=d + 1):
            if all(
                V.evaluate(w, point) == label * V.evaluate(f, point) % V.Q
                for point, label in zip(support, labels)
            ) and V.gcd_poly(f, w) == (1,):
                count += 1
        counts[defect] = count
    return counts


def main() -> None:
    core = (0, 1, 2)
    labels = (1, 1, 2)

    strict = numerator_counts(core, (3, 4, 5), labels, d=2)
    assert len(strict) == comb(3, 1) == 3
    assert set(strict.values()) == {1}

    # At h=d the numerator need not be unique; strict maximality is
    # load-bearing in the theorem.
    boundary = numerator_counts(core, (3, 4), labels[:2], d=2)
    assert max(boundary.values()) > 1

    arithmetic = 0
    for n in range(2, 80):
        for a in range(n + 1):
            d = n - a
            for gap in range(1, n + 1):
                left = d * d <= n * (d - gap)
                right = a * (n - a) >= n * gap
                assert left == right
                arithmetic += 1

    print(
        "L1_BOUNDED_RETAINED_CORE_PASS "
        f"strict={sum(strict.values())} boundary_max={max(boundary.values())} "
        f"arithmetic={arithmetic}"
    )


if __name__ == "__main__":
    main()
