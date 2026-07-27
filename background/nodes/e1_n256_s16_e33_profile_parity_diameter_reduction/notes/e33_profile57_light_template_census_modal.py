#!/usr/bin/env python3
"""Exhaust the 100 diameter-Sidon light templates for E33 profile (5,7)."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e33_profile57_light_template_census.cpp"
RESULT = HERE / "e33_profile57_light_template_census_result.json"
REMOTE_SOURCE = "/root/e33_profile57_light_template_census.cpp"
REMOTE_BINARY = "/root/e33_profile57_light_template_census"
TEMPLATES = 100

app = modal.App("e1-n256-e33-profile57-light-template-census")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(SOURCE, REMOTE_SOURCE, copy=True)
    .run_commands(f"g++ -O3 -std=c++17 {REMOTE_SOURCE} -o {REMOTE_BINARY}")
)


@app.function(image=image, cpu=1.0, memory=256, timeout=60)
def run_template(template: int) -> dict[str, object]:
    import subprocess
    import time

    started = time.monotonic()
    completed = subprocess.run(
        [REMOTE_BINARY, str(template)],
        check=True,
        capture_output=True,
        text=True,
        timeout=55,
    )
    result = json.loads(completed.stdout)
    result["worker_seconds"] = time.monotonic() - started
    return result


def write_checkpoint(rows: list[dict[str, object]], errors: list[dict[str, object]]) -> None:
    packet = {
        "schema": "e1-e33-profile57-light-template-v1",
        "complete": len(rows) == TEMPLATES and not errors,
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "expected_templates": TEMPLATES,
        "returned_templates": sorted(int(row["template"]) for row in rows),
        "errors": errors,
        "rows": sorted(rows, key=lambda row: int(row["template"])),
    }
    RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main() -> None:
    rows: list[dict[str, object]] = []
    errors: list[dict[str, object]] = []
    returned = run_template.map(range(TEMPLATES), return_exceptions=True)
    for template, result in enumerate(returned):
        if isinstance(result, BaseException):
            errors.append({"template": template, "error": repr(result)})
        else:
            rows.append(result)
        write_checkpoint(rows, errors)

    maximum = max((int(row["maximum_m3"]) for row in rows), default=-1)
    summary = {
        "complete": len(rows) == TEMPLATES and not errors,
        "returned": len(rows),
        "errors": len(errors),
        "supports": sum(int(row["supports"]) for row in rows),
        "vectors": sum(int(row["vectors"]) for row in rows),
        "profile_57": sum(int(row["profile_57"]) for row in rows),
        "full_conductor": sum(int(row["full_conductor"]) for row in rows),
        "maximum_m3": maximum,
        "maximum_full_conductor_m3": max(
            (int(row["maximum_full_conductor_m3"]) for row in rows), default=-1
        ),
        "worker_seconds": sum(float(row["worker_seconds"]) for row in rows),
    }
    print("E33_PROFILE57_LIGHT_TEMPLATE_CENSUS " + json.dumps(summary, sort_keys=True))
    print(f"E33_PROFILE57_LIGHT_TEMPLATE_RESULT {RESULT}")
