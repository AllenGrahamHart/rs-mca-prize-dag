#!/usr/bin/env python3
"""Exact dual evaluators for raw-clipped adjacent-support LPs."""

from __future__ import annotations

from fractions import Fraction
from math import comb


DEFICITS = {2: 36, 3: 28, 4: 21, 5: 15, 6: 10, 7: 6, 8: 3, 9: 1}


def pair_data(k: int, m: int, union: int, dimension: int, support: int):
    residual, outside = k - union - dimension, m - union
    assert residual >= 0 and 2 <= support <= dimension - 1
    rows = []
    for inside in range(support - 1):
        high_coefficient = support + 1 - inside
        low_coefficient = outside - residual - support + 1 + inside
        rhs = (
            comb(union, inside)
            * residual
            * comb(outside, support - inside)
        )
        low_cap = (
            comb(union, inside)
            * residual
            * comb(outside, support - 1 - inside)
            // (support - inside)
        )
        rows.append(
            (inside, high_coefficient, low_coefficient, rhs, low_cap)
        )
    direct_low = (
        comb(union, support - 1) * residual + comb(union, support)
    )
    direct_high = (
        comb(union, support - 1) * residual * outside // 2
        + comb(union, support) * residual
        + comb(union, support + 1)
    )
    return rows, direct_low, direct_high


def weighted_value(
    m: int, support: int, low: Fraction, high: Fraction
) -> Fraction:
    return (
        DEFICITS[support] * comb(m - support, 11 - support) * low
        + DEFICITS[support + 1]
        * comb(m - support - 1, 10 - support)
        * high
    )


def lower_orientation(
    k: int,
    m: int,
    union: int,
    dimension: int,
    support: int,
    raw_low: int,
    raw_high: int,
) -> Fraction:
    rows, direct_low, direct_high = pair_data(
        k, m, union, dimension, support
    )
    ordered = sorted(rows, key=lambda row: Fraction(row[2], row[1]))
    maximum_low = min(raw_low, direct_low + sum(row[4] for row in rows))
    maximum_high_at_zero = Fraction(direct_high) + sum(
        Fraction(row[3], row[1]) for row in rows
    )
    candidates = {Fraction(0), Fraction(maximum_low)}
    start = Fraction(direct_low)
    if 0 <= start <= maximum_low:
        candidates.add(start)
    current_high = maximum_high_at_zero
    for _, high_coefficient, low_coefficient, _, low_cap in ordered:
        end = start + low_cap
        clipped_end = min(end, Fraction(maximum_low))
        if start <= maximum_low:
            candidates.add(start)
            candidates.add(clipped_end)
            loss = Fraction(low_coefficient, high_coefficient)
            crossing = start + (current_high - raw_high) / loss
            if start <= crossing <= clipped_end:
                candidates.add(crossing)
        current_high -= Fraction(low_coefficient * low_cap, high_coefficient)
        start = end

    def evaluate(total_low: Fraction) -> Fraction:
        remaining = max(Fraction(0), total_low - direct_low)
        loss = Fraction(0)
        for _, high_coefficient, low_coefficient, _, low_cap in ordered:
            used = min(remaining, Fraction(low_cap))
            loss += Fraction(low_coefficient, high_coefficient) * used
            remaining -= used
        assert remaining == 0
        total_high = min(Fraction(raw_high), maximum_high_at_zero - loss)
        return weighted_value(m, support, total_low, total_high)

    return max(evaluate(total_low) for total_low in candidates)


def upper_orientation(
    k: int,
    m: int,
    union: int,
    dimension: int,
    support: int,
    raw_low: int,
    raw_high: int,
) -> Fraction:
    rows, direct_low, direct_high = pair_data(
        k, m, union, dimension, support
    )
    full_low = direct_low + sum(row[4] for row in rows)
    baseline_high = Fraction(direct_high) + sum(
        Fraction(row[3] - row[2] * row[4], row[1]) for row in rows
    )
    ordered = sorted(rows, key=lambda row: Fraction(row[1], row[2]))
    maximum_high = min(
        Fraction(raw_high),
        Fraction(direct_high) + sum(
            Fraction(row[3], row[1]) for row in rows
        ),
    )
    candidates = {Fraction(0), maximum_high}
    start = baseline_high
    if 0 <= start <= maximum_high:
        candidates.add(start)
    current_low = Fraction(full_low)
    for _, high_coefficient, low_coefficient, _, low_cap in ordered:
        width = Fraction(low_coefficient * low_cap, high_coefficient)
        end = start + width
        clipped_end = min(end, maximum_high)
        if start <= maximum_high:
            candidates.add(start)
            candidates.add(clipped_end)
            loss = Fraction(high_coefficient, low_coefficient)
            crossing = start + (current_low - raw_low) / loss
            if start <= crossing <= clipped_end:
                candidates.add(crossing)
        current_low -= low_cap
        start = end

    def evaluate(total_high: Fraction) -> Fraction:
        extra = max(Fraction(0), total_high - baseline_high)
        loss_low = Fraction(0)
        for _, high_coefficient, low_coefficient, _, low_cap in ordered:
            width = Fraction(low_coefficient * low_cap, high_coefficient)
            used = min(extra, width)
            loss_low += Fraction(high_coefficient, low_coefficient) * used
            extra -= used
        assert extra == 0
        total_low = min(Fraction(raw_low), Fraction(full_low) - loss_low)
        return weighted_value(m, support, total_low, total_high)

    return max(evaluate(total_high) for total_high in candidates)
