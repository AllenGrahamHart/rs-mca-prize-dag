#!/usr/bin/env python3
"""Explore conservative K'=72 two-step carrier caps; certify no theorem."""

from __future__ import annotations

import importlib.util
import itertools
import json
import re
import tarfile
from functools import lru_cache
from math import comb
from pathlib import Path


ARCHIVE = next(Path(".").glob("*.tar.gz"))
ROOT = Path("repo")


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


with tarfile.open(ARCHIVE, "r:gz") as archive:
    archive.extractall(ROOT, filter="data")

K71 = load_module(
    "k71_payment_probe",
    ROOT
    / "background/nodes/rate_half_mca_rank11_k71_carrier_trichotomy_payment/verify.py",
)


@lru_cache(maxsize=None)
def fixed_union_cap(kprime: int, union: int, dimension: int):
    """Return the reusable cap vector imposed by one fixed-union charge."""
    return K71.charged_vector(
        kprime,
        (10**500,) * len(K71.SUPPORTS),
        union,
        dimension,
    )


@lru_cache(maxsize=None)
def joint45_weighted_cap(kprime: int, union: int, dimension: int):
    """Return one nonseparable support-four/five flat-coupling charge."""
    m = 67472 + kprime
    outside = m - union
    degree = kprime - 1 - union
    rank3_cap = degree - dimension + 4
    completion = rank3_cap - 3

    def lower(support: int) -> int:
        total = comb(union, support)
        for external in range(1, support):
            total += (
                comb(union, support - external)
                * comb(outside, external - 1)
                * completion
                // external
            )
        return total

    top4 = completion * comb(outside, 3) // 4
    top5 = (
        completion * comb(outside, 4)
        - (outside - rank3_cap) * top4
    ) // 5
    incidence4 = (lower(4) + top4) * comb(m - 4, 7)
    incidence5 = (lower(5) + top5) * comb(m - 5, 6)
    return (
        K71.LEDGER.DEFICITS[4] * incidence4
        + K71.LEDGER.DEFICITS[5] * incidence5
    )


def position23_group(kprime: int, baseline: dict[int, int]):
    q = kprime - 10
    ordinary = {}
    steps = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    carrier32 = []
    impossible = 0
    for s2 in range(q + 1):
        for s3 in range(q + 1):
            vector = K71.base23_vector(kprime, baseline, s2, s3)
            m2 = q - s2
            m3 = q - s3
            if m2 > 0 and m3 > 0 and m3 <= m2:
                if s2 + s3 < q:
                    impossible += 1
                    continue
                b2 = m2 + 1
                b3 = m3 + 2
                for name, union, dimension in (
                    ("T23", b2 + b3, 7),
                    ("A23", b2 + b3 - 1, 8),
                ):
                    charged = K71.charged_vector(
                        kprime, vector, union, dimension
                    )
                    ordinary[charged] = f"s2={s2}/s3={s3}/{name}"
            elif m2 > 0 and m3 == 30 and m2 < 30:
                carrier32.append((s2, s3, vector))
            elif m2 > 0 and m3 - m2 in steps:
                steps[m3 - m2].append((s2, s3, vector))
            else:
                ordinary[vector] = f"s2={s2}/s3={s3}/U23"
    return ordinary, K71.maximal_vectors(ordinary), steps, carrier32, impossible


def offset_cases(m2: int, offset: int, include_support5: bool):
    b2 = m2 + 1
    b3 = m2 + offset + 2
    b4 = m2 + offset + 3
    b5 = m2 + offset + 4
    cases = {
        "T23": [(b2 + b3, 7)],
        "A23": [(b2 + b3 - 1, 8)],
        "T24": [(b2 + b4, 6)],
        "A24": [(b2 + b4 - 1, 7)],
    }
    outside3 = offset + 1
    outside4 = offset + 2
    outside5 = offset + 3
    position5 = {
        "T25": (b2 + b5, 5),
        "A25": (b2 + b5 - 1, 6),
    }
    # Full overlap is impossible: only offset-1 of the outside points can be
    # higher-support completion points, so at least two would be deletion
    # anchors.  Their line also contains the B2 point, contradicting full
    # completion relative to that deletion.
    for overlap35 in range(outside3):
        union35 = b2 + outside3 + outside5 - overlap35
        dimension35 = 6 if overlap35 >= 1 else 5
        position5[f"N35_t{overlap35}"] = (union35, dimension35)

    max_overlap34 = outside3 - 1
    for overlap34 in range(max_overlap34 + 1):
        union34 = b2 + outside3 + outside4 - overlap34
        dimension34 = 7 if overlap34 >= 1 else 6
        if not include_support5:
            cases[f"N34_t{overlap34}"] = [(union34, dimension34)]
            continue
        for name5, charge5 in position5.items():
            cases[f"N34_t{overlap34}__{name5}"] = [
                (union34, dimension34),
                charge5,
            ]
    return cases


