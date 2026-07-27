#!/usr/bin/env python3
"""Run the E33 profile-(1,8) coupled quotient census."""

from __future__ import annotations

import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e33_profile18_coupled_census.cpp"
REMOTE_SOURCE = "/root/e33_profile18_coupled_census.cpp"
REMOTE_BINARY = "/root/e33_profile18_coupled_census"
SHARDS = 8

app = modal.App("e1-n256-e33-profile18-coupled-probe")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(SOURCE, REMOTE_SOURCE, copy=True)
    .run_commands(f"g++ -O3 -std=c++17 {REMOTE_SOURCE} -o {REMOTE_BINARY}")
)


@app.function(image=image, cpu=1.0, memory=512, timeout=60)
def run_shard(order: int, shard: int) -> dict[str, object]:
    import subprocess

    completed = subprocess.run(
        [REMOTE_BINARY, str(order), str(shard), str(SHARDS)],
        check=True,
        capture_output=True,
        text=True,
        timeout=55,
    )
    return json.loads(completed.stdout)


@app.local_entrypoint()
def main() -> None:
    orders = [order for order in (128, 64) for _ in range(SHARDS)]
    shards = list(range(SHARDS)) * 2
    results = list(run_shard.map(orders, shards))
    summary = {
        order: {
            "tested": sum(int(row["tested"]) for row in results if row["order"] == order),
            "best": max(int(row["best"]["value"]) for row in results if row["order"] == order),
            "best_refined": max(
                int(row["best_refined"]["value"])
                for row in results
                if row["order"] == order
            ),
            "best_double_even": max(
                int(row["best_double_even"]["value"])
                for row in results
                if row["order"] == order
            ),
            "best_double_odd": max(
                int(row["best_double_odd"]["value"])
                for row in results
                if row["order"] == order
            ),
        }
        for order in (128, 64)
    }
    print("E33_PROFILE18_COUPLED_PROBE " + json.dumps(summary, sort_keys=True))
    print("E33_PROFILE18_COUPLED_ROWS " + json.dumps(results, sort_keys=True))
