#!/usr/bin/env python3
"""Test whether the support-4/5 edge pays one K'=85 residual lane."""

from __future__ import annotations

import argparse
import importlib.util
import json
import tarfile
from math import comb
from pathlib import Path


ARCHIVES = list(Path(".").glob("*.tar.gz"))
ROOT = Path("repo") if ARCHIVES else Path(__file__).resolve().parents[2]
if ARCHIVES:
    for archive_path in ARCHIVES:
        with tarfile.open(archive_path, "r:gz") as archive:
            archive.extractall(ROOT, filter="data")


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ROUTER = load_module(
    "k85_edge4_falsifier_router",
    ROOT
    / "experiments/prize_resolution/"
    "rate_half_mca_rank11_k83_stratified56_lane_probe.py",
)
PROBE, K71 = ROUTER.PROBE, ROUTER.K71
KPRIME, Q, M, N_CODE = 85, 75, 67557, 1048661
LEADER = 41412868016209776721228891386909879523306833354
OLD_ROW = K71.LEDGER.row(KPRIME)
CEILING = (
    K71.LEDGER.RECORD_FLOOR * 55 * comb(M, 11)
    - 55 * comb(N_CODE, 11)
    - 55 * int(OLD_ROW["kernel"])
    - int(OLD_ROW["marks"])
    - 1
) // K71.LEDGER.RECORD_FLOOR
INFINITY = 10**500


def exact45_rows(baseline: dict[int, int]):
    caps4 = {
        defect: K71.PARENT.exact_cross_caps(KPRIME, 4, defect, baseline)
        for defect in range(Q + 1)
    }
    caps5 = {
        defect: K71.PARENT.exact_cross_caps(KPRIME, 5, defect, baseline)
        for defect in range(Q + 1)
    }
    for s4 in range(Q + 1):
        for s5 in range(Q + 1):
            vector = [
                min(baseline[target], caps4[s4][target], caps5[s5][target])
                for target in K71.SUPPORTS
            ]
            if s4 + s5 < Q:
                vector[2] = min(
                    vector[2],
                    K71.PARENT.PARENT.PARENT.JOINT.cap_for_defects(
                        KPRIME, M, s4, s5
                    )[0],
                )
            yield s4, s5, tuple(vector)


def raw_maximum(local, high):
    return max(
        (
            K71.premium(K71.combine(local, high_vector)),
            high_name,
            K71.combine(local, high_vector),
        )
        for high_name, high_vector in high
    )


def edge4_cap(union: int, dimension: int) -> int | None:
    if dimension < 5 or KPRIME - union - dimension < 0:
        return None
    return min(
        ROUTER.adjacent_weighted_cap(KPRIME, union, dimension, 4),
        PROBE.joint45_weighted_cap(KPRIME, union, dimension),
    )


def geometry_profiles(cases):
    profiles = {}
    for case, charges in cases.items():
        fixed = (INFINITY,) * len(K71.SUPPORTS)
        adjacent = None
        for union, dimension in charges:
            fixed = K71.combine(
                fixed,
                PROBE.fixed_union_cap(KPRIME, union, dimension),
            )
            local = edge4_cap(union, dimension)
            if local is not None:
                adjacent = local if adjacent is None else min(adjacent, local)
        profiles[(fixed, adjacent)] = (case, charges)
    return sorted(
        (case, charges, fixed, adjacent)
        for (fixed, adjacent), (case, charges) in profiles.items()
    )


def edge4_price(caps, adjacent: int | None) -> int:
    if adjacent is None:
        return K71.premium(caps)
    old = sum(
        K71.LEDGER.DEFICITS[support] * caps[support - 2]
        for support in (4, 5)
    )
    return K71.premium(caps) - old + adjacent


def scan(offset: int) -> dict[str, object]:
    assert offset in {1, 11, 23, 41}
    baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(Q, M)
    middle = list(exact45_rows(baseline))
    _, high = K71.PARENT.high_group(KPRIME, baseline)
    high = sorted(high)
    units = unsafe_units = profiles_checked = 0

    for m2 in range(1, Q - offset + 1):
        m3 = m2 + offset
        s2, s3 = Q - m2, Q - m3
        left = K71.base23_vector(KPRIME, baseline, s2, s3)
        raw_cache = {}
        for s4, s5, middle_vector in middle:
            units += 1
            local_caps = K71.combine(left, middle_vector)
            raw = raw_cache.get(local_caps)
            if raw is None:
                raw = raw_maximum(local_caps, high)
                raw_cache[local_caps] = raw
            if raw[0] <= CEILING:
                continue
            unsafe_units += 1
            cases = PROBE.mixed_cases(
                m2, offset, Q - s4, Q - s5
            )
            for case, charges, fixed, adjacent in geometry_profiles(cases):
                candidate = K71.combine(local_caps, fixed)
                after = max(
                    (
                        edge4_price(
                            K71.combine(candidate, high_vector), adjacent
                        ),
                        high_name,
                        K71.combine(candidate, high_vector),
                    )
                    for high_name, high_vector in high
                )
                profiles_checked += 1
                if after[0] > LEADER:
                    return {
                        "event": "FALSIFIED",
                        "offset": offset,
                        "m2": m2,
                        "m3": m3,
                        "s2": s2,
                        "s3": s3,
                        "s4": s4,
                        "s5": s5,
                        "m4": Q - s4,
                        "m5": Q - s5,
                        "case": case,
                        "charges": charges,
                        "edge4_cap": adjacent,
                        "raw_before": raw[0],
                        "raw_before_high": raw[1],
                        "edge4_after": after[0],
                        "edge4_high": after[1],
                        "leader": LEADER,
                        "excess_over_leader": after[0] - LEADER,
                        "units_checked": units,
                        "unsafe_units_checked": unsafe_units,
                        "profiles_checked": profiles_checked,
                        "complete": False,
                    }
        print(json.dumps({
            "event": "PROGRESS",
            "offset": offset,
            "m2": m2,
            "units_checked": units,
            "unsafe_units_checked": unsafe_units,
            "profiles_checked": profiles_checked,
        }, sort_keys=True), flush=True)
    return {
        "event": "SURVIVED",
        "offset": offset,
        "units_checked": units,
        "unsafe_units_checked": unsafe_units,
        "profiles_checked": profiles_checked,
        "leader": LEADER,
        "complete": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("offset", type=int)
    args = parser.parse_args()
    print(json.dumps(scan(args.offset), sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
