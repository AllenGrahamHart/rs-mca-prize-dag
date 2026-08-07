#!/usr/bin/env python3
"""Compatibility replay of the sole PR #1144 Sage 10.9 failure."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


APP_NAME = "rs-mca-k3-pr1144-m01-sage107-review"
UPSTREAM = "https://github.com/przchojecki/rs-mca.git"
COMMIT = "05ff2348de8f2c0f99683875ff12a9a79dcf21ec"
SCRIPT = (
    "/repo/experimental/scripts/"
    "compile_kb_mca_v4_m2_aligned_positive_moving_closure_v1.sage"
)
OUTPUT = Path(__file__).resolve().parent / "modal_review_m01_sage107_output.json"

app = modal.App(APP_NAME)
image = (
    modal.Image.micromamba(python_version="3.11")
    .apt_install("git")
    .micromamba_install("sage=10.7", channels=["conda-forge"])
    .run_commands(
        "git init /repo",
        f"git -C /repo remote add origin {UPSTREAM}",
        "git -C /repo fetch --depth=1 origin "
        "pull/1144/head:refs/remotes/origin/pr1144",
        "git -C /repo fetch --depth=1 origin "
        "pull/1138/head:refs/remotes/origin/pr1138",
        "git -C /repo checkout --detach refs/remotes/origin/pr1144",
    )
)


@app.function(image=image, cpu=1, memory=8192, timeout=1800)
def review() -> dict[str, object]:
    import os
    import resource
    import subprocess
    import time

    argv = [SCRIPT, "--cell", "M01-R11"]
    command = (
        f"import sys; sys.argv={argv!r}; "
        f"__file__={SCRIPT!r}; load({SCRIPT!r}); main()"
    )
    environment = dict(os.environ)
    environment["HOME"] = "/tmp/sage-home"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    os.makedirs(environment["HOME"], exist_ok=True)
    began = time.monotonic()
    completed = subprocess.run(
        ["sage", "-c", command],
        cwd="/repo",
        env=environment,
        capture_output=True,
        text=True,
        timeout=1740,
        check=False,
    )
    stdout = completed.stdout
    stderr = completed.stderr
    marker = "PASS aligned-positive moving closure compiler scope=M01-R11"
    return {
        "name": "M01-R11",
        "status": (
            "PASS" if completed.returncode == 0 and marker in stdout else "FAIL"
        ),
        "returncode": completed.returncode,
        "seconds": round(time.monotonic() - began, 6),
        "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        "sage_version": subprocess.check_output(
            ["sage", "--version"], env=environment, text=True
        ).strip(),
        "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
        "stdout_tail": stdout[-4000:],
        "stderr_tail": stderr[-4000:],
    }


@app.local_entrypoint()
def main() -> None:
    row = review.remote()
    output = {
        "schema": "kb-c2-112-pr1144-m01-sage107-review-v1",
        "app": APP_NAME,
        "upstream_commit": COMMIT,
        "purpose": "compatibility replay of the Sage 10.9 conversion failure",
        "result": row,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"name": row["name"], "status": row["status"]}))
    print(f"wrote {OUTPUT}")
