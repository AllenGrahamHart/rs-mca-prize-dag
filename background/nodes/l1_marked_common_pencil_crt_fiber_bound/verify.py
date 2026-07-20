#!/usr/bin/env python3
"""Verify the marked common-pencil CRT fiber bound."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_marked_common_pencil_crt_fiber_bound"


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def mul(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % prime
    return trim(out)


def add(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % prime
    return trim(out)


def lagrange(xs: list[int], ys: list[int], prime: int) -> list[int]:
    result = [0]
    for index, x_i in enumerate(xs):
        basis = [1]
        denominator = 1
        for other, x_j in enumerate(xs):
            if other == index:
                continue
            basis = mul(basis, [(-x_j) % prime, 1], prime)
            denominator = denominator * (x_i - x_j) % prime
        scale = ys[index] * pow(denominator, -1, prime) % prime
        result = add(result, [(scale * value) % prime for value in basis], prime)
    return result


def evaluate(poly: list[int], value: int, prime: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * value + coefficient) % prime
    return out


def main() -> None:
    checks = 0
    profiles = 0

    for m in range(1, 9):
        for ell in range(2, 24):
            for p in range(ell):
                for d in range(m * ell + 1, (m + 1) * ell - p):
                    eta = d - m * ell
                    lower = (d - p + ell) // ell
                    for t in range(lower, 2 * m + 1):
                        for v in range(p + 1):
                            support_degree = t * ell - v
                            if t >= m + 1:
                                assert support_degree > d
                            else:
                                assert t == m
                                assert eta <= p - 1
                                assert d - support_degree == eta + v <= 2 * p - 1
                            profiles += 1
                            checks += 2
    assert profiles > 100000

    # Exact CRT fibers on four split support points over F_5.
    prime = 5
    xs = [0, 1, 2, 3]
    ys = [1, 1, 4, 4]
    w0 = lagrange(xs, ys, prime)
    support = [1]
    for value in xs:
        support = mul(support, [(-value) % prime, 1], prime)
    assert len(w0) - 1 < len(support) - 1
    for x, y in zip(xs, ys):
        assert evaluate(w0, x, prime) == y
        checks += 1

    # For a degree allowance deg(S)+r, all q^(r+1) coefficient vectors give
    # distinct solutions in the same residue class.
    for residual_degree in (0, 1, 2):
        seen = set()
        for coefficients in itertools.product(range(prime), repeat=residual_degree + 1):
            candidate = add(w0, mul(support, list(coefficients), prime), prime)
            seen.add(tuple(candidate))
            for x, y in zip(xs, ys):
                assert evaluate(candidate, x, prime) == y
                checks += 1
        assert len(seen) == prime ** (residual_degree + 1)
        checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {
        (edge["from"], edge["to"], edge["kind"])
        for edge in dag["edges"]
    }
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_marked_constant_shift_forney_window_normal_form",
        "l1_bounded_polarity_marked_full_pencil_reduction",
    ):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    for consumer in (
        "l1_mixed_residual_intersection_pin",
        "l1_mixed_petal_amplification",
        "petal_mixed_amplification",
    ):
        assert (NODE, consumer, "ev") in edges
        checks += 1

    statement = (
        ROOT / "background" / "nodes" / NODE / "statement.md"
    ).read_text()
    for anchor in (
        "deg S=t ell-v",
        "q^(eta+v+1)<=q^(2p)",
        "only non-polynomial common-pencil issue",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_CRT_FIBER_PASS checks={checks} profiles={profiles}")


if __name__ == "__main__":
    main()
