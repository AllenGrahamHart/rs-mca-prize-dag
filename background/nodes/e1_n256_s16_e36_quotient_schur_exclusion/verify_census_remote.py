#!/usr/bin/env python3
"""Run the exact E=36 mod-16 quotient census on Modal."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import modal


ROOT = Path(__file__).resolve().parents[3]
NOTES = (
    ROOT
    / "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes"
)
CPP = NOTES / "e36_mod16_quotient_census.cpp"
OUTPUT = NOTES / "e36_mod16_quotient_census_result.json"
SHARDS = {(profile, order): 8 for profile in range(3) for order in (128, 64)}
base = modal.Image.debian_slim().apt_install("g++")
image = (
    base.add_local_file(str(CPP), "/root/census.cpp", copy=True)
    .run_commands("g++ -O3 -std=c++17 /root/census.cpp -o /usr/local/bin/e36-census")
)
app = modal.App("e1-e36-mod16-quotient-census")


@app.function(image=image, cpu=1.0, memory=256, timeout=180, max_containers=48)
def census_shard(task: tuple[int, int, int]) -> dict[str, object]:
    profile, order, shard = task
    completed = subprocess.run(
        [
            "/usr/local/bin/e36-census",
            str(profile),
            str(order),
            str(shard),
            str(SHARDS[profile, order]),
        ],
        capture_output=True,
        check=True,
        text=True,
        timeout=170,
    )
    return json.loads(completed.stdout)


@app.local_entrypoint()
def main() -> None:
    tasks = [
        (profile, order, shard)
        for (profile, order), shard_count in SHARDS.items()
        for shard in range(shard_count)
    ]
    results = list(census_shard.map(tasks, return_exceptions=True))
    complete_results = [result for result in results if isinstance(result, dict)]
    summaries = {}
    for profile, order in SHARDS:
        selected = [
            result
            for result in complete_results
            if result["profile"] == profile and result["order"] == order
        ]
        summaries[f"profile{profile}_order{order}"] = {
            "complete": len(selected) == SHARDS[profile, order],
            "shards": len(selected),
            "expected_shards": SHARDS[profile, order],
            "tested": sum(int(result["tested"]) for result in selected),
            "best": max(selected, key=lambda result: int(result["best"]))
            if selected
            else None,
            "best_outside_inner2": max(
                selected, key=lambda result: int(result["best_outside_inner2"])
            )
            if selected
            and any(int(result["best_outside_inner2"]) >= 0 for result in selected)
            else None,
            "best_inner2_refined": max(
                selected,
                key=lambda result: int(result["best_inner2_refined"]),
            )
            if selected
            and any(int(result["best_inner2_refined"]) >= 0 for result in selected)
            else None,
        }
    packet = {
        "schema": "e1-e36-mod16-quotient-census-v1",
        "complete": len(complete_results) == len(tasks),
        "source_sha256": hashlib.sha256(CPP.read_bytes()).hexdigest(),
        "errors": [repr(result) for result in results if not isinstance(result, dict)],
        "results": complete_results,
        "summaries": summaries,
    }
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    print("E1_E36_MOD16_QUOTIENT_CENSUS " + repr(summaries))
