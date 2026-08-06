#!/usr/bin/env python3
"""Jointly census the two live two-odd E30 profiles on 87 templates."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e30_two_odd_joint_census.cpp"
ORBITS = HERE / "e30_two_six_odd_light_orbit_result.json"
RESULT = HERE / "e30_two_odd_joint_census_result.json"
REMOTE_SOURCE = "/root/e30_two_odd_joint_census.cpp"
REMOTE_BINARY = "/root/e30_two_odd_joint_census"
PROFILES = ("profile_27", "profile_151")

app = modal.App("e1-n256-e30-two-odd-joint-census")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(SOURCE, REMOTE_SOURCE, copy=True)
    .run_commands(f"g++ -O3 -std=c++17 {REMOTE_SOURCE} -o {REMOTE_BINARY}")
)


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=87)
def run_template(template: int, light: list[int]) -> dict[str, object]:
    import subprocess
    import time

    started = time.monotonic()
    completed = subprocess.run(
        [REMOTE_BINARY, str(template), *(str(value) for value in light)],
        check=True, capture_output=True, text=True, timeout=55,
    )
    row = json.loads(completed.stdout)
    row["worker_seconds"] = time.monotonic() - started
    return row


@app.local_entrypoint()
def main() -> None:
    orbit_packet = json.loads(ORBITS.read_text())
    representatives = [row["representative"] for row in orbit_packet["rows"]]
    rows: list[dict[str, object]] = []

    def write_checkpoint(complete: bool) -> dict[str, dict[str, int]]:
        summary = {}
        if rows:
            for profile in PROFILES:
                summary[profile] = {
                    "count": sum(int(row[profile]["count"]) for row in rows),
                    "full_conductor": sum(int(row[profile]["full_conductor"]) for row in rows),
                    "maximum_m3": max(int(row[profile]["maximum_m3"]) for row in rows),
                    "maximum_full_conductor_m3": max(int(row[profile]["maximum_full_conductor_m3"]) for row in rows),
                }
        packet = {
            "schema": "e1-e30-two-odd-joint-census-v1",
            "complete": complete,
            "completed_templates": len(rows),
            "expected_templates": len(representatives),
            "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            "orbits_sha256": hashlib.sha256(ORBITS.read_bytes()).hexdigest(),
            "summary": summary,
            "rows": rows,
        }
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        return summary

    write_checkpoint(False)
    try:
        for row in run_template.map(range(len(representatives)), representatives):
            rows.append(row)
            write_checkpoint(False)
    except BaseException:
        print(f"E30_TWO_ODD_JOINT_INCOMPLETE completed={len(rows)}/87 result={RESULT}")
        raise
    complete = len(rows) == 87 and all(bool(row["complete"]) for row in rows)
    summary = write_checkpoint(complete)
    print("E30_TWO_ODD_JOINT_CENSUS " + json.dumps(summary, sort_keys=True))
    print(f"E30_TWO_ODD_JOINT_COMPLETE {complete}")
    print(f"E30_TWO_ODD_JOINT_RESULT {RESULT}")
