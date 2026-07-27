#!/usr/bin/env python3
"""Run the E=34 profile-(2,8) refined quotient and inner-4Z censuses."""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
QUOTIENT_CPP = HERE / "e34_profile2_refined_quotient_census.cpp"
SUPPORT_CPP = HERE / "e34_profile2_inner4_support_census.cpp"
OUTPUT = HERE / "e34_profile2_coupled_result.json"
QUOTIENT_SHARDS = 16
SUPPORT_SHARDS = 32

base = modal.Image.debian_slim().apt_install("g++")
image = (
    base.add_local_file(str(QUOTIENT_CPP), "/root/quotient.cpp", copy=True)
    .add_local_file(str(SUPPORT_CPP), "/root/support.cpp", copy=True)
    .run_commands(
        "g++ -O3 -std=c++17 /root/quotient.cpp -o /usr/local/bin/profile2-quotient",
        "g++ -O3 -std=c++17 /root/support.cpp -o /usr/local/bin/profile2-support",
    )
)
app = modal.App("e1-e34-profile2-coupled-census")


@app.function(image=image, cpu=1.0, memory=256, timeout=120, max_containers=64)
def census_task(task: tuple[str, int, int]) -> dict[str, object]:
    kind, parameter, shards = task
    started = time.perf_counter()
    try:
        if kind == "quotient128" or kind == "quotient64":
            order = 128 if kind == "quotient128" else 64
            shard = parameter
            command = [
                "/usr/local/bin/profile2-quotient",
                str(order),
                str(shard),
                str(shards),
            ]
        elif kind == "support":
            shard = parameter
            command = [
                "/usr/local/bin/profile2-support",
                str(shard),
                str(shards),
            ]
        else:
            raise ValueError(f"unknown task kind {kind}")
        completed = subprocess.run(
            command,
            capture_output=True,
            check=True,
            text=True,
            timeout=110,
        )
        result = json.loads(completed.stdout)
        result["kind"] = "support" if kind == "support" else "quotient"
        result["wall_seconds"] = time.perf_counter() - started
        return result
    except Exception as error:
        return {
            "complete": False,
            "kind": kind,
            "parameter": parameter,
            "shards": shards,
            "wall_seconds": time.perf_counter() - started,
            "error": repr(error),
        }


def write_packet(results: list[dict[str, object]], expected: int) -> None:
    complete = [result for result in results if result.get("complete") is True]
    packet = {
        "schema": "e1-e34-profile2-coupled-v1",
        "complete": len(complete) == expected,
        "quotient_source_sha256": hashlib.sha256(QUOTIENT_CPP.read_bytes()).hexdigest(),
        "support_source_sha256": hashlib.sha256(SUPPORT_CPP.read_bytes()).hexdigest(),
        "errors": [result for result in results if result.get("complete") is not True],
        "quotient_results": [result for result in complete if result["kind"] == "quotient"],
        "support_results": [result for result in complete if result["kind"] == "support"],
    }
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main() -> None:
    tasks = [
        (kind, shard, QUOTIENT_SHARDS)
        for kind in ("quotient128", "quotient64")
        for shard in range(QUOTIENT_SHARDS)
    ] + [("support", shard, SUPPORT_SHARDS) for shard in range(SUPPORT_SHARDS)]
    results: list[dict[str, object]] = []
    for result in census_task.map(tasks, order_outputs=False):
        results.append(result)
        write_packet(results, len(tasks))
        print(f"E1_E34_PROFILE2_PROGRESS returned={len(results)}/{len(tasks)}")
    complete = [result for result in results if result.get("complete") is True]
    print(
        "E1_E34_PROFILE2_COUPLED_CENSUS "
        f"complete={len(complete)}/{len(tasks)} "
        f"worker_seconds={sum(float(result['wall_seconds']) for result in complete):.6f}"
    )
