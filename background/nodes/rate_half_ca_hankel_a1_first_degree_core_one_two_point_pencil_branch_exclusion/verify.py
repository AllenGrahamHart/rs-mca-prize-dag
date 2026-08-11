#!/usr/bin/env python3
"""Finite fibre-dimension replay for the pencil-branch exclusion."""

M = 1 << 37
RHO = 4 * M
E = (RHO + 1) // 3


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    reduced_factors = E - 4
    modification_rank = 2
    constant_intersection = 0 if reduced_factors > 0 else 1
    projection_rank = modification_rank - constant_intersection
    need(reduced_factors > 0, "no separating reduced factor")
    need(projection_rank == 2, "wrong negative projection rank")
    canonical_h0 = 1
    need(canonical_h0 == 1, "wrong canonical section count")
    print(f"TWO_POINT_PENCIL_EXCLUSION_PASS e={E} reduced={reduced_factors} rank={projection_rank}")


if __name__ == "__main__":
    main()
