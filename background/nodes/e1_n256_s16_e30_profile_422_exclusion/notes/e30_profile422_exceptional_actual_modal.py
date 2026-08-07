#!/usr/bin/env python3
"""Census actual vectors above the profile-(4,2,2) structured cutoff."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
PRODUCTION_SOURCE = HERE / "e30_profile422_exceptional_actual_census.cpp"
AUDIT_SOURCE = HERE / "e30_profile422_exceptional_actual_audit.cpp"
RELAXATION = HERE / "e30_profile422_odd_difference_relaxation_result.json"
RESULT = HERE / "e30_profile422_exceptional_actual_result.json"
REMOTE_PRODUCTION_SOURCE = "/root/e30_profile422_exceptional_actual_census.cpp"
REMOTE_AUDIT_SOURCE = "/root/e30_profile422_exceptional_actual_audit.cpp"
REMOTE_PRODUCTION = "/root/e30_profile422_exceptional_actual_census"
REMOTE_AUDIT = "/root/e30_profile422_exceptional_actual_audit"
TEMPLATES = 3

app = modal.App("e1-n256-e30-profile422-exceptional-actual")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(PRODUCTION_SOURCE, REMOTE_PRODUCTION_SOURCE, copy=True)
    .add_local_file(AUDIT_SOURCE, REMOTE_AUDIT_SOURCE, copy=True)
    .run_commands(
        f"g++ -O3 -std=c++17 {REMOTE_PRODUCTION_SOURCE} -o {REMOTE_PRODUCTION}",
        f"g++ -O3 -std=c++17 {REMOTE_AUDIT_SOURCE} -o {REMOTE_AUDIT}",
    )
)


def _run(binary: str, template: int) -> dict[str, object]:
    import subprocess
    import time

    started = time.monotonic()
    completed = subprocess.run(
        [binary, str(template)],
        check=True,
        capture_output=True,
        text=True,
        timeout=55,
    )
    row = json.loads(completed.stdout)
    row["worker_seconds"] = time.monotonic() - started
    return row


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=3)
def run_production(template: int) -> dict[str, object]:
    return _run(REMOTE_PRODUCTION, template)


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=3)
def run_audit(template: int) -> dict[str, object]:
    return _run(REMOTE_AUDIT, template)


@app.local_entrypoint()
def main() -> None:
    production: list[dict[str, object]] = []
    audit: list[dict[str, object]] = []

    def write_checkpoint(complete: bool) -> dict[str, object]:
        first = {int(row["template"]): row for row in production}
        second = {int(row["template"]): row for row in audit}
        agreement = len(first) == len(second) == TEMPLATES
        if agreement:
            for template in range(TEMPLATES):
                for key in (
                    "light",
                    "supports",
                    "vectors",
                    "count",
                    "full_conductor",
                    "witness",
                    "matches",
                ):
                    if first[template][key] != second[template][key]:
                        agreement = False
        packet = {
            "schema": "e1-e30-profile422-exceptional-actual-v1",
            "complete": complete,
            "agreement": agreement,
            "completed_production": len(production),
            "completed_audit": len(audit),
            "expected_each": TEMPLATES,
            "production_source_sha256": hashlib.sha256(PRODUCTION_SOURCE.read_bytes()).hexdigest(),
            "audit_source_sha256": hashlib.sha256(AUDIT_SOURCE.read_bytes()).hexdigest(),
            "relaxation_sha256": hashlib.sha256(RELAXATION.read_bytes()).hexdigest(),
            "summary": {
                "vectors_per_engine": sum(int(row["vectors"]) for row in production),
                "count": sum(int(row["count"]) for row in production),
                "full_conductor": sum(int(row["full_conductor"]) for row in production),
                "production_worker_seconds": sum(float(row["worker_seconds"]) for row in production),
                "audit_worker_seconds": sum(float(row["worker_seconds"]) for row in audit),
            },
            "production": sorted(production, key=lambda row: int(row["template"])),
            "audit": sorted(audit, key=lambda row: int(row["template"])),
        }
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        return packet

    write_checkpoint(False)
    try:
        for row in run_production.map(range(TEMPLATES)):
            production.append(row)
            write_checkpoint(False)
        for row in run_audit.map(range(TEMPLATES)):
            audit.append(row)
            write_checkpoint(False)
    except BaseException:
        print(
            "E30_PROFILE422_EXCEPTIONAL_INCOMPLETE "
            f"production={len(production)}/{TEMPLATES} audit={len(audit)}/{TEMPLATES}"
        )
        raise
    packet = write_checkpoint(
        len(production) == len(audit) == TEMPLATES
        and all(bool(row["complete"]) for row in production + audit)
    )
    print("E30_PROFILE422_EXCEPTIONAL " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E30_PROFILE422_EXCEPTIONAL_AGREEMENT {packet['agreement']}")
    print(f"E30_PROFILE422_EXCEPTIONAL_RESULT {RESULT}")
