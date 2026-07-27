#!/usr/bin/env python3
"""Jointly census the two live E32 profiles on 148 affine light templates."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e32_four_odd_joint_census.cpp"
ORBITS = HERE / "e32_four_odd_light_orbit_result.json"
RESULT = HERE / "e32_four_odd_joint_census_result.json"
REMOTE_SOURCE = "/root/e32_four_odd_joint_census.cpp"
REMOTE_BINARY = "/root/e32_four_odd_joint_census"

app = modal.App("e1-n256-e32-four-odd-joint-census")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(SOURCE, REMOTE_SOURCE, copy=True)
    .run_commands(f"g++ -O3 -std=c++17 {REMOTE_SOURCE} -o {REMOTE_BINARY}")
)


@app.function(image=image, cpu=1.0, memory=256, timeout=60)
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
    result = json.loads(completed.stdout)
    result["worker_seconds"] = time.monotonic() - started
    return result


@app.local_entrypoint()
def main() -> None:
    orbit_packet = json.loads(ORBITS.read_text())
    representatives = [row["representative"] for row in orbit_packet["rows"]]
    rows = list(run_template.map(range(len(representatives)), representatives))
    summary = {}
    for profile in ("profile_47", "profile_351"):
        summary[profile] = {
            "count": sum(int(row[profile]["count"]) for row in rows),
            "full_conductor": sum(
                int(row[profile]["full_conductor"]) for row in rows
            ),
            "maximum_m3": max(int(row[profile]["maximum_m3"]) for row in rows),
            "maximum_full_conductor_m3": max(
                int(row[profile]["maximum_full_conductor_m3"]) for row in rows
            ),
        }
    packet = {
        "schema": "e1-e32-four-odd-joint-census-v1",
        "complete": all(bool(row["complete"]) for row in rows),
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "orbits_sha256": hashlib.sha256(ORBITS.read_bytes()).hexdigest(),
        "summary": summary,
        "rows": rows,
    }
    RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    print("E32_FOUR_ODD_JOINT_CENSUS " + json.dumps(summary, sort_keys=True))
    print(f"E32_FOUR_ODD_JOINT_RESULT {RESULT}")
