#!/usr/bin/env python3
"""Adapt the exact K'=85 primary raw-threshold scanner to K'=86."""

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


BASE = load_module(
    "k86_raw_threshold_primary_base",
    Path(__file__).with_name(
        "rate_half_mca_rank11_k85_raw_threshold_offset_probe.py"
    ),
)
BASE.KPRIME, BASE.Q, BASE.M, BASE.N_CODE = 86, 76, 67558, 1048662
BASE.OLD_ROW = BASE.K71.LEDGER.row(BASE.KPRIME)
BASE.CEILING = (
    BASE.K71.LEDGER.RECORD_FLOOR * 55 * comb(BASE.M, 11)
    - 55 * comb(BASE.N_CODE, 11)
    - 55 * int(BASE.OLD_ROW["kernel"])
    - int(BASE.OLD_ROW["marks"])
    - 1
) // BASE.K71.LEDGER.RECORD_FLOOR


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("offset", type=int)
    args = parser.parse_args()
    row = BASE.offset_envelope(args.offset)
    row["event"] = "K86_RAW_OFFSET"
    print(json.dumps(row, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
