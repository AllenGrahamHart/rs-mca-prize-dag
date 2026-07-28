#!/usr/bin/env python3
"""Run dual count-only E24 six-profile actual-vector engines on Modal."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
PRIMARY_SOURCE = HERE / "e24_six_profile_count.cpp"
AUDIT_SOURCE = HERE / "e24_six_profile_count_audit.cpp"
PROBE = HERE / "e24_profile_parity_probe_result.json"
RESULT = HERE / "e24_six_profile_count_result.json"
REMOTE_PRIMARY_SOURCE = "/root/e24_six_profile_count.cpp"
REMOTE_AUDIT_SOURCE = "/root/e24_six_profile_count_audit.cpp"
REMOTE_PRIMARY = "/root/e24_six_profile_count"
REMOTE_AUDIT = "/root/e24_six_profile_count_audit"

app = modal.App("e1-n256-e24-six-profile-count")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(PRIMARY_SOURCE, REMOTE_PRIMARY_SOURCE, copy=True)
    .add_local_file(AUDIT_SOURCE, REMOTE_AUDIT_SOURCE, copy=True)
    .run_commands(
        f"g++ -O3 -std=c++17 {REMOTE_PRIMARY_SOURCE} -o {REMOTE_PRIMARY}",
        f"g++ -O3 -std=c++17 {REMOTE_AUDIT_SOURCE} -o {REMOTE_AUDIT}",
    )
)


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=100)
def run_template(template: int, light: list[int]) -> dict[str, object]:
    import subprocess
    import time

    started = time.monotonic()
    command_tail = [str(template), *(str(value) for value in light)]
    primary = subprocess.run(
        [REMOTE_PRIMARY, *command_tail], check=True, capture_output=True,
        text=True, timeout=27,
    )
    audit = subprocess.run(
        [REMOTE_AUDIT, *command_tail], check=True, capture_output=True,
        text=True, timeout=27,
    )
    primary_row = json.loads(primary.stdout)
    audit_row = json.loads(audit.stdout)
    if primary_row != audit_row:
        raise RuntimeError(f"engine disagreement at template {template}")
    return {
        "template": template,
        "primary": primary_row,
        "audit": audit_row,
        "worker_seconds": time.monotonic()-started,
    }


@app.local_entrypoint()
def main() -> None:
    probe = json.loads(PROBE.read_text())
    if not probe["complete"] or int(probe["relevant_affine_templates"]) != 154:
        raise RuntimeError("E24 router is incomplete or changed")
    root = HERE.parents[1]
    e26_path = (
        root
        / "background/nodes/e1_n256_s16_e26_profile_parity_light_reduction/notes"
        / "e26_profile_parity_probe_result.json"
    )
    four_path = (
        root
        / "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes"
        / "e32_four_odd_light_orbit_result.json"
    )
    e26 = json.loads(e26_path.read_text())
    four = json.loads(four_path.read_text())
    tasks = list(e26["light_geometry"]["zero_odd_orbits"]) + [
        row["representative"] for row in four["rows"]
    ]
    if len(tasks) != 154 or not four["complete"]:
        raise RuntimeError("zero/four-odd atlas mismatch")

    rows: list[dict[str, object]] = []

    def vector_sum(key: str) -> list[int]:
        return [
            sum(int(row["primary"][key][index]) for row in rows)
            for index in range(6)
        ]

    def write_checkpoint(complete: bool) -> dict[str, object]:
        profile_counts = vector_sum("profile_counts")
        full_counts = vector_sum("full_conductor_counts")
        packet = {
            "schema": "e1-e24-six-profile-count-v1",
            "complete": complete,
            "completed_templates": len(rows),
            "expected_templates": len(tasks),
            "primary_source_sha256": hashlib.sha256(PRIMARY_SOURCE.read_bytes()).hexdigest(),
            "audit_source_sha256": hashlib.sha256(AUDIT_SOURCE.read_bytes()).hexdigest(),
            "probe_sha256": hashlib.sha256(PROBE.read_bytes()).hexdigest(),
            "e26_atlas_sha256": hashlib.sha256(e26_path.read_bytes()).hexdigest(),
            "four_atlas_sha256": hashlib.sha256(four_path.read_bytes()).hexdigest(),
            "summary": {
                "vectors_per_engine": sum(int(row["primary"]["vectors"]) for row in rows),
                "profile_counts": profile_counts,
                "full_conductor_counts": full_counts,
                "proper_conductor_counts": [
                    profile_counts[index]-full_counts[index] for index in range(6)
                ],
                "worker_seconds_dual": sum(float(row["worker_seconds"]) for row in rows),
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
        print(f"E24_SIX_PROFILE_COUNT_INCOMPLETE completed={len(rows)}/{len(tasks)}")
        raise

    packet = write_checkpoint(
        len(rows) == len(tasks)
        and all(row["primary"] == row["audit"] for row in rows)
        and sum(int(row["primary"]["vectors"]) for row in rows)
        == int(probe["direct_vector_floor"])
    )
    print("E24_SIX_PROFILE_COUNT " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E24_SIX_PROFILE_COUNT_COMPLETE {packet['complete']}")
    print(f"E24_SIX_PROFILE_COUNT_RESULT {RESULT}")
