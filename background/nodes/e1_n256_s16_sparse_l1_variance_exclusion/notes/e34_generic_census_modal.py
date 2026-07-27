#!/usr/bin/env python3
"""Run the exact 57-orbit E34 generic census on Modal."""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e34_generic_census.cpp"
ORBIT_PACKET = HERE / "e34_generic_orbit_result.json"
OUTPUT = HERE / "e34_generic_census_result.json"


def tasks() -> list[tuple[int, int, int]]:
    packet = json.loads(ORBIT_PACKET.read_text())
    rows = packet["results"]["primary"]["rows"]
    return [(index, row["heavy"][1], row["heavy"][2]) for index, row in enumerate(rows)]


image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(str(SOURCE), "/root/census.cpp", copy=True)
    .run_commands("g++ -O3 -std=c++17 /root/census.cpp -o /usr/local/bin/e34-generic")
)
app = modal.App("e1-e34-generic-census")


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=45)
def census(task: tuple[int, int, int]) -> dict[str, object]:
    orbit, a, b = task
    started = time.perf_counter()
    try:
        completed = subprocess.run(
            ["/usr/local/bin/e34-generic", str(orbit), str(a), str(b)],
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
            "orbit": orbit,
            "heavy": [0, a, b],
            "wall_seconds": time.perf_counter() - started,
            "error": repr(error),
        }


def write_packet(results: list[dict[str, object]], expected: int) -> None:
    complete = [result for result in results if result.get("complete") is True]
    ordered = sorted(complete, key=lambda result: int(result["orbit"]))
    witnesses = []
    for result in ordered:
        for witness in result.get("witnesses", []):
            if len(witnesses) < 12:
                witnesses.append({"orbit": result["orbit"], **witness})
    packet = {
        "schema": "e1-e34-generic-census-v1",
        "complete": len(complete) == expected,
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "orbit_packet_sha256": hashlib.sha256(ORBIT_PACKET.read_bytes()).hexdigest(),
        "expected_tasks": expected,
        "errors": [result for result in results if result.get("complete") is not True],
        "results": [
            {key: value for key, value in result.items() if key != "witnesses"}
            for result in ordered
        ],
        "witnesses": witnesses,
    }
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main() -> None:
    work = tasks()
    results: list[dict[str, object]] = []
    for result in census.map(work, order_outputs=False):
        results.append(result)
        write_packet(results, len(work))
        print(f"E1_E34_GENERIC_PROGRESS returned={len(results)}/{len(work)}")
    complete = [result for result in results if result.get("complete") is True]
    print(
        "E1_E34_GENERIC_CENSUS "
        f"complete={len(complete)}/{len(work)} "
        f"worker_seconds={sum(float(result['wall_seconds']) for result in complete):.6f}"
    )
