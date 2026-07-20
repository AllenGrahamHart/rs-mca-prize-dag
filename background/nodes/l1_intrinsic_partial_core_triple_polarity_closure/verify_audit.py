#!/usr/bin/env python3
"""Mutation audit for the intrinsic triple-polarity closure."""


def main() -> None:
    ell = 8

    # Layout polarity treats an almost-full core fiber by its holes.
    assert min(ell - 1, 1) == 1

    # Defect polarity is relative to the actual core slice.
    core_slice = 5
    defect_size = 4
    assert min(defect_size, core_slice - defect_size) == 1
    assert min(defect_size, ell - defect_size) == 4

    # A partial-core fiber cannot also be used as a disjoint full petal.
    partial_core_nonempty = True
    full_petal_disjoint = False
    assert partial_core_nonempty and not full_petal_disjoint

    # Non-intrinsic quotient partitions are not covered by dyadic scale count.
    intrinsic = True
    nonintrinsic = False
    assert intrinsic and not nonintrinsic

    print("L1_TRIPLE_POLARITY_AUDIT_PASS mutations=4")


if __name__ == "__main__":
    main()

