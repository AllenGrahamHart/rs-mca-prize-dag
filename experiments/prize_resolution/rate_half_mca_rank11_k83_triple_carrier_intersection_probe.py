#!/usr/bin/env python3
"""Test the forced triple-carrier intersection charge at the K'=83 wall."""

from __future__ import annotations

import importlib.util
import json
import tarfile
from math import comb
from pathlib import Path


ARCHIVES = list(Path(".").glob("*.tar.gz"))
ROOT = Path("repo") if ARCHIVES else Path(__file__).resolve().parents[2]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if ARCHIVES:
    with tarfile.open(ARCHIVES[0], "r:gz") as archive:
        archive.extractall(ROOT, filter="data")


PROBE = load_module(
    "pairwise_carrier_probe_for_k83",
    (
        Path(__file__).with_name("rate_half_mca_rank11_k72_two_step_probe.py")
        if ARCHIVES
        else ROOT
        / "experiments/prize_resolution/rate_half_mca_rank11_k72_two_step_probe.py"
    ),
)
K71 = PROBE.K71


def row_contract(kprime: int, completion_premium: int) -> dict[str, int]:
    m = 67472 + kprime
    n = 1048576 + kprime
    old = K71.LEDGER.row(kprime)
    marks = int(old["marks"])
    kernel = int(old["kernel"])
    record_floor = K71.LEDGER.RECORD_FLOOR
    full = (marks + record_floor * completion_premium) // 55
    total = kernel + full
    demand = record_floor * comb(m, 11) - comb(n, 11)
    ceiling = (
        record_floor * 55 * comb(m, 11)
        - 55 * comb(n, 11)
        - 55 * kernel
        - marks
        - 1
    ) // record_floor
    coefficient = 55 * comb(m, 11) - completion_premium
    raw = (
        record_floor * coefficient
        - 55 * comb(n, 11)
        - 55 * kernel
        - marks
    )
    return {
        "rank_nine_marks": marks,
        "kernel_capacity": kernel,
        "record_floor": record_floor,
        "completion_premium": completion_premium,
        "safe_premium_ceiling": ceiling,
        "premium_ceiling_margin": ceiling - completion_premium,
        "full_rank_capacity": full,
        "total_capacity": total,
        "required_component_incidence": demand,
        "gap": demand - total,
        "record_coefficient_cross": coefficient,
        "floor_record_raw_cross": raw,
    }


def audit() -> dict[str, object]:
    kprime = 83
    q = kprime - 10
    m = 67472 + kprime
    n = 1048576 + kprime
    defects = (50, 49, 49, 48)
    m2, m3, m4, m5 = (q - value for value in defects)
    baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(q, m)
    left = K71.base23_vector(kprime, baseline, defects[0], defects[1])
    exact45, _, _ = K71.exact45_rows(kprime, baseline)
    middle = next(
        vector
        for s4, s5, vector in exact45
        if (s4, s5) == defects[2:]
    )
    local = K71.combine(left, middle)
    _, high = K71.PARENT.high_group(kprime, baseline)
    cases = PROBE.mixed_cases(m2, m3 - m2, m4, m5)
    charges = cases["F23__N4_t0__N5_t2"]
    assert charges == [(29, 6), (29, 6)]

    pairwise = local
    joint45 = None
    for union, dimension in charges:
        pairwise = K71.combine(
            pairwise,
            PROBE.fixed_union_cap(kprime, union, dimension),
        )
        coupled = PROBE.joint45_weighted_cap(kprime, union, dimension)
        joint45 = coupled if joint45 is None else min(joint45, coupled)

    def premium(vector: tuple[int, ...]) -> int:
        value = K71.premium(vector)
        old45 = sum(
            K71.LEDGER.DEFICITS[support] * vector[support - 2]
            for support in (4, 5)
        )
        assert joint45 is not None
        return value - old45 + min(old45, joint45)

    old = K71.LEDGER.row(kprime)
    marks = int(old["marks"])
    kernel = int(old["kernel"])
    record_floor = K71.LEDGER.RECORD_FLOOR
    ceiling = (
        record_floor * 55 * comb(m, 11)
        - 55 * comb(n, 11)
        - 55 * kernel
        - marks
        - 1
    ) // record_floor

    rows = []
    pairwise_maximum = max(
        premium(K71.combine(pairwise, vector)) for _, vector in high
    )
    for overlap45 in range(4):
        union = 32 - overlap45
        triple = K71.combine(
            pairwise,
            PROBE.fixed_union_cap(kprime, union, 4),
        )
        maximum = max(
            premium(K71.combine(triple, vector)) for _, vector in high
        )
        rows.append(
            {
                "overlap45": overlap45,
                "triple_union": union,
                "triple_dimension": 4,
                "maximum": maximum,
                "safe_premium_ceiling": ceiling,
                "margin": ceiling - maximum,
            }
        )

    return {
        "kprime": kprime,
        "defects": defects,
        "completion_maxima": [m2, m3, m4, m5],
        "pairwise_charges": charges,
        "pairwise_maximum": pairwise_maximum,
        "pairwise_margin": ceiling - pairwise_maximum,
        "rows": rows,
        "closure_rows": {
            "81": row_contract(
                81,
                41316738803727121977844753592626079710298860916,
            ),
            "82": row_contract(
                82,
                41340768193812712537232048213849077199458005267,
            ),
        },
    }


def main() -> None:
    print(
        json.dumps(
            audit(),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
