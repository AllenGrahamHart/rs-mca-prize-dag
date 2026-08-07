#!/usr/bin/env python3
"""Run the two exact fixed-literal inversion transports on Modal."""

from __future__ import annotations

import json
from pathlib import Path

import modal


APP_NAME = "rs-mca-k3-fixed-literal-companion-inversion-transport"
UPSTREAM = "https://github.com/przchojecki/rs-mca.git"
COMMIT = "55ac3e07477bd7a768190a3e755f22b0d44354b0"
HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "literal_fixed_inversion_transport_probe.sage"
OUTPUT = HERE / "modal_literal_fixed_inversion_transport_output.json"
CASES = ({"pair": "F04-F05"}, {"pair": "F06-F07"})

app = modal.App(APP_NAME)
image = (
    modal.Image.from_registry("sagemath/sagemath:10.9")
    .apt_install("git", "python3", "python-is-python3")
    .run_commands(
        "git init /repo",
        f"git -C /repo remote add origin {UPSTREAM}",
        "git -C /repo fetch --depth=1 origin pull/1149/head:refs/remotes/origin/pr1149",
        "git -C /repo checkout --detach refs/remotes/origin/pr1149",
    )
    .add_local_file(SCRIPT, "/literal_fixed_inversion_transport_probe.sage")
)


@app.function(image=image, cpu=2, memory=16384, timeout=1200, max_containers=2)
def run_pair(case: dict[str, str]) -> dict[str, object]:
    import hashlib
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
            [
                "sage",
                "/literal_fixed_inversion_transport_probe.sage",
                "--pair",
                case["pair"],
            ],
            cwd="/repo",
            env=environment,
            capture_output=True,
            text=True,
            timeout=1140,
            check=False,
        )
        records = []
        for line in completed.stdout.splitlines():
            if line.startswith("{"):
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
        return {
            **case,
            "status": "PASS" if completed.returncode == 0 and records else "FAIL",
            "returncode": completed.returncode,
            "seconds": round(time.monotonic() - began, 6),
            "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
            "records": records,
            "stdout_sha256": hashlib.sha256(completed.stdout.encode()).hexdigest(),
            "stdout_tail": completed.stdout[-12000:],
            "stderr_tail": completed.stderr[-12000:],
        }
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout or ""
        stderr = error.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode(errors="replace")
        return {
            **case,
            "status": "TIMEOUT",
            "seconds": round(time.monotonic() - began, 6),
            "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
            "stdout_tail": stdout[-12000:],
            "stderr_tail": stderr[-12000:],
        }


@app.local_entrypoint()
def main() -> None:
    raw_rows = list(run_pair.map(CASES, return_exceptions=True))
    rows = []
    for case, row in zip(CASES, raw_rows):
        if isinstance(row, BaseException):
            rows.append({**case, "status": "REMOTE_ERROR", "error": repr(row)})
        else:
            rows.append(row)
    output = {
        "schema": "kb-c2-112-fixed-literal-companion-inversion-transport-modal-v1",
        "app": APP_NAME,
        "upstream_commit": COMMIT,
        "counts": {
            status: sum(row["status"] == status for row in rows)
            for status in ("PASS", "FAIL", "TIMEOUT", "REMOTE_ERROR")
        },
        "results": rows,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output["counts"], sort_keys=True))
    print(f"wrote {OUTPUT}")
