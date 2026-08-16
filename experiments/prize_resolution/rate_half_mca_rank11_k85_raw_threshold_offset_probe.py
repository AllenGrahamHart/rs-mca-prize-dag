#!/usr/bin/env python3
"""Locate the exact raw-safe K'=85 maximum in one positive offset lane."""

from __future__ import annotations

import argparse
import hashlib
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


K71 = load_module(
    "k85_raw_threshold_primary_k71",
    ROOT
    / "background/nodes/"
    "rate_half_mca_rank11_k71_carrier_trichotomy_payment/verify.py",
)
KPRIME, Q, M, N_CODE = 85, 75, 67557, 1048661
OLD_ROW = K71.LEDGER.row(KPRIME)
CEILING = (
    K71.LEDGER.RECORD_FLOOR * 55 * comb(M, 11)
    - 55 * comb(N_CODE, 11)
    - 55 * int(OLD_ROW["kernel"])
    - int(OLD_ROW["marks"])
    - 1
) // K71.LEDGER.RECORD_FLOOR


def offset_envelope(offset: int) -> dict[str, object]:
    assert 1 <= offset < Q
    baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(Q, M)
    exact45, _, _ = K71.exact45_rows(KPRIME, baseline)
    _, high = K71.PARENT.high_group(KPRIME, baseline)
    high = sorted(high)
    digest = hashlib.sha256()
    safe_max = (-1, "")
    unsafe_min: tuple[int, str] | None = None
    unsafe_max = (-1, "")
    safe_units = unsafe_units = 0
    profile = []

    for m2 in range(1, Q - offset + 1):
        m3 = m2 + offset
        s2, s3 = Q - m2, Q - m3
        left = K71.base23_vector(KPRIME, baseline, s2, s3)
        local_safe = local_unsafe = 0
        local_safe_max = -1
        local_unsafe_min: int | None = None
        local_unsafe_max = -1
        for s4, s5, middle in exact45:
            local = K71.combine(left, middle)
            raw = max(
                (
                    K71.premium(K71.combine(local, high_vector)),
                    high_name,
                )
                for high_name, high_vector in high
            )
            label = (
                f"s2={s2}/s3={s3}/s4={s4}/s5={s5}/"
                f"offset{offset}/{raw[1]}"
            )
            safe = raw[0] <= CEILING
            digest.update(
                f"{m2},{s4},{s5}:{raw[0]}:{raw[1]}:{int(safe)}\n".encode()
            )
            if safe:
                safe_units += 1
                local_safe += 1
                local_safe_max = max(local_safe_max, raw[0])
                safe_max = max(safe_max, (raw[0], label))
            else:
                unsafe_units += 1
                local_unsafe += 1
                local_unsafe_min = (
                    raw[0]
                    if local_unsafe_min is None
                    else min(local_unsafe_min, raw[0])
                )
                local_unsafe_max = max(local_unsafe_max, raw[0])
                item = (raw[0], label)
                unsafe_min = item if unsafe_min is None else min(unsafe_min, item)
                unsafe_max = max(unsafe_max, item)
        row = {
            "m2": m2,
            "safe_units": local_safe,
            "unsafe_units": local_unsafe,
            "safe_maximum": local_safe_max,
            "unsafe_minimum": local_unsafe_min,
            "unsafe_maximum": local_unsafe_max,
        }
        profile.append(row)
        print(
            json.dumps(
                {
                    "event": "K85_RAW_PROGRESS",
                    "implementation": "primary",
                    "offset": offset,
                    **row,
                },
                sort_keys=True,
            ),
            flush=True,
        )

    units = (Q - offset) * (Q + 1) ** 2
    assert safe_units + unsafe_units == units
    assert safe_max[0] >= 0
    return {
        "event": "K85_RAW_OFFSET",
        "implementation": "primary",
        "offset": offset,
        "units": units,
        "raw_rows": len(high) * units,
        "high_vectors": len(high),
        "safe_units": safe_units,
        "unsafe_units": unsafe_units,
        "safe_maximum": safe_max[0],
        "safe_margin": CEILING - safe_max[0],
        "safe_branch": safe_max[1],
        "unsafe_minimum": None if unsafe_min is None else unsafe_min[0],
        "unsafe_minimum_branch": None if unsafe_min is None else unsafe_min[1],
        "unsafe_maximum": None if unsafe_min is None else unsafe_max[0],
        "unsafe_maximum_branch": None if unsafe_min is None else unsafe_max[1],
        "classification_sha256": digest.hexdigest(),
        "m2_profile": profile,
        "complete": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("offset", type=int)
    args = parser.parse_args()
    row = offset_envelope(args.offset)
    print(json.dumps(row, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
