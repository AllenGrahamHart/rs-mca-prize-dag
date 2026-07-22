#!/usr/bin/env python3
"""Verify coarse p-free Wronskian distance packing."""

from __future__ import annotations

import json
import math
from collections import defaultdict
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_coarse_pfree_wronskian_distance_packing"


def gf4_mul(a: int, b: int) -> int:
    product = 0
    left = a
    right = b
    while right:
        if right & 1:
            product ^= left
        right >>= 1
        left <<= 1
    for bit in range(4, 1, -1):
        if product & (1 << bit):
            product ^= 0b111 << (bit - 2)
    return product


def gf4_pow(a: int, exponent: int) -> int:
    result = 1
    base = a
    while exponent:
        if exponent & 1:
            result = gf4_mul(result, base)
        base = gf4_mul(base, base)
        exponent >>= 1
    return result


def moment(points: tuple[int, ...], exponent: int) -> int:
    total = 0
    for point in points:
        total ^= gf4_pow(point, exponent)
    return total


def main() -> None:
    checks = 0

    # In F_4=F_2[alpha]/(alpha^2+alpha+1), these disjoint pairs have
    # equal moments through depth two. The only p-free coordinate is S_1.
    first = (0, 1)
    second = (2, 3)
    assert moment(first, 1) == moment(second, 1) == 1
    assert moment(first, 2) == moment(second, 2) == 1
    tau = math.ceil((2 + 2) / 2)
    assert tau == 2
    assert len(set(first) - set(second)) == tau
    checks += 4

    # The tail polynomials are Z^2+Z and Z^2+Z+1; their ordinary
    # Wronskian is the nonzero constant one, attaining degree 2t-d-2=0.
    assert 2 * 2 - 2 - 2 == 0
    checks += 1

    s = 2 - tau + 1
    cap = math.comb(4, s) // math.comb(2, s)
    assert s == 1
    assert cap == 2
    checks += 2

    # Exhaust every subset and p-free prefix over several small prime fields.
    # This is a non-load-bearing replay of both the distance and packing claims.
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

                local_tau = math.ceil((depth + 2) / 2)
                local_s = size - local_tau + 1
                local_cap = math.comb(prime, local_s) // math.comb(size, local_s)
                for fiber in fibers.values():
                    assert len(fiber) <= local_cap
                    checks += 1
                    for first_set, second_set in combinations(fiber, 2):
                        tail = len(set(first_set) - set(second_set))
                        assert tail >= local_tau
                        checks += 1

    # When s>=n/2, the numerical packing ceiling is at least 2^(n-a).
    for n in range(4, 31):
        for k in range(1, n):
            for a in range(k + 1, n + 1):
                depth = a - k
                local_tau = math.ceil((depth + 2) / 2)
                local_s = a - local_tau + 1
                if 2 * local_s < n:
                    continue
                cap = math.comb(n, local_s) // math.comb(a, local_s)
                assert cap >= 2 ** (n - a)
                checks += 1

    # The deployed KoalaBear crossing lies very far inside the range where
    # the cap itself cannot fit the official numerator. No large binomial is
    # materialized here.
    deployed_n = 2**21
    deployed_k = 2**20
    for deployed_a in (1_116_047, 1_116_048):
        deployed_s = (deployed_a + deployed_k) // 2
        assert 2 * deployed_s >= deployed_n
        assert deployed_n - deployed_a >= 128
        checks += 2
    assert (1 << 128) > 274_980_728_111_395_087
    checks += 1

    for k in range(1, 12):
        for d in range(1, 12):
            a = k + d
            local_tau = math.ceil((d + 2) / 2)
            local_s = a - local_tau + 1
            assert local_s == (a + k) // 2
            checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    supplier = "l1_official_frobenius_checkpoint_q_router"
    assert nodes[supplier]["status"] == "PROVED"
    assert (supplier, NODE, "req") in edges
    assert (NODE, "l1_mixed_petal_amplification", "ev") in edges
    checks += 4

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "t>=tau:=ceil((d+2)/2)",
        "deg W<=2t-d-2",
        "floor(binom(n,s)/binom(a,s))",
        "s=floor((a+k)/2)",
        ">=2^r",
        "stronger elementary bound `t>=d+1`",
        "can remain exponential",
    ):
        assert anchor in statement or anchor in (
            ROOT / "background" / "nodes" / NODE / "proof.md"
        ).read_text()
        checks += 1

    print(f"L1_COARSE_PFREE_WRONSKIAN_DISTANCE_PACKING_PASS checks={checks}")


if __name__ == "__main__":
    main()
