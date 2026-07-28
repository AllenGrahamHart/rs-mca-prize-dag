#!/usr/bin/env python3
"""Project full m16 branch runtimes from measured parity-class samples."""

from __future__ import annotations

import json
from pathlib import Path
import re

import modal


ROOT = Path.cwd()
PREFIX = ROOT / "experiments/prize_resolution"
ATLAS = PREFIX / "e1_profile_36_mu4_m16_chord_orbits.json"
BENCHMARK = PREFIX / "e1_profile_36_mu4_m16_direct_radius_benchmark_result.json"
OUTPUT = PREFIX / "e1_profile_36_mu4_m16_cost_projection_result.json"

app = modal.App("e1-profile-36-mu4-m16-cost-projection")
image = modal.Image.debian_slim()


@app.function(image=image, cpu=0.125, memory=128, timeout=30)
def project(
    weights: dict[str, dict[str, int]],
    samples: list[dict[str, object]],
) -> dict[str, object]:
    seconds_by_class: dict[tuple[str, int], float] = {}
    for row in samples:
        match = re.search(r"\bseconds=([0-9.]+)$", str(row["stdout"]).strip())
        if match is None:
            raise ValueError(f"missing runtime in benchmark row: {row}")
        key = (str(row["branch"]), int(row["odd_weight"]))
        seconds_by_class[key] = float(match.group(1))

    branches: dict[str, dict[str, object]] = {}
    for branch, branch_weights in sorted(weights.items()):
        missing = [
            int(q) for q in branch_weights
            if (branch, int(q)) not in seconds_by_class
        ]
        if missing:
            raise ValueError(f"{branch}: missing benchmark classes {missing}")
        projected_seconds = sum(
            count * seconds_by_class[(branch, int(q))]
            for q, count in branch_weights.items()
        )
        branches[branch] = {
            "orbits": sum(branch_weights.values()),
            "projected_cpu_seconds": projected_seconds,
            "projected_cpu_hours": projected_seconds / 3600,
            "sample_weighted_seconds_per_orbit": (
                projected_seconds / sum(branch_weights.values())
            ),
            "parity_classes": len(branch_weights),
        }
    return {
        "schema": "e1-profile-36-mu4-m16-cost-projection-v1",
        "method": "one measured representative runtime per branch and odd-chord class",
        "branches": branches,
    }


@app.local_entrypoint()
def main(
    benchmark_path: str = "",
    output_path: str = "",
    branch: str = "",
) -> None:
    atlas = json.loads(ATLAS.read_text())
    benchmark_file = ROOT / benchmark_path if benchmark_path else BENCHMARK
    output_file = ROOT / output_path if output_path else OUTPUT
    benchmark = json.loads(benchmark_file.read_text())
    weights = {
        branch_name: packet["orbit_weights"]
        for branch_name, packet in atlas["branches"].items()
        if not branch or branch_name == branch
    }
    result = project.remote(weights, benchmark["rows"])
    output_file.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
