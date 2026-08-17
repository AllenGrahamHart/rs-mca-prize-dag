#!/usr/bin/env python3
"""Price K'=87 residual profiles by support-disjoint adjacent edges."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SINGLE = load_module(
    "k87_disjoint_primary_base",
    Path(__file__).with_name(
        "rate_half_mca_rank11_k87_best_single_domination_falsifier.py"
    ),
)
BASE = SINGLE.BASE
BASE.edge4_price = lambda caps, adjacent: BASE.ROUTER.priced_all_adjacent(
    BASE.KPRIME, caps, adjacent
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("offset", type=int)
    args = parser.parse_args()
    row = SINGLE.CORE.scan(BASE, args.offset)
    if row["event"] == "FALSIFIED":
        row["adjacent_edges"] = row.pop("single_edges")
        row["disjoint_after"] = row.pop("single_after")
        row["disjoint_high"] = row.pop("single_high")
    print(json.dumps(row, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
