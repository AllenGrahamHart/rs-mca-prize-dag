#!/usr/bin/env python3
"""Exhaust the fixed-support cross-determinant quotient injection over F_7."""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
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


def saturated_pairs() -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    pairs = []
    for lower in product(range(V.Q), repeat=V.D):
        f = tuple(lower) + (1,)
        for w in product(range(V.Q), repeat=V.D + 1):
            pair = f, tuple(w)
            if V.satisfies(pair, V.SUPPORTS) and V.gcd_poly(f, tuple(w)) == (1,):
                pairs.append(pair)
    return pairs


def quotient_injection(
    pairs: list[tuple[tuple[int, ...], tuple[int, ...]]]
) -> tuple[int, int]:
    support_locator = (1,)
    for support in V.SUPPORTS:
        support_locator = V.mul(support_locator, V.locator(support))
    v = sum(len(marks) for marks in V.MARKS)
    t, ell = len(V.PETALS), len(V.PETALS[0])
    cross_slack = 2 * V.D + v - t * ell

    if not pairs:
        return cross_slack, 0
    f0, w0 = pairs[0]
    images = set()
    for f, w in pairs:
        delta = V.sub(V.mul(w0, f), V.mul(w, f0))
        quotient, remainder = V.divmod_poly(delta, support_locator)
        assert remainder == (0,)
        if cross_slack < 0:
            assert quotient == (0,)
        else:
            assert len(quotient) - 1 <= cross_slack
        images.add(quotient)
    assert len(images) == len(pairs)
    assert len(pairs) <= V.Q ** max(0, cross_slack + 1)
    return cross_slack, len(images)


def main() -> None:
    # Negative cross slack: one populated point and exact singleton bound.
    configure(
        petals=((0, 1), (2, 3), (4, 5)),
        supports=((0,), (2, 3), (4, 5)),
        marks=((1,), (), ()),
        labels=(1, 2, 3),
    )
    paid_pairs = saturated_pairs()
    paid_slack, paid_images = quotient_injection(paid_pairs)
    assert (paid_slack, len(paid_pairs), paid_images) == (-1, 1, 1)

    # Positive cross slack r=2: all syndromes together still inject into the
    # 7^3 quotient space. This is the hostile chart from the singleton audit.
    configure(
        petals=((1, 2), (3, 4)),
        supports=((1,), (3,)),
        marks=((2,), (4,)),
        labels=(1, 3),
    )
    hostile_pairs = saturated_pairs()
    hostile_slack, hostile_images = quotient_injection(hostile_pairs)
    assert hostile_slack == 2
    assert len(hostile_pairs) == hostile_images == 227
    assert hostile_images < V.Q ** (hostile_slack + 1)

    print(
        "L1_FIXED_SUPPORT_FIBER_PASS "
        f"paid={len(paid_pairs)} hostile={len(hostile_pairs)} "
        f"hostile_images={hostile_images} cap={V.Q ** (hostile_slack + 1)}"
    )


if __name__ == "__main__":
    main()
