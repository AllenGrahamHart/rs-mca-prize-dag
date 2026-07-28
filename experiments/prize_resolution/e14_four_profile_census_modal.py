#!/usr/bin/env python3
"""Run dual complete E14 four-profile censuses on Modal."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1] if len(HERE.parents) > 1 else HERE
PRIMARY = HERE / "e14_four_profile_census.cpp"
AUDIT = HERE / "e14_four_profile_census_audit.cpp"
PROBE = HERE / "e14_profile_parity_probe_result.json"
TWO_ATLAS = ROOT / "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_two_six_odd_light_orbit_result.json"
SIX_ATLAS = ROOT / "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_six_odd_mask_orbits_result.json"
RESULT = HERE / "e14_four_profile_census_result.json"
REMOTE_PRIMARY_SOURCE = "/root/e14_four_profile_census.cpp"
REMOTE_AUDIT_SOURCE = "/root/e14_four_profile_census_audit.cpp"
REMOTE_PRIMARY = "/root/e14_four_profile_census"
REMOTE_AUDIT = "/root/e14_four_profile_census_audit"

app = modal.App("e1-n256-e14-four-profile-census")
image = (modal.Image.debian_slim().apt_install("g++")
         .add_local_file(PRIMARY, REMOTE_PRIMARY_SOURCE, copy=True)
         .add_local_file(AUDIT, REMOTE_AUDIT_SOURCE, copy=True)
         .run_commands(
             f"g++ -O3 -std=c++17 {REMOTE_PRIMARY_SOURCE} -o {REMOTE_PRIMARY}",
             f"g++ -O3 -std=c++17 {REMOTE_AUDIT_SOURCE} -o {REMOTE_AUDIT}"))


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=100)
def run_template(template: int, light: list[int]) -> dict[str, object]:
    import json as remote_json
    import subprocess
    import time
    started = time.monotonic()
    tail = [str(template), *(str(value) for value in light)]
    primary = remote_json.loads(subprocess.run(
        [REMOTE_PRIMARY, *tail], check=True, capture_output=True, text=True, timeout=27).stdout)
    audit = remote_json.loads(subprocess.run(
        [REMOTE_AUDIT, *tail], check=True, capture_output=True, text=True, timeout=27).stdout)
    if primary != audit:
        raise RuntimeError(f"engine disagreement at template {template}")
    return {"template": template, "primary": primary, "audit": audit,
            "worker_seconds": time.monotonic() - started}


def atlas_tasks() -> list[list[int]]:
    two = json.loads(TWO_ATLAS.read_text())
    six = json.loads(SIX_ATLAS.read_text())
    if not two["complete"] or not six["complete"]:
        raise RuntimeError("an E14 light atlas is incomplete")
    two_tasks = [row["representative"] for row in two["rows"]]
    six_tasks = [row["orbits"][0] for row in sorted(six["rows"], key=lambda row: int(row["odd_mask"]))]
    if len(two_tasks) != 87 or len(six_tasks) != 1234:
        raise RuntimeError("two/six-odd atlas cardinality mismatch")
    return two_tasks + six_tasks


@app.local_entrypoint()
def main() -> None:
    probe = json.loads(PROBE.read_text())
    tasks = atlas_tasks()
    if (not probe["complete"] or int(probe["relevant_affine_templates"]) != len(tasks)
            or probe["used_odd_counts"] != ["2", "6"]):
        raise RuntimeError("E14 router is incomplete or changed")
    rows: list[dict[str, object]] = []

    def vector_sum(key: str) -> list[int]:
        return [sum(int(row["primary"][key][index]) for row in rows) for index in range(4)]

    def write_checkpoint(complete: bool, error: str | None = None) -> dict[str, object]:
        profile = vector_sum("profile_counts")
        full = vector_sum("full_conductor_counts")
        packet = {
            "schema": "e1-e14-four-profile-census-v1", "complete": complete,
            "completed_templates": len(rows), "expected_templates": len(tasks), "error": error,
            "primary_source_sha256": hashlib.sha256(PRIMARY.read_bytes()).hexdigest(),
            "audit_source_sha256": hashlib.sha256(AUDIT.read_bytes()).hexdigest(),
            "probe_sha256": hashlib.sha256(PROBE.read_bytes()).hexdigest(),
            "two_atlas_sha256": hashlib.sha256(TWO_ATLAS.read_bytes()).hexdigest(),
            "six_atlas_sha256": hashlib.sha256(SIX_ATLAS.read_bytes()).hexdigest(),
            "summary": {
                "vectors_per_engine": sum(int(row["primary"]["vectors"]) for row in rows),
                "profile_counts": profile, "full_conductor_counts": full,
                "proper_conductor_counts": [profile[i] - full[i] for i in range(4)],
                "collected_full_conductor": sum(len(row["primary"]["matches"]) for row in rows),
                "worker_seconds_dual": sum(float(row["worker_seconds"]) for row in rows)},
            "rows": sorted(rows, key=lambda row: int(row["template"]))}
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        return packet

    write_checkpoint(False)
    try:
        for row in run_template.map(range(len(tasks)), tasks):
            if len(row["primary"]["matches"]) != sum(int(value) for value in row["primary"]["full_conductor_counts"]):
                raise RuntimeError(f"match/count mismatch at template {row['template']}")
            rows.append(row)
            if len(rows) % 16 == 0:
                write_checkpoint(False)
    except BaseException as error:
        write_checkpoint(False, f"{type(error).__name__}: {error}")
        print(f"E14_FOUR_PROFILE_CENSUS_INCOMPLETE completed={len(rows)}/{len(tasks)}")
        raise
    packet = write_checkpoint(
        len(rows) == len(tasks) and all(row["primary"] == row["audit"] for row in rows)
        and sum(int(row["primary"]["vectors"]) for row in rows) == int(probe["direct_vector_floor"]))
    print("E14_FOUR_PROFILE_CENSUS " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E14_FOUR_PROFILE_CENSUS_COMPLETE {packet['complete']}")
    print(f"E14_FOUR_PROFILE_CENSUS_RESULT {RESULT}")
