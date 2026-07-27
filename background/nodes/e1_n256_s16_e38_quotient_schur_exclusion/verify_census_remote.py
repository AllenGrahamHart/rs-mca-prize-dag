#!/usr/bin/env python3
"""Replay the exact odd-support mod-16 quotient census on Modal."""

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
CPP = NOTES / "e38_mod16_quotient_census.cpp"
OUTPUT = NOTES / "e38_mod16_quotient_census_result.json"
SHARDS = {
    (0, 128): 32,
    (0, 64): 16,
    (1, 128): 8,
    (1, 64): 8,
    (2, 128): 8,
    (2, 64): 8,
}
base = modal.Image.debian_slim().apt_install("g++")
image = (
    base.add_local_file(str(CPP), "/root/census.cpp", copy=True)
    .run_commands("g++ -O3 -std=c++17 /root/census.cpp -o /usr/local/bin/e38-census")
)
app = modal.App("e1-e38-mod16-quotient-census")


@app.function(image=image, cpu=1.0, memory=256, timeout=180, max_containers=80)
def census_shard(task: tuple[int, int, int]) -> dict[str, object]:
    profile, order, shard = task
    completed = subprocess.run(
        [
            "/usr/local/bin/e38-census",
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
    results = list(census_shard.map(tasks))
    assert len(results) == sum(SHARDS.values())
    assert all(result["complete"] for result in results)
    summaries = {}
    for (profile, order), shard_count in SHARDS.items():
        order_results = [
            result
            for result in results
            if result["profile"] == profile and result["order"] == order
        ]
        assert {result["shard"] for result in order_results} == set(range(shard_count))
        summaries[profile, order] = {
            "complete": True,
            "shards": shard_count,
            "tested": sum(int(result["tested"]) for result in order_results),
            "best": max(order_results, key=lambda result: int(result["best"])),
        }
    packet = {
        "schema": "e1-e38-mod16-quotient-census-v1",
        "complete": True,
        "source_sha256": hashlib.sha256(CPP.read_bytes()).hexdigest(),
        "results": results,
        "summaries": {
            f"profile{profile}_order{order}": summary
            for (profile, order), summary in summaries.items()
        },
    }
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    print("E1_E38_MOD16_QUOTIENT_CENSUS " + repr(packet["summaries"]))
