#!/usr/bin/env python3
"""List the largest K'=72 cells still left on conservative plain routing."""

from __future__ import annotations

import heapq
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


PROBE = load_module(
    "k72_two_step_for_plain_frontier",
    Path("rate_half_mca_rank11_k72_two_step_probe.py"),
)
K71 = PROBE.K71
KPRIME = 72
KEEP = 30
q = KPRIME - 10
m = 67472 + KPRIME
baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(q, m)
_, front23, steps, carrier32, _ = PROBE.position23_group(KPRIME, baseline)
exact45, _, front45 = K71.exact45_rows(KPRIME, baseline)
_, high = K71.PARENT.high_group(KPRIME, baseline)
heap = []
serial = 0
unsafe_by_defects = {}
safe_maximum = (-1, "", ())

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


def defects(label: str) -> tuple[int, int, int, int]:
    return tuple(int(re.search(rf"s{i}=([0-9]+)", label).group(1)) for i in range(2, 6))


def keep(label: str, caps: tuple[int, ...]) -> None:
    global serial, safe_maximum
    serial += 1
    value = K71.premium(caps)
    values = defects(label)
    row = (value, serial, label, values, caps)
    if value > ceiling:
        previous = unsafe_by_defects.get(values)
        if previous is None or value > previous[0]:
            unsafe_by_defects[values] = (value, label)
    elif value > safe_maximum[0]:
        safe_maximum = (value, label, caps)
    if len(heap) < KEEP:
        heapq.heappush(heap, row)
    elif row[0] > heap[0][0]:
        heapq.heapreplace(heap, row)


for left_name, left in front23:
    for middle_name, middle in front45:
        local = K71.combine(left, middle)
        for high_name, high_vector in high:
            keep(
                f"{left_name}/{middle_name}/{high_name}/ordinary",
                K71.combine(local, high_vector),
            )

for s2, s3, left in carrier32:
    for s4, s5, middle in exact45:
        if (q - s4, q - s5) == (31, 31):
            continue
        local = K71.combine(left, middle)
        for high_name, high_vector in high:
            keep(
                f"s2={s2}/s3={s3}/s4={s4}/s5={s5}/{high_name}/carrier32_plain",
                K71.combine(local, high_vector),
            )

for offset, rows in steps.items():
    for s2, s3, left in rows:
        m2 = q - s2
        for s4, s5, middle in exact45:
            if q - s4 > m2:
                continue
            local = K71.combine(left, middle)
            for high_name, high_vector in high:
                keep(
                    f"s2={s2}/s3={s3}/s4={s4}/s5={s5}/{high_name}/offset{offset}_plain",
                    K71.combine(local, high_vector),
                )

rows = sorted(heap, reverse=True)
unsafe = sorted(
    (
        (value, values, label)
        for values, (value, label) in unsafe_by_defects.items()
    ),
    reverse=True,
)
print(json.dumps({
    "evaluations": serial,
    "safe_premium_ceiling": ceiling,
    "unsafe_distinct_defect_tuples": len(unsafe),
    "safe_maximum": {
        "premium": safe_maximum[0],
        "label": safe_maximum[1],
        "defects": defects(safe_maximum[1]),
        "caps": safe_maximum[2],
        "premium_margin": ceiling - safe_maximum[0],
    },
    "unsafe": [
        {"premium": value, "defects": values, "label": label}
        for value, values, label in unsafe
    ],
    "top": [
        {"premium": value, "label": label, "defects": values}
        for value, _, label, values, _ in rows
    ],
}, indent=2))
