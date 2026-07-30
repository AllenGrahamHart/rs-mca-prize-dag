#!/usr/bin/env python3
"""Audit deck-invariant four-root subsets of six free fibers."""

from itertools import combinations


def main() -> None:
    fibers = tuple((2 * index, 2 * index + 1) for index in range(6))
    invariant = []
    for subset in combinations(range(12), 4):
        chosen = set(subset)
        if all((left in chosen) == (right in chosen) for left, right in fibers):
            invariant.append(chosen)
    assert len(invariant) == 15
    assert all(sum({left, right} <= chosen for left, right in fibers) == 2
               for chosen in invariant)
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_COLORED_QUOTIENT_RESULTANT_COMPILER_AUDIT_PASS "
        f"quotient_quadratics={len(invariant)}"
    )


if __name__ == "__main__":
    main()
