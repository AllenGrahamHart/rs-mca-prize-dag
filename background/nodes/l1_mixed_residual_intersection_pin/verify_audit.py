#!/usr/bin/env python3
"""Mutation audit for the L1 mixed-residual intersection pin."""


def paid(ell: int, d: int, root: int, g2: int, gr: int) -> bool:
    return root <= 2 or (d <= ell + 1 and (g2 <= 2 or gr <= 1))


def residual(ell: int, d: int, root: int, g2: int, gr: int) -> bool:
    return root > 2 and (d > ell + 1 or (g2 > 2 and gr > 1))


def main() -> None:
    cases = [
        # Paid only by the G_2 arm.
        (8, 9, 3, 2, 5),
        # Paid only by the G_R arm.
        (8, 9, 3, 5, 1),
        # Inclusive defect boundary.
        (8, 9, 3, 5, 5),
        # Root-pinning payment outside the anchor box.
        (8, 12, 2, 5, 5),
        # Genuine residual.
        (8, 12, 3, 5, 5),
    ]
    for case in cases:
        assert residual(*case) == (not paid(*case))

    # Mutation: use AND between the two anchor gates.
    and_paid = lambda ell, d, root, g2, gr: root <= 2 or (
        d <= ell + 1 and (g2 <= 2 and gr <= 1)
    )
    assert any(and_paid(*case) != paid(*case) for case in cases)

    # Mutation: make the bounded defect comparison strict.
    strict_paid = lambda ell, d, root, g2, gr: root <= 2 or (
        d < ell + 1 and (g2 <= 2 or gr <= 1)
    )
    assert any(strict_paid(*case) != paid(*case) for case in cases)

    # Mutation: union rather than intersect the two residual complements.
    union_residual = lambda ell, d, root, g2, gr: root > 2 or (
        d > ell + 1 or (g2 > 2 and gr > 1)
    )
    assert any(union_residual(*case) != residual(*case) for case in cases)

    print("L1_MIXED_RESIDUAL_INTERSECTION_AUDIT_PASS mutations=3")


if __name__ == "__main__":
    main()
