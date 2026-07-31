#!/usr/bin/env python3
"""Regenerate the exhaustive fixed-swap direct-component certificate."""

import subprocess
import sys
import tempfile
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NOTES = ROOT / "critical/nodes/rate_half_band_closure/notes"
ROUTER = NOTES / "kb_c2_112_aligned_positive_unramified_fixed_direct_router.py"
SURVIVORS = NOTES / (
    "kb_c2_112_aligned_positive_unramified_fixed_swap_survivors.json"
)


with tempfile.TemporaryDirectory() as directory:
    generated = Path(directory) / "survivors.json"
    completed = subprocess.run(
        [
            sys.executable,
            str(ROUTER),
            "--allocation", "swap",
            "--finite-replay",
            "--dump-survivors", str(generated),
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=60,
        check=False,
    )
    marker = "SURVIVOR_CERTIFICATE_PASS allocation=swap count=1"
    if completed.returncode != 0 or marker not in completed.stdout:
        raise RuntimeError(f"exhaustive replay failed:\n{completed.stdout}")
    if generated.read_bytes() != SURVIVORS.read_bytes():
        raise RuntimeError("regenerated survivor certificate mismatch")

print(
    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_SWAP_"
    "EXHAUSTIVE_PASS norm_factors=26 survivors=1 certificate_match=true"
)
