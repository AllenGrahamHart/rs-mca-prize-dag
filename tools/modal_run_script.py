#!/usr/bin/env python3
"""Generic Modal script runner — the COMPUTE LAW tool (2026-07-13).

House law after three WSL OOM crashes (7.5GiB box; kern.log:5064): NO local
compute scripts. Any check/enumeration/verification script runs on Modal via
this wrapper, or does not run.

Usage:
    ~/.venvs/modal/bin/modal run tools/modal_run_script.py \
        --script path/to/check.py [--data path1,path2,...] [--args "a b c"]

The script and optional data files are shipped by content (no mounts —
version-proof) into /work (flat basenames); the script runs with cwd=/work;
stdout/stderr and the exit code come back verbatim. Worker: 2 CPU, 16GiB,
timeout 280s (the Modal-law ceiling). numpy/sympy preinstalled.
"""
import pathlib

import modal

app = modal.App("rs-mca-script-runner")
image = modal.Image.debian_slim().pip_install("numpy", "sympy")


@app.function(image=image, cpu=2.0, memory=16384, timeout=280)
def run_remote(files: dict, script_name: str, argv: list) -> dict:
    import os
    import resource
    import subprocess
    os.makedirs("/work", exist_ok=True)
    for name, blob in files.items():
        with open(f"/work/{name}", "wb") as fh:
            fh.write(blob)
    r = subprocess.run(
        ["python3", script_name] + list(argv), cwd="/work",
        capture_output=True, text=True, timeout=270,
    )
    peak = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    return {"exit": r.returncode, "stdout": r.stdout[-40000:],
            "stderr": r.stderr[-20000:], "peak_kb": peak}


@app.local_entrypoint()
def main(script: str, data: str = "", args: str = ""):
    files = {}
    sp = pathlib.Path(script).resolve()
    files[sp.name] = sp.read_bytes()
    for p in (data.split(",") if data else []):
        if p:
            fp = pathlib.Path(p).resolve()
            files[fp.name] = fp.read_bytes()
    res = run_remote.remote(files, sp.name, [a for a in args.split(" ") if a])
    print(res["stdout"], end="")
    if res["stderr"]:
        print("--- stderr ---\n" + res["stderr"], end="")
    print(f"\nMODAL_RUN exit={res['exit']} peak_rss={res['peak_kb'] // 1024}MB")
    raise SystemExit(res["exit"])
