#!/usr/bin/env python3
"""Guard the official private-linear route against the two-factor resultant loss.

The two-factor resultant relation has bidegree H in the two private variables.
This compiler verifies that shape on small symbolic H and checks that every
official private-linear compiler box has B-1 < H, so this specific small-H
relation cannot lie wholly inside the official B x B exponent box.
"""

from __future__ import annotations

import sympy as sp

from f3_h3_private_linear_lowrow_budget import EXPECTED_ROWS


X, U, V = sp.symbols("X U V")
ALPHA, BETA, GAMMA, DELTA = sp.symbols("alpha beta gamma delta")


def resultant_profile(h_order: int) -> tuple[int, int, int]:
    f = (X - ALPHA) ** h_order - U * (X - BETA) ** h_order
    g = (X - GAMMA) ** h_order - V * (X - DELTA) ** h_order
    poly = sp.Poly(sp.resultant(f, g, X), U, V)
    return poly.degree(U), poly.degree(V), len(poly.terms())


def official_margin_summary() -> dict[str, int]:
    min_pass_margin = None
    min_next_margin = None
    max_pass_b = 0
    max_next_b = 0
    for row in EXPECTED_ROWS:
        h_order = 1 << row.s
        pass_margin = h_order - (row.b - 1)
        next_margin = h_order - (row.next_b - 1)
        if pass_margin <= 0 or next_margin <= 0:
            raise AssertionError((row.s, h_order, row.b, row.next_b))
        min_pass_margin = (
            pass_margin if min_pass_margin is None else min(min_pass_margin, pass_margin)
        )
        min_next_margin = (
            next_margin if min_next_margin is None else min(min_next_margin, next_margin)
        )
        max_pass_b = max(max_pass_b, row.b)
        max_next_b = max(max_next_b, row.next_b)
    return {
        "rows": len(EXPECTED_ROWS),
        "first_s": EXPECTED_ROWS[0].s,
        "last_s": EXPECTED_ROWS[-1].s,
        "min_pass_margin": int(min_pass_margin),
        "min_next_margin": int(min_next_margin),
        "max_pass_b": max_pass_b,
        "max_next_b": max_next_b,
    }


def main() -> None:
    expected_profiles = {
        1: (1, 1, 4),
        2: (2, 2, 9),
        3: (3, 3, 16),
    }
    actual_profiles = {h: resultant_profile(h) for h in expected_profiles}
    if actual_profiles != expected_profiles:
        raise AssertionError(actual_profiles)

    official = official_margin_summary()
    if official["rows"] != 29 or official["first_s"] != 13 or official["last_s"] != 41:
        raise AssertionError(official)
    if official["min_pass_margin"] != 8128:
        raise AssertionError(official)
    if official["min_next_margin"] != 8129:
        raise AssertionError(official)

    print("h=3 private-linear resultant degree guard")
    for h, profile in actual_profiles.items():
        print(
            f"symbolic H={h}: deg_U={profile[0]} deg_V={profile[1]} "
            f"terms={profile[2]}"
        )
    print(
        "official private-linear boxes: "
        f"s={official['first_s']}..{official['last_s']} rows={official['rows']}"
    )
    print(
        "B-1 < H margins: "
        f"passing_min={official['min_pass_margin']} "
        f"next_failure_min={official['min_next_margin']}"
    )
    print(
        "max B values: "
        f"passing={official['max_pass_b']} next_failure={official['max_next_b']}"
    )
    print("the bidegree-H resultant obstruction is outside every official private-linear exponent box")
    print("H3_PRIVATE_LINEAR_RESULTANT_DEGREE_GUARD_PASS")


if __name__ == "__main__":
    main()
