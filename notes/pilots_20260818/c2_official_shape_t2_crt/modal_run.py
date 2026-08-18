#!/usr/bin/env python3
"""Parallel exact CRT launcher for the n/t=256, t=2 C2 analogue."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import time

import modal


HERE = Path(__file__).resolve().parent
TARGET_MODULI = (
    1152921504607075139,
    1152921504607136587,
    1152921504607459189,
    1152921504607597447,
    1152921504608457719,
    1152921504609241181,
    1152921504609333353,
    1152921504609486973,
    1152921504609978557,
    1152921504610301159,
)
TASKS = tuple(("target", 512, 7681, modulus) for modulus in TARGET_MODULI) + (
    ("control97", 32, 97, 1152921504606848701),
    ("control5857", 32, 5857, 1152921504607016701),
)

app = modal.App("rs-mca-c2-official-shape-t2-crt")
image = modal.Image.debian_slim().apt_install("g++").add_local_file(
    str(HERE / "exact_fourier.cpp"), "/root/exact_fourier.cpp"
)


@app.function(image=image, cpu=1.0, memory=1024, timeout=240, max_containers=12)
def exact_residue(task: tuple[str, int, int, int]) -> dict[str, object]:
    label, n, q, modulus = task
    started = time.monotonic()
    try:
        subprocess.run(
            ["g++", "-O3", "-std=c++17", "/root/exact_fourier.cpp", "-o", "/tmp/exact_fourier"],
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        process = subprocess.run(
            ["/tmp/exact_fourier", str(n), str(q), str(modulus)],
            check=True,
            capture_output=True,
            text=True,
            timeout=200,
        )
        values = dict(line.split("=", 1) for line in process.stdout.splitlines())
        return {
            "status": "PASS",
            "label": label,
            "n": n,
            "q": q,
            "modulus": modulus,
            "orbits": int(values["orbits"]),
            "z0": int(values["z0"]),
            "c1": int(values["c1"]),
            "z1": int(values["z1"]),
            "b0": int(values["b0"]),
            "seconds": time.monotonic() - started,
        }
    except subprocess.TimeoutExpired as error:
        return {
            "status": "TIMEOUT",
            "label": label,
            "n": n,
            "q": q,
            "modulus": modulus,
            "stage": str(error.cmd[0]),
            "seconds": time.monotonic() - started,
        }
    except Exception as error:
        return {
            "status": "ERROR",
            "label": label,
            "n": n,
            "q": q,
            "modulus": modulus,
            "error": repr(error),
            "seconds": time.monotonic() - started,
        }


@app.local_entrypoint()
def main(output: str = str(HERE / "results.json")) -> None:
    destination = Path(output)
    results: list[dict[str, object]] = []
    for result in exact_residue.map(TASKS, order_outputs=False):
        results.append(result)
        payload = {
            "schema": "c2-official-shape-t2-crt-v1",
            "tasks_requested": len(TASKS),
            "tasks_returned": len(results),
            "results": sorted(results, key=lambda row: (str(row["label"]), int(row["modulus"]))),
        }
        destination.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        print(json.dumps(result, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
