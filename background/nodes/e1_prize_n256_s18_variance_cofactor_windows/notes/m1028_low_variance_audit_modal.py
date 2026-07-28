#!/usr/bin/env python3
"""Independent direct-convolution audit of the m=1028 low-variance census."""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "m1028_low_variance_audit.cpp"
OUTPUT = HERE / "m1028_low_variance_audit_result.json"
SHARDS = 32

image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(str(SOURCE), "/root/audit.cpp", copy=True)
    .run_commands("g++ -O3 -std=c++17 /root/audit.cpp -o /usr/local/bin/audit")
)
app = modal.App("e1-prize-m1028-low-variance-audit")


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=32)
def audit(shard: int) -> dict[str, object]:
    started = time.perf_counter()
    try:
        completed = subprocess.run(
            ["/usr/local/bin/audit", str(shard)],
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
    totals = {
        key: sum(int(result[key]) for result in complete)
        for key in (
            "combination_count",
            "signed_vector_count",
            "energy5_count",
            "energy9_count",
            "energy5_div257_count",
            "energy9_div257_count",
        )
    }
    packet = {
        "schema": "e1-prize-m1028-low-variance-audit-v1",
        "complete": len(complete) == SHARDS,
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "enumeration": "lexicographic combinations modulo 32 shards",
        "correlation": "independent full 128-slot ordered-pair convolution",
        "returned_shards": len(results),
        "errors": [result for result in results if result.get("complete") is not True],
        "totals": totals,
        "worker_seconds": sum(float(result["wall_seconds"]) for result in complete),
        "container_seconds": sum(float(result["container_seconds"]) for result in complete),
        "results": complete,
    }
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main() -> None:
    results: list[dict[str, object]] = []
    for result in audit.map(range(SHARDS), order_outputs=False):
        results.append(result)
        write_packet(results)
        print(f"M1028_LOW_VARIANCE_AUDIT_PROGRESS returned={len(results)}/{SHARDS}")
    print(
        "M1028_LOW_VARIANCE_AUDIT "
        f"complete={sum(result.get('complete') is True for result in results)}/{SHARDS}"
    )
