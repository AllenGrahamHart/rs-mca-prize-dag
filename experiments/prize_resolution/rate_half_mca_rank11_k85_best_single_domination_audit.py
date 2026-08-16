#!/usr/bin/env python3
"""Independent best-single-edge traversal of one K'=85 residual lane."""

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
    "k85_best_single_audit_base",
    Path(__file__).with_name(
        "rate_half_mca_rank11_k85_edge4_domination_falsifier.py"
    ),
)
AUDIT = load_module(
    "k85_best_single_audit_formulas",
    BASE.ROOT
    / "experiments/prize_resolution/"
    "rate_half_mca_rank11_k83_threshold_frontier_audit.py",
)
AUDIT.KPRIME, AUDIT.Q, AUDIT.M = BASE.KPRIME, BASE.Q, BASE.M
AUDIT.adjacent_pair.cache_clear()


def independent_adjacent_caps(charges):
    edges = {}
    for union, dimension in charges:
        if BASE.KPRIME - union - dimension < 0:
            continue
        for support in range(4, min(dimension, 9)):
            value = AUDIT.adjacent_pair(union, dimension, support)
            if support == 4:
                value = min(
                    value,
                    AUDIT.PROBE.joint45_weighted_cap(
                        BASE.KPRIME, union, dimension
                    ),
                )
            edges[support] = min(edges.get(support, value), value)
    return tuple(sorted(edges.items()))


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
        adjacent = independent_adjacent_caps(charges)
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
    row["implementation"] = "audit"
    if row["event"] == "FALSIFIED":
        row["single_edges"] = row.pop("edge4_cap")
        row["single_after"] = row.pop("edge4_after")
        row["single_high"] = row.pop("edge4_high")
    print(json.dumps(row, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
