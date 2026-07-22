#!/usr/bin/env python3
"""Verify that quotient boundaries are owned by the agreement raise."""

from __future__ import annotations

from itertools import combinations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_quotient_boundary_agreement_raise_owner"
DEPENDENCIES = {
    "xr_quotient_image_remainder_one_boundary_descent",
    "xr_mismatch_terminal_tangent_agreement_raise",
}
CONSUMER = "xr_tangent_support_mismatch_bridge"


def support_family(
    length: int, fiber_size: int, size: int
) -> tuple[frozenset[int], ...]:
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
    left: tuple[int, ...],
    right: tuple[int, ...],
    support: frozenset[int],
) -> bool:
    return (
        len({left[index] for index in support}) <= 1
        and len({right[index] for index in support}) <= 1
    )


def line_roots(
    prime: int,
    left: tuple[int, ...],
    right: tuple[int, ...],
    support: frozenset[int],
) -> frozenset[int]:
    return frozenset(
        slope
        for slope in range(prime)
        if len(
            {
                (left[index] + slope * right[index]) % prime
                for index in support
            }
        )
        <= 1
    )


def quotient_roots(
    prime: int,
    left: tuple[int, ...],
    right: tuple[int, ...],
    support: frozenset[int],
) -> frozenset[int]:
    if contained(left, right, support):
        return frozenset()
    return line_roots(prime, left, right, support)


def exhaustive_fixture() -> tuple[int, int, int, int]:
    prime = 3
    length = 4
    fiber_size = 2
    agreement = 2
    families = {
        size: support_family(length, fiber_size, size)
        for size in range(agreement, length + 1)
    }
    all_supports = {
        size: tuple(frozenset(indices) for indices in combinations(range(length), size))
        for size in range(agreement + 1, length + 1)
    }
    fibers = tuple(
        frozenset((start, start + 1)) for start in range(0, length, fiber_size)
    )

    pairs = 0
    boundary_occurrences = 0
    not_owned_at_a_plus_two = 0
    exact_not_owned_at_a_plus_one = 0
    vectors = tuple(product(range(prime), repeat=length))
    for left in vectors:
        for right in vectors:
            exact = frozenset().union(
                *(
                    quotient_roots(prime, left, right, support)
                    for support in families[agreement]
                )
            )
            boundary: set[int] = set()
            for size in range(agreement + 1, length + 1):
                if size % fiber_size != 1:
                    continue
                for support in families[size]:
                    tail = tuple(
                        index
                        for index in support
                        if not any(
                            index in fiber and fiber <= support for fiber in fibers
                        )
                    )
                    assert len(tail) == 1
                    predecessor = support - frozenset(tail)
                    if contained(left, right, predecessor):
                        roots = quotient_roots(prime, left, right, support)
                        boundary.update(roots)
                        boundary_occurrences += len(roots)

            threshold = frozenset().union(
                *(
                    quotient_roots(prime, left, right, support)
                    for size in range(agreement, length + 1)
                    for support in families[size]
                )
            )
            raised = frozenset().union(
                *(
                    line_roots(prime, left, right, support)
                    for support in all_supports[agreement + 1]
                )
            )
            raised_twice = frozenset().union(
                *(
                    line_roots(prime, left, right, support)
                    for support in all_supports[agreement + 2]
                )
            )
            assert boundary <= raised
            assert threshold <= exact | raised
            not_owned_at_a_plus_two += len(boundary - raised_twice)
            exact_not_owned_at_a_plus_one += len(exact - raised)
            pairs += 1

    assert boundary_occurrences > 0
    assert not_owned_at_a_plus_two > 0
    assert exact_not_owned_at_a_plus_one > 0
    return (
        pairs,
        boundary_occurrences,
        not_owned_at_a_plus_two,
        exact_not_owned_at_a_plus_one,
    )


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "Q_c(>=A)",
        "B_(A+1)(u,v)",
        "contributesnoseparateone-point-tailboundarycurrency",
        "doesnotboundtheunionofexact-`A`quotientimages",
    ):
        assert marker in statement


def main() -> None:
    pairs, boundary, next_failures, exact_required = exhaustive_fixture()
    packet_check()
    print(
        "XR_QUOTIENT_BOUNDARY_AGREEMENT_RAISE_OWNER_PASS "
        f"pairs={pairs} boundary={boundary} "
        f"a_plus_two_failures={next_failures} exact_required={exact_required}"
    )


if __name__ == "__main__":
    main()
