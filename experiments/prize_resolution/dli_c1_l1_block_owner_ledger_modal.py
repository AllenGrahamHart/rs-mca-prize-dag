#!/usr/bin/env python3
"""Replay the DLI C1 L=1 block-owner verifier on Modal."""

import json
from pathlib import Path
import subprocess

import modal


REMOTE_VERIFY = "/root/verify_dli_c1_l1_block_owner_ledger.py"
HERE = Path(__file__).resolve()
VERIFY = (
    HERE.parents[2]
    / "background/nodes/dli_c1_l1_block_owner_ledger/verify.py"
    if len(HERE.parents) > 2
    else Path(REMOTE_VERIFY)
)

app = modal.App("rs-mca-dli-c1-l1-block-owner-ledger")
image = modal.Image.debian_slim(python_version="3.12").add_local_file(
    VERIFY, REMOTE_VERIFY
)


@app.function(image=image, cpu=1.0, memory=512, timeout=300)
def replay():
    process = subprocess.run(
        ["python", REMOTE_VERIFY], capture_output=True, text=True, timeout=270
    )
    return {
        "status": "COMPLETE" if process.returncode == 0 else "ERROR",
        "stdout": process.stdout,
        "stderr": process.stderr[-4000:],
    }


@app.local_entrypoint()
def main():
    print(json.dumps({
        "scope": "one full order-512 split-prime replay; proof is algebraic",
        "result": replay.remote(),
    }, sort_keys=True))
