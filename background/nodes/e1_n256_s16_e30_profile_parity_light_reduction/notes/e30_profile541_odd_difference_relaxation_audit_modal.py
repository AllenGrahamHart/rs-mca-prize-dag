#!/usr/bin/env python3
"""Run the independent profile-(5,4,1) odd-difference relaxation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e30_profile541_odd_difference_relaxation_audit.cpp"
PRODUCTION = HERE / "e30_profile541_odd_difference_relaxation_result.json"
RESULT = HERE / "e30_profile541_odd_difference_relaxation_audit_result.json"
REMOTE_SOURCE = "/root/e30_profile541_odd_difference_relaxation_audit.cpp"
REMOTE_BINARY = "/root/e30_profile541_odd_difference_relaxation_audit"
SHARDS = 64

app = modal.App("e1-n256-e30-profile541-odd-difference-relaxation-audit")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(SOURCE, REMOTE_SOURCE, copy=True)
    .run_commands(f"g++ -O3 -std=c++17 {REMOTE_SOURCE} -o {REMOTE_BINARY}")
)


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=64)
def run_shard(shard: int) -> dict[str, object]:
    import subprocess
    import time

    started = time.monotonic()
    completed = subprocess.run(
        [REMOTE_BINARY, str(shard), str(SHARDS)],
        check=True,
        capture_output=True,
        text=True,
        timeout=55,
    )
    row = json.loads(completed.stdout)
    row["worker_seconds"] = time.monotonic() - started
    return row


@app.local_entrypoint()
def main() -> None:
    rows: list[dict[str, object]] = []

    def write_checkpoint(complete: bool) -> dict[str, object]:
        packet = {
            "schema": "e1-e30-profile541-odd-difference-relaxation-audit-v1",
            "complete": complete,
            "completed_shards": len(rows),
            "expected_shards": SHARDS,
            "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            "production_sha256": hashlib.sha256(PRODUCTION.read_bytes()).hexdigest(),
            "summary": {
                "assignments": sum(int(row["assignments"]) for row in rows),
                "above_threshold": sum(int(row["above_threshold"]) for row in rows),
                "maximum_m3": max((int(row["maximum_m3"]) for row in rows), default=None),
                "worker_seconds": sum(float(row["worker_seconds"]) for row in rows),
            },
            "rows": sorted(rows, key=lambda row: int(row["shard"])),
        }
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        return packet

    write_checkpoint(False)
    try:
        for row in run_shard.map(range(SHARDS)):
            rows.append(row)
            write_checkpoint(False)
    except BaseException:
        print(f"E30_PROFILE541_ODD_DIFFERENCE_AUDIT_INCOMPLETE completed={len(rows)}/{SHARDS}")
        raise
    packet = write_checkpoint(
        len(rows) == SHARDS
        and all(bool(row["complete"]) for row in rows)
        and sum(int(row["tested_masks"]) for row in rows)
        == int(rows[0]["distinct_odd_masks"])
    )
    print("E30_PROFILE541_ODD_DIFFERENCE_AUDIT " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E30_PROFILE541_ODD_DIFFERENCE_AUDIT_COMPLETE {packet['complete']}")
    print(f"E30_PROFILE541_ODD_DIFFERENCE_AUDIT_RESULT {RESULT}")
