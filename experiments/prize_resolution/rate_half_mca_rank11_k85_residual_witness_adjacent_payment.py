#!/usr/bin/env python3
"""Print all adjacent-edge prices on one exact K'=85 residual witness."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import tarfile
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
    "k85_residual_primary_adjacent_router",
    ROOT
    / "experiments/prize_resolution/"
    "rate_half_mca_rank11_k83_stratified56_lane_probe.py",
)
AUDIT = load_module(
    "k85_residual_independent_adjacent_audit",
    ROOT
    / "experiments/prize_resolution/"
    "rate_half_mca_rank11_k83_threshold_frontier_audit.py",
)
PROBE, K71 = ROUTER.PROBE, ROUTER.K71
KPRIME, Q, M = 85, 75, 67557
LEADER = 41412868016209776721228891386909879523306833354
CEILING = 41412869809855175413648318362513310330909061869
SUPPORTS = tuple(range(2, 10))


def source_vector(baseline, support, defect):
    caps = K71.PARENT.exact_cross_caps(KPRIME, support, defect, baseline)
    return tuple(caps[target] for target in SUPPORTS)


def combine(*vectors):
    return tuple(min(values) for values in zip(*vectors))


def premium(vector):
    return sum(
        K71.LEDGER.DEFICITS[target] * vector[index]
        for index, target in enumerate(SUPPORTS)
    )


def option_prices(caps, adjacent):
    base = premium(caps)
    edges = dict(adjacent)
    result = {"none": base}
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
            result["+".join(map(str, selected))] = (
                base - old + sum(edges[edge] for edge in selected)
            )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    for name in ("offset", "m2", "s4", "s5"):
        parser.add_argument(name, type=int)
    parser.add_argument("case")
    args = parser.parse_args()
    m3 = args.m2 + args.offset
    s2, s3 = Q - args.m2, Q - m3
    baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(Q, M)
    left = combine(
        tuple(baseline[target] for target in SUPPORTS),
        source_vector(baseline, 2, s2),
        source_vector(baseline, 3, s3),
    )
    middle = list(combine(
        tuple(baseline[target] for target in SUPPORTS),
        source_vector(baseline, 4, args.s4),
        source_vector(baseline, 5, args.s5),
    ))
    if args.s4 + args.s5 < Q:
        middle[2] = min(
            middle[2],
            K71.PARENT.PARENT.PARENT.JOINT.cap_for_defects(
                KPRIME, M, args.s4, args.s5
            )[0],
        )
    local = combine(left, tuple(middle))
    cases = PROBE.mixed_cases(
        args.m2, args.offset, Q - args.s4, Q - args.s5
    )
    assert args.case in cases
    charges = cases[args.case]
    candidate = local
    for union, dimension in charges:
        candidate = combine(
            candidate,
            PROBE.fixed_union_cap(KPRIME, union, dimension),
        )
    _, high = K71.PARENT.high_group(KPRIME, baseline)
    _, high_name, caps = max(
        (premium(combine(candidate, vector)), name, combine(candidate, vector))
        for name, vector in sorted(high)
    )

    primary_edges = ROUTER.all_adjacent_caps(KPRIME, charges)
    primary_prices = option_prices(caps, primary_edges)
    assert ROUTER.priced_all_adjacent(
        KPRIME, caps, primary_edges
    ) == min(primary_prices.values())

    AUDIT.KPRIME, AUDIT.Q, AUDIT.M = KPRIME, Q, M
    AUDIT.adjacent_pair.cache_clear()
    audit_edges = {}
    for union, dimension in charges:
        if KPRIME - union - dimension < 0:
            continue
        for support in range(4, min(dimension, 9)):
            value = AUDIT.adjacent_pair(union, dimension, support)
            if support == 4:
                value = min(
                    value,
                    AUDIT.PROBE.joint45_weighted_cap(
                        KPRIME, union, dimension
                    ),
                )
            audit_edges[support] = min(
                audit_edges.get(support, value), value
            )
    audit_edges_tuple = tuple(sorted(audit_edges.items()))
    audit_prices = option_prices(caps, audit_edges_tuple)
    assert AUDIT.price(caps, audit_edges_tuple) == min(audit_prices.values())

    primary_best = min((value, name) for name, value in primary_prices.items())
    audit_best = min((value, name) for name, value in audit_prices.items())
    print(json.dumps({
        "event": "PASS",
        "witness": {
            "offset": args.offset,
            "m2": args.m2,
            "s2": s2,
            "s3": s3,
            "s4": args.s4,
            "s5": args.s5,
            "case": args.case,
            "charges": charges,
            "high": high_name,
        },
        "raw_after_fixed_union": premium(caps),
        "leader": LEADER,
        "ceiling": CEILING,
        "primary_edges": dict(primary_edges),
        "primary_prices": primary_prices,
        "primary_best_price": primary_best[0],
        "primary_best_edges": primary_best[1],
        "primary_margin_to_leader": LEADER - primary_best[0],
        "audit_edges": audit_edges,
        "audit_prices": audit_prices,
        "audit_best_price": audit_best[0],
        "audit_best_edges": audit_best[1],
        "audit_margin_to_leader": LEADER - audit_best[0],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
