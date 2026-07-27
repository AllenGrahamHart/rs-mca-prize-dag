#!/usr/bin/env python3
"""Pilot the six actual light templates for the E33 profile (1,8)."""

from __future__ import annotations

import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e33_profile18_light_template_census.cpp"
REMOTE_SOURCE = "/root/e33_profile18_light_template_census.cpp"
REMOTE_BINARY = "/root/e33_profile18_light_template_census"
PILOT_SHARDS = 128

app = modal.App("e1-n256-e33-profile18-light-template-pilot")
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
        [REMOTE_BINARY, str(template), "0", str(PILOT_SHARDS)],
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
    results = list(run_template.map(range(6)))
    print("E33_PROFILE18_LIGHT_TEMPLATE_PILOT " + json.dumps(results, sort_keys=True))
