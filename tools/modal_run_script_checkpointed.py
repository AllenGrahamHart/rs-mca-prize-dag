#!/usr/bin/env python3
"""Modal runner that returns flushed stdout after success or hard timeout."""

from __future__ import annotations

import pathlib

import modal


app = modal.App("rs-mca-checkpointed-script-runner")
image = modal.Image.debian_slim()


@app.function(image=image, cpu=2.0, memory=1024, timeout=300)
def run_remote(files: dict[str, bytes], script_name: str, argv: list[str]) -> dict:
    import os
    import resource
    import subprocess

    os.makedirs("/work", exist_ok=True)
    for name, blob in files.items():
        with open(f"/work/{name}", "wb") as handle:
            handle.write(blob)
    stdout_path, stderr_path = "/work/stdout.log", "/work/stderr.log"
    timed_out = False
    with open(stdout_path, "w") as stdout, open(stderr_path, "w") as stderr:
        process = subprocess.Popen(
            ["python3", script_name] + list(argv),
            cwd="/work",
            stdout=stdout,
            stderr=stderr,
            text=True,
        )
        try:
            exit_code = process.wait(timeout=285)
        except subprocess.TimeoutExpired:
            timed_out = True
            process.kill()
            exit_code = 124
            process.wait()
    peak = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    return {
        "exit": exit_code,
        "timed_out": timed_out,
        "stdout": pathlib.Path(stdout_path).read_text()[-60000:],
        "stderr": pathlib.Path(stderr_path).read_text()[-20000:],
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
    status = "INCOMPLETE" if result["timed_out"] else (
        "PASS" if result["exit"] == 0 else "FAIL"
    )
    print(
        f"\nMODAL_CHECKPOINTED status={status} exit={result['exit']} "
        f"peak_rss={result['peak_kb'] // 1024}MB"
    )
    raise SystemExit(result["exit"])
