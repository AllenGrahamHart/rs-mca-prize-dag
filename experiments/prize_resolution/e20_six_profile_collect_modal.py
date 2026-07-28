#!/usr/bin/env python3
"""Collect the full-conductor E20 residue with two exact Modal engines."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1] if len(HERE.parents) > 1 else HERE
PRIMARY_SOURCE = HERE / "e20_six_profile_collect.cpp"
AUDIT_SOURCE = HERE / "e20_six_profile_collect_audit.cpp"
PROBE = HERE / "e20_profile_parity_probe_result.json"
COUNT = HERE / "e20_six_profile_count_result.json"
E26_ATLAS = (
    ROOT
    / "background/nodes/e1_n256_s16_e26_profile_parity_light_reduction/notes"
    / "e26_profile_parity_probe_result.json"
)
FOUR_ATLAS = (
    ROOT
    / "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes"
    / "e32_four_odd_light_orbit_result.json"
)
RESULT = HERE / "e20_six_profile_collect_result.json"
REMOTE_PRIMARY_SOURCE = "/root/e20_six_profile_collect.cpp"
REMOTE_AUDIT_SOURCE = "/root/e20_six_profile_collect_audit.cpp"
REMOTE_PRIMARY = "/root/e20_six_profile_collect"
REMOTE_AUDIT = "/root/e20_six_profile_collect_audit"

app = modal.App("e1-n256-e20-six-profile-collect")
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
    tail = [str(template), *(str(value) for value in light)]
    primary = json.loads(
        subprocess.run(
            [REMOTE_PRIMARY, *tail], check=True, capture_output=True, text=True, timeout=27
        ).stdout
    )
    audit = json.loads(
        subprocess.run(
            [REMOTE_AUDIT, *tail], check=True, capture_output=True, text=True, timeout=27
        ).stdout
    )
    if primary != audit:
        raise RuntimeError(f"collector disagreement at template {template}")
    return {
        "template": template,
        "primary": primary,
        "audit": audit,
        "worker_seconds": time.monotonic() - started,
    }


def atlas_tasks() -> list[list[int]]:
    e26 = json.loads(E26_ATLAS.read_text())
    four = json.loads(FOUR_ATLAS.read_text())
    tasks = list(e26["light_geometry"]["zero_odd_orbits"]) + [
        row["representative"] for row in four["rows"]
    ]
    if not e26["complete"] or not four["complete"] or len(tasks) != 154:
        raise RuntimeError("zero/four-odd atlas mismatch")
    return tasks


@app.local_entrypoint()
def main() -> None:
    probe = json.loads(PROBE.read_text())
    count = json.loads(COUNT.read_text())
    tasks = atlas_tasks()
    if not probe["complete"] or not count["complete"]:
        raise RuntimeError("E20 router or count packet is incomplete")

    rows: list[dict[str, object]] = []

    def vector_sum(key: str) -> list[int]:
        return [sum(int(row["primary"][key][i]) for row in rows) for i in range(6)]

    def write_checkpoint(complete: bool, error: str | None = None) -> dict[str, object]:
        packet = {
            "schema": "e1-e20-six-profile-collect-v1",
            "complete": complete,
            "completed_templates": len(rows),
            "expected_templates": len(tasks),
            "primary_source_sha256": hashlib.sha256(PRIMARY_SOURCE.read_bytes()).hexdigest(),
            "audit_source_sha256": hashlib.sha256(AUDIT_SOURCE.read_bytes()).hexdigest(),
            "probe_sha256": hashlib.sha256(PROBE.read_bytes()).hexdigest(),
            "count_sha256": hashlib.sha256(COUNT.read_bytes()).hexdigest(),
            "e26_atlas_sha256": hashlib.sha256(E26_ATLAS.read_bytes()).hexdigest(),
            "four_atlas_sha256": hashlib.sha256(FOUR_ATLAS.read_bytes()).hexdigest(),
            "error": error,
            "summary": {
                "vectors_per_engine": sum(int(row["primary"]["vectors"]) for row in rows),
                "profile_counts": vector_sum("profile_counts"),
                "full_conductor_counts": vector_sum("full_conductor_counts"),
                "hash_sums": vector_sum("hash_sums"),
                "hash_xors": vector_sum("hash_xors"),
                "collected_full_conductor": sum(
                    len(row["primary"]["matches"]) for row in rows
                ),
                "worker_seconds_dual": sum(float(row["worker_seconds"]) for row in rows),
            },
            "rows": sorted(rows, key=lambda row: int(row["template"])),
        }
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        return packet

    write_checkpoint(False)
    try:
        for row in run_template.map(range(len(tasks)), tasks):
            if len(row["primary"]["matches"]) != sum(
                int(value) for value in row["primary"]["full_conductor_counts"]
            ):
                raise RuntimeError(f"match/count mismatch at template {row['template']}")
            rows.append(row)
            if len(rows) % 16 == 0:
                write_checkpoint(False)
    except BaseException as error:
        write_checkpoint(False, f"{type(error).__name__}: {error}")
        print(f"E20_SIX_PROFILE_COLLECT_INCOMPLETE completed={len(rows)}/{len(tasks)}")
        raise

    count_summary = count["summary"]
    packet = write_checkpoint(
        len(rows) == len(tasks)
        and all(row["primary"] == row["audit"] for row in rows)
        and vector_sum("profile_counts") == count_summary["profile_counts"]
        and vector_sum("full_conductor_counts") == count_summary["full_conductor_counts"]
        and vector_sum("hash_sums") == count_summary["hash_sums"]
        and vector_sum("hash_xors") == count_summary["hash_xors"]
    )
    print("E20_SIX_PROFILE_COLLECT " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E20_SIX_PROFILE_COLLECT_COMPLETE {packet['complete']}")
    print(f"E20_SIX_PROFILE_COLLECT_RESULT {RESULT}")
