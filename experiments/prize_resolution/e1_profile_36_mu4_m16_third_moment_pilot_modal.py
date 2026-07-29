#!/usr/bin/env python3
"""Probe cubic-Hermite exclusions for the profile-(3,6) cofactor-16 frontier."""

from __future__ import annotations

from functools import lru_cache
import json
import math
from pathlib import Path
import re

import modal


HERE = Path(__file__).resolve()
ROOT = Path("/repo") if Path("/repo").is_dir() else (
    HERE.parents[2] if len(HERE.parents) > 2 else Path.cwd()
)
PRODUCT = ROOT / "experiments/prize_resolution/e1_profile_36_mu4_m16_parity_product_result.json"
OUTPUT = Path(
    "experiments/prize_resolution/e1_profile_36_mu4_m16_third_moment_pilot_result.json"
)
B_PRIZE = 317494674775468773183020924238786383963
TARGET_MEAN_LOG = math.log(16 * B_PRIZE * 2**128) / 64

app = modal.App("e1-profile-36-mu4-m16-third-moment-pilot")
image = modal.Image.debian_slim()


def phi(profile: tuple[int, ...]) -> int:
    layers = [
        2 * sum(profile[level - 1 :])
        for level in range(1, len(profile) + 1)
    ]
    total = 0
    for first in layers:
        for second in layers:
            for third in layers:
                total += min(
                    first * second - min(first, second),
                    first * third - min(first, third),
                    second * third - min(second, third),
                )
    return total


@lru_cache(maxsize=None)
def maximum_phi(energy: int, l1_bound: int) -> tuple[int, tuple[int, ...], int]:
    maximum_level = math.isqrt(energy)
    best_score = -1
    best_profile: tuple[int, ...] = ()
    profile = [0] * maximum_level
    profile_count = 0

    def visit(level: int, remaining_energy: int, used_l1: int, used_classes: int) -> None:
        nonlocal best_score, best_profile, profile_count
        if level == 0:
            if remaining_energy == 0:
                profile_count += 1
                candidate = tuple(profile)
                score = phi(candidate)
                if (score, candidate) > (best_score, best_profile):
                    best_score = score
                    best_profile = candidate
            return
        maximum = min(
            remaining_energy // (level * level),
            (l1_bound - used_l1) // level,
            36 - used_classes,
        )
        for count in range(maximum + 1):
            profile[level - 1] = count
            visit(
                level - 1,
                remaining_energy - count * level * level,
                used_l1 + count * level,
                used_classes + count,
            )
        profile[level - 1] = 0

    visit(maximum_level, energy, 0, 0)
    assert best_score >= 0
    return best_score, best_profile, profile_count


def hermite_coefficients(a: int, b: int) -> tuple[float, float, float, float]:
    gap = b - a
    value_gap = math.log(b / a) - gap / a
    derivative_gap = 1 / b - 1 / a
    cubic = derivative_gap / gap**2 - 2 * value_gap / gap**3
    quadratic = 3 * value_gap / gap**2 - derivative_gap / gap
    return (
        math.log(a) - 1 + a * a * quadratic - a**3 * cubic,
        1 / a - 2 * a * quadratic + 3 * a * a * cubic,
        quadratic - 3 * a * cubic,
        cubic,
    )


CONTACTS = [
    (a, b, hermite_coefficients(a, b))
    for a in range(1, 144)
    for b in range(a + 1, 145)
]


@app.function(image=image, cpu=1.0, memory=256, timeout=180, max_containers=1)
def probe(records: list[tuple[int, int]]) -> dict[str, object]:
    rows = []
    for index, (energy, l1_norm) in enumerate(records):
        moment_bound, profile, profile_count = maximum_phi(energy, l1_norm)
        mean_square = 324 + 2 * energy
        central_to_raw = 5832 + 108 * energy
        best = (math.inf, -1, -1)
        for a, b, coefficients in CONTACTS:
            constant, linear, quadratic, cubic = coefficients
            third = central_to_raw + (moment_bound if cubic >= 0 else -moment_bound)
            bound = constant + 18 * linear + mean_square * quadratic + third * cubic
            if bound < best[0]:
                best = (bound, a, b)
        rows.append({
            "energy": energy,
            "l1": l1_norm,
            "phi": moment_bound,
            "phi_profile": profile,
            "profile_count": profile_count,
            "best_mean_log": best[0],
            "contacts": [best[1], best[2]],
            "margin": TARGET_MEAN_LOG - best[0],
            "excluded": best[0] < TARGET_MEAN_LOG - 1e-12,
        })
        if (index + 1) % 32 == 0:
            print(f"progress={index + 1}/{len(records)}")
    return {
        "schema": "e1-profile-36-mu4-m16-third-moment-pilot-v1",
        "complete": True,
        "method": "floating planning probe; not a proof certificate",
        "target_mean_log": TARGET_MEAN_LOG,
        "rows": rows,
    }


@app.local_entrypoint()
def main() -> None:
    product = json.loads(PRODUCT.read_text())
    records = sorted({
        (int(match.group(1)), int(match.group(3)))
        for record in product["live"]
        if (match := re.fullmatch(r"E(\d+)q(\d+)L(\d+)", record))
    })
    result = probe.remote(records)
    excluded_pairs = {
        (row["energy"], row["l1"])
        for row in result["rows"] if row["excluded"]
    }
    surviving_records = [
        record for record in product["live"]
        if (int(re.match(r"E(\d+)q(\d+)L(\d+)", record).group(1)),
            int(re.match(r"E(\d+)q(\d+)L(\d+)", record).group(3)))
        not in excluded_pairs
    ]
    result["live_pairs"] = len(records)
    result["excluded_pairs"] = len(excluded_pairs)
    result["surviving_records"] = surviving_records
    result["max_surviving_energy"] = max(
        int(re.match(r"E(\d+)", record).group(1)) for record in surviving_records
    ) if surviving_records else None
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "E1_PROFILE_36_MU4_M16_THIRD_MOMENT_PILOT_DONE "
        f"pairs={len(records)} excluded_pairs={len(excluded_pairs)} "
        f"surviving_records={len(surviving_records)} "
        f"max_surviving_E={result['max_surviving_energy']} output={OUTPUT}"
    )


if __name__ == "__main__":
    main()
