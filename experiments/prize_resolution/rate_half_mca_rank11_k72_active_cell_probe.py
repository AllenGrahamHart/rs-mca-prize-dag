#!/usr/bin/env python3
"""Evaluate K'=72 defect cells through every mixed carrier geometry."""

from __future__ import annotations

import importlib.util
import argparse
import json
from math import comb
from pathlib import Path


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PROBE = load_module(
    "k72_two_step_for_active_cell",
    Path("rate_half_mca_rank11_k72_two_step_probe.py"),
)
K71 = PROBE.K71
KPRIME = 72

parser = argparse.ArgumentParser()
parser.add_argument(
    "defects",
    nargs="?",
    default="34,31,32,31",
    help="semicolon-separated s2,s3,s4,s5 tuples",
)
arguments = parser.parse_args()
DEFECT_CELLS = [
    tuple(int(value) for value in cell.split(","))
    for cell in arguments.defects.split(";")
]
assert DEFECT_CELLS and all(len(cell) == 4 for cell in DEFECT_CELLS)

q = KPRIME - 10
m = 67472 + KPRIME
baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(q, m)
exact45, _, _ = K71.exact45_rows(KPRIME, baseline)
_, high = K71.PARENT.high_group(KPRIME, baseline)
old = K71.LEDGER.row(KPRIME)
n = 1048576 + KPRIME
marks = int(old["marks"])
kernel = int(old["kernel"])
ceiling = (
    K71.LEDGER.RECORD_FLOOR * 55 * comb(m, 11)
    - 55 * comb(n, 11)
    - 55 * kernel
    - marks
    - 1
) // K71.LEDGER.RECORD_FLOOR


def evaluate(defects):
    s2, s3, s4, s5 = defects
    m2, m3, m4, m5 = (q - value for value in defects)
    left = K71.base23_vector(KPRIME, baseline, s2, s3)
    middle = next(
        vector for a, b, vector in exact45 if (a, b) == (s4, s5)
    )
    local = K71.combine(left, middle)
    cases = PROBE.mixed_cases(m2, m3 - m2, m4, m5)
    charged = PROBE.charged_case_rows(KPRIME, local, cases)
    rows = []
    for (candidate, joint), name in charged.items():
        for high_name, high_vector in high:
            caps = K71.combine(candidate, high_vector)
            value = K71.premium(caps)
            if joint is not None:
                old45 = sum(
                    K71.LEDGER.DEFICITS[support] * caps[support - 2]
                    for support in (4, 5)
                )
                value -= old45 - min(old45, joint)
            rows.append((value, f"{name}/{high_name}", caps))

    rows.sort(reverse=True)
    maximum, label, caps = rows[0]
    return {
        "defects": defects,
        "maxima": (m2, m3, m4, m5),
        "raw_cases": len(cases),
        "distinct_charges": len(charged),
        "evaluations": len(rows),
        "maximum": maximum,
        "active_geometry": label,
        "active_caps": caps,
        "premium_margin": ceiling - maximum,
        "top_five": [(value, name) for value, name, _ in rows[:5]],
    }


summaries = [evaluate(cell) for cell in DEFECT_CELLS]
active = max(summaries, key=lambda row: row["maximum"])


def compact(row):
    return {
        "defects": row["defects"],
        "maxima": row["maxima"],
        "raw_cases": row["raw_cases"],
        "distinct_charges": row["distinct_charges"],
        "maximum": row["maximum"],
        "active_geometry": row["active_geometry"],
        "premium_margin": row["premium_margin"],
    }


unsafe = [row for row in summaries if row["premium_margin"] < 0]
print(json.dumps({
    "cells": len(summaries),
    "evaluations": sum(row["evaluations"] for row in summaries),
    "safe_premium_ceiling": ceiling,
    "all_safe": not unsafe,
    "unsafe_cells": len(unsafe),
    "maximum": compact(active),
    "unsafe": [compact(row) for row in unsafe],
    "margins": [
        {"defects": row["defects"], "premium_margin": row["premium_margin"]}
        for row in summaries
    ],
}, indent=2))
