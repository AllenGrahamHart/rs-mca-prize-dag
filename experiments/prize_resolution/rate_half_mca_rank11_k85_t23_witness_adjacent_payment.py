#!/usr/bin/env python3
"""Price every adjacent-edge option on the first K'=85 T23 witness."""

from __future__ import annotations

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
    "k85_t23_primary_adjacent_router",
    ROOT
    / "experiments/prize_resolution/"
    "rate_half_mca_rank11_k83_stratified56_lane_probe.py",
)
AUDIT = load_module(
    "k85_t23_independent_adjacent_audit",
    ROOT
    / "experiments/prize_resolution/"
    "rate_half_mca_rank11_k83_threshold_frontier_audit.py",
)
PROBE, K71 = ROUTER.PROBE, ROUTER.K71
KPRIME, Q, M = 85, 75, 67557
LEADER = 41412868016209776721228891386909879523306833354
CEILING = 41412869809855175413648318362513310330909061869
UNION, DIMENSION = 16, 7
SUPPORTS = tuple(range(2, 10))


def source_vector(baseline: dict[int, int], support: int, defect: int):
    caps = K71.PARENT.exact_cross_caps(
        KPRIME, support, defect, baseline
    )
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
    baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(Q, M)
    left = combine(
        tuple(baseline[target] for target in SUPPORTS),
        source_vector(baseline, 2, 74),
        source_vector(baseline, 3, 63),
    )
    middle = list(combine(
        tuple(baseline[target] for target in SUPPORTS),
        source_vector(baseline, 4, 37),
        source_vector(baseline, 5, 37),
    ))
    middle[2] = min(
        middle[2],
        K71.PARENT.PARENT.PARENT.JOINT.cap_for_defects(
            KPRIME, M, 37, 37
        )[0],
    )
    local = combine(left, tuple(middle))
    candidate = combine(
        local,
        PROBE.fixed_union_cap(KPRIME, UNION, DIMENSION),
    )
    _, high = K71.PARENT.high_group(KPRIME, baseline)
    _, high_name, caps = max(
        (premium(combine(candidate, vector)), name, combine(candidate, vector))
        for name, vector in sorted(high)
    )
    assert high_name == "c6F/c7F/c8F/c9F"
    assert premium(caps) > CEILING

    primary_edges = ROUTER.all_adjacent_caps(
        KPRIME, [(UNION, DIMENSION)]
    )
    primary_prices = option_prices(caps, primary_edges)
    assert ROUTER.priced_all_adjacent(
        KPRIME, caps, primary_edges
    ) == min(primary_prices.values())

    AUDIT.KPRIME, AUDIT.Q, AUDIT.M = KPRIME, Q, M
    AUDIT.adjacent_pair.cache_clear()
    audit_edges = {}
    for support in range(4, DIMENSION):
        value = AUDIT.adjacent_pair(UNION, DIMENSION, support)
        if support == 4:
            value = min(
                value,
                AUDIT.PROBE.joint45_weighted_cap(
                    KPRIME, UNION, DIMENSION
                ),
            )
        audit_edges[support] = value
    audit_prices = option_prices(caps, tuple(sorted(audit_edges.items())))
    assert AUDIT.price(
        caps, tuple(sorted(audit_edges.items()))
    ) == min(audit_prices.values())

    primary_best = min((value, name) for name, value in primary_prices.items())
    audit_best = min((value, name) for name, value in audit_prices.items())
    print(json.dumps({
        "event": "PASS",
        "witness": {
            "offset": 11,
            "m2": 1,
            "s2": 74,
            "s3": 63,
            "s4": 37,
            "s5": 37,
            "case": "T23",
            "union": UNION,
            "dimension": DIMENSION,
            "high": high_name,
        },
        "raw": premium(caps),
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
