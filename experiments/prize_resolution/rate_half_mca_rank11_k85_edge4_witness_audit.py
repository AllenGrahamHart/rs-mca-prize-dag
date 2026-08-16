#!/usr/bin/env python3
"""Independently replay one failed K'=85 edge-4-only witness."""

from __future__ import annotations

import argparse
import importlib.util
import json
import tarfile
from math import comb
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


AUDIT = load_module(
    "k85_edge4_witness_independent_audit",
    ROOT
    / "experiments/prize_resolution/"
    "rate_half_mca_rank11_k83_threshold_frontier_audit.py",
)
PROBE, K71 = AUDIT.PROBE, AUDIT.K71
KPRIME, Q, M, N_CODE = 85, 75, 67557, 1048661
LEADER = 41412868016209776721228891386909879523306833354
OLD_ROW = K71.LEDGER.row(KPRIME)
CEILING = (
    K71.LEDGER.RECORD_FLOOR * 55 * comb(M, 11)
    - 55 * comb(N_CODE, 11)
    - 55 * int(OLD_ROW["kernel"])
    - int(OLD_ROW["marks"])
    - 1
) // K71.LEDGER.RECORD_FLOOR
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
    _, high = K71.PARENT.high_group(KPRIME, baseline)
    high = sorted(high)
    raw = max(
        (premium(combine(local, vector)), name)
        for name, vector in high
    )
    assert raw[0] > CEILING

    cases = PROBE.mixed_cases(
        args.m2, args.offset, Q - args.s4, Q - args.s5
    )
    assert args.case in cases
    candidate = local
    edge4 = None
    AUDIT.KPRIME, AUDIT.Q, AUDIT.M = KPRIME, Q, M
    AUDIT.adjacent_pair.cache_clear()
    for union, dimension in cases[args.case]:
        candidate = combine(
            candidate,
            PROBE.fixed_union_cap(KPRIME, union, dimension),
        )
        if dimension < 5 or KPRIME - union - dimension < 0:
            continue
        value = min(
            AUDIT.adjacent_pair(union, dimension, 4),
            PROBE.joint45_weighted_cap(KPRIME, union, dimension),
        )
        edge4 = value if edge4 is None else min(edge4, value)

    def price(caps):
        if edge4 is None:
            return premium(caps)
        old = sum(
            K71.LEDGER.DEFICITS[support] * caps[support - 2]
            for support in (4, 5)
        )
        return premium(caps) - old + edge4

    after = max(
        (price(combine(candidate, vector)), name)
        for name, vector in high
    )
    assert after[0] > LEADER
    print(json.dumps({
        "event": "WITNESS_PASS",
        "offset": args.offset,
        "m2": args.m2,
        "s2": s2,
        "s3": s3,
        "s4": args.s4,
        "s5": args.s5,
        "case": args.case,
        "charges": cases[args.case],
        "edge4_cap": edge4,
        "raw_before": raw[0],
        "raw_before_high": raw[1],
        "edge4_after": after[0],
        "edge4_high": after[1],
        "leader": LEADER,
        "excess_over_leader": after[0] - LEADER,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
