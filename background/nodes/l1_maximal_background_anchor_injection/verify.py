#!/usr/bin/env python3
"""Finite-field and ledger replay for the maximal background-anchor injection."""

from __future__ import annotations

from itertools import product
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_maximal_background_anchor_injection"
P = 7


def trim(poly: tuple[int, ...]) -> tuple[int, ...]:
    out = list(x % P for x in poly)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out) if out else (0,)


def sub(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    size = max(len(left), len(right))
    return trim(tuple(
        (left[i] if i < len(left) else 0)
        - (right[i] if i < len(right) else 0)
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


def div_exact(
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


def fixed_layer(
    ell: int,
    d: int,
    background: tuple[int, ...],
    supports: tuple[tuple[int, ...], ...],
    labels: tuple[int, ...],
) -> int:
    r = len(background)
    h = sum(map(len, supports))
    a_star = max(map(len, supports))
    assert r < ell and r + h >= ell + d
    assert len(labels) == len(supports) and len(set(labels)) == len(labels)
    assert 0 not in labels

    pairs = []
    for lower in product(range(P), repeat=d):
        f = tuple(lower) + (1,)
        for w in product(range(P), repeat=d + 1):
            if any(evaluate(w, point) for point in background):
                continue
            if any(
                evaluate(w, point) != label * evaluate(f, point) % P
                for support, label in zip(supports, labels)
                for point in support
            ):
                continue
            pairs.append((f, trim(tuple(w))))

    largest = max(range(len(supports)), key=lambda index: len(supports[index]))
    petal_images = set()
    background_images = set()
    for f, w in pairs:
        petal_images.add(div_exact(sub(w, scale(f, labels[largest])), locator(supports[largest])))
        background_images.add(div_exact(w, locator(background)))

    assert len(petal_images) == len(pairs)
    assert len(background_images) == len(pairs)
    exponent = max(0, d - max(r, a_star) + 1)
    assert len(pairs) <= P**exponent
    return len(pairs)


def main() -> None:
    checks = 0
    cases = (
        (2, 2, (), ((0, 1), (2, 3)), (1, 2)),
        (2, 2, (4,), ((0,), (1, 2)), (1, 3)),
        (2, 1, (4,), ((0,), (1,)), (2, 5)),
        (3, 2, (6,), ((0, 1), (2, 3)), (1, 4)),
    )
    populated = 0
    for case in cases:
        count = fixed_layer(*case)
        populated += int(count > 0)
        checks += 4
    assert populated >= 2

    # Exhaust the arithmetic behind the B4 exponent and support-pattern cap.
    profiles = 0
    for ell in range(1, 7):
        for t in range(2, 6):
            for sizes in product(range(1, ell + 1), repeat=t):
                u = t * ell - sum(sizes)
                a_star = max(sizes)
                assert a_star >= ell - u // t
                exact_patterns = 1
                for size in sizes:
                    exact_patterns *= comb(ell, size)
                assert exact_patterns <= comb(t * ell, u)
                for excess in range(4):
                    for r in range(ell):
                        gamma = min(
                            excess + u // t + 1,
                            max(0, excess + ell - r + 1),
                        )
                        for d in range(ell + excess + 1):
                            exponent = max(0, d - max(r, a_star) + 1)
                            assert exponent <= gamma
                            checks += 1
                profiles += 1

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
    checks += 5

    print(
        "L1_MAXIMAL_BACKGROUND_ANCHOR_PASS "
        f"checks={checks} profiles={profiles} populated_cases={populated}"
    )


if __name__ == "__main__":
    main()
