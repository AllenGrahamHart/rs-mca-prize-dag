#!/usr/bin/env python3
"""Replay the h=3 repeat-boundary support compiler constants."""

from __future__ import annotations

from f3_h3_repeat_boundary_fiber_cap import line_support
from f3_h3_repeat_boundary_q0_cell import ceil_cuberoot
from f3_h3_repeat_residue_boundary_compiler import verify_row as verify_residue_row


def support_bound_row(p: int, n: int) -> dict[str, int]:
    support = line_support(p, n)
    q0_cap = ceil_cuberoot((132**3) * (n**2))
    fiber_cap = ceil_cuberoot((66**3) * (n**2))
    if support["genuine_support"] % 6:
        raise AssertionError((p, n, support["genuine_support"]))
    r_orb = support["genuine_support"] // 6
    b_line_bound = q0_cap + 6 * r_orb * fiber_cap
    residue_bound = 12 * n * b_line_bound + 18 * n * n
    if support["b_line"] > b_line_bound:
        raise AssertionError((p, n, support["b_line"], b_line_bound))
    return {
        **support,
        "r_orb": r_orb,
        "q0_cap": q0_cap,
        "fiber_cap": fiber_cap,
        "b_line_bound": b_line_bound,
        "residue_bound": residue_bound,
    }


def main() -> None:
    print("h=3 repeat-boundary support compiler")
    for p, n in ((97, 16), (97, 32), (193, 64), (257, 128)):
        row = support_bound_row(p, n)
        print(
            f"p={p} n={n} B_line={row['b_line']} "
            f"R_orb={row['r_orb']} q0_cap={row['q0_cap']} "
            f"fiber_cap={row['fiber_cap']} B_line_bound={row['b_line_bound']} "
            f"residue_bound={row['residue_bound']}"
        )

    for p, n in ((97, 16), (97, 32), (193, 64)):
        residue = verify_residue_row(p, n)["repeat_residue"]
        bound = support_bound_row(p, n)["residue_bound"]
        if residue > bound:
            raise AssertionError((p, n, residue, bound))
        print(f"p={p} n={n} repeat_residue={residue} support_bound={bound}")

    print("If R_orb <= C*n^beta, repeat_residue is O_C(n^(5/3+beta)) plus O(n^2)")
    print("Subcubic repeat residue follows from beta < 4/3")
    print("H3_REPEAT_BOUNDARY_SUPPORT_COMPILER_PASS")


if __name__ == "__main__":
    main()
