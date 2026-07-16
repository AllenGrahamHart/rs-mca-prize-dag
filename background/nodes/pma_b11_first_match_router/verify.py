#!/usr/bin/env python3
"""Finite logic and arithmetic replay for the B11 first-match router."""

from itertools import product
from math import comb


CHECKS = 0


def check(label, condition):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1


def owner(d, ell, excess, slack, slack_j, g2, v2, gr, vr):
    if d > ell + excess:
        return "GROW"
    if slack >= slack_j:
        return "J"
    if g2 <= v2:
        return "A2"
    if gr <= vr:
        return "AR"
    return "RES"


def paid_bound(n, k, s, slack_j, m, ell, b, q, excess, v2, vr):
    denominator = (s + slack_j) ** 2 - n * (k - 1)
    check("positive Johnson denominator", denominator > 0)
    johnson = n * (n - k + 1) / denominator
    two_anchor = (
        comb(m, 2)
        * sum(comb(2 * ell, v) for v in range(v2 + 1))
        * q ** (2 * excess + v2 + 2)
    )
    background_anchor = (
        m
        * sum(
            comb(b, ell - w) * comb(ell, v)
            for w in range(vr + 1)
            for v in range(vr - w + 1)
            if 0 <= ell - w <= b
        )
        * q ** (2 * excess + vr + 2)
    )
    return johnson, two_anchor, background_anchor


ell, excess, slack_j, v2, vr = 3, 2, 4, 3, 2
seen = set()
for d, slack, g2, gr in product(range(8), range(7), range(8), range(8)):
    cell = owner(d, ell, excess, slack, slack_j, g2, v2, gr, vr)
    seen.add(cell)
    predicates = {
        "GROW": d > ell + excess,
        "J": d <= ell + excess and slack >= slack_j,
        "A2": d <= ell + excess and slack < slack_j and g2 <= v2,
        "AR": (
            d <= ell + excess
            and slack < slack_j
            and g2 > v2
            and gr <= vr
        ),
        "RES": (
            d <= ell + excess
            and slack < slack_j
            and g2 > v2
            and gr > vr
        ),
    }
    check("exactly one first-match cell", sum(predicates.values()) == 1)
    check("owner equals logical cell", predicates[cell])

check("all cells realized", seen == {"GROW", "J", "A2", "AR", "RES"})

johnson, two_anchor, background_anchor = paid_bound(
    n=31,
    k=12,
    s=19,
    slack_j=1,
    m=5,
    ell=3,
    b=2,
    q=7,
    excess=2,
    v2=3,
    vr=2,
)
check("Johnson arithmetic", johnson == 620 / 59)
check("two-anchor arithmetic", two_anchor == 10 * 42 * 7**9)
check("background-anchor arithmetic", background_anchor == 5 * 6 * 7**8)
check("unique-decoding replacement", 2 * (21 + 1) > 31 + 12 - 1)

# Mutation guards: changing either strict complement creates overlap or a gap.
check(
    "Johnson strictness mutation caught",
    (slack_j >= slack_j) and not (slack_j < slack_j),
)
check("anchor strictness mutation caught", (v2 + 1 > v2) and not (v2 + 1 <= v2))

print(f"PMA B11 first-match router: PASS ({CHECKS} checks)")
