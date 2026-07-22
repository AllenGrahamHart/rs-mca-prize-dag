#!/usr/bin/env python3
"""Verify the XR quotient remainder-one boundary descent."""

from __future__ import annotations

from itertools import combinations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_quotient_image_remainder_one_boundary_descent"
DEPENDENCY = "xr_threshold_quotient_image_lcm_normal_form"
CONSUMER = "xr_tangent_support_mismatch_bridge"


def support_family(length: int, fiber_size: int, size: int) -> tuple[frozenset[int], ...]:
    fibers = tuple(
        frozenset(range(start, start + fiber_size))
        for start in range(0, length, fiber_size)
    )
    full_count, remainder = divmod(size, fiber_size)
    supports: set[frozenset[int]] = set()
    for selected in combinations(range(len(fibers)), full_count):
        core = frozenset().union(*(fibers[index] for index in selected))
        outside = tuple(index for index in range(length) if index not in core)
        for tail in combinations(outside, remainder):
            support = core | frozenset(tail)
            if sum(fiber <= support for fiber in fibers) == full_count:
                supports.add(support)
    return tuple(sorted(supports, key=lambda support: tuple(support)))


def contained(
    prime: int,
    left: tuple[int, ...],
    right: tuple[int, ...],
    support: frozenset[int],
) -> bool:
    left_constant = len({left[index] for index in support}) <= 1
    right_constant = len({right[index] for index in support}) <= 1
    return left_constant and right_constant


def roots(
    prime: int,
    left: tuple[int, ...],
    right: tuple[int, ...],
    support: frozenset[int],
) -> frozenset[int]:
    if contained(prime, left, right, support):
        return frozenset()
    return frozenset(
        slope
        for slope in range(prime)
        if len({(left[index] + slope * right[index]) % prime for index in support}) <= 1
    )


def exhaustive_fixture() -> tuple[int, int, int]:
    prime = 3
    length = 4
    fiber_size = 2
    agreement = 2
    families = {
        size: support_family(length, fiber_size, size)
        for size in range(agreement, length + 1)
    }
    assert {size: len(family) for size, family in families.items()} == {2: 2, 3: 4, 4: 1}

    pairs = 0
    boundary_occurrences = 0
    slope_equalities = 0
    vectors = tuple(product(range(prime), repeat=length))
    fibers = tuple(frozenset((start, start + 1)) for start in range(0, length, 2))
    for left in vectors:
        for right in vectors:
            exact = frozenset().union(
                *(roots(prime, left, right, support) for support in families[agreement])
            )
            boundary: set[int] = set()
            for size in range(agreement + 1, length + 1):
                if size % fiber_size != 1:
                    continue
                for support in families[size]:
                    tail = tuple(
                        index
                        for index in support
                        if not any(index in fiber and fiber <= support for fiber in fibers)
                    )
                    assert len(tail) == 1
                    predecessor = support - frozenset(tail)
                    if contained(prime, left, right, predecessor):
                        support_roots = roots(prime, left, right, support)
                        boundary.update(support_roots)
                        boundary_occurrences += len(support_roots)

            threshold = frozenset().union(
                *(
                    roots(prime, left, right, support)
                    for size in range(agreement, length + 1)
                    for support in families[size]
                )
            )
            assert threshold == exact | boundary
            slope_equalities += 1
            pairs += 1
    assert boundary_occurrences > 0
    return pairs, boundary_occurrences, slope_equalities


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "Q_c(>=A)=Q_c(A)unionT_c(A)",
        "p_z=c_0+zc_1",
        "doesnotboundtheboundarytangentimage",
    ):
        assert marker in statement


def main() -> None:
    pairs, boundary, equalities = exhaustive_fixture()
    packet_check()
    print(
        "XR_QUOTIENT_IMAGE_REMAINDER_ONE_BOUNDARY_DESCENT_PASS "
        f"pairs={pairs} boundary={boundary} equalities={equalities}"
    )


if __name__ == "__main__":
    main()
