#!/usr/bin/env python3
"""Seek a K'=85 residual case not paid by fixed-union caps alone."""

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
    "k85_fixed_union_falsifier_router",
    ROOT
    / "experiments/prize_resolution/"
    "rate_half_mca_rank11_k83_stratified56_lane_probe.py",
)
PROBE = ROUTER.PROBE
K71 = ROUTER.K71
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


def raw_maximum(local: tuple[int, ...], high):
    return max(
        (
            K71.premium(K71.combine(local, high_vector)),
            high_name,
            K71.combine(local, high_vector),
        )
        for high_name, high_vector in high
    )


def scan(offset: int) -> dict[str, object]:
    assert offset in {1, 11, 23, 41}
    baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(Q, M)
    middle = list(exact45_rows(baseline))
    _, high = K71.PARENT.high_group(KPRIME, baseline)
    high = sorted(high)
    units = unsafe_units = cases_checked = 0

    for m2 in range(1, Q - offset + 1):
        m3 = m2 + offset
        s2, s3 = Q - m2, Q - m3
        left = K71.base23_vector(KPRIME, baseline, s2, s3)
        raw_cache = {}
        for s4, s5, middle_vector in middle:
            units += 1
            local = K71.combine(left, middle_vector)
            raw = raw_cache.get(local)
            if raw is None:
                raw = raw_maximum(local, high)
                raw_cache[local] = raw
            if raw[0] <= CEILING:
                continue
            unsafe_units += 1
            m4, m5 = Q - s4, Q - s5
            cases = PROBE.mixed_cases(m2, offset, m4, m5)
            for case, charges in cases.items():
                candidate = local
                for union, dimension in charges:
                    candidate = K71.combine(
                        candidate,
                        PROBE.fixed_union_cap(KPRIME, union, dimension),
                    )
                after = raw_maximum(candidate, high)
                cases_checked += 1
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
                        "m4": m4,
                        "m5": m5,
                        "case": case,
                        "charges": charges,
                        "raw_before": raw[0],
                        "raw_before_high": raw[1],
                        "fixed_union_after": after[0],
                        "fixed_union_high": after[1],
                        "leader": LEADER,
                        "excess_over_leader": after[0] - LEADER,
                        "local_caps": list(local),
                        "fixed_union_caps": list(after[2]),
                        "units_checked": units,
                        "unsafe_units_checked": unsafe_units,
                        "cases_checked": cases_checked,
                        "complete": False,
                    }
        print(json.dumps({
            "event": "PROGRESS",
            "offset": offset,
            "m2": m2,
            "units_checked": units,
            "unsafe_units_checked": unsafe_units,
            "cases_checked": cases_checked,
        }, sort_keys=True), flush=True)
    return {
        "event": "SURVIVED",
        "offset": offset,
        "units_checked": units,
        "unsafe_units_checked": unsafe_units,
        "cases_checked": cases_checked,
        "leader": LEADER,
        "complete": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("offset", type=int)
    args = parser.parse_args()
    row = scan(args.offset)
    print(json.dumps(row, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
