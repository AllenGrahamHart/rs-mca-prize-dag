#!/usr/bin/env python3
"""Run the checked verifier manifest on Modal without loading WSL."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


ROOT = Path("/repo") if Path("/repo").is_dir() else Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "tools" / "verifier_manifest.json"
OUTPUT = ROOT / "experiments" / "prize_resolution" / "modal_verifier_replay.json"

app = modal.App("rs-mca-verifier-replay")
image = (
    modal.Image.debian_slim()
    .pip_install("mpmath", "numpy", "sympy")
    .add_local_dir(str(ROOT), remote_path="/repo", copy=True,
                   # w10 infra fix: exclude regenerables — .git alone is 121MB
                   ignore=[".git", "orbit", "**/__pycache__"])
)


@app.function(image=image, cpu=1, memory=2048, timeout=290, max_containers=24  # 180->290: the weight-5 MITM verifier needs ~150-280s (passes locally); fast scripts finish early)
def run_verifier(payload: tuple[str, str]) -> dict[str, object]:
    import hashlib
    import os
    import subprocess
    import sys
    import time
    from pathlib import Path

    rel, expected_hash = payload
    path = Path("/repo") / rel
    actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual_hash != expected_hash:
        return {"script": rel, "status": "HASH_MISMATCH", "sha256": actual_hash}
    start = time.monotonic()
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    try:
        result = subprocess.run(
            [sys.executable, rel],
            cwd="/repo",
            env=env,
            capture_output=True,
            text=True,
            timeout=270,  # 150->270: heavy MITM search headroom (KB #107)
        )
        return {
            "script": rel,
            "status": "PASS" if result.returncode == 0 else "FAIL",
            "returncode": result.returncode,
            "sha256": actual_hash,
            "seconds": round(time.monotonic() - start, 6),
            "stdout_tail": result.stdout[-2000:],
            "stderr_tail": result.stderr[-2000:],
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "script": rel,
            "status": "TIMEOUT",
            "returncode": None,
            "sha256": actual_hash,
            "seconds": round(time.monotonic() - start, 6),
            "stdout_tail": (exc.stdout or "")[-2000:],
            "stderr_tail": (exc.stderr or "")[-2000:],
        }


@app.local_entrypoint()
def main(match: str = "") -> None:
    manifest = json.loads(MANIFEST.read_text())
    payloads = [
        (rel, expected_hash)
        for rel, expected_hash in manifest["scripts"].items()
        if match in rel
    ]
    rows = list(run_verifier.map(payloads, return_exceptions=True))
    normalized: list[dict[str, object]] = []
    for payload, row in zip(payloads, rows):
        if isinstance(row, BaseException):
            normalized.append(
                {
                    "script": payload[0],
                    "status": "REMOTE_ERROR",
                    "sha256": hashlib.sha256((ROOT / payload[0]).read_bytes()).hexdigest(),
                    "error": repr(row),
                }
            )
        else:
            normalized.append(row)
    output = {
        "schema": "prize-modal-verifier-replay-v1",
        "manifest_sha256": hashlib.sha256(MANIFEST.read_bytes()).hexdigest(),
        "complete": len(normalized) == len(payloads),
        "match": match,
        "counts": {
            status: sum(row["status"] == status for row in normalized)
            for status in ("PASS", "FAIL", "TIMEOUT", "HASH_MISMATCH", "REMOTE_ERROR")
        },
        "results": sorted(normalized, key=lambda row: str(row["script"])),
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output["counts"], sort_keys=True))
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
