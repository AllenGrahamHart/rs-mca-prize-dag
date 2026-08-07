#!/usr/bin/env python3
"""Verify the finite scaling model and F2 route wiring."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
P = 5


def add(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return ((x[0] + y[0]) % P, (x[1] + y[1]) % P)


def mul(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    # F_25 = F_5[a]/(a^2-2); 2 is a nonsquare modulo 5.
    return (
        (x[0] * y[0] + 2 * x[1] * y[1]) % P,
        (x[0] * y[1] + x[1] * y[0]) % P,
    )


def power(x: tuple[int, int], exponent: int) -> tuple[int, int]:
    result = (1, 0)
    while exponent:
        if exponent & 1:
            result = mul(result, x)
        x = mul(x, x)
        exponent //= 2
    return result


def total(values: list[tuple[int, int]]) -> tuple[int, int]:
    result = (0, 0)
    for value in values:
        result = add(result, value)
    return result


def moments(
    points: list[tuple[int, int]], indices: tuple[int, ...]
) -> tuple[tuple[int, int], ...]:
    return tuple(total([power(x, j) for x in points]) for j in indices)


def main() -> None:
    checks = 0
    mu4 = [(1, 0), (2, 0), (4, 0), (3, 0)]
    g = (0, 1)
    scaled = [mul(g, x) for x in mu4]
    indices = (1, 2, 3)
    base_zero = []
    scaled_zero = []

    for mask in range(1 << len(mu4)):
        base = [mu4[i] for i in range(4) if mask >> i & 1]
        extension = [scaled[i] for i in range(4) if mask >> i & 1]
        base_moments = moments(base, indices)
        extension_moments = moments(extension, indices)
        expected = tuple(
            mul(power(g, j), value)
            for j, value in zip(indices, base_moments)
        )
        assert extension_moments == expected
        checks += len(indices)
        base_zero.append(all(value == (0, 0) for value in base_moments))
        scaled_zero.append(all(value == (0, 0) for value in extension_moments))
    assert base_zero == scaled_zero
    checks += 1

    for left in range(16):
        for right in range(16):
            base_left = [mu4[i] for i in range(4) if left >> i & 1]
            base_right = [mu4[i] for i in range(4) if right >> i & 1]
            ext_left = [scaled[i] for i in range(4) if left >> i & 1]
            ext_right = [scaled[i] for i in range(4) if right >> i & 1]
            assert (moments(base_left, indices) == moments(base_right, indices)) == (
                moments(ext_left, indices) == moments(ext_right, indices)
            )
            checks += 1

    window_base = mu4[:2]
    window_ext = scaled[:2]
    for word in itertools.product((-1, 0, 1), repeat=2):
        base_syndrome = tuple(
            total(
                [
                    (
                        word[i] * power(window_base[i], j)[0] % P,
                        word[i] * power(window_base[i], j)[1] % P,
                    )
                    for i in range(2)
                ]
            )
            for j in (1, 3)
        )
        ext_syndrome = tuple(
            total(
                [
                    (
                        word[i] * power(window_ext[i], j)[0] % P,
                        word[i] * power(window_ext[i], j)[1] % P,
                    )
                    for i in range(2)
                ]
            )
            for j in (1, 3)
        )
        assert (base_syndrome == ((0, 0), (0, 0))) == (
            ext_syndrome == ((0, 0), (0, 0))
        )
        checks += 1

    non_generating = {
        *(("plus", 1, e) for e in (2, 3, 4, 5, 6)),
        ("plus", 2, 4),
        ("minus", 2, 4),
    }
    descent = {row: (row[0], row[1], row[1]) for row in non_generating}
    assert len(non_generating) == 7
    assert set(descent.values()) == {
        ("plus", 1, 1),
        ("plus", 2, 2),
        ("minus", 2, 2),
    }
    generating = {
        ("plus", 1, 1),
        ("plus", 2, 2),
        ("plus", 4, 4),
        ("minus", 2, 2),
        ("minus", 4, 4),
    }
    assert set(descent.values()) <= generating and len(generating) == 5
    checks += 3

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    node_id = "f2_generated_field_ambient_invariance"
    assert nodes[node_id]["status"] == "PROVED"
    assert nodes["f2_admissible_object"]["status"] == "REFUTED"
    assert (
        "f2_admissible_degree_order_classification",
        node_id,
        "req",
    ) in edges
    assert (node_id, "f2_conditional_close", "ev") in edges
    checks += 4

    print(
        "F2_GENERATED_FIELD_AMBIENT_INVARIANCE_PASS "
        f"checks={checks} types=12_to_5"
    )


if __name__ == "__main__":
    main()
