#!/usr/bin/env python3
"""Independently verify the upper-support allocation form."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb


def main() -> None:
    k, m, u, g, d = 87, 67559, 34, 6, 5
    raw_low = 5194160756685726492
    raw_high = 91910188382798260682360
    residual, outside = k - u - g, m - u
    rows = []
    for inside in range(d - 1):
        a = d + 1 - inside
        b = outside - residual - d + 1 + inside
        rhs = comb(u, inside) * residual * comb(outside, d - inside)
        low_cap = (
            comb(u, inside) * residual * comb(outside, d - 1 - inside)
            // (d - inside)
        )
        rows.append((inside, a, b, rhs, low_cap))
    direct_low = comb(u, d - 1) * residual + comb(u, d)
    direct_high = (
        comb(u, d - 1) * residual * outside // 2
        + comb(u, d) * residual
        + comb(u, d + 1)
    )
    full_low = direct_low + sum(row[4] for row in rows)
    free_high = Fraction(direct_high) + sum(
        Fraction(row[3] - row[2] * row[4], row[1]) for row in rows
    )
    ordered = sorted(rows, key=lambda row: Fraction(row[1], row[2]))
    max_high = min(
        Fraction(raw_high),
        Fraction(direct_high) + sum(Fraction(row[3], row[1]) for row in rows),
    )
    candidates = {Fraction(0), max_high, free_high}
    start, current_low = free_high, Fraction(full_low)
    for _, a, b, _, low_cap in ordered:
        width = Fraction(b * low_cap, a)
        end = start + width
        candidates.update((start, min(end, max_high)))
        crossing = start + (current_low - raw_low) / Fraction(a, b)
        if start <= crossing <= min(end, max_high):
            candidates.add(crossing)
        current_low -= low_cap
        start = end

    def evaluate(total_high):
        if not 0 <= total_high <= max_high:
            return None
        extra = max(Fraction(0), total_high - free_high)
        loss = Fraction(0)
        for _, a, b, _, low_cap in ordered:
            width = Fraction(b * low_cap, a)
            used = min(extra, width)
            loss += Fraction(a, b) * used
            extra -= used
        assert extra == 0
        total_low = min(Fraction(raw_low), Fraction(full_low) - loss)
        weight_low = 15 * comb(m - 5, 6)
        weight_high = 10 * comb(m - 6, 5)
        return weight_low * total_low + weight_high * total_high

    optimum = max(
        value for value in (evaluate(candidate) for candidate in candidates)
        if value is not None
    )
    assert optimum == Fraction(
        42623778408284696740784253522991572305773969600, 3
    )
    assert raw_low < full_low
    print(json.dumps({
        "status": "PASS",
        "orientation": "upper-support",
        "cap": optimum.numerator // optimum.denominator,
        "raw_low_active": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
