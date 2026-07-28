#!/usr/bin/env python3
"""Exact normalized m=2 third-moment frontier through V=194."""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "m2_residual_m3_frontier.cpp"
OUTPUT = HERE / "m2_residual_m3_frontier_result.json"
SHARDS = 32
ENERGIES = list(range(5, 98, 4))

image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(str(SOURCE), "/root/frontier.cpp", copy=True)
    .run_commands(
        "g++ -O3 -std=c++17 /root/frontier.cpp -o /usr/local/bin/frontier"
    )
)
app = modal.App("e1-prize-m2-residual-m3-frontier")


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=32)
def frontier(shard: int) -> dict[str, object]:
    started = time.perf_counter()
    try:
        completed = subprocess.run(
            ["/usr/local/bin/frontier", str(shard)],
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
    rows = []
    for index, energy in enumerate(ENERGIES):
        populated = [
            result["rows"][index]
            for result in complete
            if int(result["rows"][index]["count"]) > 0
        ]
        if populated:
            maximum = max(populated, key=lambda row: int(row["maximum_m3"]))
            rows.append(
                {
                    "energy": energy,
                    "variance": 2 * energy,
                    "count": sum(int(row["count"]) for row in populated),
                    "minimum_m3": min(int(row["minimum_m3"]) for row in populated),
                    "maximum_m3": int(maximum["maximum_m3"]),
                    "maximum_witness": {
                        "positions": maximum["maximum_positions"],
                        "coefficients": maximum["maximum_coefficients"],
                    },
                }
            )
        else:
            rows.append(
                {
                    "energy": energy,
                    "variance": 2 * energy,
                    "count": 0,
                    "minimum_m3": None,
                    "maximum_m3": None,
                    "maximum_witness": None,
                }
            )
    packet = {
        "schema": "e1-prize-m2-residual-m3-frontier-v1",
        "complete": len(complete) == SHARDS,
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "normalization": {"singleton_positions": [0, 1]},
        "returned_shards": len(results),
        "errors": [
            result for result in results if result.get("complete") is not True
        ],
        "rows": rows,
        "worker_seconds": sum(float(result["wall_seconds"]) for result in complete),
        "container_seconds": sum(
            float(result["container_seconds"]) for result in complete
        ),
        "results": [
            {"shard": result["shard"], "wall_seconds": result["wall_seconds"]}
            for result in complete
        ],
    }
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main() -> None:
    results: list[dict[str, object]] = []
    for result in frontier.map(range(SHARDS), order_outputs=False):
        results.append(result)
        write_packet(results)
        print(f"M2_RESIDUAL_M3_PROGRESS returned={len(results)}/{SHARDS}")
    print(
        "M2_RESIDUAL_M3 "
        f"complete={sum(result.get('complete') is True for result in results)}/"
        f"{SHARDS}"
    )
