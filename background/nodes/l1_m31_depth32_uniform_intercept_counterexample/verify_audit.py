#!/usr/bin/env python3
"""Independent truncated-prefix audit of the M31 depth-32 counterexample."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m31_depth32_uniform_intercept_counterexample"
CONSUMER = "l1_mixed_petal_amplification"
P = 2**31 - 1
SCALE = pow(2, -2047, P)
GENERATOR = (1717986917, 1288490189)
ANCHOR_CLASSES = frozenset((
    5, 7, 9, 11, 13, 17, 19, 45, 47, 51, 53, 55, 57, 59,
    69, 71, 73, 75, 77, 81, 83, 109, 111, 115, 117, 119,
    121, 123, 125,
))
EXPECTED_ETA = (
    173262001, 1991954384, 675887777, 1391977736, 1091118249,
    2003694163, 420992802, 776638025, 367223569, 1846719195,
    2143278248, 668818770, 72200137, 842191233, 409563302,
    1496140795, 1309711074, 690240569, 1945503956, 1539728667,
    918364989, 1791559593, 1564755684, 341216000, 1692806458,
    2092860389, 1543768796, 1547853218, 1351243040, 2102639491,
    906658074, 2121057296,
)
MIXED = (
    ((5,13,19,45,47,69,73,75,77,111,117,119), (29,35,37,39,41,85,95,97,101,103,105,107)),
    ((9,11,17,51,53,55,59,81,83,109,115,123), (21,23,25,27,31,33,43,87,89,91,93,99)),
    ((7,59,71,75,77,81,83,109,111,115,117,123), (21,25,39,43,79,85,91,93,99,101,107,113)),
    ((5,11,13,17,19,45,47,51,53,57,69,121), (15,21,27,29,35,37,43,49,85,89,103,107)),
    ((7,59,71,75,77,81,83,109,111,115,117,123), (23,25,39,41,79,87,91,93,99,101,105,113)),
    ((5,11,13,17,19,45,47,51,53,57,69,121), (15,23,27,29,35,37,41,49,87,89,103,105)),
    ((7,59,71,75,77,81,83,109,111,115,117,123), (25,31,33,39,79,91,93,95,97,99,101,113)),
    ((5,11,13,17,19,45,47,51,53,57,69,121), (15,27,29,31,33,35,37,49,89,95,97,103)),
    ((5,11,17,45,51,57,69,75,81,109,115,121), (15,23,33,39,41,49,65,79,97,103,113,127)),
    ((5,11,17,45,51,57,69,75,81,109,115,121), (21,23,33,39,41,43,65,85,97,103,107,127)),
    ((5,11,17,45,51,57,69,75,81,109,115,121), (23,27,33,37,39,41,65,91,97,101,103,127)),
    ((5,11,17,45,51,57,69,75,81,109,115,121), (23,29,33,35,39,41,65,93,97,99,103,127)),
)


def mul(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    a, b = left
    c, d = right
    return ((a * c - b * d) % P, (a * d + b * c) % P)


def square_n(value: tuple[int, int], count: int) -> tuple[int, int]:
    for _ in range(count):
        value = mul(value, value)
    return value


def labels_by_recurrence() -> dict[int, int]:
    first = square_n(GENERATOR, 19)
    step = mul(first, first)
    power = first
    out = {}
    for r in range(1, 2048, 2):
        out[r] = SCALE * power[0] % P
        power = mul(power, step)
    return out


def block16(name: int) -> set[int]:
    return {
        r for r in range(1, 2048, 2)
        if r % 256 in {name, 256 - name}
    }


def support(classes: frozenset[int]) -> tuple[int, ...]:
    reps = block16(3) - {3}
    for name in classes:
        reps.update(block16(name))
    return tuple(sorted(reps))


def truncated_prefix(reps: tuple[int, ...], labels: dict[int, int], depth: int) -> tuple[int, ...]:
    # Descending monic coefficients, retaining only the requested prefix.
    coefficients = [1]
    for rep in reps:
        root = labels[rep]
        width = min(depth, len(coefficients))
        updated = [1]
        for j in range(1, width + 1):
            old = coefficients[j] if j < len(coefficients) else 0
            updated.append((old - root * coefficients[j - 1]) % P)
        coefficients = updated
    return tuple(coefficients[1:])


def main() -> None:
    labels = labels_by_recurrence()
    if len(labels) != len(set(labels.values())) or len(labels) != 1024:
        raise AssertionError("label recurrence")

    anchor = support(ANCHOR_CLASSES)
    if len(anchor) != 479:
        raise AssertionError("anchor size")
    if truncated_prefix(anchor, labels, 32) != EXPECTED_ETA:
        raise AssertionError("independent anchor prefix")

    seen = set()
    for index, (removed, added) in enumerate(MIXED, start=1):
        classes = frozenset((set(ANCHOR_CLASSES) - set(removed)) | set(added))
        candidate = support(classes)
        if len(candidate) != 479 or len(set(anchor) - set(candidate)) != 192:
            raise AssertionError(("support geometry", index))
        if truncated_prefix(candidate, labels, 32) != EXPECTED_ETA:
            raise AssertionError(("independent mixed prefix", index))
        seen.add(candidate)
    if len(seen) != 12:
        raise AssertionError("mixed distinctness")

    # Hostile mutations: one class substitution and one restored puncture.
    removed, added = MIXED[0]
    mutated_classes = frozenset(
        (set(ANCHOR_CLASSES) - set(removed)) | (set(added) - {107}) | {15}
    )
    mutated = support(mutated_classes)
    if len(mutated) == 479 and truncated_prefix(mutated, labels, 32) == EXPECTED_ETA:
        raise AssertionError("class mutation survived")
    restored = tuple(sorted(set(anchor) | {3}))
    if truncated_prefix(restored, labels, 32) == EXPECTED_ETA:
        raise AssertionError("puncture mutation survived")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    if nodes[NODE]["status"] != "PROVED":
        raise AssertionError("DAG status")
    if (NODE, CONSUMER, "ev") not in edges:
        raise AssertionError("DAG evidence edge")

    print(
        "L1_M31_DEPTH32_UNIFORM_INTERCEPT_COUNTEREXAMPLE_AUDIT_PASS "
        "labels=1024 mixed=12 mutations=2 eta_pinned=32"
    )


if __name__ == "__main__":
    main()
