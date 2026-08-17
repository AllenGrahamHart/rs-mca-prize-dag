#!/usr/bin/env python3
"""Test a simultaneous support-4/5/6 fixed-union bound on the K'=87 wall."""

from __future__ import annotations

import importlib.util
import itertools
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
    "k87_joint456_witness_base",
    Path(__file__).with_name(
        "rate_half_mca_rank11_k87_residual_witness_adjacent_payment.py"
    ),
)
BASE = WITNESS.BASE
KPRIME, Q, M = BASE.KPRIME, BASE.Q, BASE.M
SUPPORTS = BASE.SUPPORTS


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def weights() -> dict[int, int]:
    return {
        support: BASE.K71.LEDGER.DEFICITS[support]
        * comb(M - support, 11 - support)
        for support in (4, 5, 6)
    }


def stratum_primary(
    union: int, dimension: int, inside: int, weight: dict[int, int]
) -> tuple[Fraction, tuple[Fraction, Fraction, Fraction]]:
    residual, outside = KPRIME - union - dimension, M - union
    a5, a6 = 5 - inside, 6 - inside
    b4 = outside - residual - 3 + inside
    b5 = outside - residual - 4 + inside
    rhs4 = comb(union, inside) * residual * comb(outside, 4 - inside)
    rhs5 = comb(union, inside) * residual * comb(outside, 5 - inside)
    cap4 = (
        comb(union, inside)
        * residual
        * comb(outside, 3 - inside)
        // (4 - inside)
    )
    cap5 = (
        comb(union, inside)
        * residual
        * comb(outside, 4 - inside)
        // (5 - inside)
    )
    ymax = min(
        Fraction(cap5),
        Fraction(rhs4, a5),
        Fraction(rhs5, b5),
    )
    candidates = {Fraction(0), ymax}
    transition = Fraction(rhs4 - b4 * cap4, a5)
    if 0 <= transition <= ymax:
        candidates.add(transition)

    def evaluate(y: Fraction):
        x = min(Fraction(cap4), Fraction(rhs4 - a5 * y, b4))
        z = Fraction(rhs5 - b5 * y, a6)
        value = weight[4] * x + weight[5] * y + weight[6] * z
        return value, (x, y, z)

    return max(evaluate(y) for y in candidates)


def solve_equalities(rows, rhs):
    size = len(rhs)
    matrix = [
        [Fraction(value) for value in row] + [Fraction(target)]
        for row, target in zip(rows, rhs)
    ]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if matrix[row][column]),
            None,
        )
        if pivot is None:
            return None
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        scale = matrix[column][column]
        matrix[column] = [value / scale for value in matrix[column]]
        for row in range(size):
            if row == column:
                continue
            scale = matrix[row][column]
            if scale:
                matrix[row] = [
                    left - scale * right
                    for left, right in zip(matrix[row], matrix[column])
                ]
    return tuple(matrix[row][-1] for row in range(size))


def lp_vertex_max(constraints, objective):
    size = len(objective)
    augmented = list(constraints)
    for index in range(size):
        row = [0] * size
        row[index] = -1
        augmented.append((tuple(row), 0))
    best = None
    for selected in itertools.combinations(augmented, size):
        point = solve_equalities(
            [row for row, _ in selected],
            [rhs for _, rhs in selected],
        )
        if point is None:
            continue
        if any(
            sum(Fraction(a) * x for a, x in zip(row, point)) > rhs
            for row, rhs in augmented
        ):
            continue
        value = sum(Fraction(a) * x for a, x in zip(objective, point))
        if best is None or (value, point) > best:
            best = (value, point)
    assert best is not None
    return best


def stratum_audit(
    union: int, dimension: int, inside: int, weight: dict[int, int]
):
    residual, outside = KPRIME - union - dimension, M - union
    a5, a6 = 5 - inside, 6 - inside
    b4 = outside - residual - 3 + inside
    b5 = outside - residual - 4 + inside
    rhs4 = comb(union, inside) * residual * comb(outside, 4 - inside)
    rhs5 = comb(union, inside) * residual * comb(outside, 5 - inside)
    cap4 = (
        comb(union, inside)
        * residual
        * comb(outside, 3 - inside)
        // (4 - inside)
    )
    cap5 = (
        comb(union, inside)
        * residual
        * comb(outside, 4 - inside)
        // (5 - inside)
    )
    return lp_vertex_max(
        [
            ((1, 0, 0), cap4),
            ((0, 1, 0), cap5),
            ((b4, a5, 0), rhs4),
            ((0, b5, a6), rhs5),
        ],
        (weight[4], weight[5], weight[6]),
    )


