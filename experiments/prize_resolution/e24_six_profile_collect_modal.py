#!/usr/bin/env python3
"""Collect the full-conductor E24 residue with two exact Modal engines."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
PRIMARY_SOURCE = HERE / "e24_six_profile_collect.cpp"
AUDIT_SOURCE = HERE / "e24_six_profile_collect_audit.cpp"
PROBE = HERE / "e24_profile_parity_probe_result.json"
COUNT = HERE / "e24_six_profile_count_result.json"
RESULT = HERE / "e24_six_profile_collect_result.json"
REMOTE_PRIMARY_SOURCE = "/root/e24_six_profile_collect.cpp"
REMOTE_AUDIT_SOURCE = "/root/e24_six_profile_collect_audit.cpp"
REMOTE_PRIMARY = "/root/e24_six_profile_collect"
REMOTE_AUDIT = "/root/e24_six_profile_collect_audit"

app = modal.App("e1-n256-e24-six-profile-collect")
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
    import json as remote_json
    import subprocess
    import time

    started = time.monotonic()
    tail = [str(template), *(str(value) for value in light)]
    primary = remote_json.loads(subprocess.run(
        [REMOTE_PRIMARY, *tail], check=True, capture_output=True, text=True,
        timeout=27,
    ).stdout)
    audit = remote_json.loads(subprocess.run(
        [REMOTE_AUDIT, *tail], check=True, capture_output=True, text=True,
        timeout=27,
    ).stdout)
    if primary != audit:
        raise RuntimeError(f"collector disagreement at template {template}")
    return {
        "template": template,
        "primary": primary,
        "audit": audit,
        "worker_seconds": time.monotonic()-started,
    }


@app.local_entrypoint()
def main() -> None:
    probe = json.loads(PROBE.read_text())
    count = json.loads(COUNT.read_text())
    if not probe["complete"] or not count["complete"]:
        raise RuntimeError("E24 router or count packet is incomplete")
    root = HERE.parents[1]
    e26_path = root / "background/nodes/e1_n256_s16_e26_profile_parity_light_reduction/notes/e26_profile_parity_probe_result.json"
    four_path = root / "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_four_odd_light_orbit_result.json"
    e26 = json.loads(e26_path.read_text())
    four = json.loads(four_path.read_text())
    tasks = list(e26["light_geometry"]["zero_odd_orbits"]) + [
        row["representative"] for row in four["rows"]
    ]
    if len(tasks) != 154:
        raise RuntimeError("zero/four-odd atlas mismatch")

    rows: list[dict[str, object]] = []

    def vector_sum(key: str) -> list[int]:
        return [sum(int(row["primary"][key][i]) for row in rows) for i in range(6)]

    def write_checkpoint(complete: bool) -> dict[str, object]:
        packet = {
            "schema": "e1-e24-six-profile-collect-v1",
            "complete": complete,
            "completed_templates": len(rows),
            "expected_templates": len(tasks),
            "primary_source_sha256": hashlib.sha256(PRIMARY_SOURCE.read_bytes()).hexdigest(),
            "audit_source_sha256": hashlib.sha256(AUDIT_SOURCE.read_bytes()).hexdigest(),
            "probe_sha256": hashlib.sha256(PROBE.read_bytes()).hexdigest(),
            "count_sha256": hashlib.sha256(COUNT.read_bytes()).hexdigest(),
            "e26_atlas_sha256": hashlib.sha256(e26_path.read_bytes()).hexdigest(),
            "four_atlas_sha256": hashlib.sha256(four_path.read_bytes()).hexdigest(),
            "summary": {
                "vectors_per_engine": sum(int(row["primary"]["vectors"]) for row in rows),
                "profile_counts": vector_sum("profile_counts"),
                "full_conductor_counts": vector_sum("full_conductor_counts"),
                "collected_full_conductor": sum(len(row["primary"]["matches"]) for row in rows),
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
        print(f"E24_SIX_PROFILE_COLLECT_INCOMPLETE completed={len(rows)}/{len(tasks)}")
        raise
    packet = write_checkpoint(
        len(rows) == 154
        and all(row["primary"] == row["audit"] for row in rows)
        and vector_sum("profile_counts") == count["summary"]["profile_counts"]
        and vector_sum("full_conductor_counts") == count["summary"]["full_conductor_counts"]
    )
    print("E24_SIX_PROFILE_COLLECT " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E24_SIX_PROFILE_COLLECT_COMPLETE {packet['complete']}")
    print(f"E24_SIX_PROFILE_COLLECT_RESULT {RESULT}")
