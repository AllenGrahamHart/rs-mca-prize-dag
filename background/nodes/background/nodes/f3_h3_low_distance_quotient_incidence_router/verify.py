#!/usr/bin/env python3
"""Verify the H3 low-distance edge–quotient incidence router."""

from __future__ import annotations

import collections
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_low_distance_quotient_incidence_router"
DEPENDENCIES = {
    "f3_h3_high_excess_low_distance_moment_reduction",
    "f3_h3_distance_four_cross_overlap_router",
}
CONSUMER = "f3_h3_mobius_excess_half"


def vector(pair: tuple[int, int], order: int) -> dict[int, int]:
    out: collections.Counter[int] = collections.Counter()
    half = order // 2
    for exponent, coefficient in (
        ((pair[0] + pair[1]) % order, 1),
        (pair[0], -1),
        (pair[1], -1),
    ):
        if exponent >= half:
            exponent -= half
            coefficient = -coefficient
        out[exponent] += coefficient
    return {key: value for key, value in out.items() if value}


def distance(left: dict[int, int], right: dict[int, int]) -> int:
    return sum(
        (left.get(key, 0) - right.get(key, 0)) ** 2
        for key in left.keys() | right.keys()
    )


def order_root(prime: int, order: int) -> int:
    for base in range(2, prime):
        root = pow(base, (prime - 1) // order, prime)
        if pow(root, order // 2, prime) == prime - 1:
            return root
    raise AssertionError((prime, order))


def finite_identity_check() -> tuple[int, int]:
    order, prime = 32, 97
    root = order_root(prime, order)
    powers = [pow(root, exponent, prime) for exponent in range(order)]
    logs = {value: exponent for exponent, value in enumerate(powers)}
    pairs = list(itertools.combinations_with_replacement(range(1, order), 2))
    vectors = {pair: vector(pair, order) for pair in pairs}
    small = [pair for pair in pairs if sum(value * value for value in vectors[pair].values()) <= 3]
    fibers: dict[int, list[tuple[int, int]]] = collections.defaultdict(list)
    quotients: dict[int, list[tuple[int, int]]] = collections.defaultdict(list)
    for pair in small:
        target = (1 - powers[pair[0]]) * (1 - powers[pair[1]]) % prime
        fibers[target].append(pair)
    for z in range(1, order):
        for w in range(1, order):
            target = (1 - powers[w]) * pow(1 - powers[z], prime - 2, prime) % prime
            quotients[target].append((z, w))

    direct = {4: 0, 6: 0}
    for target, fiber in fibers.items():
        if target == 1:
            continue
        for left, right in itertools.combinations(sorted(fiber), 2):
            square = distance(vectors[left], vectors[right])
            if square in direct:
                direct[square] += len(quotients[target])

    routed = {4: 0, 6: 0}
    inverse = {value: pow(value, prime - 2, prime) for value in range(1, prime)}
    for x in range(1, order):
        for y in range(x, order):
            left = (x, y)
            if left not in vectors or left not in small:
                continue
            target = (1 - powers[x]) * (1 - powers[y]) % prime
            if target == 1:
                continue
            for u in range(1, order):
                numerator = (powers[x] + powers[y] - powers[x] * powers[y] - powers[u]) % prime
                v_value = numerator * inverse[(1 - powers[u]) % prime] % prime
                if v_value not in logs or logs[v_value] == 0:
                    continue
                v = logs[v_value]
                if u > v:
                    continue
                right = (u, v)
                if right not in vectors or right not in small or not left < right:
                    continue
                square = distance(vectors[left], vectors[right])
                if square not in routed:
                    continue
                for z in range(1, order):
                    w_value = (1 - target * (1 - powers[z])) % prime
                    if w_value in logs and logs[w_value] != 0:
                        routed[square] += 1
    assert routed == direct
    return direct[4], direct[6]


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    for dependency in DEPENDENCIES:
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md",
        "dependency_subdag.md", "audit.md", "result.md", "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = (base / "statement.md").read_text() + (base / "proof.md").read_text()
    for marker in ("M_33=2|I_4|+|I_6|", "v=(x+y-xy-u)/(1-u)", "w=1-t(1-z)"):
        assert marker in text


def main() -> None:
    distance_four, distance_six = finite_identity_check()
    packet_check()
    print(
        "F3_H3_LOW_DISTANCE_QUOTIENT_INCIDENCE_ROUTER_PASS "
        f"n32_d4={distance_four} n32_d6={distance_six}"
    )


if __name__ == "__main__":
    main()
