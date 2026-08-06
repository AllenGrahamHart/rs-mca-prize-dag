#!/usr/bin/env python3
"""Probe all eight E30 profiles with the complete mod-16 relaxation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
BASE_SOURCE = (
    HERE.parent.parent
    / "e1_n256_s16_sparse_l1_variance_exclusion"
    / "notes"
    / "e34_nested_quotient_census.cpp"
)
SOURCE = HERE / "e30_eight_profile_quotient_census.cpp"
RESULT = HERE / "e30_eight_profile_quotient_probe_result.json"
REMOTE_BASE = "/root/e34_nested_quotient_census.cpp"
REMOTE_SOURCE = "/root/e30_eight_profile_quotient_census.cpp"
REMOTE_BINARY = "/root/e30_eight_profile_quotient_census"
SHARDS = 8
PROFILES = (
    "6,6",
    "2,7",
    "5,4,1",
    "1,5,1",
    "4,2,2",
    "0,3,2",
    "6,2,0,1",
    "3,0,3",
)

app = modal.App("e1-n256-e30-eight-profile-quotient-probe")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(BASE_SOURCE, REMOTE_BASE, copy=True)
    .add_local_file(SOURCE, REMOTE_SOURCE, copy=True)
    .run_commands(f"g++ -O3 -std=c++17 {REMOTE_SOURCE} -o {REMOTE_BINARY}")
)


@app.function(image=image, cpu=1.0, memory=512, timeout=60, max_containers=64)
def run_shard(profile: int, order: int, shard: int) -> dict[str, object]:
    import subprocess
    import time

    started = time.monotonic()
    completed = subprocess.run(
        [REMOTE_BINARY, str(profile), str(order), str(shard), str(SHARDS)],
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
    tasks = [
        (profile, order, shard)
        for profile in range(len(PROFILES))
        for order in (128, 64)
        for shard in range(SHARDS)
    ]
    rows: list[dict[str, object]] = []

    def write_checkpoint(complete: bool) -> dict[str, object]:
        summary = {}
        for profile, name in enumerate(PROFILES):
            summary[name] = {}
            for order in (128, 64):
                selected = [
                    row for row in rows
                    if int(row["profile"]) == profile and int(row["order"]) == order
                ]
                summary[name][str(order)] = {
                    "completed_shards": len(selected),
                    "tested": sum(int(row["tested"]) for row in selected),
                    "maximum": max((int(row["best"]) for row in selected), default=-1),
                }
        packet = {
            "schema": "e1-e30-eight-profile-quotient-probe-v1",
            "complete": complete,
            "completed_tasks": len(rows),
            "expected_tasks": len(tasks),
            "shards": SHARDS,
            "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            "base_source_sha256": hashlib.sha256(BASE_SOURCE.read_bytes()).hexdigest(),
            "profiles": list(PROFILES),
            "summary": summary,
            "rows": rows,
        }
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        return summary

    write_checkpoint(False)
    try:
        for row in run_shard.map(
            [task[0] for task in tasks],
            [task[1] for task in tasks],
            [task[2] for task in tasks],
        ):
            rows.append(row)
            write_checkpoint(False)
    except BaseException:
        print(f"E30_QUOTIENT_PROBE_INCOMPLETE completed={len(rows)}/{len(tasks)} result={RESULT}")
        raise

    complete = len(rows) == len(tasks) and all(bool(row["complete"]) for row in rows)
    summary = write_checkpoint(complete)
    print("E30_QUOTIENT_PROBE " + json.dumps(summary, sort_keys=True))
    print(f"E30_QUOTIENT_PROBE_COMPLETE {complete}")
    print(f"E30_QUOTIENT_PROBE_RESULT {RESULT}")
