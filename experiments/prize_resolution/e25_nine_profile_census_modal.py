#!/usr/bin/env python3
"""Complete dual actual-vector census for the nine E25 profiles."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1] if len(HERE.parents) > 1 else HERE
PRODUCTION_SOURCE = HERE / "e25_nine_profile_census.cpp"
AUDIT_SOURCE = HERE / "e25_nine_profile_census_audit.cpp"
REDUCTION = HERE / "e25_profile_parity_probe_result.json"
ATLAS = (
    ROOT
    / "background/nodes/e1_n256_s16_e27_profile_parity_light_reduction/notes"
    / "e27_profile_parity_probe_result.json"
)
RESULT = HERE / "e25_nine_profile_census_result.json"
REMOTE_PRODUCTION_SOURCE = "/root/e25_nine_profile_census.cpp"
REMOTE_AUDIT_SOURCE = "/root/e25_nine_profile_census_audit.cpp"
REMOTE_PRODUCTION = "/root/e25_nine_profile_census"
REMOTE_AUDIT = "/root/e25_nine_profile_census_audit"

app = modal.App("e1-e25-nine-profile-census")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(PRODUCTION_SOURCE, REMOTE_PRODUCTION_SOURCE, copy=True)
    .add_local_file(AUDIT_SOURCE, REMOTE_AUDIT_SOURCE, copy=True)
    .run_commands(
        f"g++ -O3 -std=c++20 {REMOTE_PRODUCTION_SOURCE} -o {REMOTE_PRODUCTION}",
        f"g++ -O3 -std=c++20 {REMOTE_AUDIT_SOURCE} -o {REMOTE_AUDIT}",
    )
)


def _run(binary: str, task: tuple[int, list[int]]) -> dict[str, object]:
    import subprocess
    import time

    template, light = task
    started = time.monotonic()
    completed = subprocess.run(
        [binary, str(template), *(str(value) for value in light)],
        capture_output=True,
        check=True,
        text=True,
        timeout=55,
    )
    row = json.loads(completed.stdout)
    row["worker_seconds"] = time.monotonic() - started
    return row


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=100)
def run_production(task: tuple[int, list[int]]) -> dict[str, object]:
    return _run(REMOTE_PRODUCTION, task)


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=100)
def run_audit(task: tuple[int, list[int]]) -> dict[str, object]:
    return _run(REMOTE_AUDIT, task)


def summary(rows: list[dict[str, object]]) -> dict[str, object]:
    def extrema(key: str, profile: int, minimum: bool) -> int:
        values = [int(row[key][profile]) for row in rows if int(row[key][profile]) >= 0]
        if not values:
            return -1
        return min(values) if minimum else max(values)

    return {
        "vectors": sum(int(row["vectors"]) for row in rows),
        "profile_counts": [
            sum(int(row["profile_counts"][profile]) for row in rows)
            for profile in range(9)
        ],
        "above_cutoff": [
            sum(int(row["above_cutoff"][profile]) for row in rows)
            for profile in range(9)
        ],
        "full_above_cutoff": [
            sum(int(row["full_above_cutoff"][profile]) for row in rows)
            for profile in range(9)
        ],
        "minimum_m3": [extrema("minimum_m3", profile, True) for profile in range(9)],
        "minimum_full_m3": [
            extrema("minimum_full_m3", profile, True) for profile in range(9)
        ],
        "maximum_m3": [extrema("maximum_m3", profile, False) for profile in range(9)],
        "maximum_full_m3": [
            extrema("maximum_full_m3", profile, False) for profile in range(9)
        ],
        "worker_seconds": sum(float(row["worker_seconds"]) for row in rows),
    }


def strip_runtime(row: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in row.items() if key != "worker_seconds"}


@app.local_entrypoint()
def main() -> None:
    reduction = json.loads(REDUCTION.read_text())
    atlas = json.loads(ATLAS.read_text())
    assert reduction["complete"] is atlas["complete"] is True
    assert reduction["relevant_affine_templates"] == 111
    representatives = atlas["light_geometry"]["orbit_representatives"]
    lights = [
        [int(value) for value in row]
        for odd in ("1", "5")
        for row in representatives[odd]
    ]
    tasks = list(enumerate(lights))
    assert len(tasks) == 111
    production: list[dict[str, object]] = []
    audit: list[dict[str, object]] = []

    def write_checkpoint(complete: bool, error: str | None = None) -> dict[str, object]:
        first = {int(row["template"]): row for row in production}
        second = {int(row["template"]): row for row in audit}
        compared = sorted(set(first) & set(second))
        mismatches = [
            template
            for template in compared
            if strip_runtime(first[template]) != strip_runtime(second[template])
        ]
        packet = {
            "schema": "e1-e25-nine-profile-census-v1",
            "complete": complete,
            "agreement": complete and not mismatches,
            "completed_production": len(production),
            "completed_audit": len(audit),
            "expected_each": len(tasks),
            "mismatch_templates": mismatches,
            "source_sha256": hashlib.sha256(PRODUCTION_SOURCE.read_bytes()).hexdigest(),
            "audit_source_sha256": hashlib.sha256(AUDIT_SOURCE.read_bytes()).hexdigest(),
            "driver_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "reduction_sha256": hashlib.sha256(REDUCTION.read_bytes()).hexdigest(),
            "atlas_sha256": hashlib.sha256(ATLAS.read_bytes()).hexdigest(),
            "error": error,
            "production_summary": summary(production),
            "audit_summary": summary(audit),
            "production": sorted(production, key=lambda row: int(row["template"])),
            "audit": sorted(audit, key=lambda row: int(row["template"])),
        }
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        return packet

    write_checkpoint(False)
    try:
        for row in run_production.map(tasks):
            assert len(row["matches"]) == sum(int(value) for value in row["above_cutoff"])
            production.append(row)
            if len(production) % 16 == 0:
                write_checkpoint(False)
        for row in run_audit.map(tasks):
            assert len(row["matches"]) == sum(int(value) for value in row["above_cutoff"])
            audit.append(row)
            if len(audit) % 16 == 0:
                write_checkpoint(False)
    except BaseException as error:
        write_checkpoint(False, f"{type(error).__name__}: {error}")
        print(
            "E25_NINE_PROFILE_CENSUS_INCOMPLETE "
            f"production={len(production)}/{len(tasks)} audit={len(audit)}/{len(tasks)}"
        )
        raise
    packet = write_checkpoint(
        len(production) == len(audit) == len(tasks)
        and all(bool(row["complete"]) for row in production + audit)
    )
    print("E25_NINE_PROFILE_CENSUS " + json.dumps(packet["production_summary"], sort_keys=True))
    print(f"E25_NINE_PROFILE_CENSUS_AGREEMENT {packet['agreement']}")
