#!/usr/bin/env python3
"""Price the parity-stable support-three template after its forced carrier."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
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
    "single_support3_postcharge_router",
    ROOT
    / "experiments/prize_resolution/"
    "rate_half_mca_rank11_k83_stratified56_lane_probe.py",
)
K71, PROBE = ROUTER.K71, ROUTER.PROBE


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


def priced_breakdown(
    caps: tuple[int, ...], adjacent: tuple[tuple[int, int], ...]
) -> tuple[int, str]:
    base = K71.premium(caps)
    edges = dict(adjacent)
    choices = [(base, "raw")]
    ordered = sorted(edges)
    for width in range(1, len(ordered) + 1):
        for selected in itertools.combinations(ordered, width):
            covered = {
                support
                for edge in selected
                for support in (edge, edge + 1)
            }
            if len(covered) != 2 * len(selected):
                continue
            old = sum(
                K71.LEDGER.DEFICITS[support] * caps[support - 2]
                for support in covered
            )
            value = base - old + sum(edges[edge] for edge in selected)
            choices.append((value, "+".join(f"A{edge}{edge + 1}" for edge in selected)))
    return min(choices)


def template_row(kprime: int) -> dict[str, object]:
    q, m = kprime - 10, 67472 + kprime
    completion = q // 2
    defect = q - completion
    union, dimension = completion + 2, 8
    baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(q, m)
    left = K71.base23_vector(kprime, baseline, q, defect)
    exact45, _, _ = K71.exact45_rows(kprime, baseline)
    middle = next(
        vector
        for s4, s5, vector in exact45
        if (s4, s5) == (defect, defect)
    )
    _, high = K71.PARENT.high_group(kprime, baseline)
    high_vector = next(
        vector
        for name, vector in high
        if name == "c6d2/c7d1/c8d1/c9d0"
    )
    local = K71.combine(left, middle)
    raw_caps = K71.combine(local, high_vector)
    charged_rows = ROUTER.charged_case_rows_all_adjacent(
        kprime, local, {"C3": [(union, dimension)]}
    )
    assert len(charged_rows) == 1
    (charged_local, adjacent), case = next(iter(charged_rows.items()))
    assert case == "C3"
    charged_caps = K71.combine(charged_local, high_vector)
    priced, active_charge = priced_breakdown(charged_caps, adjacent)
    assert priced == ROUTER.priced_all_adjacent(kprime, charged_caps, adjacent)
    safe = ceiling(kprime)
    return {
        "event": "POSTCHARGE_TEMPLATE_ROW",
        "kprime": kprime,
        "q": q,
        "parity": q % 2,
        "defects": [q, defect, defect, defect],
        "completion": completion,
        "carrier": [union, dimension],
        "raw_premium": K71.premium(raw_caps),
        "charged_raw_premium": K71.premium(charged_caps),
        "priced_premium": priced,
        "ceiling": safe,
        "margin": safe - priced,
        "active_charge": active_charge,
        "adjacent_caps": dict(adjacent),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("interval", help="inclusive START:END")
    args = parser.parse_args()
    start, end = map(int, args.interval.split(":"))
    assert 83 <= start <= end <= 15528 and end - start <= 128
    rows = []
    for kprime in range(start, end + 1):
        row = template_row(kprime)
        rows.append(row)
        print(json.dumps(row, sort_keys=True), flush=True)
    print(json.dumps({
        "event": "POSTCHARGE_TEMPLATE_INTERVAL",
        "interval": [start, end],
        "rows": len(rows),
        "minimum_margin": min(row["margin"] for row in rows),
        "active_charges": sorted({row["active_charge"] for row in rows}),
        "complete": True,
    }, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
