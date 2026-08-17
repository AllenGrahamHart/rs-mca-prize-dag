#!/usr/bin/env python3
"""Modal runner for bounded low-memory jobs that need more than 270 seconds."""

from __future__ import annotations

import pathlib

import modal


app = modal.App("rs-mca-long-script-runner")
image = modal.Image.debian_slim()


@app.function(image=image, cpu=2.0, memory=1024, timeout=600)
def run_remote(files: dict[str, bytes], script_name: str, argv: list[str]) -> dict:
    import os
    import resource
    import subprocess

    os.makedirs("/work", exist_ok=True)
    for name, blob in files.items():
        with open(f"/work/{name}", "wb") as handle:
            handle.write(blob)
    result = subprocess.run(
        ["python3", script_name] + list(argv),
        cwd="/work",
        capture_output=True,
        text=True,
        timeout=590,
    )
    peak = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    return {
        "exit": result.returncode,
        "stdout": result.stdout[-40000:],
        "stderr": result.stderr[-20000:],
        "peak_kb": peak,
    }


@app.local_entrypoint()
def main(script: str, data: str = "", args: str = "") -> None:
    files = {}
    script_path = pathlib.Path(script).resolve()
    files[script_path.name] = script_path.read_bytes()
    for path in data.split(",") if data else []:
        if path:
            source = pathlib.Path(path).resolve()
            files[source.name] = source.read_bytes()
    result = run_remote.remote(
        files,
        script_path.name,
        [item for item in args.split(" ") if item],
    )
    print(result["stdout"], end="")
    if result["stderr"]:
        print("--- stderr ---\n" + result["stderr"], end="")
    print(
        f"\nMODAL_RUN exit={result['exit']} "
        f"peak_rss={result['peak_kb'] // 1024}MB"
    )
    raise SystemExit(result["exit"])
