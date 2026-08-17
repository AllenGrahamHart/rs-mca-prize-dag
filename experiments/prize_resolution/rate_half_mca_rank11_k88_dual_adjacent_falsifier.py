#!/usr/bin/env python3
"""Raw-clip both adjacent edges in the K'=88 residual router."""

from __future__ import annotations

import argparse
import importlib.util
import json
from functools import lru_cache
from math import comb
from pathlib import Path


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


DIRECTORY = Path(__file__).resolve().parent
OLD = load_module(
    "k88_dual_adjacent_primary_base",
    DIRECTORY / "rate_half_mca_rank11_k88_clipped_domination_falsifier_cached.py",
)
CLIPPED = load_module(
    "k88_dual_adjacent_primary_formula",
    DIRECTORY / "rate_half_mca_raw_clipped_adjacent_support.py",
)
BASE = OLD.BASE


@lru_cache(maxsize=None)
def clipped_bound(
    support: int, union: int, dimension: int, raw_low: int, raw_high: int
) -> int:
    value = CLIPPED.lower_orientation(
        BASE.KPRIME,
        BASE.M,
        union,
        dimension,
        support,
        raw_low,
        raw_high,
    )
    return value.numerator // value.denominator


def clipped_price(caps, adjacent, charges) -> int:
    edges = dict(adjacent)
    for support in (4, 5):
        factor_low = comb(BASE.M - support, 11 - support)
        factor_high = comb(BASE.M - support - 1, 10 - support)
        raw_low = caps[support - 2] // factor_low
        raw_high = caps[support - 1] // factor_high
        for union, dimension in charges:
            if dimension < support + 1 or BASE.KPRIME - union - dimension < 0:
                continue
            bound = clipped_bound(
                support, union, dimension, raw_low, raw_high
            )
            edges[support] = min(edges.get(support, bound), bound)
    return BASE.ROUTER.priced_all_adjacent(
        BASE.KPRIME, caps, tuple(sorted(edges.items()))
    )


BASE.clipped_price = clipped_price


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("offset", type=int)
    args = parser.parse_args()
    row = OLD.CORE.scan(BASE, args.offset)
    row["implementation"] = "primary-dual-adjacent"
    row["clipped_cache_entries"] = clipped_bound.cache_info().currsize
    print(json.dumps(row, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
