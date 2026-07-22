#!/usr/bin/env python3
"""Replay universal first-layout carriage at two petal sizes."""

from __future__ import annotations

from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_general_first_layout_domination"
P = 17


def trim(poly: tuple[int, ...]) -> tuple[int, ...]:
    out = [value % P for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out) if out else (0,)


def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    size = max(len(left), len(right))
    return trim(tuple(
        (left[i] if i < len(left) else 0)
        + (right[i] if i < len(right) else 0)
        for i in range(size)
    ))


def scale(poly: tuple[int, ...], scalar: int) -> tuple[int, ...]:
    return trim(tuple(scalar * value for value in poly))


def mul(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % P
    return trim(tuple(out))


def evaluate(poly: tuple[int, ...], point: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * point + coefficient) % P
    return value


def locator(points: tuple[int, ...]) -> tuple[int, ...]:
    out = (1,)
    for point in points:
        out = mul(out, (-point, 1))
    return out


def divide_exact(
    numerator: tuple[int, ...], denominator: tuple[int, ...]
) -> tuple[int, ...]:
    work = list(trim(numerator))
    divisor = trim(denominator)
    quotient = [0] * max(1, len(work) - len(divisor) + 1)
    while trim(tuple(work)) != (0,) and len(trim(tuple(work))) >= len(divisor):
        work = list(trim(tuple(work)))
        shift = len(work) - len(divisor)
        factor = work[-1] * pow(divisor[-1], -1, P) % P
        quotient[shift] = factor
        for index, coefficient in enumerate(divisor):
            work[index + shift] = (work[index + shift] - factor * coefficient) % P
    assert trim(tuple(work)) == (0,)
    return trim(tuple(quotient))


def source_replay(ell: int) -> tuple[int, int, int]:
    k, m, b = 3, 2, 1
    n = (k - 1) + m * ell + b
    domain = tuple(range(n))
    if ell == 2:
        core = (0, 1)
        background = (2,)
        petals = ((3, 4), (5, 6))
        labels = (2, 5)
    else:
        # Deterministic hostile layout with a genuine non-anchor extra.
        assert ell == 3
        core = (0, 2)
        background = (5,)
        petals = ((7, 6, 4), (8, 3, 1))
        labels = (8, 6)
    base = (2, 3, 1)
    core_locator = locator(core)
    anchors = tuple(add(base, scale(core_locator, label)) for label in labels)

    word = {point: evaluate(base, point) for point in core + background}
    for petal, anchor in zip(petals, anchors):
        for point in petal:
            word[point] = evaluate(anchor, point)

    listed = extras = checks = 0
    threshold = k + ell - 1
    for coefficients in product(range(P), repeat=k):
        polynomial = trim(tuple(coefficients))
        agreements = {
            point for point in domain
            if evaluate(polynomial, point) == word[point]
        }
        if len(agreements) < threshold:
            continue
        listed += 1
        if polynomial in anchors:
            continue
        extras += 1
        shifted = add(polynomial, scale(base, -1))
        retained = tuple(point for point in core if point in agreements)
        missed = tuple(point for point in core if point not in agreements)
        d = len(missed)
        w = divide_exact(shifted, locator(retained))
        assert len(w) - 1 <= d
        for point in background:
            if point in agreements:
                assert evaluate(w, point) == 0
        missed_locator = locator(missed)
        for petal, label in zip(petals, labels):
            support = tuple(point for point in petal if point in agreements)
            assert len(support) <= d
            for point in support:
                assert evaluate(w, point) == label * evaluate(missed_locator, point) % P
        checks += 3

    assert listed >= m
    return listed, extras, checks


def main() -> None:
    listed_two, extras_two, checks_two = source_replay(2)
    listed_three, extras_three, checks_three = source_replay(3)
    assert extras_two > 0 and extras_three > 0

    # First non-planted carriage: all later groups lie in the first anchors.
    anchors = ({0, 1, 2}, {1, 2, 3}, {0, 2, 4}, {0, 1, 5})
    universe = set(range(8))
    groups = [set() for _ in anchors]
    unassigned = set()
    for item in universe:
        owner = next((j for j, planted in enumerate(anchors) if item not in planted), None)
        if owner is None:
            unassigned.add(item)
        else:
            groups[owner].add(item)
    later = set().union(*groups[1:]) if len(groups) > 1 else set()
    assert later <= anchors[0]
    assert unassigned <= anchors[0]
    assert len(universe) <= len(groups[0]) + len(anchors[0])

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert ("l1_core_defect_reduction", NODE, "req") in edges
    for consumer in (
        "l1_mixed_residual_intersection_pin",
        "l1_mixed_petal_amplification",
        "petal_mixed_amplification",
    ):
        assert (NODE, consumer, "ev") in edges

    print(
        "L1_GENERAL_FIRST_LAYOUT_DOMINATION_PASS "
        f"ell2=({listed_two},{extras_two}) ell3=({listed_three},{extras_three}) "
        f"normal_form_checks={checks_two + checks_three} later={len(later)}"
    )


if __name__ == "__main__":
    main()