def tail_primary(union: int, dimension: int, weight: dict[int, int]) -> Fraction:
    residual, outside = KPRIME - union - dimension, M - union
    inside = 3
    b5, a6 = outside - residual - 1, 3
    rhs5 = comb(union, inside) * residual * comb(outside, 2)
    cap5 = comb(union, inside) * residual * outside // 2
    ymax = min(Fraction(cap5), Fraction(rhs5, b5))

    def value(y: Fraction):
        z = Fraction(rhs5 - b5 * y, a6)
        return weight[5] * y + weight[6] * z

    coupled = max(value(Fraction(0)), value(ymax))
    direct4 = comb(union, 3) * residual + comb(union, 4)
    direct5 = comb(union, 4) * residual + comb(union, 5)
    direct6 = (
        comb(union, 4) * residual * outside // 2
        + comb(union, 5) * residual
        + comb(union, 6)
    )
    return coupled + weight[4] * direct4 + weight[5] * direct5 + weight[6] * direct6


def tail_audit(union: int, dimension: int, weight: dict[int, int]) -> Fraction:
    residual, outside = KPRIME - union - dimension, M - union
    b5, a6 = outside - residual - 1, 3
    rhs5 = comb(union, 3) * residual * comb(outside, 2)
    cap5 = comb(union, 3) * residual * outside // 2
    coupled, _ = lp_vertex_max(
        [((1, 0), cap5), ((b5, a6), rhs5)],
        (weight[5], weight[6]),
    )
    direct4 = comb(union, 3) * residual + comb(union, 4)
    direct5 = comb(union, 4) * residual + comb(union, 5)
    direct6 = (
        comb(union, 4) * residual * outside // 2
        + comb(union, 5) * residual
        + comb(union, 6)
    )
    return coupled + weight[4] * direct4 + weight[5] * direct5 + weight[6] * direct6


def joint456_cap(union: int, dimension: int) -> dict[str, object]:
    assert dimension >= 6 and KPRIME - union - dimension >= 0
    weight = weights()
    primary_rows = [
        stratum_primary(union, dimension, inside, weight)
        for inside in range(3)
    ]
    audit_rows = [
        stratum_audit(union, dimension, inside, weight)
        for inside in range(3)
    ]
    for primary, audit in zip(primary_rows, audit_rows):
        assert primary == audit
    primary_total = sum(row[0] for row in primary_rows) + tail_primary(
        union, dimension, weight
    )
    audit_total = sum(row[0] for row in audit_rows) + tail_audit(
        union, dimension, weight
    )
    assert primary_total == audit_total
    return {
        "cap": floor_fraction(primary_total),
        "fractional_numerator": primary_total.numerator,
        "fractional_denominator": primary_total.denominator,
        "vertices": [
            [str(value) for value in row[1]] for row in primary_rows
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
    assert high_name == "c6F/c7F/c8F/c9F"
    assert raw == 46379149947314413797407146505601291913428074818
    raw456 = sum(
        BASE.K71.LEDGER.DEFICITS[support] * caps[support - 2]
        for support in (4, 5, 6)
    )
    cap = joint456_cap(34, 6)
    repaired = raw - raw456 + int(cap["cap"])
    print(json.dumps({
        "event": "PASS",
        "witness": {
            "offset": 1,
            "m2": 28,
            "s2": 49,
            "s3": 48,
            "s4": 48,
            "s5": 47,
            "case": case,
            "charges": cases[case],
            "high": high_name,
        },
        "raw": raw,
        "raw456": raw456,
        "joint456": cap,
        "repaired": repaired,
        "leader": BASE.LEADER,
        "margin_to_leader": BASE.LEADER - repaired,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
