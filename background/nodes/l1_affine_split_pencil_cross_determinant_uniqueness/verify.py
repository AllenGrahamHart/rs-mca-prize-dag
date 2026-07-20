#!/usr/bin/env python3
"""Check cross-determinant uniqueness and its strict-threshold control."""

from __future__ import annotations

from collections import defaultdict
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, product
from pathlib import Path


COMPILER = (
    Path(__file__).resolve().parents[1]
    / "l1_bounded_mark_affine_split_pencil_compiler"
    / "verify.py"
)
SPEC = spec_from_file_location("l1_affine_compiler_verify", COMPILER)
assert SPEC is not None and SPEC.loader is not None
V = module_from_spec(SPEC)
SPEC.loader.exec_module(V)


def configure(
    petals: tuple[tuple[int, ...], ...],
    supports: tuple[tuple[int, ...], ...],
    marks: tuple[tuple[int, ...], ...],
    labels: tuple[int, ...],
) -> None:
    V.PETALS = petals
    V.SUPPORTS = supports
    V.MARKS = marks
    V.LABELS = labels


def saturated_fibers() -> dict[tuple[int, ...], list[tuple[tuple[int, ...], tuple[int, ...]]]]:
    fibers: dict[
        tuple[int, ...], list[tuple[tuple[int, ...], tuple[int, ...]]]
    ] = defaultdict(list)
    for lower in product(range(V.Q), repeat=V.D):
        f = tuple(lower) + (1,)
        for w in product(range(V.Q), repeat=V.D + 1):
            pair = f, tuple(w)
            if not V.satisfies(pair, V.SUPPORTS):
                continue
            if V.gcd_poly(f, tuple(w)) != (1,):
                continue
            fibers[V.syndrome(pair)].append(pair)
    return fibers


def cross_check(
    fibers: dict[tuple[int, ...], list[tuple[tuple[int, ...], tuple[int, ...]]]],
    expect_unique: bool,
) -> int:
    j = (1,)
    full_locator = (1,)
    for marks, petal in zip(V.MARKS, V.PETALS):
        j = V.mul(j, V.locator(marks))
        full_locator = V.mul(full_locator, V.locator(petal))

    pairs_checked = 0
    for values in fibers.values():
        if expect_unique:
            assert len(values) <= 1
        for (f0, w0), (f1, w1) in combinations(values, 2):
            delta = V.sub(V.mul(w0, f1), V.mul(w1, f0))
            _, remainder = V.divmod_poly(V.mul(j, delta), full_locator)
            assert remainder == (0,)
            pairs_checked += 1
    return pairs_checked


def main() -> None:
    # Strict paid region: t*ell=6 > 2d+v=5. The cell is populated and unique.
    configure(
        petals=((0, 1), (2, 3), (4, 5)),
        supports=((0,), (2, 3), (4, 5)),
        marks=((1,), (), ()),
        labels=(1, 2, 3),
    )
    paid = saturated_fibers()
    assert sum(map(len, paid.values())) == 1
    assert len(paid) == 1
    assert 3 * 2 > 2 * V.D + 1
    assert cross_check(paid, expect_unique=True) == 0

    # Below threshold: t*ell=4 <= 2d+v=6. Same-syndrome multiplicity occurs,
    # while the cross-determinant divisibility still holds.
    configure(
        petals=((1, 2), (3, 4)),
        supports=((1,), (3,)),
        marks=((2,), (4,)),
        labels=(1, 3),
    )
    hostile = saturated_fibers()
    assert 2 * 2 <= 2 * V.D + 2
    assert max(map(len, hostile.values())) > 1
    hostile_pairs = cross_check(hostile, expect_unique=False)
    assert hostile_pairs > 0

    print(
        "L1_CROSS_DETERMINANT_PASS "
        f"paid_points={sum(map(len, paid.values()))} "
        f"hostile_points={sum(map(len, hostile.values()))} "
        f"hostile_pairs={hostile_pairs}"
    )


if __name__ == "__main__":
    main()
