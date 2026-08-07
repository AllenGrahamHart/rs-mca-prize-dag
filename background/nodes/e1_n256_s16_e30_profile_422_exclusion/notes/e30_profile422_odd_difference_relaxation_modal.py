#!/usr/bin/env python3
"""Run the exact profile-(4,2,2) odd-difference relaxation on Modal."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e30_profile422_odd_difference_relaxation.cpp"
RESULT = HERE / "e30_profile422_odd_difference_relaxation_result.json"
REMOTE_SOURCE = "/root/e30_profile422_odd_difference_relaxation.cpp"
REMOTE_BINARY = "/root/e30_profile422_odd_difference_relaxation"
SHARDS = 4

app = modal.App("e1-n256-e30-profile422-odd-difference-relaxation")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(SOURCE, REMOTE_SOURCE, copy=True)
    .run_commands(f"g++ -O3 -std=c++20 {REMOTE_SOURCE} -o {REMOTE_BINARY}")
)


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=4)
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
        maximum_row = max(rows, key=lambda row: int(row["maximum_m3"])) if rows else None
        packet = {
            "schema": "e1-e30-profile422-odd-difference-relaxation-v1",
            "complete": complete,
            "completed_shards": len(rows),
            "expected_shards": SHARDS,
            "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            "summary": {
                "assignments": sum(int(row["assignments"]) for row in rows),
                "above_threshold": sum(int(row["above_threshold"]) for row in rows),
                "exceptional": [
                    candidate
                    for row in rows
                    for candidate in row["exceptional"]
                ],
                "maximum_m3": int(maximum_row["maximum_m3"]) if maximum_row else None,
                "threshold": 1087,
                "closes_profile": bool(maximum_row and int(maximum_row["maximum_m3"]) <= 1087),
                "witness": maximum_row["witness"] if maximum_row else None,
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
        print(f"E30_PROFILE422_ODD_DIFFERENCE_INCOMPLETE completed={len(rows)}/{SHARDS}")
        raise
    complete = (
        len(rows) == SHARDS
        and all(bool(row["complete"]) for row in rows)
        and sum(int(row["tested_masks"]) for row in rows)
        == int(rows[0]["distinct_odd_masks"])
    )
    packet = write_checkpoint(complete)
    print("E30_PROFILE422_ODD_DIFFERENCE " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E30_PROFILE422_ODD_DIFFERENCE_COMPLETE {complete}")
    print(f"E30_PROFILE422_ODD_DIFFERENCE_RESULT {RESULT}")
