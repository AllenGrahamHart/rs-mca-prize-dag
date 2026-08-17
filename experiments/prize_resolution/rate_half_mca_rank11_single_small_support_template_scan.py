#!/usr/bin/env python3
"""Scan exact raw one-sided support-2/3 templates over a short K' interval."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
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
    "single_small_support_template_router",
    ROOT
    / "experiments/prize_resolution/"
    "rate_half_mca_rank11_k83_stratified56_lane_probe.py",
)
K71 = ROUTER.K71


def ceiling(kprime: int) -> int:
    m, n = 67472 + kprime, 1048576 + kprime
    row = K71.LEDGER.row(kprime)
    return (
        K71.LEDGER.RECORD_FLOOR * 55 * comb(m, 11)
        - 55 * comb(n, 11)
        - 55 * int(row["kernel"])
        - int(row["marks"])
        - 1
    ) // K71.LEDGER.RECORD_FLOOR


def scan_row(kprime: int) -> dict[str, object]:
    q, m = kprime - 10, 67472 + kprime
    baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(q, m)
    _, _, front45 = K71.exact45_rows(kprime, baseline)
    _, high = K71.PARENT.high_group(kprime, baseline)
    maximum = (-1, "", ())
    rows = 0

    for source in (2, 3):
        for completion in range(1, q + 1):
            if source == 2:
                s2, s3 = q - completion, q
            else:
                s2, s3 = q, q - completion
            left = K71.base23_vector(kprime, baseline, s2, s3)
            for middle_name, middle in front45:
                for high_name, high_vector in high:
                    caps = K71.combine(left, middle, high_vector)
                    value = K71.premium(caps)
                    rows += 1
                    if value > maximum[0]:
                        maximum = (
                            value,
                            (
                                f"source={source}/M={completion}/"
                                f"s2={s2}/s3={s3}/{middle_name}/{high_name}"
                            ),
                            caps,
                        )

    active = maximum[1]
    defects = {
        str(support): int(re.search(rf"s{support}=(\d+)", active).group(1))
        for support in range(2, 6)
    }
    safe = ceiling(kprime)
    return {
        "event": "SINGLE_TEMPLATE_ROW",
        "kprime": kprime,
        "q": q,
        "rows": rows,
        "maximum": maximum[0],
        "ceiling": safe,
        "margin": safe - maximum[0],
        "active_branch": active,
        "active_defects": defects,
        "active_caps": {
            str(support): maximum[2][support - 2]
            for support in range(2, 10)
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("interval", help="inclusive START:END")
    args = parser.parse_args()
    start, end = map(int, args.interval.split(":"))
    assert 83 <= start <= end <= 15528 and end - start <= 128
    rows = []
    for kprime in range(start, end + 1):
        row = scan_row(kprime)
        rows.append(row)
        print(json.dumps(row, sort_keys=True), flush=True)
    first_unsafe = next(
        (row["kprime"] for row in rows if row["margin"] < 0),
        None,
    )
    print(json.dumps({
        "event": "SINGLE_TEMPLATE_SCAN",
        "interval": [start, end],
        "rows": len(rows),
        "minimum_margin": min(row["margin"] for row in rows),
        "first_unsafe": first_unsafe,
    }, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
