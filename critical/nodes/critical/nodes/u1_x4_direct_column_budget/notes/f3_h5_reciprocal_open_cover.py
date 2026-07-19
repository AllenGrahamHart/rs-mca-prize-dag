#!/usr/bin/env python3
"""Verify the h=5 reciprocal open cover and exclude its all-zero chart."""

from __future__ import annotations

from math import gcd

import sympy as sp

from f3_h5_basefree_reciprocal_system import ALL_BARS, basefree_summary
from f3_h5_reciprocal_compatibility_compiler import TOP, reciprocal_part
from f3_h5_x83_triangular_norm_gate import LOCATOR


SUPPORT_SIZE = 10


def high_parts_vanish_at_top_zero() -> dict[int, int]:
    substitutions = {variable: 0 for variable in TOP}
    terms = {}
    for key_index in range(1, 5):
        _, high_part, _ = reciprocal_part(key_index)
        specialized = sp.expand(high_part.subs(substitutions))
        if specialized != 0:
            raise AssertionError((key_index, specialized))
        terms[key_index] = len(sp.Poly(high_part, *TOP, domain=sp.ZZ).terms())
    return terms


def official_fiber_bounds() -> dict[str, int]:
    fiber_sizes = {s: gcd(SUPPORT_SIZE, 2**s) for s in range(13, 42)}
    if set(fiber_sizes.values()) != {2}:
        raise AssertionError(fiber_sizes)
    return {
        "first_s": 13,
        "last_s": 41,
        "max_fiber_size": max(fiber_sizes.values()),
        "support_size": SUPPORT_SIZE,
    }


def finite_exponent_controls() -> dict[int, int]:
    controls = {}
    for n in (32, 64, 128):
        buckets: dict[int, int] = {}
        for exponent in range(n):
            buckets[(SUPPORT_SIZE * exponent) % n] = (
                buckets.get((SUPPORT_SIZE * exponent) % n, 0) + 1
            )
        max_fiber = max(buckets.values())
        if max_fiber != gcd(SUPPORT_SIZE, n):
            raise AssertionError((n, max_fiber, gcd(SUPPORT_SIZE, n)))
        controls[n] = max_fiber
    return controls


def open_cover_summary() -> dict[str, int]:
    basefree = basefree_summary()
    terms = high_parts_vanish_at_top_zero()
    official = official_fiber_bounds()
    controls = finite_exponent_controls()
    if len(ALL_BARS) != 5:
        raise AssertionError(ALL_BARS)
    if official["max_fiber_size"] >= official["support_size"]:
        raise AssertionError(official)
    return {
        "charts": len(ALL_BARS),
        "basefree_equations": basefree["pairwise_equations"],
        "high_parts": len(terms),
        "min_high_part_terms": min(terms.values()),
        "max_high_part_terms": max(terms.values()),
        "first_s": official["first_s"],
        "last_s": official["last_s"],
        "official_max_x10_fiber": official["max_fiber_size"],
        "support_size": official["support_size"],
        "control_rows": len(controls),
    }


def main() -> None:
    summary = open_cover_summary()
    print("h=5 reciprocal open-cover compiler")
    print(
        f"basefree_equations={summary['basefree_equations']} "
        f"charts={summary['charts']}"
    )
    print(
        "high-zero specialization: "
        f"P_j vanish for {summary['high_parts']} triangular high parts; "
        f"terms={summary['min_high_part_terms']}..{summary['max_high_part_terms']}"
    )
    print(
        "official high-zero cell exclusion: "
        f"s={summary['first_s']}..{summary['last_s']} "
        f"max_x10_fiber={summary['official_max_x10_fiber']} "
        f"support_size={summary['support_size']}"
    )
    print(f"finite exponent controls checked: {summary['control_rows']}")
    print("H5_RECIPROCAL_OPEN_COVER_PASS")


if __name__ == "__main__":
    main()
