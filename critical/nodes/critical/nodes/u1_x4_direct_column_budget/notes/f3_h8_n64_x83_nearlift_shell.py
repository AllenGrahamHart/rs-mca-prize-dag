#!/usr/bin/env python3
"""Adversarial one-exchange shell around paid h=8 n=64 square-lifts.

The preceding x83 interface packet verifies the paid antipodal branch.  This
script checks the nearest non-antipodal shell: remove one root from a paid
16-support and insert one root outside it.  Any full x83-zero support in this
shell would be an immediate primitive/norm-gate candidate to isolate.
"""

from __future__ import annotations

from f3_h8_n64_x83_obstruction_interface import (
    antipodal_lift,
    forced_obstructions,
    h4_anchored_trades,
    is_square_mod,
    locator_from_exponents,
    root_table,
)
from itertools import combinations
import os


EXPECTED_ROWS = {
    (1, 4289): {"paid_supports": 7, "shell_supports": 5376, "first_zero": 0, "full_zero": 0},
    (1, 262337): {"paid_supports": 7, "shell_supports": 5376, "first_zero": 0, "full_zero": 0},
    (2, 4289): {"paid_supports": 7, "shell_supports": 947520, "first_zero": 1504, "full_zero": 0},
    (2, 262337): {"paid_supports": 7, "shell_supports": 947520, "first_zero": 1344, "full_zero": 0},
}


def paid_lift_supports(p: int) -> list[tuple[int, ...]]:
    supports = []
    for left4, right4, is_paid_toral in h4_anchored_trades(p):
        if not is_paid_toral:
            continue
        support = tuple(sorted(set(antipodal_lift(left4)) | set(antipodal_lift(right4))))
        if len(support) != 16:
            raise AssertionError((p, left4, right4, support))
        supports.append(support)
    return sorted(set(supports))


def scan_exchange_shell(p: int, radius: int) -> dict[str, int]:
    if radius not in (1, 2):
        raise ValueError("supported shell radii are 1 and 2")
    vals = root_table(p, 64)
    bases = paid_lift_supports(p)
    shell: set[tuple[int, ...]] = set()
    for support in bases:
        support_set = set(support)
        outside = [e for e in range(64) if e not in support_set]
        for removed in combinations(support, radius):
            reduced = support_set - set(removed)
            for added in combinations(outside, radius):
                candidate = tuple(sorted(reduced | set(added)))
                if len(candidate) != 16:
                    raise AssertionError((p, support, removed, added, candidate))
                shell.add(candidate)

    full_zero = 0
    first_zero = 0
    first_candidate: tuple[int, ...] | None = None
    for support in sorted(shell):
        L = locator_from_exponents(support, vals, p)
        _, obs, lam = forced_obstructions(L, p, 8)
        first_zero += int(obs[-1] == 0)
        if all(v == 0 for v in obs) and lam != 0 and is_square_mod(lam, p):
            full_zero += 1
            if first_candidate is None:
                first_candidate = support

    if full_zero:
        raise AssertionError((p, full_zero, first_candidate))
    return {
        "paid_supports": len(bases),
        "shell_supports": len(shell),
        "first_zero": first_zero,
        "full_zero": full_zero,
    }


def main() -> None:
    radius = int(os.environ.get("F3_H8_X83_SHELL_RADIUS", "1"))
    primes = tuple(
        int(item)
        for item in os.environ.get("F3_H8_X83_SHELL_PRIMES", "4289,262337").split(",")
        if item
    )
    label = {1: "one-exchange", 2: "two-exchange"}[radius]
    for p in primes:
        row = scan_exchange_shell(p, radius)
        expected = EXPECTED_ROWS.get((radius, p))
        if expected is not None and row != expected:
            raise AssertionError((radius, p, row, expected))
        print(
            f"p={p} {label} shell: paid={row['paid_supports']} "
            f"supports={row['shell_supports']} full_zero={row['full_zero']} "
            f"first_obstruction_zero={row['first_zero']}"
        )
    digest = "H8_N64_X83_NEARLIFT_SHELL_PASS"
    if radius == 2:
        digest = "H8_N64_X83_NEARLIFT_RADIUS2_PASS"
    print(digest)


if __name__ == "__main__":
    main()
