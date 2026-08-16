#!/usr/bin/env python3
"""Reconstruct a compact adjacent-row carrier-atlas frontier and payment."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
from math import comb
from pathlib import Path


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def defect_tuple(label: str) -> tuple[int, int, int, int]:
    return tuple(
        int(re.search(rf"s{support}=([0-9]+)", label).group(1))
        for support in range(2, 6)
    )


def tuple_digest(rows: list[tuple[int, int, int, int]]) -> str:
    payload = json.dumps(rows, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def audit(kprime: int = 74) -> dict[str, object]:
    KPRIME = kprime
    Q = KPRIME - 10
    M = 67472 + KPRIME
    N = 1048576 + KPRIME
    probe = load_module(
        "carrier_atlas_for_k74_audit",
        Path(__file__).with_name(
            "rate_half_mca_rank11_k72_two_step_probe.py"
        ),
    )
    k71 = probe.K71
    baseline = k71.PARENT.PARENT.PARENT.CAPS.baseline_caps(Q, M)
    _, front23, steps, carrier32, _ = probe.position23_group(KPRIME, baseline)
    exact45, _, front45 = k71.exact45_rows(KPRIME, baseline)
    _, high = k71.PARENT.high_group(KPRIME, baseline)
    old = k71.LEDGER.row(KPRIME)
    marks = int(old["marks"])
    kernel = int(old["kernel"])
    record_floor = k71.LEDGER.RECORD_FLOOR
    ceiling = (
        record_floor * 55 * comb(M, 11)
        - 55 * comb(N, 11)
        - 55 * kernel
        - marks
        - 1
    ) // record_floor

    evaluations = 0
    unsafe_by_defects: dict[
        tuple[int, int, int, int], tuple[int, str]
    ] = {}
    safe_maximum = (-1, "")

    def retain(label: str, caps: tuple[int, ...]) -> None:
        nonlocal evaluations, safe_maximum
        evaluations += 1
        value = k71.premium(caps)
        defects = defect_tuple(label)
        if value > ceiling:
            previous = unsafe_by_defects.get(defects)
            if previous is None or value > previous[0]:
                unsafe_by_defects[defects] = (value, label)
        elif value > safe_maximum[0]:
            safe_maximum = (value, label)

    for left_name, left in front23:
        for middle_name, middle in front45:
            local = k71.combine(left, middle)
            for high_name, high_vector in high:
                retain(
                    f"{left_name}/{middle_name}/{high_name}/ordinary",
                    k71.combine(local, high_vector),
                )

    for s2, s3, left in carrier32:
        for s4, s5, middle in exact45:
            if (Q - s4, Q - s5) == (31, 31):
                continue
            local = k71.combine(left, middle)
            for high_name, high_vector in high:
                retain(
                    f"s2={s2}/s3={s3}/s4={s4}/s5={s5}/"
                    f"{high_name}/carrier32_plain",
                    k71.combine(local, high_vector),
                )

    for offset, rows in steps.items():
        for s2, s3, left in rows:
            m2 = Q - s2
            for s4, s5, middle in exact45:
                if Q - s4 > m2:
                    continue
                local = k71.combine(left, middle)
                for high_name, high_vector in high:
                    retain(
                        f"s2={s2}/s3={s3}/s4={s4}/s5={s5}/"
                        f"{high_name}/offset{offset}_plain",
                        k71.combine(local, high_vector),
                    )

    unsafe = sorted(unsafe_by_defects)
    unsafe_ranked = sorted(
        (
            (value, defects, label)
            for defects, (value, label) in unsafe_by_defects.items()
        ),
        reverse=True,
    )
    reroute_evaluations = 0
    reroute_maximum = (-1, (), "")
    reroute_minimum_margin = None
    for s2, s3, s4, s5 in unsafe:
        maxima = tuple(Q - value for value in (s2, s3, s4, s5))
        m2, m3, m4, m5 = maxima
        left = k71.base23_vector(KPRIME, baseline, s2, s3)
        middle = next(
            vector for a, b, vector in exact45 if (a, b) == (s4, s5)
        )
        local = k71.combine(left, middle)
        cases = probe.mixed_cases(m2, m3 - m2, m4, m5)
        charged = probe.charged_case_rows(KPRIME, local, cases)
        cell_maximum = (-1, "")
        for (candidate, joint), name in charged.items():
            for high_name, high_vector in high:
                reroute_evaluations += 1
                caps = k71.combine(candidate, high_vector)
                value = k71.premium(caps)
                if joint is not None:
                    old45 = sum(
                        k71.LEDGER.DEFICITS[support] * caps[support - 2]
                        for support in (4, 5)
                    )
                    value -= old45 - min(old45, joint)
                cell_maximum = max(
                    cell_maximum,
                    (value, f"{name}/{high_name}"),
                )
        margin = ceiling - cell_maximum[0]
        reroute_minimum_margin = (
            margin
            if reroute_minimum_margin is None
            else min(reroute_minimum_margin, margin)
        )
        reroute_maximum = max(
            reroute_maximum,
            (cell_maximum[0], (s2, s3, s4, s5), cell_maximum[1]),
        )

    premium = safe_maximum[0]
    full_rank = (marks + record_floor * premium) // 55
    total = kernel + full_rank
    demand = record_floor * comb(M, 11) - comb(N, 11)
    return {
        "kprime": KPRIME,
        "plain_frontier": {
            "evaluations": evaluations,
            "unsafe_distinct_defect_tuples": len(unsafe),
            "unsafe_tuple_sha256": tuple_digest(unsafe),
            "unsafe_maximum": {
                "premium": unsafe_ranked[0][0],
                "defects": unsafe_ranked[0][1],
                "label": unsafe_ranked[0][2],
            },
            "unsafe_minimum": {
                "premium": unsafe_ranked[-1][0],
                "defects": unsafe_ranked[-1][1],
                "label": unsafe_ranked[-1][2],
            },
            "safe_maximum": premium,
            "safe_maximum_label": safe_maximum[1],
        },
        "reroute": {
            "cells": len(unsafe),
            "evaluations": reroute_evaluations,
            "all_safe": reroute_minimum_margin is not None
            and reroute_minimum_margin > 0,
            "maximum": reroute_maximum[0],
            "active_defects": reroute_maximum[1],
            "active_geometry": reroute_maximum[2],
            "minimum_margin": reroute_minimum_margin,
        },
        "row": {
            "rank_nine_marks": marks,
            "kernel_capacity": kernel,
            "record_floor": record_floor,
            "completion_premium": premium,
            "safe_premium_ceiling": ceiling,
            "premium_ceiling_margin": ceiling - premium,
            "full_rank_capacity": full_rank,
            "total_capacity": total,
            "required_component_incidence": demand,
            "gap": demand - total,
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("kprime", nargs="?", type=int, default=74)
    args = parser.parse_args()
    print(json.dumps(audit(args.kprime), indent=2))
