#!/usr/bin/env python3
"""Run either independent raw-threshold scanner at K'=88."""

from __future__ import annotations

import argparse
import importlib.util
import json
from math import comb
from pathlib import Path


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("implementation", choices=("primary", "audit"))
    parser.add_argument("offset", type=int)
    args = parser.parse_args()

    suffix = "probe" if args.implementation == "primary" else "audit"
    base = load_module(
        f"k88_raw_threshold_{args.implementation}_base",
        Path(__file__).with_name(
            f"rate_half_mca_rank11_k85_raw_threshold_offset_{suffix}.py"
        ),
    )
    base.KPRIME, base.Q, base.M, base.N_CODE = 88, 78, 67_560, 1_048_664
    base.OLD_ROW = base.K71.LEDGER.row(base.KPRIME)
    base.CEILING = (
        base.K71.LEDGER.RECORD_FLOOR * 55 * comb(base.M, 11)
        - 55 * comb(base.N_CODE, 11)
        - 55 * int(base.OLD_ROW["kernel"])
        - int(base.OLD_ROW["marks"])
        - 1
    ) // base.K71.LEDGER.RECORD_FLOOR
    row = base.offset_envelope(args.offset)
    row["event"] = "K88_RAW_OFFSET"
    print(json.dumps(row, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
