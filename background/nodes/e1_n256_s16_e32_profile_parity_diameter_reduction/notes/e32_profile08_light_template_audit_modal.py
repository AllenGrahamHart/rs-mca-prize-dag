#!/usr/bin/env python3
"""Independently audit the six E32 profile-(0,8) light templates."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e32_profile08_light_template_audit.cpp"
RESULT = HERE / "e32_profile08_light_template_audit_result.json"
REMOTE_SOURCE = "/root/e32_profile08_light_template_audit.cpp"
REMOTE_BINARY = "/root/e32_profile08_light_template_audit"

app = modal.App("e1-n256-e32-profile08-light-template-audit")
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


@app.local_entrypoint()
def main() -> None:
    rows = list(run_template.map(range(6)))
    packet = {
        "schema": "e1-e32-profile08-light-template-audit-v1",
        "complete": all(bool(row["complete"]) for row in rows),
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    print("E32_PROFILE08_LIGHT_TEMPLATE_AUDIT " + json.dumps(rows, sort_keys=True))
    print(f"E32_PROFILE08_LIGHT_TEMPLATE_AUDIT_RESULT {RESULT}")
