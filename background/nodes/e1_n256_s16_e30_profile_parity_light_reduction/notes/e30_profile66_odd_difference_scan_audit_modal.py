#!/usr/bin/env python3
"""Independently replay the exact profile-(6,6) odd-difference scan."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e30_profile66_odd_difference_scan_audit.cpp"
ORBITS = HERE / "e30_six_odd_mask_orbits_result.json"
PRODUCTION = HERE / "e30_profile66_odd_difference_scan_result.json"
RESULT = HERE / "e30_profile66_odd_difference_scan_audit_result.json"
REMOTE_SOURCE = "/root/e30_profile66_odd_difference_scan_audit.cpp"
REMOTE_BINARY = "/root/e30_profile66_odd_difference_scan_audit"

app = modal.App("e1-n256-e30-profile66-odd-difference-scan-audit")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(SOURCE, REMOTE_SOURCE, copy=True)
    .run_commands(f"g++ -O3 -std=c++17 {REMOTE_SOURCE} -o {REMOTE_BINARY}")
)


@app.function(image=image, cpu=1.0, memory=256, timeout=120, max_containers=100)
def run_mask(index: int, odd_mask: int, light: list[int]) -> dict[str, object]:
    import subprocess
    import time

    started = time.monotonic()
    completed = subprocess.run(
        [REMOTE_BINARY, str(index), str(odd_mask), *(str(value) for value in light)],
        check=True,
        capture_output=True,
        text=True,
        timeout=110,
    )
    row = json.loads(completed.stdout)
    row["worker_seconds"] = time.monotonic() - started
    return row


@app.local_entrypoint()
def main() -> None:
    orbit_packet = json.loads(ORBITS.read_text())
    production = json.loads(PRODUCTION.read_text())
    if not orbit_packet["complete"] or not production["complete"]:
        raise RuntimeError("profile-(6,6) production inputs are incomplete")
    tasks = [
        (index, int(row["odd_mask"]), list(row["orbits"][0]))
        for index, row in enumerate(orbit_packet["rows"])
    ]
    rows: list[dict[str, object]] = []

    def write_checkpoint(complete: bool) -> dict[str, object]:
        packet = {
            "schema": "e1-e30-profile66-odd-difference-scan-audit-v1",
            "complete": complete,
            "completed_masks": len(rows),
            "expected_masks": len(tasks),
            "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            "orbits_sha256": hashlib.sha256(ORBITS.read_bytes()).hexdigest(),
            "production_sha256": hashlib.sha256(PRODUCTION.read_bytes()).hexdigest(),
            "summary": {
                "assignments": sum(int(row["assignments"]) for row in rows),
                "above_threshold": sum(int(row["above_threshold"]) for row in rows),
                "exceptional_masks": sum(int(row["above_threshold"]) > 0 for row in rows),
                "maximum_m3": max((int(row["maximum_m3"]) for row in rows), default=None),
                "worker_seconds": sum(float(row["worker_seconds"]) for row in rows),
            },
            "rows": sorted(rows, key=lambda row: int(row["index"])),
        }
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        return packet

    write_checkpoint(False)
    try:
        for row in run_mask.map(
            [task[0] for task in tasks],
            [task[1] for task in tasks],
            [task[2] for task in tasks],
        ):
            rows.append(row)
            if len(rows) % 16 == 0:
                write_checkpoint(False)
    except BaseException:
        write_checkpoint(False)
        print(f"E30_PROFILE66_ODD_DIFFERENCE_AUDIT_INCOMPLETE completed={len(rows)}/{len(tasks)}")
        raise
    packet = write_checkpoint(
        len(rows) == len(tasks)
        and all(bool(row["complete"]) for row in rows)
        and sum(int(row["assignments"]) for row in rows) == 44_779_702_968
    )
    print("E30_PROFILE66_ODD_DIFFERENCE_AUDIT " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E30_PROFILE66_ODD_DIFFERENCE_AUDIT_COMPLETE {packet['complete']}")
    print(f"E30_PROFILE66_ODD_DIFFERENCE_AUDIT_RESULT {RESULT}")
