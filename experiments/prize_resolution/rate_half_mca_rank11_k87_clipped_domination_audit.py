#!/usr/bin/env python3
"""Apply upper-oriented raw-clipped pricing to K'=87 residual profiles."""

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


DIRECTORY = Path(__file__).resolve().parent
SINGLE = load_module(
    "k87_clipped_audit_base",
    DIRECTORY / "rate_half_mca_rank11_k87_best_single_domination_audit.py",
)
CLIPPED = load_module(
    "k87_clipped_audit_formula",
    DIRECTORY / "rate_half_mca_raw_clipped_adjacent_support.py",
)
CORE = load_module(
    "k87_clipped_audit_core",
    DIRECTORY / "rate_half_mca_rank11_k87_clipped_scan_core.py",
)
BASE = SINGLE.BASE


def clipped_price(caps, adjacent, charges) -> int:
    edges = dict(adjacent)
    factor5, factor6 = comb(BASE.M - 5, 6), comb(BASE.M - 6, 5)
    raw5, raw6 = caps[5 - 2] // factor5, caps[6 - 2] // factor6
    for union, dimension in charges:
        if dimension < 6 or BASE.KPRIME - union - dimension < 0:
            continue
        value = CLIPPED.upper_orientation(
            BASE.KPRIME, BASE.M, union, dimension, 5, raw5, raw6
        )
        bound = value.numerator // value.denominator
        edges[5] = min(edges.get(5, bound), bound)
    return SINGLE.BEST.AUDIT.price(caps, tuple(sorted(edges.items())))


BASE.clipped_price = clipped_price


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("offset", type=int)
    args = parser.parse_args()
    row = CORE.scan(BASE, args.offset)
    row["implementation"] = "audit"
    print(json.dumps(row, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
