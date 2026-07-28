#!/usr/bin/env python3
"""Independently audit the E28 census by direct negacyclic products."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e28_eight_profile_joint_census_audit.cpp"
PRODUCTION = HERE / "e28_eight_profile_joint_census_result.json"
RESULT = HERE / "e28_eight_profile_joint_census_audit_result.json"
REMOTE_SOURCE = "/root/e28_eight_profile_joint_census_audit.cpp"
REMOTE_BINARY = "/root/e28_eight_profile_joint_census_audit"

app = modal.App("e1-n256-e28-eight-profile-joint-census-audit")
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
    production = json.loads(PRODUCTION.read_text())
    if not production["complete"]:
        raise RuntimeError("E28 production census is incomplete")
    production_rows = sorted(production["rows"], key=lambda row: int(row["template"]))
    tasks = [row["light"] for row in production_rows]
    if len(tasks) != 154 or int(production["expected_templates"]) != 154:
        raise RuntimeError("E28 production task count mismatch")
    source_sha256 = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    production_sha256 = hashlib.sha256(PRODUCTION.read_bytes()).hexdigest()
    rows: list[dict[str, object]] = []
    if RESULT.exists():
        prior = json.loads(RESULT.read_text())
        if (
            prior.get("schema") == "e1-e28-eight-profile-joint-census-audit-v1"
            and prior.get("source_sha256") == source_sha256
            and prior.get("production_sha256") == production_sha256
        ):
            rows = list(prior["rows"])
    completed = {int(row["template"]) for row in rows}
    remaining = [(index, light) for index, light in enumerate(tasks) if index not in completed]

    def vector_sum(key: str) -> list[int]:
        return [sum(int(row[key][index]) for row in rows) for index in range(8)]

    def vector_max(key: str) -> list[int]:
        return [max((int(row[key][index]) for row in rows), default=-1) for index in range(8)]

    def comparable(row: dict[str, object]) -> dict[str, object]:
        return {key: value for key, value in row.items() if key != "worker_seconds"}

    def mismatches() -> list[int]:
        audits = {int(row["template"]): comparable(row) for row in rows}
        return [
            int(row["template"])
            for row in production_rows
            if audits.get(int(row["template"])) != comparable(row)
        ]

    def write_checkpoint(complete: bool) -> dict[str, object]:
        mismatch_templates = mismatches()
        packet = {
            "schema": "e1-e28-eight-profile-joint-census-audit-v1",
            "complete": complete,
            "agreement": len(rows) == len(tasks) and not mismatch_templates,
            "completed_templates": len(rows),
            "expected_templates": len(tasks),
            "source_sha256": source_sha256,
            "production_sha256": production_sha256,
            "mismatch_templates": mismatch_templates,
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
        for row in run_template.map(
            [item[0] for item in remaining], [item[1] for item in remaining]
        ):
            rows.append(row)
            if len(rows) % 16 == 0:
                write_checkpoint(False)
    except BaseException:
        write_checkpoint(False)
        print(f"E28_EIGHT_PROFILE_JOINT_AUDIT_INCOMPLETE completed={len(rows)}/{len(tasks)}")
        raise
    packet = write_checkpoint(
        len(rows) == len(tasks)
        and all(bool(row["complete"]) for row in rows)
        and not mismatches()
    )
    print("E28_EIGHT_PROFILE_JOINT_AUDIT " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E28_EIGHT_PROFILE_JOINT_AUDIT_AGREEMENT {packet['agreement']}")
    print(f"E28_EIGHT_PROFILE_JOINT_AUDIT_RESULT {RESULT}")
