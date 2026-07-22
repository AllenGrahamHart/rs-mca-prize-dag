#!/usr/bin/env python3
"""Verify the coarse p-free Wronskian neighbor compiler."""

from __future__ import annotations

import json
import math
from collections import defaultdict
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_coarse_pfree_wronskian_neighbor_compiler"


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


def evaluate(poly: list[int] | tuple[int, ...], point: int, prime: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * point + coefficient) % prime
    return value


def locator(points: tuple[int, ...], prime: int) -> list[int]:
    out = [1]
    for point in points:
        out = multiply(out, [-point, 1], prime)
    return out


def certificate_count(q: int, tail: int, degree: int) -> int:
    return sum(
        (-1) ** j
        * math.comb(tail, j)
        * q ** max(degree + 1 - j, 0)
        for j in range(tail + 1)
    )


def main() -> None:
    checks = 0

    # Replay the full-support inclusion-exclusion count directly.
    for prime in (2, 3, 5, 7):
        for tail in range(1, prime + 1):
            points = tuple(range(tail))
            for degree in range(4):
                direct = 0
                for coefficients in product(range(prime), repeat=degree + 1):
                    if all(evaluate(coefficients, x, prime) for x in points):
                        direct += 1
                assert direct == certificate_count(prime, tail, degree)
                checks += 1

    # Exhaust small prime-field coarse fibers. Check degree, full support,
    # fixed-X injectivity, and the complete neighbor bound.
    for prime in (2, 3, 5, 7):
        universe = tuple(range(prime))
        for size in range(1, prime + 1):
            subsets = tuple(combinations(universe, size))
            for depth in range(1, size + 1):
                exponents = tuple(j for j in range(1, depth + 1) if j % prime)
                fibers: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
                for subset in subsets:
                    key = tuple(
                        sum(pow(point, exponent, prime) for point in subset) % prime
                        for exponent in exponents
                    )
                    fibers[key].append(subset)

                tau = max(
                    math.ceil((depth + 2) / 2),
                    min(depth + 1, prime),
                )
                endpoint = min(size, prime - size)
                neighbor_bound = 1
                for tail in range(tau, endpoint + 1):
                    degree = 2 * tail - depth - 2
                    neighbor_bound += math.comb(size, tail) * min(
                        math.comb(prime - size, tail),
                        certificate_count(prime, tail, degree),
                    )

                for fiber in fibers.values():
                    assert len(fiber) <= neighbor_bound
                    checks += 1
                    for anchor in fiber:
                        seen: dict[tuple[tuple[int, ...], tuple[int, ...]], tuple[int, ...]] = {}
                        anchor_set = set(anchor)
                        for other in fiber:
                            if other == anchor:
                                continue
                            other_set = set(other)
                            x_tail = tuple(sorted(anchor_set - other_set))
                            y_tail = tuple(sorted(other_set - anchor_set))
                            tail = len(x_tail)
                            degree = 2 * tail - depth - 2
                            fx = locator(x_tail, prime)
                            fy = locator(y_tail, prime)
                            wronskian = subtract(
                                multiply(derivative(fx, prime), fy, prime),
                                multiply(fx, derivative(fy, prime), prime),
                                prime,
                            )
                            assert wronskian != [0]
                            assert len(wronskian) - 1 <= degree
                            assert all(
                                evaluate(wronskian, point, prime)
                                for point in x_tail + y_tail
                            )
                            record = (x_tail, tuple(wronskian))
                            assert record not in seen
                            seen[record] = other
                            checks += 4

    for depth in range(1, 30):
        tau_0 = math.ceil((depth + 2) / 2)
        for excess in range(8):
            degree = 2 * (tau_0 + excess) - depth - 2
            assert degree == 2 * excess + (depth % 2)
            checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    supplier = "l1_coarse_pfree_wronskian_distance_packing"
    endpoint = "l1_coarse_pfree_tame_tail_distance_upgrade"
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[supplier]["status"] == "PROVED"
    assert nodes[endpoint]["status"] == "PROVED"
    assert (supplier, NODE, "req") in edges
    assert (endpoint, NODE, "req") in edges
    assert (NODE, "l1_mixed_petal_amplification", "ev") in edges
    checks += 6

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "W_(X,Y)=F_X'F_Y-F_XF_Y'",
        "R_q(t,D)=sum_(j=0)^t",
        "tau_p=max(tau_0,min(d+1,p))",
        "binom(a,t) min(binom(n-a,t),R_q(t,2t-d-2))",
        "D_t=2j+1",
        "choice of `X` can",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_COARSE_PFREE_WRONSKIAN_NEIGHBOR_COMPILER_PASS checks={checks}")


if __name__ == "__main__":
    main()
