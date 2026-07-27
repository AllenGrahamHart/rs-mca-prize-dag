#!/usr/bin/env python3
"""Run an independent negacyclic audit of the E34 progression census."""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e34_progression_audit.cpp"
OUTPUT = HERE / "e34_progression_audit_result.json"
TASKS = (1, 2, 4, 8, 16)

image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(str(SOURCE), "/root/audit.cpp", copy=True)
    .run_commands("g++ -O3 -std=c++17 /root/audit.cpp -o /usr/local/bin/e34-progression-audit")
)
app = modal.App("e1-e34-progression-audit")


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=5)
def audit(t: int) -> dict[str, object]:
    started = time.perf_counter()
    try:
        completed = subprocess.run(
            ["/usr/local/bin/e34-progression-audit", str(t)],
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
    packet = {
        "schema": "e1-e34-progression-audit-v1",
        "complete": len(complete) == len(TASKS),
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "expected_tasks": list(TASKS),
        "errors": [result for result in results if result.get("complete") is not True],
        "results": sorted(complete, key=lambda result: int(result["t"])),
    }
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main() -> None:
    results: list[dict[str, object]] = []
    for result in audit.map(TASKS, order_outputs=False):
        results.append(result)
        write_packet(results)
        print(f"E1_E34_PROGRESSION_AUDIT_PROGRESS returned={len(results)}/{len(TASKS)}")
    complete = [result for result in results if result.get("complete") is True]
    print(
        "E1_E34_PROGRESSION_AUDIT "
        f"complete={len(complete)}/{len(TASKS)} "
        f"worker_seconds={sum(float(result['wall_seconds']) for result in complete):.6f}"
    )
