#!/usr/bin/env python3
"""Run two exact E34 generic-heavy orbit classifiers on Modal."""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
PRIMARY = HERE / "e34_generic_orbit_classifier.cpp"
AUDIT = HERE / "e34_generic_orbit_audit.cpp"
OUTPUT = HERE / "e34_generic_orbit_result.json"

image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(str(PRIMARY), "/root/primary.cpp", copy=True)
    .add_local_file(str(AUDIT), "/root/audit.cpp", copy=True)
    .run_commands(
        "g++ -O3 -std=c++17 /root/primary.cpp -o /usr/local/bin/generic-primary",
        "g++ -O3 -std=c++17 /root/audit.cpp -o /usr/local/bin/generic-audit",
    )
)
app = modal.App("e1-e34-generic-orbit-classifier")


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=2)
def classify(kind: str) -> dict[str, object]:
    started = time.perf_counter()
    binary = f"/usr/local/bin/generic-{kind}"
    try:
        completed = subprocess.run(
            [binary], capture_output=True, check=True, text=True, timeout=50
        )
        result = json.loads(completed.stdout)
        result["kind"] = kind
        result["wall_seconds"] = time.perf_counter() - started
        return result
    except Exception as error:
        return {
            "complete": False,
            "kind": kind,
            "wall_seconds": time.perf_counter() - started,
            "error": repr(error),
        }


def write_packet(results: list[dict[str, object]]) -> None:
    by_kind = {str(result["kind"]): result for result in results}
    packet = {
        "schema": "e1-e34-generic-orbit-classifier-v1",
        "complete": set(by_kind) == {"primary", "audit"}
        and all(result.get("complete") is True for result in results),
        "primary_source_sha256": hashlib.sha256(PRIMARY.read_bytes()).hexdigest(),
        "audit_source_sha256": hashlib.sha256(AUDIT.read_bytes()).hexdigest(),
        "errors": [result for result in results if result.get("complete") is not True],
        "results": by_kind,
    }
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main() -> None:
    results: list[dict[str, object]] = []
    for result in classify.map(("primary", "audit"), order_outputs=False):
        results.append(result)
        write_packet(results)
        print(f"E1_E34_GENERIC_ORBIT_PROGRESS returned={len(results)}/2")
    print(
        "E1_E34_GENERIC_ORBIT_CLASSIFIER "
        f"complete={sum(result.get('complete') is True for result in results)}/2 "
        f"worker_seconds={sum(float(result['wall_seconds']) for result in results):.6f}"
    )
