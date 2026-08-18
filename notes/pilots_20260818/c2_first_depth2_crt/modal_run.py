#!/usr/bin/env python3
"""Parallel Modal launcher for the first exact depth-two C2 row."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import time

import modal


HERE = Path(__file__).resolve().parent
TARGET_MODULI = (
    1152921504606850301,
    1152921504606873847,
    1152921504606875777,
)
TASKS = tuple(("target", 64, 4, 193, modulus) for modulus in TARGET_MODULI) + (
    ("control", 32, 2, 97, 1152921504606848701),
)

app = modal.App("rs-mca-c2-first-depth2-crt")
image = modal.Image.debian_slim().apt_install("g++", "libgomp1").add_local_file(
    str(HERE / "exact_tower_fourier.cpp"), "/root/exact_tower_fourier.cpp"
)


@app.function(image=image, cpu=8.0, memory=2048, timeout=240, max_containers=4)
def exact_residue(task: tuple[str, int, int, int, int]) -> dict[str, object]:
    label, n, t, q, modulus = task
    started = time.monotonic()
    try:
        subprocess.run(
            ["g++", "-O3", "-fopenmp", "-std=c++17", "/root/exact_tower_fourier.cpp", "-o", "/tmp/exact_tower_fourier"],
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        process = subprocess.run(
            ["/tmp/exact_tower_fourier", str(n), str(t), str(q), str(modulus)],
            check=True,
            capture_output=True,
            text=True,
            timeout=200,
        )
        values = dict(line.split("=", 1) for line in process.stdout.splitlines())
        result: dict[str, object] = {
            "status": "PASS",
            "label": label,
            "n": n,
            "t": t,
            "q": q,
            "modulus": modulus,
            "seconds": time.monotonic() - started,
        }
        for key, value in values.items():
            if key not in {"n", "t", "q", "modulus"}:
                result[key] = int(value)
        return result
    except subprocess.TimeoutExpired as error:
        return {
            "status": "TIMEOUT", "label": label, "n": n, "t": t, "q": q,
            "modulus": modulus, "stage": str(error.cmd[0]),
            "seconds": time.monotonic() - started,
        }
    except Exception as error:
        return {
            "status": "ERROR", "label": label, "n": n, "t": t, "q": q,
            "modulus": modulus, "error": repr(error),
            "seconds": time.monotonic() - started,
        }


@app.local_entrypoint()
def main(output: str = str(HERE / "results.json")) -> None:
    destination = Path(output)
    results: list[dict[str, object]] = []
    for result in exact_residue.map(TASKS, order_outputs=False):
        results.append(result)
        payload = {
            "schema": "c2-first-depth2-crt-v1",
            "tasks_requested": len(TASKS),
            "tasks_returned": len(results),
            "results": sorted(results, key=lambda row: (str(row["label"]), int(row["modulus"]))),
        }
        destination.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        print(json.dumps(result, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
