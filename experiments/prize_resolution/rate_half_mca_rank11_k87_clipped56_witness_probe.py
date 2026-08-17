#!/usr/bin/env python3
"""Clip the K'=87 fixed-union support-5/6 LP by the raw support caps."""

from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from math import comb
from pathlib import Path


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


WITNESS = load_module(
    "k87_clipped56_witness_base",
    Path(__file__).with_name(
        "rate_half_mca_rank11_k87_residual_witness_adjacent_payment.py"
    ),
)
BASE = WITNESS.BASE
KPRIME, Q, M = BASE.KPRIME, BASE.Q, BASE.M
SUPPORTS = BASE.SUPPORTS
LOW, HIGH = 5, 6


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def pair_data(union: int, dimension: int):
    residual, outside = KPRIME - union - dimension, M - union
    rows = []
    for inside in range(LOW - 1):
        high_coefficient = HIGH - inside
        low_coefficient = outside - residual - LOW + 1 + inside
        rhs = (
            comb(union, inside)
            * residual
            * comb(outside, LOW - inside)
        )
        low_cap = (
            comb(union, inside)
            * residual
            * comb(outside, LOW - 1 - inside)
            // (LOW - inside)
        )
        rows.append(
            (inside, high_coefficient, low_coefficient, rhs, low_cap)
        )
    direct_low = comb(union, LOW - 1) * residual + comb(union, LOW)
    direct_high = (
        comb(union, LOW - 1) * residual * outside // 2
        + comb(union, LOW) * residual
        + comb(union, HIGH)
    )
    return rows, direct_low, direct_high


def weighted_value(low: Fraction, high: Fraction) -> Fraction:
    return (
        BASE.K71.LEDGER.DEFICITS[LOW] * comb(M - LOW, 11 - LOW) * low
        + BASE.K71.LEDGER.DEFICITS[HIGH]
        * comb(M - HIGH, 11 - HIGH)
        * high
    )


def evaluate_from_low(union: int, dimension: int, raw_low: int, raw_high: int):
    rows, direct_low, direct_high = pair_data(union, dimension)
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

    def point(total_low: Fraction):
        remaining = max(Fraction(0), total_low - direct_low)
        loss = Fraction(0)
        allocations = []
        for inside, high_coefficient, low_coefficient, _, low_cap in ordered:
            used = min(remaining, Fraction(low_cap))
            allocations.append((inside, used))
            loss += Fraction(low_coefficient, high_coefficient) * used
            remaining -= used
        assert remaining == 0
        total_high = min(Fraction(raw_high), maximum_high_at_zero - loss)
        return weighted_value(total_low, total_high), total_low, total_high, allocations

    return max(point(total_low) for total_low in candidates)


def evaluate_from_high(union: int, dimension: int, raw_low: int, raw_high: int):
    rows, direct_low, direct_high = pair_data(union, dimension)
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

    def point(total_high: Fraction):
        extra = max(Fraction(0), total_high - baseline_high)
        loss_low = Fraction(0)
        for _, high_coefficient, low_coefficient, _, low_cap in ordered:
            width = Fraction(low_coefficient * low_cap, high_coefficient)
            used = min(extra, width)
            loss_low += Fraction(high_coefficient, low_coefficient) * used
            extra -= used
        assert extra == 0
        total_low = min(Fraction(raw_low), Fraction(full_low) - loss_low)
        return weighted_value(total_low, total_high), total_low, total_high

    return max(point(total_high) for total_high in candidates)


def clipped56(caps, union: int, dimension: int):
    factor_low = comb(M - LOW, 11 - LOW)
    factor_high = comb(M - HIGH, 11 - HIGH)
    raw_low, rem_low = divmod(caps[LOW - 2], factor_low)
    raw_high, rem_high = divmod(caps[HIGH - 2], factor_high)
    primary = evaluate_from_low(union, dimension, raw_low, raw_high)
    audit = evaluate_from_high(union, dimension, raw_low, raw_high)
    assert primary[0:3] == audit
    return {
        "cap": floor_fraction(primary[0]),
        "fractional_numerator": primary[0].numerator,
        "fractional_denominator": primary[0].denominator,
        "support5_count": str(primary[1]),
        "support6_count": str(primary[2]),
        "support5_raw_count": raw_low,
        "support6_raw_count": raw_high,
        "support5_remainder": rem_low,
        "support6_remainder": rem_high,
        "primary_allocations": [
            [inside, str(value)] for inside, value in primary[3]
        ],
    }


def main() -> None:
    baseline = BASE.K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(Q, M)
    left = BASE.combine(
        tuple(baseline[support] for support in SUPPORTS),
        BASE.source_vector(baseline, 2, 49),
        BASE.source_vector(baseline, 3, 48),
    )
    middle = BASE.combine(
        tuple(baseline[support] for support in SUPPORTS),
        BASE.source_vector(baseline, 4, 48),
        BASE.source_vector(baseline, 5, 47),
    )
    local = BASE.combine(left, middle)
    cases = BASE.PROBE.mixed_cases(28, 1, 29, 30)
    case = "F23__N4_t0__N5_t0"
    assert cases[case] == [(34, 6), (36, 5)]
    candidate = local
    for union, dimension in cases[case]:
        candidate = BASE.combine(
            candidate,
            BASE.PROBE.fixed_union_cap(KPRIME, union, dimension),
        )
    _, high = BASE.K71.PARENT.high_group(KPRIME, baseline)
    raw, high_name, caps = max(
        (
            BASE.premium(BASE.combine(candidate, vector)),
            name,
            BASE.combine(candidate, vector),
        )
        for name, vector in sorted(high)
    )
    assert raw == 46379149947314413797407146505601291913428074818
    pair_raw = sum(
        BASE.K71.LEDGER.DEFICITS[support] * caps[support - 2]
        for support in (LOW, HIGH)
    )
    clipped = clipped56(caps, 34, 6)
    repaired = raw - pair_raw + int(clipped["cap"])
    print(json.dumps({
        "event": "PASS",
        "witness": {
            "case": case,
            "charges": cases[case],
            "high": high_name,
        },
        "raw": raw,
        "raw56": pair_raw,
        "clipped56": clipped,
        "repaired": repaired,
        "leader": BASE.LEADER,
        "margin_to_leader": BASE.LEADER - repaired,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
