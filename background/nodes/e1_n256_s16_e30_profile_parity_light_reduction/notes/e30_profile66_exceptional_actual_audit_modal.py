#!/usr/bin/env python3
"""Independently census actual profile-(6,6) vectors by negacyclic product."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e30_profile66_exceptional_actual_audit.cpp"
RELAXATION = HERE / "e30_profile66_odd_difference_scan_result.json"
PRODUCTION = HERE / "e30_profile66_exceptional_actual_result.json"
RESULT = HERE / "e30_profile66_exceptional_actual_audit_result.json"
REMOTE_SOURCE = "/root/e30_profile66_exceptional_actual_audit.cpp"
REMOTE_BINARY = "/root/e30_profile66_exceptional_actual_audit"

app = modal.App("e1-n256-e30-profile66-exceptional-actual-audit")
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
    production = json.loads(PRODUCTION.read_text())
    if not relaxation["complete"] or not production["complete"]:
        raise RuntimeError("profile-(6,6) production inputs are incomplete")
    tasks = [row["light"] for row in relaxation["rows"] if int(row["above_threshold"]) > 0]
    if len(tasks) != int(production["expected_templates"]):
        raise RuntimeError("exceptional-mask task count mismatch")
    source_sha256 = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    production_sha256 = hashlib.sha256(PRODUCTION.read_bytes()).hexdigest()
    relaxation_sha256 = hashlib.sha256(RELAXATION.read_bytes()).hexdigest()
    rows: list[dict[str, object]] = []
    if RESULT.exists():
        prior = json.loads(RESULT.read_text())
        if (
            prior.get("schema") == "e1-e30-profile66-exceptional-actual-audit-v1"
            and prior.get("source_sha256") == source_sha256
            and prior.get("production_sha256") == production_sha256
            and prior.get("relaxation_sha256") == relaxation_sha256
        ):
            rows = list(prior["rows"])
    completed = {int(row["template"]) for row in rows}
    remaining = [(index, light) for index, light in enumerate(tasks) if index not in completed]

    def write_checkpoint(complete: bool) -> dict[str, object]:
        packet = {
            "schema": "e1-e30-profile66-exceptional-actual-audit-v1",
            "complete": complete,
            "completed_templates": len(rows),
            "expected_templates": len(tasks),
            "source_sha256": source_sha256,
            "relaxation_sha256": relaxation_sha256,
            "production_sha256": production_sha256,
            "summary": {
                "vectors": sum(int(row["vectors"]) for row in rows),
                "profile_count": sum(int(row["profile_count"]) for row in rows),
                "above_cutoff": sum(int(row["above_cutoff"]) for row in rows),
                "full_above_cutoff": sum(int(row["full_above_cutoff"]) for row in rows),
                "maximum_m3": max((int(row["maximum_m3"]) for row in rows), default=None),
                "maximum_full_m3": max(
                    (int(row["maximum_full_m3"]) for row in rows), default=None
                ),
                "worker_seconds": sum(float(row["worker_seconds"]) for row in rows),
            },
            "rows": sorted(rows, key=lambda row: int(row["template"])),
        }
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        return packet

    write_checkpoint(False)
    try:
        for row in run_template.map(
            [item[0] for item in remaining], [item[1] for item in remaining]
        ):
            rows.append(row)
            if len(rows) % 16 == 0:
                write_checkpoint(False)
    except BaseException:
        write_checkpoint(False)
        print(f"E30_PROFILE66_EXCEPTIONAL_ACTUAL_AUDIT_INCOMPLETE completed={len(rows)}/{len(tasks)}")
        raise
    packet = write_checkpoint(
        len(rows) == len(tasks) and all(bool(row["complete"]) for row in rows)
    )
    print("E30_PROFILE66_EXCEPTIONAL_ACTUAL_AUDIT " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E30_PROFILE66_EXCEPTIONAL_ACTUAL_AUDIT_COMPLETE {packet['complete']}")
    print(f"E30_PROFILE66_EXCEPTIONAL_ACTUAL_AUDIT_RESULT {RESULT}")
