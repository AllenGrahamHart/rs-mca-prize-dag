#!/usr/bin/env python3
"""Integer audit for the calibrated dihedral trace-collision exclusion."""

from __future__ import annotations


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def audit_threshold(e: int) -> None:
    require(e >= 31, "threshold audit called below its stated range")
    minimum_complement_count = 3 * e - 3
    external_block_size = 2 * e + 1
    minimum_column_weight = minimum_complement_count - external_block_size
    require(minimum_column_weight == e - 4, "column-weight arithmetic failed")

    feasible_sizes = []
    for class_size in range(1, min(e, 128) + 1):
        lower = (e - 4) * (e - class_size)
        upper = 2 * (3 * e - class_size)
        if lower <= upper:
            feasible_sizes.append(class_size)
    if e <= 128:
        require(feasible_sizes, "collision inequality has no feasible class")
        require(min(feasible_sizes) >= e - 4, "collision inequality permits excess defect")
    else:
        require((e - 6) * 5 > 4 * e, "defect-five exclusion failed")

    maximum_classes = (3 * e) // (e - 4)
    minimum_classes = (3 * e + e - 1) // e
    require(maximum_classes == 3, "class lower bound does not force at most three")
    require(minimum_classes == 3, "class upper bound does not force at least three")
    require(minimum_complement_count > 3, "three classes could host every complement")


def main() -> None:
    for e in (31, 32, 47, 127, (1 << 38) - 1):
        audit_threshold(e)
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_DISTANCE_THREE_"
        "DIHEDRAL_TRACE_COLLISION_EXCLUSION_PASS threshold=31 "
        f"official_e={(1 << 38) - 1}"
    )


if __name__ == "__main__":
    main()
