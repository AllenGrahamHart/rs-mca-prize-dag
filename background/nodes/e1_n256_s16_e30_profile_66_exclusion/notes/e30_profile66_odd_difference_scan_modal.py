#!/usr/bin/env python3
"""Scan the exact profile-(6,6) odd-difference relaxation on Modal."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e30_profile66_odd_difference_scan.cpp"
ORBITS = HERE / "e30_six_odd_mask_orbits_result.json"
RESULT = HERE / "e30_profile66_odd_difference_scan_result.json"
REMOTE_SOURCE = "/root/e30_profile66_odd_difference_scan.cpp"
REMOTE_BINARY = "/root/e30_profile66_odd_difference_scan"

app = modal.App("e1-n256-e30-profile66-odd-difference-scan")
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
    if not orbit_packet["complete"]:
        raise RuntimeError("six-odd mask atlas is incomplete")
    tasks = [
        (index, int(row["odd_mask"]), list(row["orbits"][0]))
        for index, row in enumerate(orbit_packet["rows"])
    ]
    if len(tasks) != 1234 or any(len(row["orbits"]) != 1 for row in orbit_packet["rows"]):
        raise RuntimeError("six-odd mask atlas does not have the proved 1,234-by-one shape")
    rows: list[dict[str, object]] = []

    def write_checkpoint(complete: bool) -> dict[str, object]:
        maximum_row = max(rows, key=lambda row: int(row["maximum_m3"])) if rows else None
        histogram: dict[str, int] = {}
        for row in rows:
            for m3, count in row["above_histogram"].items():
                histogram[m3] = histogram.get(m3, 0) + int(count)
        packet = {
            "schema": "e1-e30-profile66-odd-difference-scan-v1",
            "complete": complete,
            "completed_masks": len(rows),
            "expected_masks": len(tasks),
            "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            "orbits_sha256": hashlib.sha256(ORBITS.read_bytes()).hexdigest(),
            "summary": {
                "assignments": sum(int(row["assignments"]) for row in rows),
                "above_threshold": sum(int(row["above_threshold"]) for row in rows),
                "above_histogram": dict(
                    sorted(histogram.items(), key=lambda item: int(item[0]))
                ),
                "exceptional_masks": sum(int(row["above_threshold"]) > 0 for row in rows),
                "maximum_m3": int(maximum_row["maximum_m3"]) if maximum_row else None,
                "threshold": 1087,
                "closes_profile": bool(maximum_row and int(maximum_row["maximum_m3"]) <= 1087),
                "witness": maximum_row if maximum_row else None,
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
        print(f"E30_PROFILE66_ODD_DIFFERENCE_INCOMPLETE completed={len(rows)}/{len(tasks)}")
        raise
    complete = (
        len(rows) == len(tasks)
        and all(bool(row["complete"]) for row in rows)
        and sum(int(row["assignments"]) for row in rows) == 44_779_702_968
    )
    packet = write_checkpoint(complete)
    print("E30_PROFILE66_ODD_DIFFERENCE " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E30_PROFILE66_ODD_DIFFERENCE_COMPLETE {complete}")
    print(f"E30_PROFILE66_ODD_DIFFERENCE_RESULT {RESULT}")
