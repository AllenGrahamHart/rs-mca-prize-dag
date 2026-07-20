#!/usr/bin/env python3
"""Independent exhaustive degree-two audit of the parity-kernel claim."""

from __future__ import annotations

from itertools import product


PRIME = 7


def locator(root: int, second_root: int) -> tuple[int, int, int, int]:
    # (X+r)(X^2-b), where H(Y)=(Y-r^2)(Y-b).
    return (
        -root * second_root % PRIME,
        -second_root % PRIME,
        root % PRIME,
        1,
    )


def zero_relation(
    locators: tuple[tuple[int, int, int, int], ...],
    weights: tuple[int, int, int],
) -> bool:
    return all(
        sum(weight * polynomial[degree] for weight, polynomial in zip(weights, locators, strict=True))
        % PRIME
        == 0
        for degree in range(4)
    )


def audit_roots(roots: tuple[int, int, int]) -> tuple[int, int]:
    survivors = 0
    tested = 0
    nonzero_weights = list(product(range(1, PRIME), repeat=3))
    for second_roots in product(range(PRIME), repeat=3):
        locators = tuple(
            locator(root, second_root)
            for root, second_root in zip(roots, second_roots, strict=True)
        )
        for weights in nonzero_weights:
            tested += 1
            if not zero_relation(locators, weights):
                continue
            survivors += 1
            assert len(set(second_roots)) == 1
    assert survivors > 0
    return tested, survivors


def main() -> None:
    tested = 0
    survivors = 0
    for roots in ((1, 2, 3), (1, 6, 2)):
        local_tested, local_survivors = audit_roots(roots)
        tested += local_tested
        survivors += local_survivors
    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_PATH_EXCLUSION_AUDIT_PASS "
        f"prime={PRIME} systems={tested} relations={survivors} "
        "all_relations_share_quadratic=1"
    )


if __name__ == "__main__":
    main()
