#!/usr/bin/env python3
"""Verify the official first-checkpoint split-pencil reduction."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_official_first_checkpoint_split_pencil_reduction"


def trim(poly: list[int], prime: int) -> list[int]:
    out = [coefficient % prime for coefficient in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return trim(out, prime)


def subtract(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * max(len(left), len(right))
    for i in range(len(out)):
        a = left[i] if i < len(left) else 0
        b = right[i] if i < len(right) else 0
        out[i] = (a - b) % prime
    return trim(out, prime)


def derivative(poly: list[int], prime: int) -> list[int]:
    if len(poly) == 1:
        return [0]
    return trim([i * poly[i] for i in range(1, len(poly))], prime)


def wronskian(first: list[int], second: list[int], prime: int) -> list[int]:
    return subtract(
        multiply(derivative(first, prime), second, prime),
        multiply(first, derivative(second, prime), prime),
        prime,
    )


def nonsquare(prime: int) -> int:
    squares = {x * x % prime for x in range(prime)}
    return next(value for value in range(2, prime) if value not in squares)


def extension_multiply(
    left: tuple[int, int], right: tuple[int, int], prime: int, nu: int
) -> tuple[int, int]:
    a, b = left
    c, d = right
    return ((a * c + b * d * nu) % prime, (a * d + b * c) % prime)


def extension_inverse(
    value: tuple[int, int], prime: int, nu: int
) -> tuple[int, int]:
    a, b = value
    denominator = (a * a - nu * b * b) % prime
    inverse = pow(denominator, -1, prime)
    return (a * inverse % prime, -b * inverse % prime)


def main() -> None:
    checks = 0

    # A nonconstant difference R has an uncancellable degree-p+r-1 term.
    for prime in (3, 5, 7, 11):
        first = [0] * (prime + 1)
        first[1] = 1
        first[prime] = 1
        for degree in range(1, prime):
            difference = [0] * (degree + 1)
            difference[degree] = 1
            second = first[:]
            for i, coefficient in enumerate(difference):
                second[i] = (second[i] + coefficient) % prime
            value = wronskian(first, second, prime)
            assert len(value) - 1 == prime + degree - 1
            checks += 1

    # Constant shifts have W=cF' and realize the low-degree split pencil.
    for prime in (3, 5, 7, 11):
        for bound in range(prime - 1):
            first = [0] * (prime + 1)
            first[0] = 2 % prime
            first[bound + 1] = 1
            first[prime] = 1
            second = first[:]
            second[0] = (second[0] + 1) % prime
            value = wronskian(first, second, prime)
            assert value == derivative(first, prime)
            assert len(value) - 1 == bound
            checks += 2

    # Directly count the ratio set of theta+F_p in F_(p^2).
    for prime in (3, 5, 7, 11):
        nu = nonsquare(prime)
        line = tuple((u, 1) for u in range(prime))
        ratios = {
            extension_multiply(x, extension_inverse(y, prime, nu), prime, nu)
            for x in line
            for y in line
        }
        assert (0, 0) not in line
        assert len(ratios) == prime * prime - prime + 1
        checks += 2

    p = 3583
    assert 11 * (p * p - p + 1) > 256 * p
    degree_cap = 11 * (p - 1) // 256
    ratio_floor = 1 + (p * p - p + degree_cap - 1) // degree_cap
    assert degree_cap == 153
    assert ratio_floor > (256 * p) // 11
    threshold_depth = 2 * p - 1 - degree_cap
    assert threshold_depth == 7012

    n = 8192
    row_cap = (p * (p - 1) - 1) // (n - 1)
    assert row_cap == 1566
    assert 1 + (p * (p - 1) + row_cap - 1) // row_cap > n
    assert 1 + (p * (p - 1) + row_cap) // (row_cap + 1) == n
    checks += 7

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    router = "l1_official_frobenius_checkpoint_q_router"
    endpoint = "l1_coarse_pfree_tame_tail_distance_upgrade"
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[router]["status"] == "PROVED"
    assert nodes[endpoint]["status"] == "PROVED"
    assert (router, NODE, "req") in edges
    assert (endpoint, NODE, "req") in edges
    assert (NODE, "l1_mixed_petal_amplification", "ev") in edges
    checks += 6

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "F_Y(Z)=Z^p+Q(Z)+b+c",
        "deg Q<=2p-d-1",
        "r_*(p,n)=floor((p(p-1)-1)/(n-1))",
        "floor(11(p-1)/256)",
        "|X_beta intersect lambda X_beta|<=r_d",
        "p^2-p+1",
        "d=2p-2  =>  t>=p+1",
        "does not bound that census",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_OFFICIAL_FIRST_CHECKPOINT_SPLIT_PENCIL_REDUCTION_PASS checks={checks}")


if __name__ == "__main__":
    main()
