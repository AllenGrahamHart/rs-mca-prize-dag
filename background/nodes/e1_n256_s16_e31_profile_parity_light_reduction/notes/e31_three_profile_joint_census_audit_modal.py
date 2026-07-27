#!/usr/bin/env python3
"""Independently audit the E31 joint census by direct negacyclic products."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e31_three_profile_joint_census_audit.cpp"
ORBITS = HERE.parent.parent / "e1_n256_s16_sparse_l1_variance_exclusion/notes/e31_three_odd_light_orbit_result.json"
PRODUCTION = HERE / "e31_three_profile_joint_census_result.json"
RESULT = HERE / "e31_three_profile_joint_census_audit_result.json"
REMOTE_SOURCE = "/root/e31_three_profile_joint_census_audit.cpp"
REMOTE_BINARY = "/root/e31_three_profile_joint_census_audit"

app = modal.App("e1-n256-e31-three-profile-joint-census-audit")
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
    production = json.loads(PRODUCTION.read_text())
    rows: list[dict[str, object]] = []

    def write_checkpoint(complete: bool) -> tuple[dict[str, dict[str, int]], bool]:
        summary = {}
        if rows:
            for profile in ("profile_37", "profile_251", "profile_132"):
                summary[profile] = {
                    "count": sum(int(row[profile]["count"]) for row in rows),
                    "full_conductor": sum(int(row[profile]["full_conductor"]) for row in rows),
                    "maximum_m3": max(int(row[profile]["maximum_m3"]) for row in rows),
                    "maximum_full_conductor_m3": max(
                        int(row[profile]["maximum_full_conductor_m3"]) for row in rows
                    ),
                }
        agreement = complete and production["summary"] == summary
        packet = {
            "schema": "e1-e31-three-profile-joint-census-audit-v1",
            "complete": complete,
            "agreement": agreement,
            "completed_templates": len(rows),
            "expected_templates": len(representatives),
            "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            "orbits_sha256": hashlib.sha256(ORBITS.read_bytes()).hexdigest(),
            "production_sha256": hashlib.sha256(PRODUCTION.read_bytes()).hexdigest(),
            "summary": summary,
            "rows": rows,
        }
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        return summary, agreement

    write_checkpoint(False)
    try:
        for row in run_template.map(range(len(representatives)), representatives):
            rows.append(row)
            write_checkpoint(False)
    except BaseException:
        print(f"E31_THREE_PROFILE_JOINT_AUDIT_INCOMPLETE completed={len(rows)}/8 result={RESULT}")
        raise
    complete = len(rows) == 8 and all(bool(row["complete"]) for row in rows)
    summary, agreement = write_checkpoint(complete)
    print("E31_THREE_PROFILE_JOINT_CENSUS_AUDIT " + json.dumps(summary, sort_keys=True))
    print(f"E31_THREE_PROFILE_JOINT_AUDIT_COMPLETE {complete}")
    print(f"E31_THREE_PROFILE_JOINT_AGREEMENT {agreement}")
    print(f"E31_THREE_PROFILE_JOINT_AUDIT_RESULT {RESULT}")
