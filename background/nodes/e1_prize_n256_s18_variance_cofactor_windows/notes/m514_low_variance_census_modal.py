#!/usr/bin/env python3
"""Complete normalized m=514 census at the six residual variances."""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "m514_low_variance_census.cpp"
OUTPUT = HERE / "m514_low_variance_census_result.json"
SHARDS = 32

image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(str(SOURCE), "/root/census.cpp", copy=True)
    .run_commands("g++ -O3 -std=c++17 /root/census.cpp -o /usr/local/bin/census")
)
app = modal.App("e1-prize-m514-low-variance-census")


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=32)
def census(shard: int) -> dict[str, object]:
    started = time.perf_counter()
    try:
        completed = subprocess.run(
            ["/usr/local/bin/census", str(shard)],
            capture_output=True,
            check=True,
            text=True,
            timeout=52,
        )
        result = json.loads(completed.stdout)
        result["container_seconds"] = time.perf_counter() - started
        return result
    except Exception as error:
        return {
            "complete": False,
            "shard": shard,
            "container_seconds": time.perf_counter() - started,
            "error": repr(error),
        }


def write_packet(results: list[dict[str, object]]) -> None:
    complete = sorted(
        (result for result in results if result.get("complete") is True),
        key=lambda result: int(result["shard"]),
    )
    energy_counts = [
        sum(int(result["energy_counts"][index]) for result in complete)
        for index in range(6)
    ]
    div257_counts = [
        sum(int(result["div257_counts"][index]) for result in complete)
        for index in range(6)
    ]
    witnesses = []
    for result in complete:
        for witness in result.get("witnesses", []):
            if len(witnesses) < 512:
                witnesses.append({"shard": result["shard"], **witness})
    packet = {
        "schema": "e1-prize-m514-low-variance-census-v1",
        "complete": len(complete) == SHARDS,
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "normalization": {
            "singleton_positions": [0, 1],
            "first_singleton_coefficient": 1,
            "second_singleton_coefficients": [-1, 1],
            "double_positions": "all 4-subsets of the other 126 positions",
            "double_signs": "all 16 sign patterns",
        },
        "energies": [5, 9, 13, 17, 21, 25],
        "variances": [10, 18, 26, 34, 42, 50],
        "divisor_prime": 257,
        "returned_shards": len(results),
        "errors": [result for result in results if result.get("complete") is not True],
        "totals": {
            "combination_count": sum(int(result["combination_count"]) for result in complete),
            "signed_vector_count": sum(int(result["signed_vector_count"]) for result in complete),
            "energy_counts": energy_counts,
            "div257_counts": div257_counts,
        },
        "worker_seconds": sum(float(result["wall_seconds"]) for result in complete),
        "container_seconds": sum(float(result["container_seconds"]) for result in complete),
        "results": [
            {key: value for key, value in result.items() if key != "witnesses"}
            for result in complete
        ],
        "witnesses": witnesses,
    }
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main() -> None:
    results: list[dict[str, object]] = []
    for result in census.map(range(SHARDS), order_outputs=False):
        results.append(result)
        write_packet(results)
        print(f"M514_LOW_VARIANCE_PROGRESS returned={len(results)}/{SHARDS}")
    print(
        "M514_LOW_VARIANCE_CENSUS "
        f"complete={sum(result.get('complete') is True for result in results)}/{SHARDS}"
    )
