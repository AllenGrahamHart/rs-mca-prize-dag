#!/usr/bin/env python3
"""Run dual complete E16 four-profile censuses on Modal."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1] if len(HERE.parents) > 1 else HERE
PRIMARY = HERE / "e16_four_profile_census.cpp"
AUDIT = HERE / "e16_four_profile_census_audit.cpp"
PROBE = HERE / "e16_profile_parity_probe_result.json"
ATLAS = (
    ROOT
    / "background/nodes/e1_n256_s16_e26_profile_parity_light_reduction/notes"
    / "e26_profile_parity_probe_result.json"
)
FOUR_ATLAS = (
    ROOT
    / "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes"
    / "e32_four_odd_light_orbit_result.json"
)
RESULT = HERE / "e16_four_profile_census_result.json"
REMOTE_PRIMARY_SOURCE = "/root/e16_four_profile_census.cpp"
REMOTE_AUDIT_SOURCE = "/root/e16_four_profile_census_audit.cpp"
REMOTE_PRIMARY = "/root/e16_four_profile_census"
REMOTE_AUDIT = "/root/e16_four_profile_census_audit"

app = modal.App("e1-n256-e16-four-profile-census")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(PRIMARY, REMOTE_PRIMARY_SOURCE, copy=True)
    .add_local_file(AUDIT, REMOTE_AUDIT_SOURCE, copy=True)
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
        raise RuntimeError(f"engine disagreement at template {template}")
    return {
        "template": template,
        "primary": primary,
        "audit": audit,
        "worker_seconds": time.monotonic() - started,
    }


@app.local_entrypoint()
def main() -> None:
    probe = json.loads(PROBE.read_text())
    atlas = json.loads(ATLAS.read_text())
    four = json.loads(FOUR_ATLAS.read_text())
    tasks = list(atlas["light_geometry"]["zero_odd_orbits"]) + [
        row["representative"] for row in four["rows"]
    ]
    if (
        not probe["complete"]
        or not atlas["complete"]
        or not four["complete"]
        or len(tasks) != 154
        or int(probe["relevant_affine_templates"]) != len(tasks)
    ):
        raise RuntimeError("E16 router or even-parity atlas mismatch")

    rows: list[dict[str, object]] = []

    def vector_sum(key: str) -> list[int]:
        return [sum(int(row["primary"][key][i]) for row in rows) for i in range(4)]

    def write_checkpoint(complete: bool, error: str | None = None) -> dict[str, object]:
        profile_counts = vector_sum("profile_counts")
        full_counts = vector_sum("full_conductor_counts")
        packet = {
            "schema": "e1-e16-four-profile-census-v1",
            "complete": complete,
            "completed_templates": len(rows),
            "expected_templates": len(tasks),
            "error": error,
            "primary_source_sha256": hashlib.sha256(PRIMARY.read_bytes()).hexdigest(),
            "audit_source_sha256": hashlib.sha256(AUDIT.read_bytes()).hexdigest(),
            "probe_sha256": hashlib.sha256(PROBE.read_bytes()).hexdigest(),
            "atlas_sha256": hashlib.sha256(ATLAS.read_bytes()).hexdigest(),
            "four_atlas_sha256": hashlib.sha256(FOUR_ATLAS.read_bytes()).hexdigest(),
            "summary": {
                "vectors_per_engine": sum(int(row["primary"]["vectors"]) for row in rows),
                "profile_counts": profile_counts,
                "full_conductor_counts": full_counts,
                "proper_conductor_counts": [
                    profile_counts[index] - full_counts[index] for index in range(4)
                ],
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
            rows.append(row)
            if len(rows) % 16 == 0:
                write_checkpoint(False)
    except BaseException as error:
        write_checkpoint(False, f"{type(error).__name__}: {error}")
        print(f"E16_FOUR_PROFILE_CENSUS_INCOMPLETE completed={len(rows)}/{len(tasks)}")
        raise
    packet = write_checkpoint(
        len(rows) == len(tasks)
        and all(row["primary"] == row["audit"] for row in rows)
        and sum(int(row["primary"]["vectors"]) for row in rows)
        == int(probe["direct_vector_floor"])
    )
    print("E16_FOUR_PROFILE_CENSUS " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E16_FOUR_PROFILE_CENSUS_COMPLETE {packet['complete']}")
    print(f"E16_FOUR_PROFILE_CENSUS_RESULT {RESULT}")
