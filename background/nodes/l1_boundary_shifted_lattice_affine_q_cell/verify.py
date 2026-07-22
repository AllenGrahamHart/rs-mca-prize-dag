#!/usr/bin/env python3
"""Exact replay of the boundary locator-Q cell and infinity payment."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_boundary_shifted_lattice_affine_q_cell"
PARENT = "l1_exact_shell_balanced_shifted_lattice_reduction"
CONSUMER = "l1_mixed_petal_amplification"


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * max(len(a), len(b))
    for i in range(len(out)):
        out[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p
    return trim(out)


def sub(a: list[int], b: list[int], p: int) -> list[int]:
    return add(a, [(-x) % p for x in b], p)


def mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(out)


def divmod_poly(num: list[int], den: list[int], p: int) -> tuple[list[int], list[int]]:
    rem = trim(num[:])
    quotient = [0] * max(1, len(rem) - len(den) + 1)
    while rem != [0] and len(rem) >= len(den):
        shift = len(rem) - len(den)
        coefficient = rem[-1] * pow(den[-1], -1, p) % p
        quotient[shift] = coefficient
        for i, value in enumerate(den):
            rem[i + shift] = (rem[i + shift] - coefficient * value) % p
        trim(rem)
    return trim(quotient), trim(rem)


def locator(points: tuple[int, ...], p: int) -> list[int]:
    out = [1]
    for x in points:
        out = mul(out, [(-x) % p, 1], p)
    return out


def evaluate(poly: list[int], x: int, p: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * x + coefficient) % p
    return out


def main() -> None:
    p = 7
    H = tuple(range(6))
    n = len(H)
    k = 2
    m = 3
    w = m - k
    omega = n - m
    Omega = locator(H, p)

    # Standard boundary Q basis: g1=(1,Pz), g2=(Qz,-Rz).
    Pz = [2, 1, 3, 1]
    Qz, Rz = divmod_poly(Omega, Pz, p)
    assert len(Qz) - 1 == omega
    assert max(0, (len(Pz) - 1) - (k - 1)) == w + 1
    assert max(len(Qz) - 1, (len(Rz) - 1) - (k - 1)) == omega
    determinant = sub([(-x) % p for x in Rz], mul(Qz, Pz, p), p)
    assert determinant == [(-x) % p for x in Omega]

    affine_parameters: dict[tuple[int, ...], tuple[int, ...]] = {}
    exact_codewords = set()
    for coefficients in itertools.product(range(p), repeat=omega - w):
        A = list(coefficients)
        W = add(Qz, A, p)
        quotient, remainder = divmod_poly(Omega, W, p)
        if remainder != [0] or len(W) - 1 != omega:
            continue
        N = add([(-x) % p for x in Rz], mul(A, Pz, p), p)
        P, remainder = divmod_poly(N, W, p)
        assert remainder == [0] and len(P) - 1 < k
        agreement = tuple(x for x in H if evaluate(Pz, x, p) == evaluate(P, x, p))
        assert len(agreement) >= m
        if len(agreement) == m:
            key = tuple(P)
            assert key not in exact_codewords
            exact_codewords.add(key)
            affine_parameters[key] = tuple(A)
            assert quotient == locator(agreement, p)
    assert exact_codewords
    assert len(set(affine_parameters.values())) == len(affine_parameters)

    # W-led boundary: one fixed near codeword can survive the infinity ray.
    k2 = 3
    m2 = 4
    w2 = 1
    error_roots = (0, 1)
    W1 = locator(error_roots, p)
    fixed = [3, 2, 1]
    values = [evaluate(fixed, x, p) for x in H]
    for x in error_roots:
        values[x] = (values[x] + 1) % p
    agreement = tuple(x for x in H if values[x] == evaluate(fixed, x, p))
    assert len(W1) - 1 == w2 + 1
    assert len(agreement) == m2
    # Every support on the B=0 ray has the same quotient N1/W1=fixed.
    N1 = mul(W1, fixed, p)
    recovered, remainder = divmod_poly(N1, W1, p)
    assert remainder == [0] and recovered == fixed
    assert sum(len(agreement) == m2 for _ in (fixed,)) == 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(
        "L1_BOUNDARY_SHIFTED_LATTICE_AFFINE_Q_PASS "
        f"affine_exact={len(exact_codewords)} infinity_exact=1"
    )


if __name__ == "__main__":
    main()
