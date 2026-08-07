#!/usr/bin/env python3
"""Independent sharded Sage review of upstream PR #1144 on Modal."""

from __future__ import annotations

import json
from pathlib import Path

import modal


APP_NAME = "rs-mca-k3-pr1144-independent-review"
UPSTREAM = "https://github.com/przchojecki/rs-mca.git"
SCRIPT = (
    "/repo/experimental/scripts/"
    "compile_kb_mca_v4_m2_aligned_positive_moving_closure_v1.sage"
)
VERIFY = (
    "/repo/experimental/scripts/"
    "verify_kb_mca_v4_m2_aligned_positive_moving_closure_v1.py"
)
OUTPUT = Path(__file__).resolve().parent / "modal_review_output.json"

DIRECT_CELLS = (
    "M00-R02",
    "M00-R20",
    "M01-R02",
    "M01-R11",
    "M01-R20",
    "M03-R02",
    "M03-R11",
    "M03-R20",
)


def sage_command(*arguments: str) -> list[str]:
    argv = [SCRIPT, *arguments]
    command = (
        f"import sys; sys.setrecursionlimit(500000); sys.argv={argv!r}; "
        f"__file__={SCRIPT!r}; load({SCRIPT!r}); main()"
    )
    return ["sage", "-c", command]


CASES = tuple(
    {
        "name": cell,
        "command": sage_command("--cell", cell),
        "expected_stdout": "PASS aligned-positive moving closure compiler",
    }
    for cell in DIRECT_CELLS
) + (
    {
        "name": "transport",
        "command": sage_command("--transport-only"),
        "expected_stdout": "PASS aligned-positive moving closure compiler",
    },
    {
        "name": "import",
        "command": sage_command("--import-only"),
        "expected_stdout": "PASS aligned-positive moving closure compiler",
    },
    {
        "name": "parity-M01",
        "command": sage_command("--parity-only", "M01"),
        "expected_stdout": "PASS aligned-positive moving closure compiler",
    },
    {
        "name": "parity-M03",
        "command": sage_command("--parity-only", "M03"),
        "expected_stdout": "PASS aligned-positive moving closure compiler",
    },
    {
        "name": "python-normal",
        "command": ["python3", VERIFY, "--check", "--tamper-selftest"],
        "expected_stdout": "PASS aligned-positive moving closure verifier",
    },
    {
        "name": "python-optimized",
        "command": ["python3", "-O", VERIFY, "--check", "--tamper-selftest"],
        "expected_returncode": 1,
        "expected_stderr": "optimized Python execution is refused",
    },
)

app = modal.App(APP_NAME)
image = (
    modal.Image.micromamba(python_version="3.12")
    .apt_install("git")
    .micromamba_install("sage=10.9", channels=["conda-forge"])
    .run_commands(
        "git init /repo",
        f"git -C /repo remote add origin {UPSTREAM}",
        "git -C /repo fetch --depth=1 origin "
        "pull/1144/head:refs/remotes/origin/pr1144",
        "git -C /repo fetch --depth=1 origin "
        "pull/1141/head:refs/remotes/origin/pr1141",
        "git -C /repo fetch --depth=1 origin "
        "pull/1138/head:refs/remotes/origin/pr1138",
        "git -C /repo checkout --detach refs/remotes/origin/pr1144",
    )
)


@app.function(
    image=image,
    cpu=1,
    memory=8192,
    timeout=1800,
    max_containers=14,
)
def review_case(case: dict[str, object]) -> dict[str, object]:
    import hashlib
    import os
    import resource
    import subprocess
    import time

    began = time.monotonic()
    environment = dict(os.environ)
    environment["HOME"] = "/tmp/sage-home"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    try:
        completed = subprocess.run(
            list(case["command"]),
            cwd="/repo",
            env=environment,
            capture_output=True,
            text=True,
            timeout=1740,
            check=False,
        )
        stdout = completed.stdout
        stderr = completed.stderr
        expected_returncode = int(case.get("expected_returncode", 0))
        expected_stderr = str(case.get("expected_stderr", ""))
        expected_stdout = str(case.get("expected_stdout", ""))
        passed = (
            completed.returncode == expected_returncode
            and expected_stderr in stderr
            and expected_stdout in stdout
        )
        return {
            "name": case["name"],
            "status": "PASS" if passed else "FAIL",
            "returncode": completed.returncode,
            "expected_returncode": expected_returncode,
            "expected_stderr": expected_stderr,
            "expected_stdout": expected_stdout,
            "seconds": round(time.monotonic() - began, 6),
            "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
            "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
            "stdout_tail": stdout[-4000:],
            "stderr_tail": stderr[-4000:],
        }
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout or ""
        stderr = error.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode(errors="replace")
        return {
            "name": case["name"],
            "status": "TIMEOUT",
            "returncode": None,
            "seconds": round(time.monotonic() - began, 6),
            "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
            "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
            "stdout_tail": stdout[-4000:],
            "stderr_tail": stderr[-4000:],
        }


@app.local_entrypoint()
def main(case_name: str = "") -> None:
    selected = tuple(
        case for case in CASES if not case_name or case["name"] == case_name
    )
    if not selected:
        raise ValueError(f"unknown case: {case_name}")
    rows = list(review_case.map(selected, return_exceptions=True))
    normalized = []
    for case, row in zip(selected, rows):
        if isinstance(row, BaseException):
            normalized.append(
                {"name": case["name"], "status": "REMOTE_ERROR", "error": repr(row)}
            )
        else:
            normalized.append(row)
    if case_name and OUTPUT.exists():
        previous = json.loads(OUTPUT.read_text())
        replacements = {row["name"]: row for row in normalized}
        normalized = [
            replacements.get(row["name"], row) for row in previous["results"]
        ]
    output = {
        "schema": "kb-c2-112-pr1144-independent-modal-review-v1",
        "app": APP_NAME,
        "upstream_commit": "05ff2348de8f2c0f99683875ff12a9a79dcf21ec",
        "sage": "10.9",
        "case_count": len(CASES),
        "last_selection": [case["name"] for case in selected],
        "complete": len(normalized) == len(CASES),
        "counts": {
            status: sum(row["status"] == status for row in normalized)
            for status in ("PASS", "FAIL", "TIMEOUT", "REMOTE_ERROR")
        },
        "results": normalized,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output["counts"], sort_keys=True))
    print(f"wrote {OUTPUT}")
