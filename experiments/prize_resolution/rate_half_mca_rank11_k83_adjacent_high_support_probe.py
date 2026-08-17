#!/usr/bin/env python3
"""Probe adjacent-support fixed-union charges on the exact K'=83 wall."""

from __future__ import annotations

import importlib.util
import itertools
import json
import tarfile
from functools import lru_cache
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


ROUTER = load_module(
    "k83_adjacent_high_router",
    ROOT
    / "experiments/prize_resolution/rate_half_mca_rank11_k83_stratified56_lane_probe.py",
)
PROBE, K71 = ROUTER.PROBE, ROUTER.K71
KPRIME, Q, M, N_CODE = 83, 73, 67555, 1048659


@lru_cache(maxsize=None)
def adjacent_weighted_cap(
    union: int, dimension: int, support: int
) -> int:
    """Weighted circuit cap for supports d,d+1 from one fixed union."""
    assert dimension >= support + 1
    outside = M - union
    residual = KPRIME - union - dimension
    assert residual >= 0 and outside >= residual + support - 1
    weight_d = (
        K71.LEDGER.DEFICITS[support] * comb(M - support, 11 - support)
    )
    weight_next = (
        K71.LEDGER.DEFICITS[support + 1]
        * comb(M - support - 1, 10 - support)
    )
    total = 0
    for inside in range(support - 1):
        choices = comb(union, inside)
        cap_d = (
            choices
            * residual
            * comb(outside, support - 1 - inside)
            // (support - inside)
        )
        rhs = choices * residual * comb(outside, support - inside)
        coefficient = outside - residual - support + 1 + inside
        slope = (support + 1 - inside) * weight_d - coefficient * weight_next
        numerator = weight_next * rhs + max(slope, 0) * cap_d
        total += numerator // (support + 1 - inside)

    count_d = comb(union, support - 1) * residual + comb(union, support)
    count_next = (
        comb(union, support - 1) * residual * outside // 2
        + comb(union, support) * residual
        + comb(union, support + 1)
    )
    return total + weight_d * count_d + weight_next * count_next


def main() -> None:
    baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(Q, M)
    left = K71.base23_vector(KPRIME, baseline, 55, 55)
    exact45, _, _ = K71.exact45_rows(KPRIME, baseline)
    middle = next(
        vector for s4, s5, vector in exact45 if (s4, s5) == (37, 37)
    )
    _, high = K71.PARENT.high_group(KPRIME, baseline)
    high_vector = next(
        vector
        for name, vector in high
        if name == "c6F/c7F/c8F/c9F"
    )
    raw_caps = K71.combine(left, middle, high_vector)
    raw_premium = K71.premium(raw_caps)

    old = K71.LEDGER.row(KPRIME)
    ceiling = (
        K71.LEDGER.RECORD_FLOOR * 55 * comb(M, 11)
        - 55 * comb(N_CODE, 11)
        - 55 * int(old["kernel"])
        - int(old["marks"])
        - 1
    ) // K71.LEDGER.RECORD_FLOOR

    rows = []
    for route, union, dimension in (("T23", 39, 7), ("A23", 38, 8)):
        caps = K71.combine(
            raw_caps, PROBE.fixed_union_cap(KPRIME, union, dimension)
        )
        base = K71.premium(caps)
        edge_caps = {
            support: adjacent_weighted_cap(union, dimension, support)
            for support in range(4, dimension)
        }
        choices = []
        edges = sorted(edge_caps)
        for width in range(len(edges) + 1):
            for selected in itertools.combinations(edges, width):
                covered = {value for edge in selected for value in (edge, edge + 1)}
                if len(covered) != 2 * len(selected):
                    continue
                old_weight = sum(
                    K71.LEDGER.DEFICITS[support] * caps[support - 2]
                    for support in covered
                )
                value = base - old_weight + sum(edge_caps[edge] for edge in selected)
                choices.append((value, selected))
        best, selected = min(choices)
        rows.append({
            "route": route,
            "charge": [union, dimension],
            "base_premium": base,
            "edge_caps": {str(key): value for key, value in edge_caps.items()},
            "selected_edges": list(selected),
            "charged_premium": best,
            "margin": ceiling - best,
        })

    print(json.dumps({
        "event": "ADJACENT_HIGH_PROBE",
        "kprime": KPRIME,
        "defects": [55, 55, 37, 37],
        "completion_maxima": [18, 18, 36, 36],
        "high_branch": "c6F/c7F/c8F/c9F",
        "raw_premium": raw_premium,
        "safe_premium_ceiling": ceiling,
        "routes": rows,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
