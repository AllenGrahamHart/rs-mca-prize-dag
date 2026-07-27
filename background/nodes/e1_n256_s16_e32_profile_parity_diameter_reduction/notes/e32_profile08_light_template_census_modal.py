#!/usr/bin/env python3
"""Exhaust the six actual light templates for the E32 profile (0,8)."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e32_profile08_light_template_census.cpp"
RESULT = HERE / "e32_profile08_light_template_census_result.json"
REMOTE_SOURCE = "/root/e32_profile08_light_template_census.cpp"
REMOTE_BINARY = "/root/e32_profile08_light_template_census"
SHARDS = 8

app = modal.App("e1-n256-e32-profile08-light-template-census")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(SOURCE, REMOTE_SOURCE, copy=True)
    .run_commands(f"g++ -O3 -std=c++17 {REMOTE_SOURCE} -o {REMOTE_BINARY}")
)


@app.function(image=image, cpu=1.0, memory=256, timeout=60)
def run_cell(template: int, shard: int) -> dict[str, object]:
    import subprocess
    import time

    started = time.monotonic()
    completed = subprocess.run(
        [REMOTE_BINARY, str(template), str(shard), str(SHARDS)],
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
    templates = [template for template in range(6) for _ in range(SHARDS)]
    shards = list(range(SHARDS)) * 6
    rows = list(run_cell.map(templates, shards))
    summary = {
        template: {
            "supports": sum(int(row["supports"]) for row in rows if row["template"] == template),
            "vectors": sum(int(row["vectors"]) for row in rows if row["template"] == template),
            "profile_08": sum(
                int(row["profile_08"]) for row in rows if row["template"] == template
            ),
            "full_conductor": sum(
                int(row["full_conductor"]) for row in rows if row["template"] == template
            ),
            "maximum_m3": max(
                int(row["maximum_m3"]) for row in rows if row["template"] == template
            ),
            "maximum_full_conductor_m3": max(
                int(row["maximum_full_conductor_m3"])
                for row in rows
                if row["template"] == template
            ),
        }
        for template in range(6)
    }
    packet = {
        "schema": "e1-e32-profile08-light-template-v1",
        "complete": all(bool(row["complete"]) for row in rows),
        "shards": SHARDS,
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "summary": summary,
        "rows": rows,
    }
    RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    print("E32_PROFILE08_LIGHT_TEMPLATE_CENSUS " + json.dumps(summary, sort_keys=True))
    print(f"E32_PROFILE08_LIGHT_TEMPLATE_RESULT {RESULT}")
