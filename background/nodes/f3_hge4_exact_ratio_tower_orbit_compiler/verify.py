#!/usr/bin/env python3
"""Verify the HGE4 exact-ratio tower orbit compiler."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_exact_ratio_tower_orbit_compiler"
DEPENDENCIES = {
    "f3_hge4_primitive_shift_pair_orbit_aggregate_router",
    "f3_hge4_nonfull_near_square_straight_line_lift",
}
CONSUMER = "f3_hge4_norm_gate_count"


def primitive_root(prime: int) -> int:
    factors = []
    value = prime - 1
    trial = 2
    while trial * trial <= value:
        if value % trial == 0:
            factors.append(trial)
            while value % trial == 0:
                value //= trial
        trial += 1
    if value > 1:
        factors.append(value)
    for candidate in range(2, prime):
        if all(
            pow(candidate, (prime - 1) // factor, prime) != 1
            for factor in factors
        ):
            return candidate
    raise AssertionError("no primitive root")


def signature(
    exponents: tuple[int, ...], points: list[int], width: int, prime: int
) -> tuple[int, ...]:
    locator = [1]
    for exponent in exponents:
        root = points[exponent]
        locator.append(0)
        for degree in range(len(locator) - 1, 0, -1):
            locator[degree] = (
                locator[degree] - root * locator[degree - 1]
            ) % prime
    return tuple(locator[1:width])


def translate(
    support: frozenset[int], shift: int, order: int
) -> frozenset[int]:
    return frozenset((value + shift) % order for value in support)


def orbit_key(
    left: frozenset[int], right: frozenset[int], order: int
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    return min(
        (
            tuple(sorted(translate(left, shift, order))),
            tuple(sorted(translate(right, shift, order))),
        )
        for shift in range(order)
    )


def is_primitive(
    left: frozenset[int], right: frozenset[int], order: int
) -> bool:
    return all(
        shift == 0
        or translate(left, shift, order) != left
        or translate(right, shift, order) != right
        for shift in range(order)
    )


def exact_level(
    left: frozenset[int], right: frozenset[int], order: int
) -> tuple[int, tuple[tuple[int, ...], tuple[int, ...]]]:
    anchor = next(iter(left))
    step = order
    for exponent in left | right:
        step = gcd(step, (exponent - anchor) % order)
    level = order // step
    normalized_left = frozenset(
        ((value - anchor) % order) // step for value in left
    )
    normalized_right = frozenset(
        ((value - anchor) % order) // step for value in right
    )
    return level, orbit_key(normalized_left, normalized_right, level)


def primitive_pairs(
    order: int, prime: int, width: int
) -> list[tuple[frozenset[int], frozenset[int]]]:
    generator = primitive_root(prime)
    omega = pow(generator, (prime - 1) // order, prime)
    points = [pow(omega, exponent, prime) for exponent in range(order)]
    buckets: dict[tuple[int, ...], list[frozenset[int]]] = defaultdict(list)
    for raw in combinations(range(order), width):
        buckets[signature(raw, points, width, prime)].append(frozenset(raw))

    output = []
    for bucket in buckets.values():
        for left in bucket:
            for right in bucket:
                if (
                    left != right
                    and left.isdisjoint(right)
                    and is_primitive(left, right, order)
                ):
                    output.append((left, right))
    return output


def level_orbits(
    order: int, prime: int, width: int
) -> set[tuple[tuple[int, ...], tuple[int, ...]]]:
    output = set()
    for left, right in primitive_pairs(order, prime, width):
        level, key = exact_level(left, right, order)
        if level == order:
            output.add(key)
    return output


def census_check(width: int) -> tuple[int, dict[int, int]]:
    order, prime = 16, 17
    pairs = primitive_pairs(order, prime, width)
    ambient = {
        orbit_key(left, right, order): (left, right) for left, right in pairs
    }
    image = {}
    anchor_counts: Counter[
        tuple[tuple[int, ...], tuple[int, ...]]
    ] = Counter()
    for left, right in pairs:
        ambient_key = orbit_key(left, right, order)
        if 0 in left:
            anchor_counts[ambient_key] += 1
    for ambient_key, pair in ambient.items():
        routed = exact_level(*pair, order)
        assert routed not in image
        image[routed] = ambient_key

    independent = {}
    level = 1
    while level <= order:
        if level >= 2 * width:
            for key in level_orbits(level, prime, width):
                independent[(level, key)] = True
        level *= 2
    assert set(image) == set(independent)
    assert set(anchor_counts) == set(ambient)
    assert set(anchor_counts.values()) == {width}
    return len(ambient), dict(
        sorted(Counter(level for level, _ in image).items())
    )


def geometric_check() -> None:
    for exponent in range(3, 42):
        order = 2**exponent
        square_sum = sum((2**level) ** 2 for level in range(exponent + 1))
        assert square_sum == (4 * order * order - 1) // 3
        assert Fraction(21, 2) * square_sum < 14 * order * order
        assert 11 * square_sum > 14 * order * order


def exact_selector_fixture() -> None:
    prime, order = 97, 32
    generator = primitive_root(prime)
    omega = pow(generator, (prime - 1) // order, prime)

    def center(value: int) -> int:
        return (
            pow(value, 5, prime)
            + 73 * pow(value, 3, prime)
            + 78 * value
        ) % prime

    shift = 55
    left = frozenset(
        exponent
        for exponent in range(order)
        if center(pow(omega, exponent, prime)) == shift
    )
    right = frozenset(
        exponent
        for exponent in range(order)
        if center(pow(omega, exponent, prime)) == -shift % prime
    )
    assert len(left) == len(right) == 5 and left.isdisjoint(right)
    assert 0 in left and center(1) == shift
    assert exact_level(left, right, order)[0] == order
    assert any((exponent % 2) for exponent in left | right)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {
        (edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]
    }
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join(
        (base / name).read_text() for name in required if name.endswith(".md")
    )
    for marker in (
        "O_h^prim(n,p)=sum_(m|n, m>=2h) E_h^prim(m,p)",
        "C_h^prim(m,p)=h E_h^prim(m,p)",
        "(21/2)m^2",
        "(4n^2-1)/3",
        "V_(r-1)!=1",
        "No estimate `(ERT4)`",
    ):
        assert marker in text


def main() -> None:
    h4_orbits, h4_levels = census_check(4)
    h2_orbits, h2_levels = census_check(2)
    assert (h4_orbits, h4_levels) == (14, {16: 14})
    assert (h2_orbits, h2_levels) == (42, {8: 2, 16: 40})
    exact_selector_fixture()
    geometric_check()
    packet_check()
    print(
        "F3_HGE4_EXACT_RATIO_TOWER_ORBIT_COMPILER_PASS "
        "h4_orbits=14 h2_levels=8:2,16:40 rows=39"
    )


if __name__ == "__main__":
    main()
