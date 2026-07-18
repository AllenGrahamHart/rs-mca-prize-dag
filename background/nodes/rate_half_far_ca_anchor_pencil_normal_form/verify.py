#!/usr/bin/env python3
"""Tiny exhaustive replay of the far-CA anchor-pencil normal form."""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
Q = 5
N = 4
RADIUS = 1
COLUMNS = tuple((1, x) for x in range(N))
WORDS = tuple(product(range(Q), repeat=N))


def syndrome(word: tuple[int, ...]) -> tuple[int, int]:
    return tuple(
        sum(word[i] * COLUMNS[i][j] for i in range(N)) % Q
        for j in range(2)
    )


CODE = tuple(word for word in WORDS if syndrome(word) == (0, 0))


def add(left: tuple[int, ...], right: tuple[int, ...], scale: int = 1) -> tuple[int, ...]:
    return tuple((a + scale * b) % Q for a, b in zip(left, right))


def sub(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((a - b) % Q for a, b in zip(left, right))


def weight(word: tuple[int, ...]) -> int:
    return sum(value != 0 for value in word)


def close_witness(word: tuple[int, ...]) -> tuple[int, ...] | None:
    witnesses = [codeword for codeword in CODE if weight(sub(word, codeword)) <= RADIUS]
    assert len(witnesses) <= 1
    return witnesses[0] if witnesses else None


def lift(target: tuple[int, int]) -> tuple[int, ...]:
    return next(word for word in WORDS if syndrome(word) == target)


def main() -> None:
    assert len(CODE) == Q ** 2
    f1 = lift((0, 1))
    f2 = lift((1, 4))
    spans = [
        {tuple((a * value) % Q for value in column) for a in range(Q)}
        for column in COLUMNS
    ]
    assert not any(syndrome(f1) in line and syndrome(f2) in line for line in spans)

    witnesses = {
        slope: close_witness(add(f1, f2, slope))
        for slope in range(Q)
    }
    bad = {slope for slope, codeword in witnesses.items() if codeword is not None}
    assert bad == {1, 2, 3, 4}

    checked = 0
    for gamma0 in bad:
        c0 = witnesses[gamma0]
        assert c0 is not None
        e0 = sub(add(f1, f2, gamma0), c0)
        e0_support = {i for i, value in enumerate(e0) if value}
        s = len(e0_support)

        predicted = set()
        for lam in range(1, Q):
            for p in CODE:
                error = add(e0, sub(f2, p), lam)
                if weight(error) > RADIUS:
                    continue
                predicted.add((gamma0 + lam) % Q)
                outside = {
                    i
                    for i in range(N)
                    if i not in e0_support and f2[i] != p[i]
                }
                t = len(outside)
                cancellations = sum(
                    (e0[i] + lam * (f2[i] - p[i])) % Q == 0
                    for i in e0_support
                )
                assert RADIUS - s + 1 <= t <= RADIUS
                assert cancellations >= s + t - RADIUS >= 1
                checked += 1

        assert predicted == bad - {gamma0}

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_far_ca_anchor_pencil_normal_form"]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (
        "rate_half_far_ca_anchor_pencil_normal_form",
        "rate_half_band_closure",
        "ev",
    ) in edges

    print(
        "RATE_HALF_FAR_CA_ANCHOR_PENCIL_NORMAL_FORM_PASS "
        f"anchors={len(bad)} presentations={checked}"
    )


if __name__ == "__main__":
    main()
