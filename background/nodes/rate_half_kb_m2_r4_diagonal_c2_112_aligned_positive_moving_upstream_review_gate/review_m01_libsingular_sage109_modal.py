#!/usr/bin/env python3
"""Independent libSingular replay of PR #1144 M01-R11."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


APP_NAME = "rs-mca-k3-pr1144-m01-libsingular-review"
UPSTREAM = "https://github.com/przchojecki/rs-mca.git"
COMMIT = "05ff2348de8f2c0f99683875ff12a9a79dcf21ec"
SCRIPT = Path(
    "/repo/experimental/scripts/"
    "compile_kb_mca_v4_m2_aligned_positive_moving_closure_v1.sage"
)
REVIEW_SCRIPT = SCRIPT.with_name(
    "review_kb_mca_v4_m2_aligned_positive_m01_r11_libsingular.sage"
)
OUTPUT = (
    Path(__file__).resolve().parent
    / "modal_review_m01_libsingular_sage109_output.json"
)

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
    )
)


@app.function(image=image, cpu=1, memory=8192, timeout=1800)
def review() -> dict[str, object]:
    import os
    import resource
    import subprocess
    import time

    source = SCRIPT.read_text()
    external = 'algorithm="singular:slimgb"'
    internal = 'algorithm="libsingular:slimgb"'
    replacement_count = source.count(external)
    if replacement_count != 2:
        raise RuntimeError(f"unexpected backend call count: {replacement_count}")
    patched = source.replace(external, internal)
    REVIEW_SCRIPT.write_text(patched)

    environment = dict(os.environ)
    environment["HOME"] = "/tmp/sage-home"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    os.makedirs(environment["HOME"], exist_ok=True)
    began = time.monotonic()
    try:
        completed = subprocess.run(
            ["sage", str(REVIEW_SCRIPT), "--cell", "M01-R11"],
            cwd="/repo",
            env=environment,
            capture_output=True,
            text=True,
            timeout=1740,
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
    marker = "PASS aligned-positive moving closure compiler scope=M01-R11"
    return {
        "name": "M01-R11",
        "status": (
            "TIMEOUT" if timed_out else
            ("PASS" if returncode == 0 and marker in stdout else "FAIL")
        ),
        "returncode": returncode,
        "seconds": round(time.monotonic() - began, 6),
        "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        "sage_version": subprocess.check_output(
            ["sage", "--version"], env=environment, text=True
        ).strip(),
        "backend": "libsingular:slimgb",
        "replacement_count": replacement_count,
        "upstream_script_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "review_script_sha256": hashlib.sha256(patched.encode()).hexdigest(),
        "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
        "stdout_tail": stdout[-4000:],
        "stderr_tail": stderr[-4000:],
    }


@app.local_entrypoint()
def main() -> None:
    row = review.remote()
    output = {
        "schema": "kb-c2-112-pr1144-m01-libsingular-review-v1",
        "app": APP_NAME,
        "upstream_commit": COMMIT,
        "purpose": "equivalent-backend replay after external bridge failure",
        "result": row,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"name": row["name"], "status": row["status"]}))
    print(f"wrote {OUTPUT}")
