#!/usr/bin/env python3
"""Independent scalar audit of the budget-three incidence classification."""

from __future__ import annotations


def main() -> None:
    raw = []
    for n0 in range(3):
        for n1 in range(4):
            for n2 in range(8):
                n4 = 3 * n0 + 2 * n1 + n2 - 4
                if n4 < 0:
                    continue
                pair_deficit = 3 * n0 + 3 * n1 + 2 * n2 - 3 * n4
                if pair_deficit >= 6:
                    raw.append((n0, n1, n2, n4))
    assert raw == [
        (0, 0, 4, 0),
        (0, 0, 5, 1),
        (0, 0, 6, 2),
        (0, 1, 2, 0),
        (0, 1, 3, 1),
        (0, 2, 0, 0),
    ]

    # With two singleton points and no pair/full points, two codewords have
    # singleton count zero. Their intersection would have size 2d, one above
    # the MDS cap 2d-1.
    singleton_distributions = []
    for first in range(4):
        for second in range(first, 4):
            counts = [0] * 4
            counts[first] += 1
            counts[second] += 1
            singleton_distributions.append(tuple(counts))
            assert any(
                counts[i] + counts[j] == 0
                for i in range(4)
                for j in range(i + 1, 4)
            )

    assert len(singleton_distributions) == 10
    print(
        "AUDIT_RATE_HALF_LIST_BUDGET_THREE_INTERSECTION_REDUCTION_PASS "
        f"raw_patterns={len(raw)} impossible_singleton_labels={len(singleton_distributions)}"
    )


if __name__ == "__main__":
    main()
