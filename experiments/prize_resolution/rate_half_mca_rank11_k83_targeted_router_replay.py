#!/usr/bin/env python3
"""Replay only the K'=83 cells exposed by the incomplete broad audit."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ROUTER = load_module(
    "k83_stratified56_targeted",
    ROOT
    / "experiments/prize_resolution/rate_half_mca_rank11_k83_stratified56_lane_probe.py",
)
PROBE = ROUTER.PROBE
K71 = ROUTER.K71
KPRIME = 83
Q = KPRIME - 10
M = 67472 + KPRIME
CEILING = (
    K71.LEDGER.RECORD_FLOOR * 55 * __import__("math").comb(M, 11)
    - 55 * __import__("math").comb(1048576 + KPRIME, 11)
    - 55 * int(K71.LEDGER.row(KPRIME)["kernel"])
    - int(K71.LEDGER.row(KPRIME)["marks"])
    - 1
) // K71.LEDGER.RECORD_FLOOR

TARGETS = (
    ("published_wall", 50, 49, 49, 48),
    ("offset1_new_max", 46, 45, 44, 45),
    ("offset7", 44, 37, 37, 37),
    ("carrier32", 44, 43, 37, 37),
    ("offset2", 38, 36, 38, 36),
    ("offset3", 39, 36, 39, 36),
    ("offset4", 40, 36, 40, 36),
    ("offset5", 41, 36, 41, 36),
    ("offset6", 42, 36, 42, 36),
)


def main() -> None:
    baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(Q, M)
    exact45, _, _ = K71.exact45_rows(KPRIME, baseline)
    middle = {(s4, s5): vector for s4, s5, vector in exact45}
    _, high = K71.PARENT.high_group(KPRIME, baseline)
    fallback = next(
        vector for name, vector in high if name == "c6F/c7F/c8F/c9F"
    )

    print(json.dumps({"event": "START", "ceiling": CEILING}), flush=True)
    for name, s2, s3, s4, s5 in TARGETS:
        left = K71.base23_vector(KPRIME, baseline, s2, s3)
        local = K71.combine(left, middle[(s4, s5)])
        original_caps = K71.combine(local, fallback)
        original = K71.premium(original_caps)
        m2, m3, m4, m5 = (Q - value for value in (s2, s3, s4, s5))
        cases = PROBE.mixed_cases(m2, m3 - m2, m4, m5)
        maximum = (-1, "")
        pairwise_maximum = (-1, "")
        for (candidate, joint45, joint56), case in (
            ROUTER.charged_case_rows(KPRIME, local, cases).items()
        ):
            caps = K71.combine(candidate, fallback)
            pairwise = K71.premium(caps)
            if joint45 is not None:
                old45 = sum(
                    K71.LEDGER.DEFICITS[support] * caps[support - 2]
                    for support in (4, 5)
                )
                pairwise -= old45 - min(old45, joint45)
            pairwise_maximum = max(pairwise_maximum, (pairwise, case))
            maximum = max(
                maximum,
                (ROUTER.priced(KPRIME, caps, joint45, joint56), case),
            )
        print(
            json.dumps(
                {
                    "event": "ROW",
                    "name": name,
                    "defects": [s2, s3, s4, s5],
                    "maxima": [m2, m3, m4, m5],
                    "original": original,
                    "pairwise_routed": pairwise_maximum[0],
                    "pairwise_worst_case": pairwise_maximum[1],
                    "routed": maximum[0],
                    "margin": CEILING - maximum[0],
                    "worst_case": maximum[1],
                    "geometry_cases": len(cases),
                },
                sort_keys=True,
            ),
            flush=True,
        )
    print(json.dumps({"event": "PASS"}), flush=True)


if __name__ == "__main__":
    main()
