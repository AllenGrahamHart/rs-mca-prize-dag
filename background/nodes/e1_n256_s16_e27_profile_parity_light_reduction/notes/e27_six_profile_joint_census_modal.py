#!/usr/bin/env python3
"""Run the exact E27 six-profile joint census on Modal."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e27_six_profile_joint_census.cpp"
REDUCTION = HERE / "e27_profile_parity_probe_result.json"
RESULT = HERE / "e27_six_profile_joint_census_result.json"
REMOTE_SOURCE = "/root/e27_six_profile_joint_census.cpp"
REMOTE_BINARY = "/root/e27_six_profile_joint_census"

app = modal.App("e1-n256-e27-six-profile-joint-census")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(SOURCE, REMOTE_SOURCE, copy=True)
    .run_commands(f"g++ -O3 -std=c++17 {REMOTE_SOURCE} -o {REMOTE_BINARY}")
)


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=100)
def run_template(template: int, light: list[int]) -> dict[str, object]:
    import subprocess
    import time

    started = time.monotonic()
    completed = subprocess.run(
        [REMOTE_BINARY, str(template), *(str(value) for value in light)],
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
    reduction = json.loads(REDUCTION.read_text())
    if not reduction["complete"]:
        raise RuntimeError("E27 profile reduction is incomplete")
    geometry = reduction["light_geometry"]["orbit_representatives"]
    tasks = list(geometry["3"])
    if len(tasks) != 8:
        raise RuntimeError("E27 light-template count mismatch")
    rows: list[dict[str, object]] = []

    def vector_sum(key: str) -> list[int]:
        return [sum(int(row[key][index]) for row in rows) for index in range(6)]

    def vector_max(key: str) -> list[int]:
        return [max((int(row[key][index]) for row in rows), default=-1) for index in range(6)]

    def write_checkpoint(complete: bool) -> dict[str, object]:
        packet = {
            "schema": "e1-e27-six-profile-joint-census-v1",
            "complete": complete,
            "completed_templates": len(rows),
            "expected_templates": len(tasks),
            "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            "reduction_sha256": hashlib.sha256(REDUCTION.read_bytes()).hexdigest(),
            "summary": {
                "vectors": sum(int(row["vectors"]) for row in rows),
                "profile_counts": vector_sum("profile_counts"),
                "above_cutoff": vector_sum("above_cutoff"),
                "full_above_cutoff": vector_sum("full_above_cutoff"),
                "maximum_m3": vector_max("maximum_m3"),
                "maximum_full_m3": vector_max("maximum_full_m3"),
                "worker_seconds": sum(float(row["worker_seconds"]) for row in rows),
            },
            "rows": sorted(rows, key=lambda row: int(row["template"])),
        }
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        return packet

    write_checkpoint(False)
    try:
        for row in run_template.map(range(len(tasks)), tasks):
            rows.append(row)
            write_checkpoint(False)
    except BaseException:
        print(f"E27_SIX_PROFILE_JOINT_INCOMPLETE completed={len(rows)}/{len(tasks)}")
        raise
    packet = write_checkpoint(
        len(rows) == len(tasks)
        and all(bool(row["complete"]) for row in rows)
        and sum(int(row["vectors"]) for row in rows) == 158_783_488
    )
    print("E27_SIX_PROFILE_JOINT " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E27_SIX_PROFILE_JOINT_COMPLETE {packet['complete']}")
    print(f"E27_SIX_PROFILE_JOINT_RESULT {RESULT}")
