#!/usr/bin/env python3
"""Helpers for bounded alternate-chain audit shards."""

from pathlib import Path
import subprocess
import sys


NODE = Path(__file__).resolve().parent
CERTIFICATE = NODE / "certificate.py"


def run_kind(kind):
    process = subprocess.run(
        [sys.executable, str(CERTIFICATE), "--preferred-chain", "1",
         "--kind", kind, "--unit-check", "matrix"],
        check=True, capture_output=True, text=True, timeout=55,
    )
    output = process.stdout.strip()
    if "units=60" not in output or "unit_check=matrix" not in output:
        raise RuntimeError(f"alternate kind audit {kind}: {output}")
    if "chain0=0 chain1=15 chain2=0" not in output:
        raise RuntimeError(f"alternate chain census {kind}: {output}")


def run_shard(kind, indices):
    checked = 0
    for index in indices:
        process = subprocess.run(
            [sys.executable, str(CERTIFICATE), "--preferred-chain", "1",
             "--kind", kind, "--matching", str(index),
             "--unit-check", "matrix"],
            check=True, capture_output=True, text=True, timeout=55,
        )
        output = process.stdout.strip()
        if "units=4" not in output or "unit_check=matrix" not in output:
            raise RuntimeError(f"alternate shard {kind}/{index}: {output}")
        if "chain0=0 chain1=1 chain2=0" not in output:
            raise RuntimeError(f"alternate chain {kind}/{index}: {output}")
        checked += 4
    return checked