def mixed_cases(m2: int, offset3: int, m4: int, m5: int):
    b2 = m2 + 1
    b3 = m2 + offset3 + 2
    outside3 = offset3 + 1
    cases = {
        "T23": [(b2 + b3, 7)],
        "A23": [(b2 + b3 - 1, 8)],
    }

    def higher_cases(support: int, maximum: int):
        if maximum <= 0:
            return {f"E{support}": []}
        carrier = maximum + support - 1
        rows = {
            f"T{support}": [(b2 + carrier, 10 - support)],
            f"A{support}": [(b2 + carrier - 1, 11 - support)],
        }
        if maximum <= m2:
            return rows
        offset = maximum - m2
        outside = support + offset - 2
        for overlap in range(min(outside3, offset) + 1):
            union = b2 + outside3 + outside - overlap
            dimension = 11 - support if overlap >= 1 else 10 - support
            rows[f"N{support}_t{overlap}"] = [(union, dimension)]
        return rows

    cases4 = higher_cases(4, m4)
    cases5 = higher_cases(5, m5)
    for name4, charges4 in cases4.items():
        for name5, charges5 in cases5.items():
            name = f"F23__{name4}__{name5}"
            if name4.startswith("N4_t") and name5.startswith("N5_t"):
                overlap4 = int(name4.removeprefix("N4_t"))
                overlap5 = int(name5.removeprefix("N5_t"))
                if overlap4 >= 1 and overlap5 >= 1:
                    active_k72_shape = (
                        1 <= m2 <= 29
                        and m2 + offset3 == 30
                        and m4 == 31
                        and m5 == 31
                        and overlap4 == offset3 + 1
                        and overlap5 == offset3 + 1
                    )
                    if not active_k72_shape:
                        cases[name] = charges4 + charges5
                        continue
                    outside4 = 4 + (m4 - m2) - 2
                    outside5 = 5 + (m5 - m2) - 2
                    residual4 = outside4 - overlap4
                    residual5 = outside5 - overlap5
                    union_min = b2 + outside3 + max(residual4, residual5)
                    union_max = b2 + outside3 + residual4 + residual5
                    assert (union_min, union_max) == (35, 37)
                    cases[f"{name}__J45_u36_g6"] = (
                        charges4 + charges5 + [(36, 6)]
                    )
                    cases[f"{name}__J45_u36_g5_flag"] = (
                        charges4 + charges5 + [(33, 8), (36, 5)]
                    )
                    cases[f"{name}__J45_u37_g6"] = (
                        charges4 + charges5 + [(37, 6)]
                    )
                    cases[f"{name}__J45_u37_g5"] = (
                        charges4 + charges5 + [(37, 5)]
                    )
                    continue
            cases[name] = charges4 + charges5
    return cases


