#!/usr/bin/env python3
"""Run the exact E34 nonquarter-diameter census on Modal."""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e34_nonquarter_diameter_census.cpp"
OUTPUT = HERE / "e34_nonquarter_diameter_census_result.json"
TASKS = tuple(range(1, 32))

image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(str(SOURCE), "/root/census.cpp", copy=True)
    .run_commands(
        "g++ -O3 -std=c++17 /root/census.cpp -o /usr/local/bin/e34-diameter"
    )
)
app = modal.App("e1-e34-nonquarter-diameter-census")


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=31)
def census(t: int) -> dict[str, object]:
    started = time.perf_counter()
    try:
        completed = subprocess.run(
            ["/usr/local/bin/e34-diameter", str(t)],
            capture_output=True,
            check=True,
            text=True,
            timeout=50,
        )
        result = json.loads(completed.stdout)
        result["wall_seconds"] = time.perf_counter() - started
        return result
    except Exception as error:
        return {
            "complete": False,
            "t": t,
            "wall_seconds": time.perf_counter() - started,
            "error": repr(error),
        }


def write_packet(results: list[dict[str, object]]) -> None:
    complete = [result for result in results if result.get("complete") is True]
    ordered = sorted(complete, key=lambda result: int(result["t"]))
    witnesses = []
    for result in ordered:
        for witness in result.get("witnesses", []):
            if len(witnesses) < 12:
                witnesses.append({"t": result["t"], **witness})
    compact_results = [
        {key: value for key, value in result.items() if key != "witnesses"}
        for result in ordered
    ]
    packet = {
        "schema": "e1-e34-nonquarter-diameter-census-v1",
        "complete": len(complete) == len(TASKS),
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "expected_tasks": list(TASKS),
        "errors": [result for result in results if result.get("complete") is not True],
        "results": compact_results,
        "witnesses": witnesses,
    }
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main() -> None:
    results: list[dict[str, object]] = []
    started = time.monotonic()
    for result in census.map(TASKS, order_outputs=False):
        results.append(result)
        write_packet(results)
        print(f"E1_E34_DIAMETER_PROGRESS returned={len(results)}/{len(TASKS)}")
        if time.monotonic() - started > 240:
            print("E1_E34_DIAMETER_CLIENT_STOP elapsed_above_240_seconds")
            break
    complete = [result for result in results if result.get("complete") is True]
    print(
        "E1_E34_NONQUARTER_DIAMETER_CENSUS "
        f"complete={len(complete)}/{len(TASKS)} "
        f"worker_seconds={sum(float(result['wall_seconds']) for result in complete):.6f}"
    )
