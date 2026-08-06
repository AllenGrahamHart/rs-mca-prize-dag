#!/usr/bin/env python3
"""Run the preregistered CS transport audit in one bounded Modal worker."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import modal


APP_NAME = "rs-mca-cs-independent-transport-audit"
HERE = Path(__file__).resolve().parent
CHECKER = HERE / "cs_independent_audit.py"
OUTPUT = HERE / "cs_independent_audit_result.json"
REMOTE_CHECKER = "/root/cs_independent_audit.py"

app = modal.App(APP_NAME)
image = modal.Image.debian_slim(python_version="3.12").add_local_file(
    CHECKER, REMOTE_CHECKER, copy=True
)


@app.function(image=image, cpu=1, memory=1024, timeout=120, max_containers=1)
def audit() -> dict[str, object]:
    process = subprocess.run(
        ["python3", REMOTE_CHECKER, "--json", "--tamper-selftest"],
        text=True,
        capture_output=True,
        timeout=90,
        check=False,
    )
    result: dict[str, object] = {
        "schema": "cs-independent-transport-modal-v1",
        "app": APP_NAME,
        "checker_sha256": hashlib.sha256(
            Path(REMOTE_CHECKER).read_bytes()
        ).hexdigest(),
        "returncode": process.returncode,
        "stderr": process.stderr[-4000:],
    }
    if process.returncode == 0:
        result["audit"] = json.loads(process.stdout)
        result["status"] = result["audit"]["status"]
    else:
        result["status"] = "FAIL"
        result["stdout"] = process.stdout[-4000:]
    print("CS_TRANSPORT_RESULT " + json.dumps(result, sort_keys=True), flush=True)
    return result


@app.local_entrypoint()
def main() -> None:
    result = audit.remote()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("CS_TRANSPORT_LOCAL_RESULT " + json.dumps(result, sort_keys=True))
