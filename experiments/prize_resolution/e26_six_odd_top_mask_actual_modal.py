#!/usr/bin/env python3
"""Search the top cheap-relaxation E26 masks for actual profile vectors."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e26_six_odd_top_mask_actual_census.cpp"
RELAXATION_SOURCE = HERE / "e26_six_odd_cheap_relaxation_probe.cpp"
RESULT = HERE / "e26_six_odd_top_mask_actual_result.json"
REMOTE_SOURCE = "/root/e26_six_odd_top_mask_actual_census.cpp"
REMOTE_BINARY = "/root/e26_six_odd_top_mask_actual_census"

# (profile, relaxation maximum, normalized light representative)
TASKS = (
    (0, 870, (0, 8, 24, 56)), (0, 846, (0, 8, 24, 96)),
    (0, 804, (0, 4, 20, 28)), (0, 804, (0, 2, 10, 14)),
    (0, 804, (0, 1, 5, 7)), (0, 744, (0, 4, 12, 108)),
    (0, 744, (0, 2, 6, 118)), (0, 744, (0, 1, 3, 123)),
    (0, 738, (0, 4, 12, 28)), (0, 738, (0, 2, 6, 14)),
    (0, 738, (0, 1, 3, 7)), (0, 726, (0, 4, 12, 48)),
    (0, 726, (0, 2, 6, 88)), (0, 726, (0, 1, 3, 44)),
    (0, 708, (0, 4, 12, 92)), (0, 708, (0, 4, 12, 112)),
    (1, 606, (0, 4, 12, 96)), (1, 606, (0, 2, 6, 48)),
    (1, 606, (0, 1, 3, 88)), (1, 582, (0, 4, 24, 32)),
    (1, 582, (0, 4, 20, 32)), (1, 582, (0, 2, 12, 16)),
    (1, 582, (0, 2, 10, 16)), (1, 582, (0, 1, 6, 8)),
    (1, 582, (0, 1, 5, 8)), (1, 570, (0, 4, 12, 48)),
    (1, 570, (0, 2, 6, 88)), (1, 570, (0, 1, 3, 44)),
    (1, 564, (0, 4, 20, 52)), (1, 564, (0, 4, 12, 52)),
    (1, 564, (0, 2, 6, 90)), (1, 564, (0, 1, 3, 45)),
)

app = modal.App("e1-e26-six-odd-top-mask-actual")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(SOURCE, REMOTE_SOURCE, copy=True)
    .run_commands(f"g++ -O3 -std=c++20 {REMOTE_SOURCE} -o {REMOTE_BINARY}")
)


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=32)
def run(task: tuple[int, int, tuple[int, int, int, int], int]) -> dict[str, object]:
    import subprocess
    import time

    profile, relaxation_maximum, light, task_index = task
    started = time.monotonic()
    completed = subprocess.run(
        [REMOTE_BINARY, str(task_index), str(profile), *(str(value) for value in light)],
        capture_output=True,
        check=True,
        text=True,
        timeout=55,
    )
    row = json.loads(completed.stdout)
    row["relaxation_maximum"] = relaxation_maximum
    row["worker_seconds"] = time.monotonic() - started
    return row


@app.local_entrypoint()
def main() -> None:
    rows: list[dict[str, object]] = []

    def write_checkpoint(complete: bool, error: str | None = None) -> None:
        packet = {
            "schema": "e1-e26-six-odd-top-mask-actual-v1",
            "complete": complete,
            "completed_tasks": len(rows),
            "expected_tasks": len(TASKS),
            "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            "relaxation_source_sha256": hashlib.sha256(
                RELAXATION_SOURCE.read_bytes()
            ).hexdigest(),
            "error": error,
            "rows": sorted(rows, key=lambda row: int(row["task"])),
        }
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")

    write_checkpoint(False)
    try:
        payloads = [(*task, index) for index, task in enumerate(TASKS)]
        for row in run.map(payloads):
            assert int(row["maximum_m3"]) <= int(row["relaxation_maximum"])
            rows.append(row)
            write_checkpoint(False)
    except BaseException as error:
        write_checkpoint(False, f"{type(error).__name__}: {error}")
        print(f"E26_SIX_ODD_TOP_MASK_ACTUAL_INCOMPLETE {len(rows)}/{len(TASKS)}")
        raise
    write_checkpoint(len(rows) == len(TASKS) and all(bool(row["complete"]) for row in rows))
    summary = {
        "vectors": sum(int(row["vectors"]) for row in rows),
        "profile_count": sum(int(row["profile_count"]) for row in rows),
        "above_cutoff": sum(int(row["above_cutoff"]) for row in rows),
        "full_above_cutoff": sum(int(row["full_above_cutoff"]) for row in rows),
        "maximum_full_m3": max(int(row["maximum_full_m3"]) for row in rows),
        "worker_seconds": sum(float(row["worker_seconds"]) for row in rows),
    }
    print("E26_SIX_ODD_TOP_MASK_ACTUAL " + json.dumps(summary, sort_keys=True))
