#!/usr/bin/env python3
"""Count the normalized m=4 residual (E,L) chambers through V=162."""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "m4_residual_counts.cpp"
OUTPUT = HERE / "m4_residual_counts_result.json"
SHARDS = 32
ENERGIES = list(range(5, 82, 4))

image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(str(SOURCE), "/root/counts.cpp", copy=True)
    .run_commands("g++ -O3 -std=c++17 /root/counts.cpp -o /usr/local/bin/counts")
)
app = modal.App("e1-prize-m4-residual-counts")


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=32)
def count(shard: int) -> dict[str, object]:
    started = time.perf_counter()
    try:
        completed = subprocess.run(
            ["/usr/local/bin/counts", str(shard)],
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
    packet = {
        "schema": "e1-prize-m4-residual-counts-v1",
        "complete": len(complete) == SHARDS,
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "normalization": {
            "singleton_positions": [0, 2],
            "first_singleton_coefficient": 1,
            "second_singleton_coefficients": [-1, 1],
            "double_positions": "all 4-subsets of the other 126 positions",
            "double_signs": "all 16 sign patterns",
        },
        "energies": ENERGIES,
        "variances": [2 * energy for energy in ENERGIES],
        "returned_shards": len(results),
        "errors": [
            result for result in results if result.get("complete") is not True
        ],
        "totals": {
            "combination_count": sum(
                int(result["combination_count"]) for result in complete
            ),
            "signed_vector_count": sum(
                int(result["signed_vector_count"]) for result in complete
            ),
            "energy_counts": [
                sum(int(result["energy_counts"][index]) for result in complete)
                for index in range(len(ENERGIES))
            ],
            "l1_counts": [
                [
                    sum(
                        int(result["l1_counts"][energy_index][l1])
                        for result in complete
                    )
                    for l1 in range(42)
                ]
                for energy_index in range(len(ENERGIES))
            ],
        },
        "worker_seconds": sum(float(result["wall_seconds"]) for result in complete),
        "container_seconds": sum(
            float(result["container_seconds"]) for result in complete
        ),
        "results": complete,
    }
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main() -> None:
    results: list[dict[str, object]] = []
    for result in count.map(range(SHARDS), order_outputs=False):
        results.append(result)
        write_packet(results)
        print(f"M4_RESIDUAL_COUNTS_PROGRESS returned={len(results)}/{SHARDS}")
    print(
        "M4_RESIDUAL_COUNTS "
        f"complete={sum(result.get('complete') is True for result in results)}/"
        f"{SHARDS}"
    )
