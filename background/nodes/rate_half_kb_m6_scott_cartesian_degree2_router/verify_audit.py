#!/usr/bin/env python3
"""Independent explicit permutation audit for the m=6 kernel-free chains."""

from collections import deque
from pathlib import Path

NODE = Path(__file__).resolve().parent
N = 10
ODD_BLOCK = frozenset((0, 2, 4, 6, 8))
IDENTITY = tuple(range(N))


def cycle(*cycles: tuple[int, ...]) -> tuple[int, ...]:
    permutation = list(IDENTITY)
    for points in cycles:
        for source, target in zip(points, points[1:] + points[:1]):
            permutation[source - 1] = target - 1
    return tuple(permutation)


def multiply(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(N))


def inverse(permutation: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * N
    for source, target in enumerate(permutation):
        result[target] = source
    return tuple(result)


def closure(generators: tuple[tuple[int, ...], ...]) -> set[tuple[int, ...]]:
    steps = generators + tuple(inverse(generator) for generator in generators)
    elements = {IDENTITY}
    queue = deque([IDENTITY])
    while queue:
        element = queue.popleft()
        for generator in steps:
            product = multiply(element, generator)
            if product not in elements:
                elements.add(product)
                queue.append(product)
    return elements


FIVE_CYCLE = cycle((2, 4, 6, 8, 10))
THREE_CYCLE = cycle((2, 4, 10))
BLOCK_SWAP = cycle((1, 6), (2, 7), (3, 8), (4, 9), (5, 10))
SIMULTANEOUS_ODD = cycle((2, 10), (5, 7))
TWISTED_SWAP = cycle((1, 6), (2, 5, 10, 7), (3, 8), (4, 9))
REMOTE_TRANSPOSITION = cycle((2, 10))
FIVE_CYCLE_GROUP = closure((FIVE_CYCLE,))

CASES = (
    ("[A5^2]2", (FIVE_CYCLE, THREE_CYCLE, BLOCK_SWAP), 7200, 720, 120, 600, 60),
    (
        "parity wreath, split",
        (FIVE_CYCLE, SIMULTANEOUS_ODD, BLOCK_SWAP),
        14400, 1440, 240, 1200, 120,
    ),
    (
        "parity wreath, twist",
        (FIVE_CYCLE, TWISTED_SWAP),
        14400, 1440, 240, 1200, 120,
    ),
    (
        "[S5^2]2",
        (FIVE_CYCLE, REMOTE_TRANSPOSITION, BLOCK_SWAP),
        28800, 2880, 480, 2400, 120,
    ),
)


def normalizes_five_cycle(permutation: tuple[int, ...]) -> bool:
    conjugate = multiply(multiply(permutation, FIVE_CYCLE), inverse(permutation))
    return conjugate in FIVE_CYCLE_GROUP


def coset_action_audit(
    group: set[tuple[int, ...]], subgroup: set[tuple[int, ...]]
) -> tuple[int, list[int]]:
    unseen = set(group)
    representatives = []
    owner = {}
    while unseen:
        representative = IDENTITY if IDENTITY in unseen else min(unseen)
        coset = {multiply(element, representative) for element in subgroup}
        index = len(representatives)
        representatives.append(representative)
        for element in coset:
            owner[element] = index
        unseen -= coset
    assert len(representatives) == 6

    unseen_points = set(range(6))
    subdegrees = []
    while unseen_points:
        point = min(unseen_points)
        orbit = {
            owner[multiply(representatives[point], element)]
            for element in subgroup
        }
        unseen_points -= orbit
        subdegrees.append(len(orbit))

    core = {
        element
        for element in subgroup
        if all(
            owner[multiply(representative, element)] == index
            for index, representative in enumerate(representatives)
        )
    }
    return len(group) // len(core), sorted(subdegrees)


def audit_case(case: tuple[object, ...]) -> tuple[str, int, int, int, int]:
    (
        name,
        generators,
        expected_g,
        expected_b,
        expected_a,
        expected_m,
        expected_quotient,
    ) = case
    group = closure(generators)
    block_kernel = {
        element
        for element in group
        if frozenset(element[index] for index in ODD_BLOCK) == ODD_BLOCK
    }
    block_stabilizer = {element for element in group if element[0] == 0}
    endpoint_stabilizer = {
        element for element in block_stabilizer if normalizes_five_cycle(element)
    }
    intermediate = {
        element for element in block_kernel if normalizes_five_cycle(element)
    }
    actual = (
        len(group),
        len(block_stabilizer),
        len(endpoint_stabilizer),
        len(intermediate),
    )
    assert actual == (expected_g, expected_b, expected_a, expected_m), (name, actual)
    assert endpoint_stabilizer <= intermediate <= group
    assert len(block_stabilizer) // len(endpoint_stabilizer) == 6
    assert len(intermediate) // len(endpoint_stabilizer) == 5
    quotient_order, subdegrees = coset_action_audit(
        block_stabilizer, endpoint_stabilizer
    )
    assert quotient_order == expected_quotient
    assert subdegrees == [1, 5]
    return str(name), *actual


def main() -> None:
    proof = (NODE / "proof.md").read_text()
    assert "The complete chain table is" in proof
    rows = tuple(audit_case(case) for case in CASES)
    assert tuple(row[1] for row in rows) == (7200, 14400, 14400, 28800)
    print("RATE_HALF_KB_M6_SCOTT_CARTESIAN_DEGREE2_ROUTER_AUDIT_PASS")


if __name__ == "__main__":
    main()
