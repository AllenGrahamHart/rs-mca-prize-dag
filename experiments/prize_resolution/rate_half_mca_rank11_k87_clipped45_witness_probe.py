#!/usr/bin/env python3
"""Clip the K'=87 fixed-union support-4/5 LP by the raw support caps."""

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
    "k87_clipped45_witness_base",
    Path(__file__).with_name(
        "rate_half_mca_rank11_k87_residual_witness_adjacent_payment.py"
    ),
)
BASE = WITNESS.BASE
KPRIME, Q, M = BASE.KPRIME, BASE.Q, BASE.M
SUPPORTS = BASE.SUPPORTS


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def pair_data(union: int, dimension: int):
    residual, outside = KPRIME - union - dimension, M - union
    rows = []
    for inside in range(3):
        a = 5 - inside
        b = outside - residual - 3 + inside
        rhs = comb(union, inside) * residual * comb(outside, 4 - inside)
        cap4 = (
            comb(union, inside)
            * residual
            * comb(outside, 3 - inside)
            // (4 - inside)
        )
        rows.append((inside, a, b, rhs, cap4))
    direct4 = comb(union, 3) * residual + comb(union, 4)
    direct5 = (
        comb(union, 3) * residual * outside // 2
        + comb(union, 4) * residual
        + comb(union, 5)
    )
    return rows, direct4, direct5


def evaluate_from_support4(
    union: int, dimension: int, raw4: int, raw5: int
):
    rows, direct4, direct5 = pair_data(union, dimension)
    ordered = sorted(rows, key=lambda row: Fraction(row[2], row[1]))
    maximum4 = min(raw4, direct4 + sum(row[4] for row in rows))
    maximum5_at_zero = Fraction(direct5) + sum(
        Fraction(row[3], row[1]) for row in rows
    )
    candidates = {Fraction(0), Fraction(maximum4)}
    start = Fraction(direct4)
    if 0 <= start <= maximum4:
        candidates.add(start)
    current5 = maximum5_at_zero
    for _, a, b, _, cap4 in ordered:
        end = start + cap4
        clipped_end = min(end, Fraction(maximum4))
        if start <= maximum4:
            candidates.add(start)
            candidates.add(clipped_end)
            crossing = start + (current5 - raw5) / Fraction(b, a)
            if start <= crossing <= clipped_end:
                candidates.add(crossing)
        current5 -= Fraction(b * cap4, a)
        start = end

    def point(total4: Fraction):
        remaining = max(Fraction(0), total4 - direct4)
        loss = Fraction(0)
        allocations = []
        for inside, a, b, _, cap4 in ordered:
            used = min(remaining, Fraction(cap4))
            allocations.append((inside, used))
            loss += Fraction(b, a) * used
            remaining -= used
        assert remaining == 0
        total5 = min(Fraction(raw5), maximum5_at_zero - loss)
        value = (
            BASE.K71.LEDGER.DEFICITS[4] * comb(M - 4, 7) * total4
            + BASE.K71.LEDGER.DEFICITS[5] * comb(M - 5, 6) * total5
        )
        return value, total4, total5, allocations

    return max(point(total4) for total4 in candidates)


def evaluate_from_support5(
    union: int, dimension: int, raw4: int, raw5: int
):
    rows, direct4, direct5 = pair_data(union, dimension)
    full4 = direct4 + sum(row[4] for row in rows)
    baseline5 = Fraction(direct5) + sum(
        Fraction(row[3] - row[2] * row[4], row[1]) for row in rows
    )
    ordered = sorted(rows, key=lambda row: Fraction(row[1], row[2]))
    maximum5 = min(
        Fraction(raw5),
        Fraction(direct5) + sum(Fraction(row[3], row[1]) for row in rows),
    )
    candidates = {Fraction(0), maximum5}
    start = baseline5
    if 0 <= start <= maximum5:
        candidates.add(start)
    current4 = Fraction(full4)
    for _, a, b, _, cap4 in ordered:
        width = Fraction(b * cap4, a)
        end = start + width
        clipped_end = min(end, maximum5)
        if start <= maximum5:
            candidates.add(start)
            candidates.add(clipped_end)
            crossing = start + (current4 - raw4) / Fraction(a, b)
            if start <= crossing <= clipped_end:
                candidates.add(crossing)
        current4 -= cap4
        start = end

    def point(total5: Fraction):
        if total5 <= baseline5:
            loss4 = Fraction(0)
            extra = Fraction(0)
        else:
            extra = total5 - baseline5
            loss4 = Fraction(0)
            for _, a, b, _, cap4 in ordered:
                width = Fraction(b * cap4, a)
                used = min(extra, width)
                loss4 += Fraction(a, b) * used
                extra -= used
            assert extra == 0
        total4 = min(Fraction(raw4), Fraction(full4) - loss4)
        value = (
            BASE.K71.LEDGER.DEFICITS[4] * comb(M - 4, 7) * total4
            + BASE.K71.LEDGER.DEFICITS[5] * comb(M - 5, 6) * total5
        )
        return value, total4, total5

    return max(point(total5) for total5 in candidates)


def clipped45(caps, union: int, dimension: int):
    factor4, factor5 = comb(M - 4, 7), comb(M - 5, 6)
    raw4, rem4 = divmod(caps[4 - 2], factor4)
    raw5, rem5 = divmod(caps[5 - 2], factor5)
    primary = evaluate_from_support4(union, dimension, raw4, raw5)
    audit = evaluate_from_support5(union, dimension, raw4, raw5)
    assert primary[0:3] == audit
    return {
        "cap": floor_fraction(primary[0]),
        "fractional_numerator": primary[0].numerator,
        "fractional_denominator": primary[0].denominator,
        "support4_count": str(primary[1]),
        "support5_count": str(primary[2]),
        "support4_raw_count": raw4,
        "support5_raw_count": raw5,
        "support4_remainder": rem4,
        "support5_remainder": rem5,
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
        for support in (4, 5)
    )
    clipped = clipped45(caps, 36, 5)
    repaired = raw - pair_raw + int(clipped["cap"])
    print(json.dumps({
        "event": "PASS",
        "witness": {
            "case": case,
            "charges": cases[case],
            "high": high_name,
        },
        "raw": raw,
        "raw45": pair_raw,
        "clipped45": clipped,
        "repaired": repaired,
        "leader": BASE.LEADER,
        "margin_to_leader": BASE.LEADER - repaired,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
