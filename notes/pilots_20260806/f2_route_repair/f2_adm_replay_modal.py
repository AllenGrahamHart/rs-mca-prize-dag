#!/usr/bin/env python3
"""Replay the canonical F2 admissible-row verifier in one Modal worker."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import modal


APP_NAME = "rs-mca-f2-admissible-route-repair-replay"
SOURCE = Path(__file__).resolve()
LOCAL_ROOT = SOURCE.parents[3] if len(SOURCE.parents) > 3 else Path("/repo")
OUTPUT = SOURCE.parent / "f2_adm_replay_result.json"
REMOTE_ROOT = Path("/repo")

FILES = (
    "critical/nodes/rules_freeze/statement.md",
    "notes/pilots_20260802/f2_deployed_windows/tower.py",
    "notes/pilots_20260802/f2_fixed_sector/REPORT.md",
    "notes/pilots_20260804/f2_opening/PROOFS.md",
    "notes/pilots_20260804/f2_sl1_powersums/PROOFS.md",
    "notes/pilots_20260806/f2_sl1b/PROOFS.md",
    "notes/pilots_20260806/f2_tq_pin/PROOFS.md",
    "notes/pilots_20260806/f2_adm/verify.py",
)

image = modal.Image.debian_slim(python_version="3.12")
for relative in FILES:
    image = image.add_local_file(
        LOCAL_ROOT / relative,
        str(REMOTE_ROOT / relative),
        copy=True,
    )
app = modal.App(APP_NAME)


@app.function(image=image, cpu=1, memory=1024, timeout=180, max_containers=1)
def replay() -> dict[str, object]:
    verifier = REMOTE_ROOT / "notes/pilots_20260806/f2_adm/verify.py"
    source = verifier.read_text().replace(
        'REPO = "/home/u2470931/smooth-read-solomin/prize"',
        'REPO = "/repo"',
        1,
    )
    verifier.write_text(source)
    process = subprocess.run(
        ["python3", str(verifier)],
        text=True,
        capture_output=True,
        timeout=150,
        check=False,
    )
    stdout = process.stdout
    result = {
        "schema": "f2-admissible-route-repair-replay-v1",
        "app": APP_NAME,
        "returncode": process.returncode,
        "status": "PASS"
        if process.returncode == 0
        and "TOTAL: 373 PASS, 0 FAIL" in stdout
        and "DIGEST: F2_ADM_ALL_PASS" in stdout
        else "FAIL",
        "pass_count": stdout.count("PASS  "),
        "fail_count": stdout.count("FAIL  "),
        "stdout_tail": stdout[-6000:],
        "stderr_tail": process.stderr[-4000:],
    }
    print("F2_ADM_REPLAY_RESULT " + json.dumps(result, sort_keys=True), flush=True)
    return result


@app.local_entrypoint()
def main() -> None:
    result = replay.remote()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("F2_ADM_REPLAY_LOCAL_RESULT " + json.dumps(result, sort_keys=True))
