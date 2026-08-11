#!/usr/bin/env python3
"""Degree and splitting replay for the two-point pushforward."""

M = 1 << 37
RHO = 4 * M
E = (RHO + 1) // 3
D = RHO - 1


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    rank_e = 1 + (E - 1)
    base_degree = -(E - 1) * D
    pencil_rank = 2 + (E - 2)
    canonical_rank = 3 + (E - 3)
    pencil_degree = 1 + (1 - D) + (E - 2) * (-D)
    canonical_degree = 2 * (1 - D) + (E - 3) * (-D)
    need(pencil_rank == rank_e and canonical_rank == rank_e, "rank failed")
    need(pencil_degree == base_degree + 2, "pencil degree failed")
    need(canonical_degree == base_degree + 2, "canonical degree failed")
    need(D > 1, "negative summands not negative")
    pencil_h0 = 2 + max(0, 2 - D) + (E - 2) * max(0, 1 - D)
    canonical_h0 = 1 + 2 * max(0, 2 - D) + (E - 3) * max(0, 1 - D)
    need((pencil_h0, canonical_h0) == (2, 1), "section-count ledger failed")
    print(f"TWO_POINT_PUSHFORWARD_PASS e={E} d={D} h0=(2,1)")


if __name__ == "__main__":
    main()
