#!/usr/bin/env python3
"""Independently census actual vectors over exceptional profile-(5,4,1) masks."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e30_profile541_exceptional_actual_audit.cpp"
PRODUCTION = HERE / "e30_profile541_exceptional_actual_result.json"
RELAXATION = HERE / "e30_profile541_odd_difference_relaxation_result.json"
ORBITS = HERE / "e30_six_odd_mask_orbits_result.json"
RESULT = HERE / "e30_profile541_exceptional_actual_audit_result.json"
REMOTE_SOURCE = "/root/e30_profile541_exceptional_actual_audit.cpp"
REMOTE_BINARY = "/root/e30_profile541_exceptional_actual_audit"

app = modal.App("e1-n256-e30-profile541-exceptional-actual-audit")
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
    relaxation = json.loads(RELAXATION.read_text())
    exceptional_masks = {
        int(candidate["odd_mask"]) for candidate in relaxation["summary"]["exceptional"]
    }
    orbit_packet = json.loads(ORBITS.read_text())
    tasks = [
        orbit
        for row in orbit_packet["rows"]
        if int(row["odd_mask"]) in exceptional_masks
        for orbit in row["orbits"]
    ]
    rows: list[dict[str, object]] = []

    def write_checkpoint(complete: bool) -> dict[str, object]:
        production = json.loads(PRODUCTION.read_text())
        first = {int(row["template"]): row for row in production["rows"]}
        second = {int(row["template"]): row for row in rows}
        agreement = len(first) == len(second) == len(tasks)
        if agreement:
            for template in range(len(tasks)):
                for key in (
                    "light",
                    "supports",
                    "vectors",
                    "profile_count",
                    "above_cutoff",
                    "full_above_cutoff",
                    "maximum_m3",
                    "maximum_full_m3",
                    "matches",
                ):
                    if first[template][key] != second[template][key]:
                        agreement = False
        packet = {
            "schema": "e1-e30-profile541-exceptional-actual-audit-v1",
            "complete": complete,
            "agreement": agreement,
            "completed_templates": len(rows),
            "expected_templates": len(tasks),
            "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            "production_sha256": hashlib.sha256(PRODUCTION.read_bytes()).hexdigest(),
            "relaxation_sha256": hashlib.sha256(RELAXATION.read_bytes()).hexdigest(),
            "orbits_sha256": hashlib.sha256(ORBITS.read_bytes()).hexdigest(),
            "summary": {
                "vectors": sum(int(row["vectors"]) for row in rows),
                "profile_count": sum(int(row["profile_count"]) for row in rows),
                "above_cutoff": sum(int(row["above_cutoff"]) for row in rows),
                "full_above_cutoff": sum(int(row["full_above_cutoff"]) for row in rows),
                "maximum_m3": max((int(row["maximum_m3"]) for row in rows), default=None),
                "maximum_full_m3": max((int(row["maximum_full_m3"]) for row in rows), default=None),
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
        print(f"E30_PROFILE541_EXCEPTIONAL_ACTUAL_AUDIT_INCOMPLETE completed={len(rows)}/{len(tasks)}")
        raise
    packet = write_checkpoint(
        len(rows) == len(tasks) and all(bool(row["complete"]) for row in rows)
    )
    print("E30_PROFILE541_EXCEPTIONAL_ACTUAL_AUDIT " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E30_PROFILE541_EXCEPTIONAL_ACTUAL_AUDIT_AGREEMENT {packet['agreement']}")
    print(f"E30_PROFILE541_EXCEPTIONAL_ACTUAL_AUDIT_RESULT {RESULT}")
