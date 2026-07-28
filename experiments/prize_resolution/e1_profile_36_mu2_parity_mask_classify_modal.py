#!/usr/bin/env python3
"""Run the exact mu=2 singleton parity-mask classifier on Modal."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


app = modal.App("e1-profile-36-mu2-parity-mask-classify")
root = Path("/repo") if Path("/repo").is_dir() else Path(__file__).resolve().parents[2]
source = root / "experiments/prize_resolution/e1_profile_36_mu2_parity_mask_classify.cpp"
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(source, "/repo/experiments/prize_resolution/classify.cpp", copy=True)
    .run_commands(
        "g++ -std=c++20 -O3 -o /worker "
        "/repo/experiments/prize_resolution/classify.cpp"
    )
)


@app.function(image=image, cpu=1.0, memory=512, timeout=60, max_containers=1)
def classify() -> dict[str, object]:
    import resource
    import subprocess
    import time

    started = time.monotonic()
    result = subprocess.run(
        ["/worker"], capture_output=True, check=True, text=True, timeout=55
    )
    return {
        "stdout": result.stdout,
        "worker_seconds": time.monotonic() - started,
        "peak_rss_kib": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
    }


@app.local_entrypoint()
def main() -> None:
    payload = {
        "schema": "e1-profile-36-mu2-parity-mask-classify-v1",
        "complete": False,
        "cpp_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    }
    try:
        payload.update(classify.remote())
        payload["complete"] = True
    except Exception as error:
        payload["error"] = f"{type(error).__name__}: {error}"
    print("E1_PROFILE_36_MU2_PARITY_MASK_CLASSIFY " + json.dumps(payload, sort_keys=True))
