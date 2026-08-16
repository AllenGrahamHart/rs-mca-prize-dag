#!/usr/bin/env python3
"""Fan out checkpointed script/argument jobs through one local Modal client."""

from __future__ import annotations

import json
import pathlib

import modal


app = modal.App("rs-mca-checkpointed-batch-runner")
image = modal.Image.debian_slim()


@app.function(image=image, cpu=1.0, memory=1024, timeout=660)
def run_remote(
    files: dict[str, bytes], script_name: str, argv: list[str], job: str
) -> dict:
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
            exit_code = process.wait(timeout=645)
        except subprocess.TimeoutExpired:
            timed_out = True
            process.kill()
            exit_code = 124
            process.wait()
    peak = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    return {
        "job": job,
        "exit": exit_code,
        "timed_out": timed_out,
        "stdout": pathlib.Path(stdout_path).read_text()[-60000:],
        "stderr": pathlib.Path(stderr_path).read_text()[-20000:],
        "peak_mb": peak // 1024,
    }


@app.local_entrypoint()
def main(scripts: str, data: str, lanes: str) -> None:
    files = {}
    script_paths = [pathlib.Path(item).resolve() for item in scripts.split(",")]
    for script_path in script_paths:
        files[script_path.name] = script_path.read_bytes()
    for path in data.split(",") if data else []:
        if path:
            source = pathlib.Path(path).resolve()
            files[source.name] = source.read_bytes()

    jobs = []
    implementations = [
        "audit" if "audit" in path.stem else "primary"
        for path in script_paths
    ]
    assert len(set(implementations)) == len(implementations)
    for implementation, script_path in zip(implementations, script_paths):
        for lane in lanes.split(","):
            jobs.append(
                (files, script_path.name, [lane], f"{implementation}:{lane}")
            )

    completed = 0
    failures = 0
    for result in run_remote.starmap(jobs, order_outputs=False):
        completed += 1
        if result["exit"] != 0:
            failures += 1
        print(json.dumps({
            "event": "JOB_RESULT",
            "job": result["job"],
            "exit": result["exit"],
            "timed_out": result["timed_out"],
            "peak_mb": result["peak_mb"],
            "stdout": result["stdout"],
            "stderr": result["stderr"],
        }, sort_keys=True), flush=True)
    print(json.dumps({
        "event": "BATCH_PASS" if failures == 0 else "BATCH_INCOMPLETE",
        "completed": completed,
        "expected": len(jobs),
        "failures": failures,
    }, sort_keys=True), flush=True)
    raise SystemExit(0 if completed == len(jobs) and failures == 0 else 1)
