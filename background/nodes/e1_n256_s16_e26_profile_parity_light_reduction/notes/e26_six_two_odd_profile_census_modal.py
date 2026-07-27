#!/usr/bin/env python3
"""Run the exact E26 six-profile two-odd census on Modal."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e26_six_two_odd_profile_census.cpp"
REDUCTION = HERE / "e26_profile_parity_probe_result.json"
RESULT = HERE / "e26_six_two_odd_profile_census_result.json"
REMOTE_SOURCE = "/root/e26_six_two_odd_profile_census.cpp"
REMOTE_BINARY = "/root/e26_six_two_odd_profile_census"

app = modal.App("e1-n256-e26-six-two-odd-profile-census")
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
    root = HERE.parents[1]
    atlas_path = root / "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_two_six_odd_light_orbit_result.json"
    reduction = json.loads(REDUCTION.read_text())
    if not reduction["complete"]:
        raise RuntimeError("E26 profile reduction is incomplete")
    atlas = json.loads(atlas_path.read_text())
    if not atlas["complete"]:
        raise RuntimeError("E26 two-odd atlas is incomplete")
    tasks = [row["representative"] for row in atlas["rows"]]
    if len(tasks) != 87:
        raise RuntimeError("E26 two-odd template count mismatch")
    rows: list[dict[str, object]] = []

    def vector_sum(key: str) -> list[int]:
        return [sum(int(row[key][index]) for row in rows) for index in range(6)]

    def vector_max(key: str) -> list[int]:
        return [max((int(row[key][index]) for row in rows), default=-1) for index in range(6)]

    def write_checkpoint(complete: bool) -> dict[str, object]:
        packet = {
            "schema": "e1-e26-six-two-odd-profile-census-v1",
            "complete": complete,
            "completed_templates": len(rows),
            "expected_templates": len(tasks),
            "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            "reduction_sha256": hashlib.sha256(REDUCTION.read_bytes()).hexdigest(),
            "atlas_sha256": hashlib.sha256(atlas_path.read_bytes()).hexdigest(),
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
        print(f"E26_SIX_TWO_ODD_PROFILE_INCOMPLETE completed={len(rows)}/{len(tasks)}")
        raise
    packet = write_checkpoint(
        len(rows) == len(tasks)
        and all(bool(row["complete"]) for row in rows)
        and sum(int(row["vectors"]) for row in rows) == 1_726_770_432
    )
    print("E26_SIX_TWO_ODD_PROFILE " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E26_SIX_TWO_ODD_PROFILE_COMPLETE {packet['complete']}")
    print(f"E26_SIX_TWO_ODD_PROFILE_RESULT {RESULT}")
