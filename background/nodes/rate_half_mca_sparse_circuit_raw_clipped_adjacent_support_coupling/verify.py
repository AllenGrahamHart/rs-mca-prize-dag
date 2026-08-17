#!/usr/bin/env python3
"""Verify the lower-support allocation form of the raw-clipped theorem."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb


DEFICITS = {2: 36, 3: 28, 4: 21, 5: 15, 6: 10, 7: 6, 8: 3, 9: 1}


def rows(k, m, u, g, d):
    residual, outside = k - u - g, m - u
    result = []
    for inside in range(d - 1):
        a = d + 1 - inside
        b = outside - residual - d + 1 + inside
        rhs = comb(u, inside) * residual * comb(outside, d - inside)
        cap = (
            comb(u, inside) * residual * comb(outside, d - 1 - inside)
            // (d - inside)
        )
        result.append((inside, a, b, rhs, cap))
    direct_low = comb(u, d - 1) * residual + comb(u, d)
    direct_high = (
        comb(u, d - 1) * residual * outside // 2
        + comb(u, d) * residual
        + comb(u, d + 1)
    )
    return result, direct_low, direct_high


def cap(k, m, u, g, d, raw_low, raw_high):
    data, direct_low, direct_high = rows(k, m, u, g, d)
    ordered = sorted(data, key=lambda row: Fraction(row[2], row[1]))
    max_low = min(raw_low, direct_low + sum(row[4] for row in data))
    max_high_zero = Fraction(direct_high) + sum(
        Fraction(row[3], row[1]) for row in data
    )
    candidates = {Fraction(0), Fraction(max_low), Fraction(direct_low)}
    start, current_high = Fraction(direct_low), max_high_zero
    for _, a, b, _, low_cap in ordered:
        end = start + low_cap
        candidates.update((start, min(end, Fraction(max_low))))
        crossing = start + (current_high - raw_high) / Fraction(b, a)
        if start <= crossing <= min(end, Fraction(max_low)):
            candidates.add(crossing)
        current_high -= Fraction(b * low_cap, a)
        start = end

    def evaluate(total_low):
        if not 0 <= total_low <= max_low:
            return None
        remaining = max(Fraction(0), total_low - direct_low)
        loss = Fraction(0)
        for _, a, b, _, low_cap in ordered:
            used = min(remaining, Fraction(low_cap))
            loss += Fraction(b, a) * used
            remaining -= used
        assert remaining == 0
        total_high = min(Fraction(raw_high), max_high_zero - loss)
        weight_low = DEFICITS[d] * comb(m - d, 11 - d)
        weight_high = DEFICITS[d + 1] * comb(m - d - 1, 10 - d)
        return weight_low * total_low + weight_high * total_high

    optimum = max(
        value for value in (evaluate(candidate) for candidate in candidates)
        if value is not None
    )
    return optimum


def main() -> None:
    optimum = cap(
        87, 67559, 34, 6, 5,
        5194160756685726492,
        91910188382798260682360,
    )
    assert optimum.denominator == 3
    assert optimum.numerator == 42623778408284696740784253522991572305773969600
    assert optimum.numerator // optimum.denominator == (
        14207926136094898913594751174330524101924656533
    )
    statement = open(__file__.replace("verify.py", "statement.md")).read()
    assert "Nothing here composes two\noverlapping pair bounds" in statement
    print(json.dumps({
        "status": "PASS",
        "specialization": [87, 67559, 34, 6, 5],
        "cap": optimum.numerator // optimum.denominator,
        "denominator": optimum.denominator,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
