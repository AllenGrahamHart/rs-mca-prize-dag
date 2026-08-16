#!/usr/bin/env python3
"""Explore K'=72 joint H4/H5 prices; certify no theorem or row closure."""

from __future__ import annotations

import importlib.util
import json
import tarfile
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
    "k71_payment_joint_active_probe",
    ROOT
    / "background/nodes/rate_half_mca_rank11_k71_carrier_trichotomy_payment/verify.py",
)

ACTIVE = (
    75914134508335899709894798966093890652808080,
    244053066090492313450064227236486900662170200,
    504548143592130314588511908104941831388621920,
    706691758745348881775614811130828421379743420,
    709014605156721508718484455384231706070672416,
    506454724977873231111801170170441650224086320,
    261393362018968337257639788063127069403580480,
    92573629519330911905901880122906340406215850,
)
CEILING = 41100317939998934447573065780978817075733675000

rows = {}
for union in range(35, 38):
    for dimension in (5, 6):
        caps = K71.charged_vector(72, ACTIVE, union, dimension)
        premium = K71.premium(caps)
        rows[f"u{union}_g{dimension}"] = {
            "premium": premium,
            "margin": CEILING - premium,
            "caps": caps,
        }

parallel_collision_caps = K71.charged_vector(72, ACTIVE, 31, 8)
parallel_collision_premium = K71.premium(parallel_collision_caps)
rows["u31_g8_second_parallel_class"] = {
    "premium": parallel_collision_premium,
    "margin": CEILING - parallel_collision_premium,
    "caps": parallel_collision_caps,
}
flat_extension_caps = K71.charged_vector(72, ACTIVE, 33, 8)
flat_extension_premium = K71.premium(flat_extension_caps)
rows["u33_g8_B3_parallel_extension"] = {
    "premium": flat_extension_premium,
    "margin": CEILING - flat_extension_premium,
    "caps": flat_extension_caps,
}
for union, dimension in ((36, 5), (37, 5)):
    flag_caps = K71.charged_vector(
        72,
        flat_extension_caps,
        union,
        dimension,
    )
    flag_premium = K71.premium(flag_caps)
    rows[f"u33_g8__u{union}_g{dimension}_flag"] = {
        "premium": flag_premium,
        "margin": CEILING - flag_premium,
        "caps": flag_caps,
    }


def independent_inside(union: int, parallel: int, size: int) -> int:
    if size < 0:
        return 0
    ordinary = union - parallel
    return comb(ordinary, size) + parallel * (
        comb(ordinary, size - 1) if size >= 1 else 0
    )


def parallel_class_cap(
    kprime: int,
    union: int,
    dimension: int,
    parallel: int,
    target: int,
) -> int:
    m = 67472 + kprime
    intersection = dimension + 1 - target
    if intersection <= 0:
        return 10**500
    outside_completion_budget = max(0, kprime - dimension - union)
    count = independent_inside(union, parallel, target)
    for external in range(1, target + 1):
        count += (
            independent_inside(union, parallel, target - external)
            * comb(m - union, external - 1)
            * outside_completion_budget
            // external
        )
    return count * comb(m - target, 11 - target)


def completion_stratified_cap(
    kprime: int,
    union: int,
    dimension: int,
    parallel: int,
    target: int,
    completion_maximum: int,
    fixed_budget_override: int | None = None,
) -> int:
    m = 67472 + kprime
    fixed_budget = (
        max(0, kprime - dimension - union)
        if fixed_budget_override is None
        else fixed_budget_override
    )
    count = independent_inside(union, parallel, target)
    for external in range(1, target + 1):
        budget = completion_maximum
        if external <= dimension:
            budget = min(budget, fixed_budget)
        count += (
            independent_inside(union, parallel, target - external)
            * comb(m - union, external - 1)
            * budget
            // external
        )
    return count * comb(m - target, 11 - target)


parallel_caps = tuple(
    min(
        ACTIVE[target - 2],
        parallel_class_cap(72, 37, 5, 30, target),
    )
    for target in K71.SUPPORTS
)
parallel_premium = K71.premium(parallel_caps)
rows["u37_g5_B2"] = {
    "premium": parallel_premium,
    "margin": CEILING - parallel_premium,
    "caps": parallel_caps,
}

plain_caps = tuple(
    min(
        ACTIVE[target - 2],
        parallel_class_cap(72, 37, 5, 0, target),
    )
    for target in K71.SUPPORTS
)
plain_premium = K71.premium(plain_caps)
rows["u37_g5_stratified"] = {
    "premium": plain_premium,
    "margin": CEILING - plain_premium,
    "caps": plain_caps,
}

completion_maxima = {
    2: 28,
    3: 30,
    4: 31,
    5: 31,
    6: 58,
    7: 59,
    8: 60,
    9: 61,
}
completion_caps = tuple(
    min(
        ACTIVE[target - 2],
        completion_stratified_cap(
            72,
            37,
            5,
            30,
            target,
            completion_maxima[target],
        ),
    )
    for target in K71.SUPPORTS
)
completion_premium = K71.premium(completion_caps)
rows["u37_g5_completion_stratified_B2"] = {
    "premium": completion_premium,
    "margin": CEILING - completion_premium,
    "caps": completion_caps,
}
for lowered_targets in ({4}, {5}, {4, 5}):
    lowered_caps = tuple(
        min(
            ACTIVE[target - 2],
            completion_stratified_cap(
                72,
                37,
                5,
                30,
                target,
                completion_maxima[target],
                29 if target in lowered_targets else None,
            ),
        )
        for target in K71.SUPPORTS
    )
    lowered_premium = K71.premium(lowered_caps)
    label = "budget29_" + "_".join(map(str, sorted(lowered_targets)))
    rows[label] = {
        "premium": lowered_premium,
        "margin": CEILING - lowered_premium,
        "caps": lowered_caps,
    }

for lowered_targets in ({4}, {5}, {4, 5}):
    lowered_caps = tuple(
        min(
            flat_extension_caps[target - 2],
            completion_stratified_cap(
                72,
                36,
                5,
                29,
                target,
                completion_maxima[target],
                30 if target in lowered_targets else None,
            ),
        )
        for target in K71.SUPPORTS
    )
    lowered_premium = K71.premium(lowered_caps)
    label = "u36_budget30_" + "_".join(
        map(str, sorted(lowered_targets))
    )
    rows[label] = {
        "premium": lowered_premium,
        "margin": CEILING - lowered_premium,
        "caps": lowered_caps,
    }
rows["diagnostics"] = {
    "deficits": {
        str(target): K71.LEDGER.DEFICITS[target]
        for target in K71.SUPPORTS
    },
    "active_contributions": {
        str(target): K71.LEDGER.DEFICITS[target] * ACTIVE[target - 2]
        for target in K71.SUPPORTS
    },
    "u37_g5_contributions": {
        str(target): K71.LEDGER.DEFICITS[target]
        * rows["u37_g5"]["caps"][target - 2]
        for target in K71.SUPPORTS
    },
    "completion_raw_caps": {
        str(target): completion_stratified_cap(
            72,
            37,
            5,
            30,
            target,
            completion_maxima[target],
        )
        for target in K71.SUPPORTS
    },
}

print(json.dumps(rows, indent=2))