def branch_summary(kprime: int):
    q = kprime - 10
    m = 67472 + kprime
    baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(q, m)
    raw23, front23, steps, carrier32, impossible = position23_group(
        kprime, baseline
    )
    exact45, _, front45 = K71.exact45_rows(kprime, baseline)
    _, front69 = K71.PARENT.high_group(kprime, baseline)
    maximum = (-1, "", ())
    counts = {
        "ordinary": 0,
        "one_plain": 0,
        "one_geom": 0,
        "two_plain": 0,
        "two_geom": 0,
        "three_plain": 0,
        "three_geom": 0,
        "four_plain": 0,
        "four_geom": 0,
        "five_plain": 0,
        "five_geom": 0,
        "six_plain": 0,
        "six_geom": 0,
        "carrier32_plain": 0,
        "carrier32_geom": 0,
    }
    geometry_max = {}

    def keep(value, label, caps):
        nonlocal maximum
        if value > maximum[0]:
            maximum = (value, label, caps)

    for left, middle, right in itertools.product(front23, front45, front69):
        caps = K71.combine(left[1], middle[1], right[1])
        keep(
            K71.premium(caps),
            f"{left[0]}/{middle[0]}/{right[0]}/plain",
            caps,
        )
        counts["ordinary"] += 1

    for s2, s3, left in carrier32:
        m2 = q - s2
        offset = 30 - m2
        for s4, s5, middle in exact45:
            m4 = q - s4
            m5 = q - s5
            local = K71.combine(left, middle)
            prefix = f"s2={s2}/s3={s3}/s4={s4}/s5={s5}"
            if (m4, m5) != (31, 31):
                for right in front69:
                    caps = K71.combine(local, right[1])
                    keep(
                        K71.premium(caps),
                        f"{prefix}/{right[0]}/carrier32_plain",
                        caps,
                    )
                    counts["carrier32_plain"] += 1
                continue
            cases = mixed_cases(m2, offset, m4, m5)
            for name, charges in cases.items():
                candidate = local
                for union, dimension in charges:
                    candidate = K71.combine(
                        candidate,
                        fixed_union_cap(kprime, union, dimension),
                    )
                for right in front69:
                    caps = K71.combine(candidate, right[1])
                    value = K71.premium(caps)
                    joint = None
                    if name.endswith("J45_u36_g5_flag"):
                        joint = joint45_weighted_cap(kprime, 36, 5)
                    elif name.endswith("J45_u37_g5"):
                        joint = joint45_weighted_cap(kprime, 37, 5)
                    if joint is not None:
                        old45 = sum(
                            K71.LEDGER.DEFICITS[support]
                            * caps[support - 2]
                            for support in (4, 5)
                        )
                        value -= old45 - min(old45, joint)
                    geometry_max[name] = max(
                        geometry_max.get(name, -1), value
                    )
                    keep(
                        value,
                        f"{prefix}/{right[0]}/carrier32_{name}",
                        caps,
                    )
                    counts["carrier32_geom"] += 1

    for step_name, rows, offset in (
        ("one", steps[1], 1),
        ("two", steps[2], 2),
        ("three", steps[3], 3),
        ("four", steps[4], 4),
        ("five", steps[5], 5),
        ("six", steps[6], 6),
    ):
        for s2, s3, left in rows:
            m2 = q - s2
            for s4, s5, middle in exact45:
                m4 = q - s4
                m5 = q - s5
                local = K71.combine(left, middle)
                prefix = f"s2={s2}/s3={s3}/s4={s4}/s5={s5}"
                if step_name == "one" or m4 in (
                    m2 + 1,
                    m2 + offset + 1,
                ):
                    cases = mixed_cases(m2, offset, m4, m5)
                else:
                    if m4 != m2 + offset:
                        for right in front69:
                            caps = K71.combine(local, right[1])
                            keep(
                                K71.premium(caps),
                                f"{prefix}/{right[0]}/{step_name}_plain",
                                caps,
                            )
                        counts[f"{step_name}_plain"] += len(front69)
                        continue
                    cases = offset_cases(
                        m2,
                        offset,
                        include_support5=(m5 == m2 + offset),
                    )
                for name, charges in cases.items():
                    candidate = local
                    for union, dimension in charges:
                        candidate = K71.combine(
                            candidate,
                            fixed_union_cap(kprime, union, dimension),
                        )
                    for right in front69:
                        caps = K71.combine(candidate, right[1])
                        value = K71.premium(caps)
                        joint = None
                        if name.endswith("J45_u36_g5_flag"):
                            joint = joint45_weighted_cap(kprime, 36, 5)
                        elif name.endswith("J45_u37_g5"):
                            joint = joint45_weighted_cap(kprime, 37, 5)
                        if joint is not None:
                            old45 = sum(
                                K71.LEDGER.DEFICITS[support]
                                * caps[support - 2]
                                for support in (4, 5)
                            )
                            value -= old45 - min(old45, joint)
                        geometry_max[name] = max(
                            geometry_max.get(name, -1), value
                        )
                        keep(
                            value,
                            f"{prefix}/{right[0]}/{step_name}_{name}",
                            caps,
                        )
                        counts[f"{step_name}_geom"] += 1

    defects = {
        str(support): int(
            re.search(rf"s{support}=([0-9]+)", maximum[1]).group(1)
        )
        for support in range(2, 6)
    }
    return {
        "maximum": maximum[0],
        "active_branch": maximum[1],
        "active_caps": {
            str(target): maximum[2][target - 2]
            for target in K71.SUPPORTS
        },
        "active_defects": defects,
        "impossible": impossible,
        "front23": len(front23),
        "one_step_pairs": len(steps[1]),
        "two_step_pairs": len(steps[2]),
        "three_step_pairs": len(steps[3]),
        "four_step_pairs": len(steps[4]),
        "five_step_pairs": len(steps[5]),
        "six_step_pairs": len(steps[6]),
        "carrier32_pairs": len(carrier32),
        "counts": counts,
        "geometry_max_top": sorted(
            geometry_max.items(), key=lambda item: item[1], reverse=True
        )[:20],
    }


def payment(kprime: int):
    summary = branch_summary(kprime)
    old = K71.LEDGER.row(kprime)
    n = 1048576 + kprime
    m = 67472 + kprime
    premium = summary["maximum"]
    marks = int(old["marks"])
    kernel = int(old["kernel"])
    full = (marks + K71.LEDGER.RECORD_FLOOR * premium) // 55
    demand = K71.LEDGER.RECORD_FLOOR * comb(m, 11) - comb(n, 11)
    total = kernel + full
    ceiling = (
        K71.LEDGER.RECORD_FLOOR * 55 * comb(m, 11)
        - 55 * comb(n, 11)
        - 55 * kernel
        - marks
        - 1
    ) // K71.LEDGER.RECORD_FLOOR
    summary.update(
        {
            "kprime": kprime,
            "safe_premium_ceiling": ceiling,
            "premium_margin": ceiling - premium,
            "gap": demand - total,
        }
    )
    return summary


print(json.dumps({"72": payment(72)}, indent=2))
