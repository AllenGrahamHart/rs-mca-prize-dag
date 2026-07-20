#!/usr/bin/env python3
"""Finite replay for the distance-three external split-design identity."""

from __future__ import annotations

from collections import Counter


P = 101


def locator(roots: tuple[int, ...], x: int) -> int:
    value = 1
    for root in roots:
        value = value * (x - root) % P
    return value


def main() -> None:
    e = 2
    roots_a = (1, 2, 3, 4)
    triple = (5, 6, 7)
    pairs = ((1, 2), (3, 4))
    outside = tuple(range(8, 24))
    omitted = 23
    active = tuple(x for x in outside if x != omitted)

    external = (
        (8, 9, 10, 11, 12),
        (13, 14, 15, 16, 17),
        (18, 19, 20, 21, 22),
        (8, 13, 18, 10, 15),
        (9, 14, 19, 11, 16),
        (12, 17, 20, 21, 22),
    )
    counts = Counter(x for block in external for x in block)
    assert len(external) == 3 * e
    assert all(len(block) == 2 * e + 1 for block in external)
    assert all(counts[x] == e for x in active)
    assert counts[omitted] == 0

    internal = tuple(
        triple + tuple(root for root in roots_a if root not in pair)
        for pair in pairs
    )
    for x in range(0, P):
        exceptional_internal = locator(roots_a, x)
        for roots in internal:
            exceptional_internal = exceptional_internal * locator(roots, x) % P
        canonical_power = pow(locator(roots_a + triple, x), e, P)
        assert exceptional_internal == canonical_power

        external_product = 1
        for roots in external:
            external_product = external_product * locator(roots, x) % P
        complement_power = pow(locator(active, x), e, P)
        assert external_product == complement_power

        full_product = exceptional_internal * external_product % P
        saturated_power = pow(locator(roots_a + triple + active, x), e, P)
        assert full_product == saturated_power

    # Repeating one point destroys regularity and the exact power identity.
    mutated = list(external)
    mutated[-1] = (12, 17, 20, 21, 8)
    mutated_counts = Counter(x for block in mutated for x in block)
    assert mutated_counts[8] == e + 1
    assert mutated_counts[22] == e - 1
    # Use a nonroot witness to see the polynomial values differ.
    witness = 24
    mutated_product = 1
    for roots in mutated:
        mutated_product = mutated_product * locator(roots, witness) % P
    assert mutated_product != pow(locator(active, witness), e, P)

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_"
        "DISTANCE_THREE_EXTERNAL_SPLIT_DESIGN_SATURATION_PASS "
        f"e={e} blocks={len(external)} active={len(active)} omitted={omitted}"
    )


if __name__ == "__main__":
    main()
