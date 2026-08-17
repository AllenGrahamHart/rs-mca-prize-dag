#!/usr/bin/env python3
"""Cache the exact lower-oriented K'=87 clipped-cap specializations."""

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


OLD = load_module(
    "k87_clipped_primary_uncached",
    Path(__file__).with_name(
        "rate_half_mca_rank11_k87_clipped_domination_falsifier.py"
    ),
)
BASE = OLD.BASE


@lru_cache(maxsize=None)
def clipped_bound(union: int, dimension: int, raw5: int, raw6: int) -> int:
    value = OLD.CLIPPED.lower_orientation(
        BASE.KPRIME, BASE.M, union, dimension, 5, raw5, raw6
    )
    return value.numerator // value.denominator


def clipped_price(caps, adjacent, charges) -> int:
    edges = dict(adjacent)
    factor5, factor6 = comb(BASE.M - 5, 6), comb(BASE.M - 6, 5)
    raw5, raw6 = caps[5 - 2] // factor5, caps[6 - 2] // factor6
    for union, dimension in charges:
        if dimension < 6 or BASE.KPRIME - union - dimension < 0:
            continue
        bound = clipped_bound(union, dimension, raw5, raw6)
        edges[5] = min(edges.get(5, bound), bound)
    return BASE.ROUTER.priced_all_adjacent(
        BASE.KPRIME, caps, tuple(sorted(edges.items()))
    )


BASE.clipped_price = clipped_price


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("offset", type=int)
    args = parser.parse_args()
    row = OLD.CORE.scan(BASE, args.offset)
    row["implementation"] = "primary-cached"
    row["clipped_cache_entries"] = clipped_bound.cache_info().currsize
    print(json.dumps(row, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
