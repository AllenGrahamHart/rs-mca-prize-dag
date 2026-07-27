#!/usr/bin/env python3
"""Run the exact E=34 nested quotient census on Modal."""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
CPP = HERE / "e34_nested_quotient_census.cpp"
PILOT_OUTPUT = HERE / "e34_nested_quotient_pilot_result.json"
FULL_OUTPUT = HERE / "e34_nested_quotient_census_result.json"
PROFILES = range(6)
ORDERS = (128, 64)
PILOT_SHARDS = 128
FULL_SHARDS = 16

base = modal.Image.debian_slim().apt_install("g++")
image = (
    base.add_local_file(str(CPP), "/root/census.cpp", copy=True)
    .run_commands("g++ -O3 -std=c++17 /root/census.cpp -o /usr/local/bin/e34-census")
)
app = modal.App("e1-e34-nested-quotient-census")


@app.function(image=image, cpu=1.0, memory=256, timeout=120, max_containers=100)
def census_shard(task: tuple[int, int, int, int]) -> dict[str, object]:
    profile, order, shard, shards = task
    started = time.perf_counter()
    try:
        completed = subprocess.run(
            [
                "/usr/local/bin/e34-census",
                str(profile),
                str(order),
                str(shard),
                str(shards),
            ],
            capture_output=True,
            check=True,
            text=True,
            timeout=110,
        )
        result = json.loads(completed.stdout)
        result["wall_seconds"] = time.perf_counter() - started
        return result
    except Exception as error:  # Partial packets retain the failed task key.
        return {
            "complete": False,
            "profile": profile,
            "order": order,
            "shard": shard,
            "shards": shards,
            "wall_seconds": time.perf_counter() - started,
            "error": repr(error),
        }


def write_packet(
    output: Path,
    mode: str,
    shards_per_case: int,
    expected: int,
    results: list[dict[str, object]],
) -> None:
    complete_results = [result for result in results if result.get("complete") is True]
    packet = {
        "schema": "e1-e34-nested-quotient-census-v1",
        "mode": mode,
        "complete": len(complete_results) == expected,
        "shards_per_case": shards_per_case,
        "source_sha256": hashlib.sha256(CPP.read_bytes()).hexdigest(),
        "errors": [result for result in results if result.get("complete") is not True],
        "results": complete_results,
    }
    output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main(full: bool = False) -> None:
    mode = "full" if full else "pilot"
    shards = FULL_SHARDS if full else PILOT_SHARDS
    shard_range = range(shards) if full else range(1)
    tasks = [
        (profile, order, shard, shards)
        for profile in PROFILES
        for order in ORDERS
        for shard in shard_range
    ]
    output = FULL_OUTPUT if full else PILOT_OUTPUT
    results: list[dict[str, object]] = []
    for result in census_shard.map(tasks, order_outputs=False):
        results.append(result)
        write_packet(output, mode, shards, len(tasks), results)
        print(
            "E1_E34_NESTED_QUOTIENT_PROGRESS "
            f"mode={mode} returned={len(results)}/{len(tasks)}"
        )
    complete = [result for result in results if result.get("complete") is True]
    maxima = {
        f"profile{int(result['profile'])}_order{int(result['order'])}": int(result["best"])
        for result in complete
    }
    print(
        "E1_E34_NESTED_QUOTIENT_CENSUS "
        f"mode={mode} complete={len(complete)}/{len(tasks)} "
        f"maxima={maxima!r}"
    )
