#!/usr/bin/env python3
"""Adapt the K'=85 residual scanner to the best single adjacent edge."""

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


BASE = load_module(
    "k85_best_single_base",
    Path(__file__).with_name(
        "rate_half_mca_rank11_k85_edge4_domination_falsifier.py"
    ),
)


def geometry_profiles(cases):
    profiles = {}
    for case, charges in cases.items():
        fixed = (BASE.INFINITY,) * len(BASE.K71.SUPPORTS)
        for union, dimension in charges:
            fixed = BASE.K71.combine(
                fixed,
                BASE.PROBE.fixed_union_cap(
                    BASE.KPRIME, union, dimension
                ),
            )
        adjacent = BASE.ROUTER.all_adjacent_caps(BASE.KPRIME, charges)
        profiles[(fixed, adjacent)] = (case, charges)
    return sorted(
        (case, charges, fixed, adjacent)
        for (fixed, adjacent), (case, charges) in profiles.items()
    )


def best_single_price(caps, adjacent) -> int:
    base = BASE.K71.premium(caps)
    values = [base]
    for edge, bound in adjacent:
        old = sum(
            BASE.K71.LEDGER.DEFICITS[support] * caps[support - 2]
            for support in (edge, edge + 1)
        )
        values.append(base - old + bound)
    return min(values)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("offset", type=int)
    args = parser.parse_args()
    BASE.geometry_profiles = geometry_profiles
    BASE.edge4_price = best_single_price
    row = BASE.scan(args.offset)
    if row["event"] == "FALSIFIED":
        row["single_edges"] = row.pop("edge4_cap")
        row["single_after"] = row.pop("edge4_after")
        row["single_high"] = row.pop("edge4_high")
    print(json.dumps(row, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
