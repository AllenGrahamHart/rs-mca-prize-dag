#!/usr/bin/env python3
"""Run the interreduced M01-R11 Singular certificate on Modal."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


APP_NAME = "rs-mca-k3-pr1144-m01-interred-singular-certificate"
UPSTREAM = "https://github.com/przchojecki/rs-mca.git"
COMMIT = "05ff2348de8f2c0f99683875ff12a9a79dcf21ec"
HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "review_m01_interred_singular_certificate.sage"
OUTPUT = HERE / "modal_review_m01_interred_singular_certificate_output.json"

app = modal.App(APP_NAME)
image = (
    modal.Image.from_registry("sagemath/sagemath:10.9")
    .apt_install("git", "python3", "python-is-python3")
    .run_commands(
        "git init /repo",
        f"git -C /repo remote add origin {UPSTREAM}",
        "git -C /repo fetch --depth=1 origin "
        "pull/1144/head:refs/remotes/origin/pr1144",
        "git -C /repo checkout --detach refs/remotes/origin/pr1144",
        f'test "$(git -C /repo rev-parse HEAD)" = "{COMMIT}"',
    )
    .add_local_file(SCRIPT, "/review_m01_interred_singular_certificate.sage")
)


@app.function(image=image, cpu=4, memory=32768, timeout=3600)
def review() -> dict[str, object]:
    import os
    import resource
    import subprocess
    import time

    environment = dict(os.environ)
    environment["HOME"] = "/tmp/sage-home"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    os.makedirs(environment["HOME"], exist_ok=True)
    began = time.monotonic()
    try:
        completed = subprocess.run(
            ["sage", "/review_m01_interred_singular_certificate.sage"],
            cwd="/repo",
            env=environment,
            capture_output=True,
            text=True,
            timeout=3540,
            check=False,
        )
        stdout = completed.stdout
        stderr = completed.stderr
        returncode = completed.returncode
        timed_out = False
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout or ""
        stderr = error.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode(errors="replace")
        returncode = None
        timed_out = True
    records = []
    for line in stdout.splitlines():
        if line.startswith("{"):
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    done = next((record for record in records if record.get("phase") == "DONE"), None)
    passed = (
        not timed_out
        and returncode == 0
        and done is not None
        and done.get("terminal") == "M01_R11_FULL_OPEN_EMPTY"
    )
    return {
        "status": "TIMEOUT" if timed_out else ("PASS" if passed else "FAIL"),
        "returncode": returncode,
        "seconds": round(time.monotonic() - began, 6),
        "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        "records": records,
        "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
        "stdout_tail": stdout[-30000:],
        "stderr_tail": stderr[-10000:],
    }


@app.local_entrypoint()
def main() -> None:
    row = review.remote()
    output = {
        "schema": "kb-c2-112-pr1144-m01-interred-singular-certificate-v1",
        "app": APP_NAME,
        "upstream_commit": COMMIT,
        "result": row,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": row["status"]}, sort_keys=True))
    print(f"wrote {OUTPUT}")
