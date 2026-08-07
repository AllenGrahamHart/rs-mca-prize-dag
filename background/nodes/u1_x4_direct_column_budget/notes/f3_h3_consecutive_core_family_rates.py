#!/usr/bin/env python3
"""Exact family-rate table for the A=[0,1,2] consecutive-core census."""

from __future__ import annotations

import itertools
from fractions import Fraction


N = 96

ACTIVE = {
    (3, 17, 81),
    (3, 26, 74),
    (3, 51, 53),
    (5, 17, 81),
    (7, 17, 81),
    (7, 55, 61),
    (8, 56, 63),
    (9, 29, 77),
    (9, 57, 65),
    (10, 58, 67),
    (11, 30, 78),
    (12, 60, 71),
    (13, 17, 81),
    (13, 61, 73),
    (15, 32, 80),
    (15, 63, 77),
    (16, 64, 79),
    (17, 33, 81),
    (17, 37, 81),
    (17, 43, 81),
    (17, 45, 81),
    (17, 47, 81),
    (17, 51, 81),
    (17, 53, 81),
    (17, 55, 81),
    (17, 61, 81),
    (17, 65, 81),
    (17, 81, 85),
    (17, 81, 91),
    (17, 81, 93),
    (17, 81, 95),
    (18, 66, 83),
    (19, 34, 82),
    (20, 68, 87),
    (21, 35, 83),
    (21, 69, 89),
    (24, 72, 95),
    (25, 37, 85),
    (27, 38, 86),
    (31, 40, 88),
    (33, 41, 89),
    (35, 42, 90),
    (37, 43, 91),
    (45, 47, 95),
}


def fixed_pair(b: tuple[int, int, int]) -> bool:
    return 17 in b and 81 in b


def antipodal_pair(b: tuple[int, int, int]) -> bool:
    s = set(b)
    return any((x + N // 2) % N in s for x in s)


def pct(frac: Fraction) -> str:
    return f"{100 * float(frac):.4f}%"


def main() -> None:
    classes = {
        "all": [],
        "fixed": [],
        "antipodal": [],
        "overlap": [],
        "union": [],
        "outside": [],
    }
    for b in itertools.combinations(range(3, N), 3):
        f = fixed_pair(b)
        a = antipodal_pair(b)
        classes["all"].append(b)
        if f:
            classes["fixed"].append(b)
        if a:
            classes["antipodal"].append(b)
        if f and a:
            classes["overlap"].append(b)
        if f or a:
            classes["union"].append(b)
        else:
            classes["outside"].append(b)

    expected_sizes = {
        "all": 129766,
        "fixed": 91,
        "antipodal": 4095,
        "overlap": 2,
        "union": 4184,
        "outside": 125582,
    }
    for name, expected in expected_sizes.items():
        if len(classes[name]) != expected:
            raise AssertionError((name, len(classes[name]), expected))

    active_counts = {name: sum(1 for b in vals if b in ACTIVE) for name, vals in classes.items()}
    expected_active = {
        "all": 44,
        "fixed": 18,
        "antipodal": 28,
        "overlap": 2,
        "union": 44,
        "outside": 0,
    }
    if active_counts != expected_active:
        raise AssertionError((active_counts, expected_active))

    print("family rates:")
    for name in ("all", "fixed", "antipodal", "overlap", "union", "outside"):
        frac = Fraction(active_counts[name], len(classes[name]))
        print(
            f"  {name:10s}: {active_counts[name]:6d} / {len(classes[name]):6d}"
            f" = {pct(frac)}"
        )
    print("H3_CONSECUTIVE_CORE_FAMILY_RATES_PASS")


if __name__ == "__main__":
    main()
